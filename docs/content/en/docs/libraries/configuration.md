---
title: ArturRios.Configuration
linkTitle: Configuration
weight: 40
description: >-
  Composable configuration loading from JSON files, environment variables and .env files, with clear precedence.
---

[![Docs](https://img.shields.io/badge/docs-website-blue)](https://artur-rios.github.io/dotnet-configuration)
[![NuGet](https://img.shields.io/nuget/v/ArturRios.Configuration.svg)](https://www.nuget.org/packages/ArturRios.Configuration)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/artur-rios/dotnet-configuration/blob/main/LICENSE)

A lightweight configuration loader built on `Microsoft.Extensions.Configuration`. It composes several
sources — `appsettings` and other JSON files, environment variables, `.env` files — under one simple
precedence rule: **later-added sources override earlier ones**.

## What you get

- `ConfigurationLoader` — composes multiple sources into one configuration.
- `EnvironmentProvider` — environment-specific logic (Development, Production, …).
- `SettingsProvider` — layered settings.
- Enums that name the moving parts: `ConfigurationSourceType`, `DataFormatType`, `EnvironmentType`,
  `OutputType`.
- Extensible: implement your own provider or source.

The same loader backs [`ArturRios.Util.WebApi`](../webapi-util/)'s startup and
[`ArturRios.Util.Test`](../test-util/)'s functional test base, so tests and production read settings the
same way.

## Install

```bash
dotnet add package ArturRios.Configuration
```

## Family dependencies

- [`ArturRios.Extensions`](../extensions/) — and transitively `ArturRios.Util` and `ArturRios.Output`.

Third-party: `DotNetEnv`, `Microsoft.Extensions.*`.

## Links

- **Documentation:** <https://artur-rios.github.io/dotnet-configuration>
- **Repository:** <https://github.com/artur-rios/dotnet-configuration>
- **NuGet:** <https://www.nuget.org/packages/ArturRios.Configuration>
