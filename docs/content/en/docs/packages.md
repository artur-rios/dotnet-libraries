---
title: NuGet packages
linkTitle: NuGet packages
weight: 60
description: >-
  Every published package, its current version badge, and the one-line install command.
---

Twenty packages across twelve repositories, all targeting `net10.0`. Badges show the version currently
live on nuget.org, which is the feed: the install commands below need no setup. GitHub Packages is no longer
published; use nuget.org.

## Core

{{< package-table "core" >}}

## Application building blocks

{{< package-table "app" >}}

## Data access

Install only the backend you use. All nine packages are published, including
`ArturRios.Data.MySql`, which covers both MySQL and MariaDB.

{{< package-table "data" >}}

## Versioning

Packages version independently — there is no family-wide version. Each repository releases when its owner pushes an
annotated tag on `main` (`<version>`, or `<PackageId>@<version>` for `dotnet-data`, whose packages each have a version of
their own); Jenkins packs the package at the tag's version and pushes it to nuget.org.

Because versions move separately, a package's family dependencies are pinned to whatever was current when
it was last released, and can fall behind as its dependencies move on. Catching up is a cascade: a
package has to be released before its own dependents can pin the new version, so the family is brought
current in topological waves, from `ArturRios.Output` outward.

As of {{< last-reviewed >}} every family reference is at the latest stable release of its dependency. The
[dependency graph](dependencies/) lists the exact pinned version on each edge.
