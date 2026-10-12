---
title: NuGet packages
linkTitle: NuGet packages
weight: 60
description: >-
  Every published package, its current version badge, and the one-line install command.
---

Twenty packages across twelve repositories, all targeting `net10.0`. Badges show the version currently
live on nuget.org. Every package is also published to GitHub Packages with the same versions — see
[Use the GitHub feed](#use-the-github-feed).

## Core

{{< package-table "core" >}}

## Application building blocks

{{< package-table "app" >}}

## Data access

Install only the backend you use. All nine packages are published, including
`ArturRios.Data.MySql`, which covers both MySQL and MariaDB.

{{< package-table "data" >}}

## Use the GitHub feed

nuget.org is the default source, so the install commands above need no setup. The same versions are on
[GitHub Packages](https://github.com/artur-rios?tab=packages), whose feed asks for authentication even
for public packages: a personal access token (classic) with the `read:packages` scope. Register the feed
once:

```bash
dotnet nuget add source https://nuget.pkg.github.com/artur-rios/index.json --name artur-rios --username YOUR_GITHUB_USERNAME --password YOUR_TOKEN
```

Add `--store-password-in-clear-text` on Linux and macOS, where NuGet cannot encrypt the password. Then
install from it:

```bash
dotnet add package ArturRios.Output --source artur-rios
```

For a repository or CI, put the feed in a `nuget.config` instead and keep the token in the environment.
In GitHub Actions the workflow's `GITHUB_TOKEN` works, given `packages: read`. The source mapping sends
every `ArturRios.*` package to the GitHub feed and everything else to nuget.org:

```xml
<configuration>
  <packageSources>
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" />
    <add key="artur-rios" value="https://nuget.pkg.github.com/artur-rios/index.json" />
  </packageSources>
  <packageSourceCredentials>
    <artur-rios>
      <add key="Username" value="%GITHUB_ACTOR%" />
      <add key="ClearTextPassword" value="%GITHUB_TOKEN%" />
    </artur-rios>
  </packageSourceCredentials>
  <packageSourceMapping>
    <packageSource key="artur-rios">
      <package pattern="ArturRios.*" />
    </packageSource>
    <packageSource key="nuget.org">
      <package pattern="*" />
    </packageSource>
  </packageSourceMapping>
</configuration>
```

## Versioning

Packages version independently — there is no family-wide version. Each repository releases by pushing a
tag, which triggers its `publish-package.yml` workflow to pack and push to nuget.org and GitHub Packages.

Because versions move separately, a package's family dependencies are pinned to whatever was current when
it was last released, and can fall behind as its dependencies move on. Catching up is a cascade: a
package has to be released before its own dependents can pin the new version, so the family is brought
current in topological waves, from `ArturRios.Output` outward.

As of {{< last-reviewed >}} every family reference is at the latest stable release of its dependency. The
[dependency graph](dependencies/) lists the exact pinned version on each edge.
