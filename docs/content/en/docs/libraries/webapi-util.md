---
title: ArturRios.Util.WebApi
linkTitle: Web API Util
weight: 110
description: >-
  ASP.NET Core plumbing — startup, token authentication, middleware, typed HTTP clients and response resolution.
---

[![Docs](https://img.shields.io/badge/docs-website-blue)](https://artur-rios.github.io/dotnet-webapi-util)
[![NuGet](https://img.shields.io/nuget/v/ArturRios.Util.WebApi.svg)](https://www.nuget.org/packages/ArturRios.Util.WebApi)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/artur-rios/dotnet-webapi-util/blob/main/LICENSE)

Where the family comes together for a service: it bootstraps the host with
[`ArturRios.Configuration`](../configuration/), authenticates with [`ArturRios.Jwt`](../jwt/), and turns
[`ArturRios.Output`](../output/) envelopes into `ActionResult`s.

## What you get

| Area | What it does |
|---|---|
| **Configuration / bootstrap** | `WebApiStartup` wires configuration loading, Swagger and the middleware pipeline behind a small set of virtual hooks; `WebApiParameters` parses command-line startup args. [Docs](https://artur-rios.github.io/dotnet-webapi-util/configuration/) |
| **Security** | `AuthenticationMiddleware` reads a token from the header, a cookie, or either; validates it as the app's own JWT and/or a Google ID token; and attaches an `IAuthenticatedUser` in stateless (`ClaimsOnly`) or per-request-revalidated mode. `[Authorize]`, `[AllowAnonymous]` and `[RoleRequirement(...)]` declare access rules. [Docs](https://artur-rios.github.io/dotnet-webapi-util/security/) |
| **Middleware & diagnostics** | `ExceptionMiddleware` turns unhandled exceptions into a JSON error envelope; `TraceActivityMiddleware` and `TracePropagationHandler` propagate a W3C `traceparent` across a request and its outgoing calls. [Docs](https://artur-rios.github.io/dotnet-webapi-util/middleware-and-diagnostics/) |
| **HTTP client** | `BaseWebApiClient` / `BaseWebApiClientRoute` give a typed client a shared `HttpGateway`, route grouping, and helpers to authenticate and carry the resulting bearer token on later calls. [Docs](https://artur-rios.github.io/dotnet-webapi-util/http-client/) |
| **Responses** | `ResponseResolver.Resolve(...)` wraps `DataOutput<T>`, `PaginatedOutput<T>` and `ProcessOutput` in an `ActionResult`, defaulting to 200/400 on `Success` unless a status code is supplied. [Docs](https://artur-rios.github.io/dotnet-webapi-util/responses/) |

## Install

```bash
dotnet add package ArturRios.Util.WebApi
```

## Family dependencies

- [`ArturRios.Configuration`](../configuration/) 1.1.0
- [`ArturRios.Jwt`](../jwt/) 1.1.0
- [`ArturRios.Util`](../util/) 2.0.0

…and transitively `ArturRios.Extensions` and `ArturRios.Output`.

## Links

- **Documentation:** <https://artur-rios.github.io/dotnet-webapi-util>
- **Repository:** <https://github.com/artur-rios/dotnet-webapi-util>
- **NuGet:** <https://www.nuget.org/packages/ArturRios.Util.WebApi>
