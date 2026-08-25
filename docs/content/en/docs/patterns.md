---
title: Shared patterns
linkTitle: Patterns
weight: 40
description: >-
  The design and engineering conventions that repeat across every library in the family.
---

The twelve libraries were written independently but to a shared set of conventions. Knowing them means
knowing most of what any one library will do before you open it.

## 1. Outputs, not exceptions

The defining pattern. Anything that can fail for an expected reason returns an envelope from
[`ArturRios.Output`](libraries/output/) rather than throwing:

- `ProcessOutput` — success flag plus messages, for operations with no return value.
- `DataOutput<T>` — the same, carrying a payload.
- `PaginatedOutput<T>` — a page of results plus its paging metadata.

Validation failures, missing records, optimistic-concurrency conflicts and infrastructure errors all
arrive as errors *on the result*. Exceptions are reserved for genuine defects. This is why `Output` is the
root of the [dependency graph](dependencies/): almost every other library needs it in its signatures.

```csharp
DataOutput<User> result = await repository.GetById(id);

if (!result.Success)
{
    return ResponseResolver.Resolve(result); // 400 with the messages
}
```

## 2. One capability, one package

Nothing is bundled "for convenience". Each concern lives in its own repository and NuGet package, and
where a single repository covers several backends — [`ArturRios.Data`](libraries/data/) — each backend is
still its own package. Adding SQLite support does not pull in the MongoDB or AWS SDKs.

The cost is a slightly larger dependency list; the benefit is that no application carries code it does
not run.

## 3. A core plus interchangeable providers

Where several implementations of one idea exist, a `*.Core` package defines the abstraction and the
provider packages supply the implementations:

- `ArturRios.Data.Relational.Core` holds the repository contracts and envelope handling;
  `PostgreSql`, `MySql`, `Sqlite` and `Dapper` plug into it.
- `ArturRios.Data.Export` defines the writer abstraction; `Export.Excel` adds a format.
- `ArturRios.Configuration` composes providers (`EnvironmentProvider`, `SettingsProvider`) over
  `Microsoft.Extensions.Configuration`.

Swapping a database or a file format is a package reference and a registration, not a rewrite.

## 4. Composition over the built-in container

Registration always uses the standard `IServiceCollection`; none of the libraries introduce a container
of their own. [`ArturRios.Mediator`](libraries/mediator/) is the clearest example — it dispatches each
command or query to a handler resolved from a **fresh DI scope**, so scoped dependencies such as a
`DbContext` are isolated per execution rather than shared across a request.

The same instinct shows up as small, overridable hooks: `WebApiStartup` in
[`ArturRios.Util.WebApi`](libraries/webapi-util/) wires configuration, Swagger and the middleware
pipeline behind virtual methods you override only where you differ.

## 5. Validation as a first-class result

[`ArturRios.Validation`](libraries/validation/) wraps FluentValidation's `AbstractValidator<T>` in a
`FluentValidator<T>` that returns what an application actually consumes: a `string[]` of messages, or a
`ProcessOutput` / `DataOutput<T>`. Validation results therefore flow through the same envelope as
everything else, and validators are injectable behind `IFluentValidator<T>`.

## 6. Configuration from layered sources

Configuration is loaded rather than assumed. `ConfigurationLoader` composes JSON files, environment
variables and `.env` files with a single precedence rule — later sources override earlier ones — and the
same loader is used by the web API startup and by the functional test base, so tests and production read
their settings the same way.

## 7. Diagnostics that cross process boundaries

[`ArturRios.Logging`](libraries/logging/) captures caller file and method automatically via compiler
attributes and carries a trace ID; [`ArturRios.Util.WebApi`](libraries/webapi-util/) propagates a W3C
`traceparent` through the request and onto outgoing calls with `TraceActivityMiddleware` and
`TracePropagationHandler`. Correlation is a convention of the family, not per-service wiring.

## 8. Testing conventions

- Test names follow **Given / When / Then**, without exception:
  `GivenSpecial_WhenInspected_ThenContainNoDuplicatesAndNoWhitespace`.
- xUnit throughout, with [`ArturRios.Util.Test`](libraries/test-util/) supplying extra assertions,
  in-memory repository and scheduler fakes, and a base class for functional web API tests.
- **Every test class carries a `Category` trait**, either `Unit` or `Functional`, so the two kinds can be
  run and reported separately:

  ```bash
  dotnet test <solution> --filter "Category=Unit"
  dotnet test <solution> --filter "Category=Functional"
  ```

  A unit test exercises code in isolation against test doubles. A functional test reaches something real:
  the file system, a loopback HTTP server, an in-memory ASP.NET Core host, SQLite, an ephemeral MongoDB
  replica set, DynamoDB Local.

- A repository adds a third category, `Integration`, when a test needs a server the suite cannot
  provision itself. Today only [`ArturRios.Data`](libraries/data/) has one: its MySQL tests read a
  connection string from `ARTURRIOS_DATA_MYSQL_TEST_CONNECTION` and skip when it is unset, and CI
  supplies MySQL as a service container.

- The `UnitFactAttribute`, `UnitTheoryAttribute`, `FunctionalFactAttribute` and
  `FunctionalTheoryAttribute` in [`ArturRios.Util.Test`](libraries/test-util/) stamp that same `Category`
  trait, and additionally let a suite skip tests per environment or condition. A repository that cannot
  reference the package — anything `ArturRios.Util.Test` itself depends on — puts a plain
  `[Trait("Category", "Unit")]` on the class instead. Both filter identically.

## 9. Repository layout

Every repository is laid out the same way:

```text
src/      the library (and its .sln)
tests/    xUnit test projects
docs/     the Hugo + Docsy documentation site
README.md overview, install, usage
LICENSE   MIT
```

## 10. Identical CI

Three GitHub Actions workflows per repository:

| Workflow | Trigger | What it does |
|---|---|---|
| `run-tests.yml` | pushes and pull requests | Two jobs — **Unit tests** and **Functional tests** — each restoring, building and running its half of the suite, and each uploading its own `trx` artifact. `ArturRios.Data` adds a third, **Integration tests**, against a MySQL service container. |
| `build-docs-and-coverage-report.yml` | pushes to `main` touching `src/`, `tests/` or `docs/` | Runs tests with coverage, generates the coverage report, builds the Hugo site and deploys it to GitHub Pages. In `ArturRios.Data` it also runs on pull requests as a check, deploying only on `main`. |
| `publish-package.yml` | pushing a tag | Packs and pushes to nuget.org and GitHub Packages. |

Documentation is therefore never stale relative to `main`, and a release is a tag.

Splitting the run into separate jobs rather than steps means the run graph shows which half failed before
anything is opened, and it lets both be required independently.

## 12. Protected `main`

Every repository's `main` is protected the same way:

- a pull request is required — nothing is pushed to `main` directly;
- **Unit tests** and **Functional tests** must both pass — and **Integration tests** too, where the
  repository has them;
- one approving review is required;
- force pushes and branch deletion are refused.

Administrators are not subject to the rules, so the repository owner keeps a bypass; nobody else has one.

## 11. Consistent packaging metadata

Every package targets `net10.0`, is MIT licensed, ships XML documentation
(`<DocumentationFile>`), and carries a `<PackageId>` under the `ArturRios.*` prefix with a
`<Description>` that matches the README's opening line. Versions move independently per package —
there is no lockstep family version.
