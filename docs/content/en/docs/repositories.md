---
title: Repositories
linkTitle: Repositories
weight: 50
description: >-
  Every repository in the family, with its documentation site and issue tracker.
---

All repositories are hosted at [git.techcraftsmen.net/artur-rios](https://git.techcraftsmen.net/artur-rios), and GitHub
([github.com/artur-rios](https://github.com/artur-rios)) is a read-only mirror of them. They are licensed under the Artur Rios Attribution License.
The links below go to the mirror.
Each has the same layout — `src/`, `tests/`, `docs/` — and the same pipeline: a `yggdrasil.yml` with the `test` and `coverage` checks, a docs site served at
`docs.artur-rios.tech/<library>/`, and releases by an annotated tag on `main`.

| Library | Repository | Documentation | Issues |
|---|---|---|---|
| Output | [dotnet-output](https://github.com/artur-rios/dotnet-output) | [Docs](https://docs.artur-rios.tech/dotnet-output) | [Issues](https://github.com/artur-rios/dotnet-output/issues) |
| Util | [dotnet-util](https://github.com/artur-rios/dotnet-util) | [Docs](https://docs.artur-rios.tech/dotnet-util) | [Issues](https://github.com/artur-rios/dotnet-util/issues) |
| Extensions | [dotnet-extensions](https://github.com/artur-rios/dotnet-extensions) | [Docs](https://docs.artur-rios.tech/dotnet-extensions) | [Issues](https://github.com/artur-rios/dotnet-extensions/issues) |
| Configuration | [dotnet-configuration](https://github.com/artur-rios/dotnet-configuration) | [Docs](https://docs.artur-rios.tech/dotnet-configuration) | [Issues](https://github.com/artur-rios/dotnet-configuration/issues) |
| Logging | [dotnet-logging](https://github.com/artur-rios/dotnet-logging) | [Docs](https://docs.artur-rios.tech/dotnet-logging) | [Issues](https://github.com/artur-rios/dotnet-logging/issues) |
| JWT | [dotnet-jwt](https://github.com/artur-rios/dotnet-jwt) | [Docs](https://docs.artur-rios.tech/dotnet-jwt) | [Issues](https://github.com/artur-rios/dotnet-jwt/issues) |
| Validation | [dotnet-validation](https://github.com/artur-rios/dotnet-validation) | [Docs](https://docs.artur-rios.tech/dotnet-validation) | [Issues](https://github.com/artur-rios/dotnet-validation/issues) |
| Mediator | [dotnet-mediator](https://github.com/artur-rios/dotnet-mediator) | [Docs](https://docs.artur-rios.tech/dotnet-mediator) | [Issues](https://github.com/artur-rios/dotnet-mediator/issues) |
| Messaging | [dotnet-messaging](https://github.com/artur-rios/dotnet-messaging) | [Docs](https://docs.artur-rios.tech/dotnet-messaging) | [Issues](https://github.com/artur-rios/dotnet-messaging/issues) |
| Data | [dotnet-data](https://github.com/artur-rios/dotnet-data) | [Docs](https://docs.artur-rios.tech/dotnet-data) | [Issues](https://github.com/artur-rios/dotnet-data/issues) |
| Web API Util | [dotnet-webapi-util](https://github.com/artur-rios/dotnet-webapi-util) | [Docs](https://docs.artur-rios.tech/dotnet-webapi-util) | [Issues](https://github.com/artur-rios/dotnet-webapi-util/issues) |
| Test Util | [dotnet-test-util](https://github.com/artur-rios/dotnet-test-util) | [Docs](https://docs.artur-rios.tech/dotnet-test-util) | [Issues](https://github.com/artur-rios/dotnet-test-util/issues) |

## This site

The site you are reading is built from
[dotnet-libraries](https://github.com/artur-rios/dotnet-libraries). It carries no code — only the
family-wide overview, the [dependency graph](dependencies/) and the [shared patterns](patterns/).

## Contributing

Open the issue or pull request on the repository of the library it concerns. Anything about the family as
a whole — a wrong dependency edge, a pattern worth documenting — belongs on `dotnet-libraries`.
