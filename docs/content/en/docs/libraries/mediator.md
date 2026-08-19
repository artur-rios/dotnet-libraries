---
title: ArturRios.Mediator
linkTitle: Mediator
weight: 80
description: >-
  CQRS-style command and query dispatch on top of the built-in dependency injection container.
---

[![Docs](https://img.shields.io/badge/docs-website-blue)](https://artur-rios.github.io/dotnet-mediator)
[![NuGet](https://img.shields.io/nuget/v/ArturRios.Mediator.svg)](https://www.nuget.org/packages/ArturRios.Mediator)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/artur-rios/dotnet-mediator/blob/main/LICENSE)

A lightweight implementation of the [Mediator pattern](https://refactoring.guru/design-patterns/mediator)
giving a clean CQRS-style separation between **commands** (writes) and **queries** (reads) — with no
container of its own.

## What you get

- `CommandMediator`, `QueryMediator`, and a combined `CommandQueryMediator` entry point.
- Each command or query is dispatched to a dedicated handler **resolved from a fresh DI scope**, so scoped
  dependencies such as a `DbContext` are isolated per execution rather than shared across a request.
- Synchronous and asynchronous variants for every handler type.
- Handlers return `DataOutput<T>` / `PaginatedOutput<T>` envelopes from [`ArturRios.Output`](../output/).

```csharp
builder.Services.AddSingleton<CommandQueryMediator>();
// then register each handler
```

## Install

```bash
dotnet add package ArturRios.Mediator
```

## Family dependencies

- [`ArturRios.Output`](../output/)

## Links

- **Documentation:** <https://artur-rios.github.io/dotnet-mediator>
- **Repository:** <https://github.com/artur-rios/dotnet-mediator>
- **NuGet:** <https://www.nuget.org/packages/ArturRios.Mediator>
