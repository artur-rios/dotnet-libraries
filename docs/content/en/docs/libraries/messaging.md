---
title: ArturRios.Messaging
linkTitle: Messaging
weight: 90
description: >-
  Messaging formats and protocols for .NET — currently a Mailgun-backed email service.
---

[![Docs](https://img.shields.io/badge/docs-website-blue)](https://artur-rios.github.io/dotnet-messaging)
[![NuGet](https://img.shields.io/nuget/v/ArturRios.Messaging.svg)](https://www.nuget.org/packages/ArturRios.Messaging)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/artur-rios/dotnet-messaging/blob/main/LICENSE)

The smallest member of the family, and the one most openly under construction. Today it ships a
transactional email service; more formats, protocols and providers are intended, and contributions are
welcome.

## What you get

- **Email via [Mailgun](https://www.mailgun.com/)** — `IEmailService` / `MailgunEmailService`, with a
  clean async interface.
- Registration through the standard `IServiceCollection` pattern
  (`builder.Services.AddHttpClient<IEmailService, MailgunEmailService>()`).
- `ProcessOutput` results rather than exceptions, so failures are handled the same way as everywhere else
  in the family.

Configured from environment variables — `MAILGUN_API_KEY`, `MAILGUN_DOMAIN` and an optional
`MAILGUN_API_VERSION` (default `v3`) — read on every send, so changes take effect without recreating the
service.

## Install

```bash
dotnet add package ArturRios.Messaging
```

## Family dependencies

- [`ArturRios.Output`](../output/) 3.1.0

## Links

- **Documentation:** <https://artur-rios.github.io/dotnet-messaging>
- **Repository:** <https://github.com/artur-rios/dotnet-messaging>
- **NuGet:** <https://www.nuget.org/packages/ArturRios.Messaging>
