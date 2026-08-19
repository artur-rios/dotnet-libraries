---
title: ArturRios.Output
linkTitle: Output
weight: 10
description: >-
  The result envelopes the whole family returns — ProcessOutput, DataOutput<T> and PaginatedOutput<T>.
---

[![Docs](https://img.shields.io/badge/docs-website-blue)](https://artur-rios.github.io/dotnet-output)
[![NuGet](https://img.shields.io/nuget/v/ArturRios.Output.svg)](https://www.nuget.org/packages/ArturRios.Output)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/artur-rios/dotnet-output/blob/main/LICENSE)

The root of the family. `ArturRios.Output` standardizes how an operation reports what happened: a success
flag, messages, errors and a UTC timestamp — optionally wrapped around a payload or a page of results.
Every other library that can fail returns one of these types, which is why almost all of them depend on it.

## What you get

| Type | What it does |
|---|---|
| `ProcessOutput` | Messages, errors, timestamp and a `Success` flag (true when there are no errors). Fluent `WithError` / `WithMessage` helpers and a `New` factory. |
| `DataOutput<T>` | `ProcessOutput` plus a typed `Data` payload and `WithData(T)`. |
| `PaginatedOutput<T>` | `DataOutput<List<T>>` plus `PageNumber`, `PageSize`, `TotalItems` and a computed `TotalPages`. |
| `CustomException` | Abstract base for domain exceptions that carry an array of messages. |
| `PaginatedOutputExtensions` | `Paginate` / `PaginateAsync` over `IQueryable<T>`, using EF Core's async provider when available and falling back to synchronous enumeration when not. |

No runtime dependencies beyond `Microsoft.EntityFrameworkCore` for the EF-aware `PaginateAsync` path.

```csharp
var output = DataOutput<User>.New
    .WithData(user)
    .WithMessage("User created");

if (!output.Success) { /* output.Errors has the reasons */ }
```

## Install

```bash
dotnet add package ArturRios.Output
```

## Family dependencies

{{< family-deps "ArturRios.Output" >}}

This is the root of the [dependency graph](../../dependencies/) — everything else layers on top of it.

## Links

- **Documentation:** <https://artur-rios.github.io/dotnet-output>
- **Repository:** <https://github.com/artur-rios/dotnet-output>
- **NuGet:** <https://www.nuget.org/packages/ArturRios.Output>
