---
title: ArturRios.Logging
linkTitle: Logging
weight: 50
description: >-
  Console and file loggers with automatic caller information, custom levels, trace IDs and Microsoft.Extensions.Logging integration.
---

[![Docs](https://img.shields.io/badge/docs-website-blue)](https://artur-rios.github.io/dotnet-logging)
[![NuGet](https://img.shields.io/nuget/v/ArturRios.Logging.svg)](https://www.nuget.org/packages/ArturRios.Logging)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/artur-rios/dotnet-logging/blob/main/LICENSE)

A logging library that works standalone or behind the standard `ILogger` abstractions.

## What you get

- **Console and file loggers**, each separately configurable.
- **Automatic caller information** — file path and method name captured via compiler attributes, so call
  sites stay clean.
- **Seven levels** — Trace, Debug, Information, Warning, Error, Exception, Critical.
- **Colour-coded console output** using ANSI colours, on Windows and Unix alike.
- **Flexible file logging**, including splitting logs across files.
- **Trace ID support** for correlating entries across a distributed call.
- **`Microsoft.Extensions.Logging` integration**, so it drops into ASP.NET Core and anything else that
  speaks `ILogger`.
- **Standalone and state loggers** — use directly, or as part of a larger logging state.

Pairs with [`ArturRios.Util.WebApi`](../webapi-util/), whose middleware propagates a W3C `traceparent`
across a request and its outgoing calls.

## Install

```bash
dotnet add package ArturRios.Logging
```

## Family dependencies

{{< family-deps "ArturRios.Logging" >}}

## Links

- **Documentation:** <https://artur-rios.github.io/dotnet-logging>
- **Repository:** <https://github.com/artur-rios/dotnet-logging>
- **NuGet:** <https://www.nuget.org/packages/ArturRios.Logging>
