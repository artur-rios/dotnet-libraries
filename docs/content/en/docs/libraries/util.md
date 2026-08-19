---
title: ArturRios.Util
linkTitle: Util
weight: 20
description: >-
  General-purpose helpers: hashing, flow control, randomness, files, HTTP, maths, regex and console output.
---

[![Docs](https://img.shields.io/badge/docs-website-blue)](https://artur-rios.github.io/dotnet-util)
[![NuGet](https://img.shields.io/nuget/v/ArturRios.Util.svg)](https://www.nuget.org/packages/ArturRios.Util)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/artur-rios/dotnet-util/blob/main/LICENSE)

The general toolbox: the small pieces that would otherwise be re-copied into every project.

## What you get

- **Hashing** — Argon2id password hashing and verification.
- **Flow control** — conditions, retries with backoff, and waiters.
- **Randomness** — cryptographically strong random values and strings, with character pools
  (`Characters.Digits`, `Characters.UpperLetters`, …).
- **Files** — file and CSV reading helpers.
- **HTTP** — an `HttpGateway` for straightforward typed calls.
- **Maths** — primality tests and prime generation.
- **Text** — regex helpers and string utilities.
- **Console** — `CustomConsole` writers and ANSI colour constants.

```csharp
using ArturRios.Util.Console;

CustomConsole.WriteCharLine();          // 100 dashes
CustomConsole.WriteCharLine('=', 40);   // 40 equals signs
```

## Install

```bash
dotnet add package ArturRios.Util
```

## Family dependencies

- [`ArturRios.Output`](../output/) 3.1.0 — result envelopes.

## Links

- **Documentation:** <https://artur-rios.github.io/dotnet-util>
- **Repository:** <https://github.com/artur-rios/dotnet-util>
- **NuGet:** <https://www.nuget.org/packages/ArturRios.Util>
