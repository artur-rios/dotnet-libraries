---
title: ArturRios.Validation
linkTitle: Validation
weight: 70
description: >-
  A thin, opinionated model-validation layer over FluentValidation that returns error arrays or Output envelopes.
---

[![Docs](https://img.shields.io/badge/docs-website-blue)](https://artur-rios.github.io/dotnet-validation)
[![NuGet](https://img.shields.io/nuget/v/ArturRios.Validation.svg)](https://www.nuget.org/packages/ArturRios.Validation)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/artur-rios/dotnet-validation/blob/main/LICENSE)

FluentValidation gives you a `ValidationResult`; applications want either a list of messages or a result
envelope. `ArturRios.Validation` closes that gap.

## What you get

| Type | What it does |
|---|---|
| `FluentValidator<T>` | Base validator — subclass it, declare `RuleFor(...)` rules in the constructor, and get error and `Output` helpers for free. |
| `IFluentValidator<T>` | Abstraction over `FluentValidator<T>` (extending the FluentValidation `IValidator<T>`) for DI and testing. |

Validation results come back as a plain `string[]`, or as a `ProcessOutput` / `DataOutput<T>` from
[`ArturRios.Output`](../output/) — with optional stripping of the quotes and periods FluentValidation puts
in its default messages.

## Install

```bash
dotnet add package ArturRios.Validation
```

## Family dependencies

- [`ArturRios.Output`](../output/) 3.1.0

Third-party: [FluentValidation](https://docs.fluentvalidation.net/).

## Links

- **Documentation:** <https://artur-rios.github.io/dotnet-validation>
- **Repository:** <https://github.com/artur-rios/dotnet-validation>
- **NuGet:** <https://www.nuget.org/packages/ArturRios.Validation>
