---
title: ArturRios.Jwt
linkTitle: JWT
weight: 60
description: >-
  A minimal API for creating, validating and reading JSON Web Tokens, with signing-key rotation.
---

[![Docs](https://img.shields.io/badge/docs-website-blue)](https://artur-rios.github.io/dotnet-jwt)
[![NuGet](https://img.shields.io/nuget/v/ArturRios.Jwt.svg)](https://www.nuget.org/packages/ArturRios.Jwt)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/artur-rios/dotnet-jwt/blob/main/LICENSE)

A clean, minimal token library — and the only member of the family that depends on nothing else in it, so
a service can issue and verify tokens without adopting anything more.

## What you get

- Create signed JWTs (HMAC-SHA256) from a `JwtConfiguration`.
- Validate a token signature against a secret, or against a set of keys.
- **Rotate signing keys** without invalidating tokens already issued.
- Read the user id from the `id` claim, and the `kid` naming the key that signed the token.
- Validate a `JwtConfiguration` with [FluentValidation](https://docs.fluentvalidation.net) rules before
  using it.

[`ArturRios.Util.WebApi`](../webapi-util/) builds on this for its authentication middleware.

## Install

```bash
dotnet add package ArturRios.Jwt
```

## Family dependencies

None.

## Links

- **Documentation:** <https://artur-rios.github.io/dotnet-jwt>
- **Repository:** <https://github.com/artur-rios/dotnet-jwt>
- **NuGet:** <https://www.nuget.org/packages/ArturRios.Jwt>
