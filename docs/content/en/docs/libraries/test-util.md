---
title: ArturRios.Util.Test
linkTitle: Test Util
weight: 120
description: >-
  xUnit test support — extra assertions, environment-aware attributes, in-memory fakes and a functional web API test base.
---

[![Docs](https://img.shields.io/badge/docs-website-blue)](https://artur-rios.github.io/dotnet-test-util)
[![NuGet](https://img.shields.io/nuget/v/ArturRios.Util.Test.svg)](https://www.nuget.org/packages/ArturRios.Util.Test)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/artur-rios/dotnet-test-util/blob/main/LICENSE)

The leaf of the [dependency graph](../../dependencies/): a test helper has to know about everything it
fakes, so this package pulls in more of the family than any other.

## What you get

| Component | Role |
|---|---|
| `CustomAssert` | Extra xUnit assertions for null and empty checks on collections and strings. |
| `UnitFactAttribute`, `UnitTheoryAttribute`, `FunctionalFactAttribute`, `FunctionalTheoryAttribute` | Test attributes that skip tests per environment or on a condition, so one suite runs locally and in CI with different reach. |
| In-memory fakes | Repository and scheduler doubles for tests that should not touch infrastructure. |
| Functional web API test base | A base class for end-to-end tests over an ASP.NET Core host, built on `Microsoft.AspNetCore.Mvc.Testing`. |

Test names across the family follow **Given / When / Then**, e.g.
`GivenEveryPool_WhenCombined_ThenAllIsTheirConcatenationWithoutOverlap`. See
[shared patterns](../../patterns/#8-testing-conventions).

## Install

```bash
dotnet add package ArturRios.Util.Test
```

## Family dependencies

- [`ArturRios.Configuration`](../configuration/) 1.1.0
- [`ArturRios.Data.Relational.Core`](../data/) 4.0.0
- [`ArturRios.Mediator`](../mediator/) 1.0.3
- [`ArturRios.Util`](../util/) 2.0.0
- [`ArturRios.Util.WebApi`](../webapi-util/) 3.3.0

Third-party: `xunit`, `Microsoft.AspNetCore.Mvc.Testing`.

## Links

- **Documentation:** <https://artur-rios.github.io/dotnet-test-util>
- **Repository:** <https://github.com/artur-rios/dotnet-test-util>
- **NuGet:** <https://www.nuget.org/packages/ArturRios.Util.Test>
