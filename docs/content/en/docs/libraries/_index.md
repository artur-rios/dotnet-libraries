---
title: Libraries
linkTitle: Libraries
weight: 20
description: >-
  One page per library: what it does, what it depends on, and where its own documentation lives.
---

Twelve libraries, grouped by the layer they sit in. Each page here is a summary — follow the links to
each library's own documentation site for the full API.

## Foundation

The pieces almost everything else builds on.

{{< cardpane >}}
{{< card header="**Output**" >}}
Result envelopes — `ProcessOutput`, `DataOutput<T>`, `PaginatedOutput<T>`.
[Read more](output/)
{{< /card >}}
{{< card header="**Util**" >}}
Hashing, retries, randomness, files, HTTP, regex, console helpers.
[Read more](util/)
{{< /card >}}
{{< card header="**Extensions**" >}}
Extension methods for strings, enums, collections, dates and numbers.
[Read more](extensions/)
{{< /card >}}
{{< /cardpane >}}

## Cross-cutting concerns

{{< cardpane >}}
{{< card header="**Configuration**" >}}
Layered configuration from JSON, environment variables and `.env` files.
[Read more](configuration/)
{{< /card >}}
{{< card header="**Logging**" >}}
Console and file loggers with caller info and trace IDs.
[Read more](logging/)
{{< /card >}}
{{< card header="**JWT**" >}}
Create, validate and read JSON Web Tokens, with key rotation.
[Read more](jwt/)
{{< /card >}}
{{< /cardpane >}}

## Application structure

{{< cardpane >}}
{{< card header="**Validation**" >}}
FluentValidation wrapped so results arrive as errors or `Output` envelopes.
[Read more](validation/)
{{< /card >}}
{{< card header="**Mediator**" >}}
CQRS-style command and query dispatch over the built-in DI container.
[Read more](mediator/)
{{< /card >}}
{{< card header="**Messaging**" >}}
Messaging formats and protocols; currently a Mailgun email service.
[Read more](messaging/)
{{< /card >}}
{{< /cardpane >}}

## Infrastructure and tooling

{{< cardpane >}}
{{< card header="**Data**" >}}
Nine packages: EF Core, Dapper, MongoDB, DynamoDB and file export.
[Read more](data/)
{{< /card >}}
{{< card header="**Web API Util**" >}}
ASP.NET Core startup, authentication, middleware and response resolution.
[Read more](webapi-util/)
{{< /card >}}
{{< card header="**Test Util**" >}}
xUnit assertions, in-memory fakes and a functional web API test base.
[Read more](test-util/)
{{< /card >}}
{{< /cardpane >}}
