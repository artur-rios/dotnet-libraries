#!/usr/bin/env python3
"""Verify docs/data/family.yaml against what is actually published on nuget.org.

Two kinds of finding, deliberately treated differently:

ERROR  something this repository can fix by editing the data file — a package's
       `version` is not the latest stable on nuget.org, a pinned dependency
       version was never published, a dependency names a package the file does
       not define, or an id appears twice. These fail the build.

DRIFT  something only another repository can fix — a package pins a dependency
       version older than that dependency's current release. That is a fact
       about the libraries, not a mistake in the data file, so it is reported
       but does not fail: a docs deploy should not be blocked because an
       unrelated library is behind. The site renders its own "everything is
       current" claim from the same data, so it stays truthful either way.

Usage:
    python scripts/verify_versions.py [--data docs/data/family.yaml]
"""

from __future__ import annotations

import argparse
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

FLAT_CONTAINER = "https://api.nuget.org/v3-flatcontainer/{id}/index.json"
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


def published_versions(package_id: str, attempts: int = 4) -> list[str]:
    """Every stable version of a package on nuget.org, oldest first."""
    url = FLAT_CONTAINER.format(id=package_id.lower())
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                versions = json.load(response)["versions"]
            return [v for v in versions if "-" not in v]
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return []
            last_error = exc
        except Exception as exc:  # network flake
            last_error = exc
        time.sleep(2 * (attempt + 1))
    raise SystemExit(f"could not reach nuget.org for {package_id}: {last_error}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="docs/data/family.yaml")
    args = parser.parse_args()

    with open(args.data, encoding="utf-8") as handle:
        family = yaml.safe_load(handle)

    packages = family["packages"]
    errors: list[str] = []
    drift: list[str] = []

    declared: dict[str, str | None] = {}
    for package in packages:
        if package["id"] in declared:
            errors.append(f"`{package['id']}` is defined more than once")
        declared[package["id"]] = package.get("version")

    live: dict[str, list[str]] = {}
    for package in packages:
        live[package["id"]] = published_versions(package["id"])

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

    lines = [f"Checked {len(packages)} packages against nuget.org.", ""]
    if errors:
        lines.append(f"### {len(errors)} error(s) — fix in `{args.data}`")
        lines += [f"- {e}" for e in errors] + [""]
    if drift:
        lines.append(f"### {len(drift)} dependency reference(s) behind")
        lines.append("Not a data-file problem: these need a release in the library itself.")
        lines += [f"- {d}" for d in drift] + [""]
    if not errors and not drift:
        lines.append("Every package version matches nuget.org, and every family reference is at the latest stable.")

    report = "\n".join(lines)
    print(report)

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(report + "\n")

    for message in drift:
        print(f"::warning::{message.replace('`', '')}")
    for message in errors:
        print(f"::error::{message.replace('`', '')}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
