# Dotnet Libraries

> [!NOTE]
> This is the real, open-source code of dotnet-libraries. Its home is Forgejo, at
> https://git.techcraftsmen.net/artur-rios/dotnet-libraries; the copy on GitHub is a read-only mirror, for viewing only, and
> its issues and pull requests are not followed. If you want to contribute, email me at
> arturdev@duck.com.

[![Docs](https://img.shields.io/badge/docs-website-blue)](https://docs.artur-rios.tech/dotnet-libraries)
[![License: Attribution](https://img.shields.io/badge/License-Attribution-blue.svg)](./LICENSE)

The index of the **ArturRios** .NET library family — twelve libraries, twenty NuGet packages, one set of
conventions. This repository holds no code: it is the map, and the source of the site at
<https://docs.artur-rios.tech/dotnet-libraries>.

This repository lives at <https://git.techcraftsmen.net/artur-rios/dotnet-libraries>. The GitHub repository is a read-only mirror of it.

- 📚 **Site:** <https://docs.artur-rios.tech/dotnet-libraries>
- 🧩 **Dependency graph:** <https://docs.artur-rios.tech/dotnet-libraries/docs/dependencies/>
- 📐 **Shared patterns:** <https://docs.artur-rios.tech/dotnet-libraries/docs/patterns/>

## The libraries

All target **.NET 10 (`net10.0`)** and are licensed under the Artur Rios Attribution License. Each lives in its own repository, with its own
tests, its own Docsy documentation site and its own release cadence.

| Library | Repository | Docs | NuGet |
|---|---|---|---|
| Output | [dotnet-output](https://github.com/artur-rios/dotnet-output) | [Docs](https://docs.artur-rios.tech/dotnet-output) | [![NuGet](https://img.shields.io/nuget/v/ArturRios.Output.svg?label=ArturRios.Output)](https://www.nuget.org/packages/ArturRios.Output) |
| Util | [dotnet-util](https://github.com/artur-rios/dotnet-util) | [Docs](https://docs.artur-rios.tech/dotnet-util) | [![NuGet](https://img.shields.io/nuget/v/ArturRios.Util.svg?label=ArturRios.Util)](https://www.nuget.org/packages/ArturRios.Util) |
| Extensions | [dotnet-extensions](https://github.com/artur-rios/dotnet-extensions) | [Docs](https://docs.artur-rios.tech/dotnet-extensions) | [![NuGet](https://img.shields.io/nuget/v/ArturRios.Extensions.svg?label=ArturRios.Extensions)](https://www.nuget.org/packages/ArturRios.Extensions) |
| Configuration | [dotnet-configuration](https://github.com/artur-rios/dotnet-configuration) | [Docs](https://docs.artur-rios.tech/dotnet-configuration) | [![NuGet](https://img.shields.io/nuget/v/ArturRios.Configuration.svg?label=ArturRios.Configuration)](https://www.nuget.org/packages/ArturRios.Configuration) |
| Logging | [dotnet-logging](https://github.com/artur-rios/dotnet-logging) | [Docs](https://docs.artur-rios.tech/dotnet-logging) | [![NuGet](https://img.shields.io/nuget/v/ArturRios.Logging.svg?label=ArturRios.Logging)](https://www.nuget.org/packages/ArturRios.Logging) |
| JWT | [dotnet-jwt](https://github.com/artur-rios/dotnet-jwt) | [Docs](https://docs.artur-rios.tech/dotnet-jwt) | [![NuGet](https://img.shields.io/nuget/v/ArturRios.Jwt.svg?label=ArturRios.Jwt)](https://www.nuget.org/packages/ArturRios.Jwt) |
| Validation | [dotnet-validation](https://github.com/artur-rios/dotnet-validation) | [Docs](https://docs.artur-rios.tech/dotnet-validation) | [![NuGet](https://img.shields.io/nuget/v/ArturRios.Validation.svg?label=ArturRios.Validation)](https://www.nuget.org/packages/ArturRios.Validation) |
| Mediator | [dotnet-mediator](https://github.com/artur-rios/dotnet-mediator) | [Docs](https://docs.artur-rios.tech/dotnet-mediator) | [![NuGet](https://img.shields.io/nuget/v/ArturRios.Mediator.svg?label=ArturRios.Mediator)](https://www.nuget.org/packages/ArturRios.Mediator) |
| Messaging | [dotnet-messaging](https://github.com/artur-rios/dotnet-messaging) | [Docs](https://docs.artur-rios.tech/dotnet-messaging) | [![NuGet](https://img.shields.io/nuget/v/ArturRios.Messaging.svg?label=ArturRios.Messaging)](https://www.nuget.org/packages/ArturRios.Messaging) |
| Data | [dotnet-data](https://github.com/artur-rios/dotnet-data) | [Docs](https://docs.artur-rios.tech/dotnet-data) | [9 packages](https://docs.artur-rios.tech/dotnet-libraries/docs/packages/#data-access) |
| Web API Util | [dotnet-webapi-util](https://github.com/artur-rios/dotnet-webapi-util) | [Docs](https://docs.artur-rios.tech/dotnet-webapi-util) | [![NuGet](https://img.shields.io/nuget/v/ArturRios.Util.WebApi.svg?label=ArturRios.Util.WebApi)](https://www.nuget.org/packages/ArturRios.Util.WebApi) |
| Test Util | [dotnet-test-util](https://github.com/artur-rios/dotnet-test-util) | [Docs](https://docs.artur-rios.tech/dotnet-test-util) | [![NuGet](https://img.shields.io/nuget/v/ArturRios.Util.Test.svg?label=ArturRios.Util.Test)](https://www.nuget.org/packages/ArturRios.Util.Test) |

## Installing

Every package is published to [nuget.org](https://www.nuget.org/profiles/artur-rios), which is the default
source, so nothing needs configuring. GitHub Packages is no longer published; use nuget.org.

```bash
dotnet add package ArturRios.Output
```

## How they depend on each other

Family dependencies only; third-party packages are listed on each library's own site.

```mermaid
flowchart BT
    Output["<b>ArturRios.Output</b>"]
    Util["ArturRios.Util"]
    Extensions["ArturRios.Extensions"]
    Configuration["ArturRios.Configuration"]
    Logging["ArturRios.Logging"]
    Jwt["ArturRios.Jwt"]
    Validation["ArturRios.Validation"]
    Mediator["ArturRios.Mediator"]
    Messaging["ArturRios.Messaging"]
    Data["ArturRios.Data.*"]
    WebApi["ArturRios.Util.WebApi"]
    TestUtil["ArturRios.Util.Test"]

    Util --> Output
    Validation --> Output
    Mediator --> Output
    Messaging --> Output
    Data --> Output
    Extensions --> Util
    Configuration --> Extensions
    Logging --> Extensions
    Logging --> Util
    WebApi --> Configuration
    WebApi --> Jwt
    WebApi --> Util
    TestUtil --> Configuration
    TestUtil --> Mediator
    TestUtil --> Util
    TestUtil --> WebApi
    TestUtil --> Data
```

`ArturRios.Output` is the root — almost everything needs it in its signatures. `ArturRios.Jwt` is
deliberately standalone. The full graph, including the nine `Data` packages, is on the
[dependencies page](https://docs.artur-rios.tech/dotnet-libraries/docs/dependencies/).

## The patterns

These are the ideas that repeat across the family; the
[patterns page](https://docs.artur-rios.tech/dotnet-libraries/docs/patterns/) covers them in full.

1. **Outputs, not exceptions.** Anything that can fail for an expected reason returns a `ProcessOutput`,
   `DataOutput<T>` or `PaginatedOutput<T>` envelope. Validation failures, missing records and
   optimistic-concurrency conflicts arrive as errors *on the result*; exceptions are for genuine defects.
2. **One capability, one package.** Nothing is bundled for convenience. Even within `ArturRios.Data`,
   each backend is a separate package, so SQLite support does not drag in the MongoDB or AWS SDKs.
3. **A core plus interchangeable providers.** `*.Core` packages define the abstraction and provider
   packages supply the implementations — `Relational.Core` with PostgreSQL / MySQL / SQLite / Dapper,
   `Export` with `Export.Excel`, `Configuration` with its source providers.
4. **Composition over the built-in container.** Registration always uses the standard
   `IServiceCollection`. `ArturRios.Mediator` resolves each handler from a *fresh DI scope*, so scoped
   dependencies like a `DbContext` are isolated per execution.
5. **Validation as a first-class result.** `FluentValidator<T>` turns FluentValidation results into a
   `string[]` or an `Output` envelope, behind an injectable `IFluentValidator<T>`.
6. **Configuration from layered sources.** `ConfigurationLoader` composes JSON, environment variables and
   `.env` files under one rule: later sources override earlier ones — and the same loader backs both the
   web API startup and the functional test base.
7. **Diagnostics that cross process boundaries.** Caller info and trace IDs in `ArturRios.Logging`; W3C
   `traceparent` propagation through `ArturRios.Util.WebApi` middleware and outgoing calls.
8. **Given / When / Then tests.** xUnit throughout, with `ArturRios.Util.Test` supplying assertions,
   in-memory fakes and environment-aware attributes. Every test class carries a `Category` trait —
   `Unit` or `Functional` — so the two kinds run and report separately. `ArturRios.Data` adds a third,
   `Integration`, for tests that need a server the suite cannot provision (MySQL).
9. **Identical repository layout.** `src/`, `tests/`, `docs/`, `README.md`, `LICENSE`.
10. **Identical CI.** A `yggdrasil.yml` with the same two checks, `test` (format, build, and the tests by
    category) and `coverage` (the tests again, with the HTML coverage report), run by Jenkins on pull requests
    (`ArturRios.Data` runs its MySQL integration tests with Docker); the docs site, with the coverage report, built
    and served at `docs.artur-rios.tech/<library>/`; and `publish.nuget`, which packs and pushes to nuget.org when
    the owner pushes an annotated tag on `main`. Renovate keeps the dependencies up to date.
11. **Consistent packaging metadata.** `net10.0`, the Artur Rios Attribution License (packed `LICENSE` file), XML docs, an `ArturRios.*` package id, and
    independent per-package versions — there is no lockstep family version.

## Building this site

The site is Hugo with the [Docsy](https://www.docsy.dev/) theme, installed as an npm package.

```bash
git clone https://git.techcraftsmen.net/artur-rios/dotnet-libraries.git
cd dotnet-libraries/docs
npm ci
npm run serve
```

`npm run build` produces the static site in `docs/public`. The site is served at
<https://docs.artur-rios.tech/dotnet-libraries/>: the [`Dockerfile`](Dockerfile) builds it with the address it is
served at (`PUBLIC_HOST` and `PUBLIC_PATH`) and serves it with static-web-server, and Jenkins builds and deploys that image
when `main` changes. The bare address, <https://docs.artur-rios.tech/>, redirects here.

The `verify` check (`ci/verify.sh`) runs `scripts/verify_versions.py` when `docs/data/family.yaml` or the script changes: it
compares the versions in the data file with nuget.org.

## Protected `main`

Every repository's `main` requires a pull request and the checks — **test** and **coverage**, and the branch policy — to pass. Only
`release/*` branches can be merged into it, and a release branch's version must match the library's `<Version>` (the
release-version gate; `ArturRios.Data` versions each package apart and has no such gate). Force pushes and branch
deletion are refused.

## Contributing

Open the issue or pull request on the repository of the library it concerns. Anything about the family as
a whole — a wrong dependency edge, a pattern worth documenting — belongs here.

## Legal

This project is licensed under the [Artur Rios Attribution License](./LICENSE). It is free and open source: you may view, use, fork, modify, and extend it, provided you credit the author, Artur Rios, with a link to [artur-rios.tech](https://artur-rios.tech) or [github.com/artur-rios](https://github.com/artur-rios). Copyright © Artur Rios.
