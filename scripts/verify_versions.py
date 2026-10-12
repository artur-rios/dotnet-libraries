#!/usr/bin/env python3
"""Verify docs/data/family.yaml against what is actually published on nuget.org,
and verify that GitHub Packages carries the same versions as nuget.org.

Three kinds of finding, deliberately treated differently:

ERROR  something this repository can fix by editing the data file — a package's
       `version` is not the latest stable on nuget.org, a pinned dependency
       version was never published, a dependency names a package the file does
       not define, or an id appears twice. These fail the build.

MIRROR a version published on one registry but not the other. Every library
       publishes each release to both nuget.org and GitHub Packages, so a gap
       means a publish run went wrong. Only the library's own repository can
       fix it (re-run its publish workflow on the tag, or push the nupkg), but
       it still fails the build: a registry quietly missing releases is exactly
       what this check exists to catch.

DRIFT  something only another repository can fix — a package pins a dependency
       version older than that dependency's current release. That is a fact
       about the libraries, not a mistake in the data file, so it is reported
       but does not fail: a docs deploy should not be blocked because an
       unrelated library is behind. The site renders its own "everything is
       current" claim from the same data, so it stays truthful either way.

The GitHub Packages feed needs a token even for public packages. The script
reads it from GITHUB_TOKEN (or GH_TOKEN); it needs the `read:packages` scope.
Without one the mirror check is skipped locally and fails in GitHub Actions.

Usage:
    python scripts/verify_versions.py [--data docs/data/family.yaml] [--owner artur-rios]
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

NUGET_BASE_ADDRESS = "https://api.nuget.org/v3-flatcontainer/"
GITHUB_SERVICE_INDEX = "https://nuget.pkg.github.com/{owner}/index.json"
USER_AGENT = "dotnet-libraries-version-check (+https://github.com/artur-rios/dotnet-libraries)"


def normalise(version: str) -> tuple[int, ...]:
    """NuGet treats 1.0 and 1.0.0 as the same version; so do we."""
    parts = []
    for chunk in version.split("."):
        digits = "".join(c for c in chunk if c.isdigit())
        parts.append(int(digits) if digits else 0)
    while len(parts) < 4:
        parts.append(0)
    return tuple(parts[:4])


def identity(version: str) -> tuple[tuple[int, ...], str]:
    """A version as a registry stores it: numbers plus any prerelease label.

    `normalise` drops labels, which is right for "is this the latest stable"
    but would let 1.0.0-beta stand in for 1.0.0 when comparing registries.
    """
    release, _, label = version.split("+")[0].partition("-")
    return normalise(release), label.lower()


def is_stable(version: str) -> bool:
    return "-" not in version


def fetch_json(url: str, registry: str, headers: dict[str, str] | None = None, attempts: int = 4):
    """GET a JSON document, retrying network flakes. None on 404."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            if exc.code in (401, 403):
                raise SystemExit(
                    f"{registry} refused the request for {url} (HTTP {exc.code}) "
                    f"— the token needs the read:packages scope"
                )
            last_error = exc
        except Exception as exc:  # network flake
            last_error = exc
        time.sleep(2 * (attempt + 1))
    raise SystemExit(f"could not reach {registry} at {url}: {last_error}")


class Registry:
    """A NuGet v3 feed, read through its flat container (PackageBaseAddress)."""

    def __init__(self, name: str, base_address: str, headers: dict[str, str] | None = None):
        self.name = name
        self.base_address = base_address if base_address.endswith("/") else base_address + "/"
        self.headers = headers or {}

    def versions(self, package_id: str) -> list[str]:
        """Every version of a package on this feed, prerelease included."""
        url = f"{self.base_address}{package_id.lower()}/index.json"
        document = fetch_json(url, self.name, self.headers)
        return list(document["versions"]) if document else []


def github_registry(owner: str, token: str) -> Registry:
    # Any username works with a token; the feed only checks the password.
    credentials = base64.b64encode(f"{owner}:{token}".encode()).decode()
    headers = {"Authorization": f"Basic {credentials}"}
    url = GITHUB_SERVICE_INDEX.format(owner=owner)
    index = fetch_json(url, "GitHub Packages", headers)
    if index is None:
        raise SystemExit(f"GitHub Packages has no NuGet feed at {url}")
    for resource in index["resources"]:
        if resource["@type"].startswith("PackageBaseAddress/3.0.0"):
            return Registry("GitHub Packages", resource["@id"], headers)
    raise SystemExit(f"GitHub Packages feed {url} advertises no PackageBaseAddress resource")


def mirror_gaps(package_id: str, nuget: list[str], github: list[str]) -> list[str]:
    """Versions that one registry has and the other does not."""
    on_nuget = {identity(v): v for v in nuget}
    on_github = {identity(v): v for v in github}
    gaps = []
    missing = [on_nuget[k] for k in sorted(on_nuget.keys() - on_github.keys())]
    if missing:
        gaps.append(
            f"`{package_id}` {', '.join(missing)} on nuget.org but not on GitHub Packages "
            f"— re-run the library's publish workflow on those tags"
        )
    extra = [on_github[k] for k in sorted(on_github.keys() - on_nuget.keys())]
    if extra:
        gaps.append(f"`{package_id}` {', '.join(extra)} on GitHub Packages but not on nuget.org")
    return gaps


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="docs/data/family.yaml")
    parser.add_argument("--owner", default="artur-rios", help="GitHub account that owns the packages")
    args = parser.parse_args()

    with open(args.data, encoding="utf-8") as handle:
        family = yaml.safe_load(handle)

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    in_actions = os.environ.get("GITHUB_ACTIONS") == "true"
    if not token and in_actions:
        print("::error::No GITHUB_TOKEN, so GitHub Packages cannot be checked")
        return 1

    nuget = Registry("nuget.org", NUGET_BASE_ADDRESS)
    github = github_registry(args.owner, token) if token else None

    packages = family["packages"]
    errors: list[str] = []
    mirror: list[str] = []
    drift: list[str] = []

    declared: dict[str, str | None] = {}
    for package in packages:
        if package["id"] in declared:
            errors.append(f"`{package['id']}` is defined more than once")
        declared[package["id"]] = package.get("version")

    all_versions: dict[str, list[str]] = {}
    for package in packages:
        all_versions[package["id"]] = nuget.versions(package["id"])
    live = {package_id: [v for v in versions if is_stable(v)] for package_id, versions in all_versions.items()}

    if github:
        for package in packages:
            mirror += mirror_gaps(package["id"], all_versions[package["id"]], github.versions(package["id"]))

    for package in packages:
        package_id = package["id"]
        available = live[package_id]

        if package.get("published") is False:
            # Declared as never released. Assert that is still true, so the day
            # it ships CI says so rather than the site quietly under-reporting.
            if available:
                errors.append(
                    f"`{package_id}` is marked `published: false` but nuget.org has "
                    f"{max(available, key=normalise)} — drop the flag and add `version`"
                )
            continue

        stated = package.get("version")
        if stated is None:
            errors.append(f"`{package_id}` has no `version` and is not marked `published: false`")
            continue

        if not available:
            errors.append(
                f"`{package_id}` says {stated} but is not published on nuget.org "
                f"— add `published: false` if that is deliberate"
            )
            continue

        latest = max(available, key=normalise)
        if normalise(stated) != normalise(latest):
            errors.append(
                f"`{package_id}` says {stated} but nuget.org has {latest} — update `version` in {args.data}"
            )

        for dependency in package.get("deps") or []:
            dep_id = dependency["id"]
            if dep_id not in declared:
                errors.append(f"`{package_id}` depends on `{dep_id}`, which {args.data} does not define")
                continue
            if dependency.get("project"):
                continue  # project reference, no pinned version until pack time
            pinned = dependency.get("version")
            if pinned is None:
                errors.append(f"`{package_id}` pins no version for `{dep_id}` and it is not a project reference")
                continue
            dep_available = live[dep_id]
            if not any(normalise(pinned) == normalise(v) for v in dep_available):
                errors.append(f"`{package_id}` pins `{dep_id}` {pinned}, which is not published")
                continue
            dep_latest = max(dep_available, key=normalise)
            if normalise(pinned) < normalise(dep_latest):
                drift.append(f"`{package_id}` pins `{dep_id}` {pinned}, but {dep_latest} is available")

    registries = "nuget.org and GitHub Packages" if github else "nuget.org"
    lines = [f"Checked {len(packages)} packages against {registries}.", ""]
    if not github:
        lines += ["GitHub Packages not checked: set GITHUB_TOKEN (with read:packages) to include it.", ""]
    if errors:
        lines.append(f"### {len(errors)} error(s) — fix in `{args.data}`")
        lines += [f"- {e}" for e in errors] + [""]
    if mirror:
        lines.append(f"### {len(mirror)} registry gap(s) — fix in the library's repository")
        lines.append("Every release is published to both nuget.org and GitHub Packages.")
        lines += [f"- {m}" for m in mirror] + [""]
    if drift:
        lines.append(f"### {len(drift)} dependency reference(s) behind")
        lines.append("Not a data-file problem: these need a release in the library itself.")
        lines += [f"- {d}" for d in drift] + [""]
    if not errors and not mirror and not drift:
        lines.append("Every package version matches nuget.org, and every family reference is at the latest stable.")
        if github:
            lines.append("GitHub Packages carries every version nuget.org does.")

    report = "\n".join(lines)
    print(report)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(report + "\n")

    for message in drift:
        print(f"::warning::{message.replace('`', '')}")
    for message in errors + mirror:
        print(f"::error::{message.replace('`', '')}")

    return 1 if errors or mirror else 0


if __name__ == "__main__":
    raise SystemExit(main())
