#!/usr/bin/env bash
# The `verify` check: docs/data/family.yaml against nuget.org (scripts/verify_versions.py). It ports the verify job of
# verify-versions.yml. yggdrasil.yml runs it in the pinned Python image from the repository's root, and it runs the
# same on your machine with Python 3 and network access.
#
# The check is path-filtered (`paths` in yggdrasil.yml): it runs when the data file, the script or this file changes.
# The GitHub Packages comparison and the weekly run of the old workflow are gone with the GitHub feed.
set -euo pipefail

# The repository's root, wherever this is run from.
cd "$(dirname "${BASH_SOURCE[0]}")/.."

# renovate: datasource=pypi depName=pyyaml
PYYAML_VERSION=6.0.3

# A virtual environment of its own: the image's Python is not written to, and the run needs no particular user or
# home directory.
venv="$(mktemp -d)"
trap 'rm -rf "$venv"' EXIT
python3 -m venv "$venv"
"$venv/bin/pip" install --quiet --disable-pip-version-check --retries 5 "pyyaml==$PYYAML_VERSION"

"$venv/bin/python" scripts/verify_versions.py
