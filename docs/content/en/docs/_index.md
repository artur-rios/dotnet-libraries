---
title: Documentation
linkTitle: Documentation
weight: 10
description: >-
  An index of the ArturRios .NET library family: what each library does, how they depend on each other,
  the patterns they share, and where to find their repositories and packages.
---

The **ArturRios** family is a set of twelve small .NET libraries, each in its own repository, each
published to NuGet, and each with its own documentation site. They are designed to be used
independently — but they were written together, so they share a vocabulary: the same result envelope,
the same configuration loader, the same test helpers.

This site is the map. It does not replace the per-library documentation; it tells you which library you
want and sends you there.

## Where to go

| If you want to… | Go to |
|---|---|
| Read a one-page summary of every library | [Libraries](libraries/) |
| See how the packages depend on each other | [Dependency graph](dependencies/) |
| Understand the ideas that repeat across the family | [Shared patterns](patterns/) |
| Find a GitHub repository | [Repositories](repositories/) |
| Find a NuGet package | [NuGet packages](packages/) |

## The family at a glance

All libraries target **.NET 10 (`net10.0`)** and are MIT licensed.

| Library | Package(s) | What it is |
|---|---|---|
| [Output](libraries/output/) | `ArturRios.Output` | The result envelopes — `ProcessOutput`, `DataOutput<T>`, `PaginatedOutput<T>` — that the rest of the family returns. |
| [Util](libraries/util/) | `ArturRios.Util` | General-purpose helpers: hashing, retries, randomness, files, HTTP, regex, console. |
| [Extensions](libraries/extensions/) | `ArturRios.Extensions` | Extension methods for strings, enums, collections, dates, numbers and exceptions. |
| [Configuration](libraries/configuration/) | `ArturRios.Configuration` | Composable configuration loading from JSON, environment variables and `.env` files. |
| [Logging](libraries/logging/) | `ArturRios.Logging` | Console and file loggers with caller info, trace IDs and `Microsoft.Extensions.Logging` integration. |
| [JWT](libraries/jwt/) | `ArturRios.Jwt` | Creating, validating and reading JSON Web Tokens, with key rotation. |
| [Validation](libraries/validation/) | `ArturRios.Validation` | A FluentValidation base class that returns error arrays or `Output` envelopes. |
| [Mediator](libraries/mediator/) | `ArturRios.Mediator` | CQRS-style command/query dispatch over the built-in DI container. |
| [Messaging](libraries/messaging/) | `ArturRios.Messaging` | Messaging formats and protocols; currently a Mailgun email service. |
| [Data](libraries/data/) | 9 packages | A modular data-access toolkit: EF Core, Dapper, MongoDB, DynamoDB and file export. |
| [Web API Util](libraries/webapi-util/) | `ArturRios.Util.WebApi` | ASP.NET Core plumbing: startup, authentication, middleware, typed clients, response resolution. |
| [Test Util](libraries/test-util/) | `ArturRios.Util.Test` | xUnit assertions, environment-aware attributes, in-memory fakes and a functional web API test base. |
