---
title: Dependency graph
linkTitle: Dependencies
weight: 30
description: >-
  How the ArturRios packages depend on each other — from the Output envelopes at the root up to the
  web API and test helpers.
---

Only dependencies **within the family** are shown. Third-party dependencies (FluentValidation, EF Core,
Dapper, the MongoDB and AWS SDKs, xUnit, `Microsoft.Extensions.*`) are listed on each library's own page.

## The whole family

`ArturRios.Output` is the root: it defines the envelopes every fallible operation returns, and it depends
on nothing else in the family. `ArturRios.Util.Test` is the leaf that pulls in the most, because a test
helper has to know about everything it fakes.

```mermaid
flowchart BT
    Output["<b>ArturRios.Output</b><br/><i>result envelopes</i>"]
    Util["<b>ArturRios.Util</b>"]
    Extensions["<b>ArturRios.Extensions</b>"]
    Configuration["<b>ArturRios.Configuration</b>"]
    Logging["<b>ArturRios.Logging</b>"]
    Jwt["<b>ArturRios.Jwt</b>"]
    Validation["<b>ArturRios.Validation</b>"]
    Mediator["<b>ArturRios.Mediator</b>"]
    Messaging["<b>ArturRios.Messaging</b>"]
    DataCore["<b>ArturRios.Data.*</b><br/><i>9 packages</i>"]
    WebApi["<b>ArturRios.Util.WebApi</b>"]
    TestUtil["<b>ArturRios.Util.Test</b>"]

    Util --> Output
    Validation --> Output
    Mediator --> Output
    Messaging --> Output
    DataCore --> Output

    Extensions --> Util
    Configuration --> Extensions
    Logging --> Extensions
    Logging --> Util

    WebApi --> Configuration
    WebApi --> Jwt
    WebApi --> Util

    TestUtil --> Configuration
    TestUtil --> Mediator
    TestUtil --> Util
    TestUtil --> WebApi
    TestUtil --> DataCore

    classDef root fill:#0b6e99,stroke:#084c69,color:#fff;
    classDef standalone fill:#f5f5f5,stroke:#999,color:#222;
    class Output root;
    class Jwt standalone;
```

`ArturRios.Jwt` is deliberately standalone — it depends on nothing in the family, so a service can issue
and validate tokens without adopting anything else.

## Inside ArturRios.Data

The `Data` repository ships nine packages so you install only the backend you use. The relational
packages share a common core; MongoDB, DynamoDB and the export writers are independent of it.

```mermaid
flowchart BT
    Output["<b>ArturRios.Output</b>"]

    subgraph Relational["Relational — EF Core"]
        direction BT
        Core["ArturRios.Data.Relational.Core"]
        Postgres["ArturRios.Data.PostgreSql"]
        MySql["ArturRios.Data.MySql"]
        Sqlite["ArturRios.Data.Sqlite"]
        Dapper["ArturRios.Data.Dapper<br/><i>read path</i>"]
    end

    subgraph NoSql["NoSQL"]
        direction BT
        Mongo["ArturRios.Data.MongoDb"]
        Dynamo["ArturRios.Data.DynamoDb"]
    end

    subgraph Exporting["Export writers"]
        direction BT
        Export["ArturRios.Data.Export<br/><i>CSV, JSON, TXT, MessagePack</i>"]
        Excel["ArturRios.Data.Export.Excel"]
    end

    Postgres --> Core
    MySql --> Core
    Sqlite --> Core
    Dapper --> Core
    Excel --> Export

    Core --> Output
    Mongo --> Output
    Dynamo --> Output
    Export --> Output

    classDef root fill:#0b6e99,stroke:#084c69,color:#fff;
    class Output root;
```

## Dependency table

Read an arrow as *"depends on"*. Versions are the ones currently referenced in each project file, and
move independently of one another.

| Package | Depends on (family only) |
|---|---|
| `ArturRios.Output` | — |
| `ArturRios.Jwt` | — |
| `ArturRios.Util` | `ArturRios.Output` |
| `ArturRios.Extensions` | `ArturRios.Util` |
| `ArturRios.Configuration` | `ArturRios.Extensions` |
| `ArturRios.Logging` | `ArturRios.Extensions`, `ArturRios.Util` |
| `ArturRios.Validation` | `ArturRios.Output` |
| `ArturRios.Mediator` | `ArturRios.Output` |
| `ArturRios.Messaging` | `ArturRios.Output` |
| `ArturRios.Data.Relational.Core` | `ArturRios.Output` |
| `ArturRios.Data.PostgreSql` | `ArturRios.Data.Relational.Core` |
| `ArturRios.Data.MySql` | `ArturRios.Data.Relational.Core` |
| `ArturRios.Data.Sqlite` | `ArturRios.Data.Relational.Core` |
| `ArturRios.Data.Dapper` | `ArturRios.Data.Relational.Core` |
| `ArturRios.Data.MongoDb` | `ArturRios.Output` |
| `ArturRios.Data.DynamoDb` | `ArturRios.Output` |
| `ArturRios.Data.Export` | `ArturRios.Output` |
| `ArturRios.Data.Export.Excel` | `ArturRios.Data.Export` |
| `ArturRios.Util.WebApi` | `ArturRios.Configuration`, `ArturRios.Jwt`, `ArturRios.Util` |
| `ArturRios.Util.Test` | `ArturRios.Configuration`, `ArturRios.Data.Relational.Core`, `ArturRios.Mediator`, `ArturRios.Util`, `ArturRios.Util.WebApi` |

## A typical service

A web API built on the family usually ends up with this stack — and picks up the rest transitively.

```mermaid
flowchart LR
    App["Your service"] --> WebApi["ArturRios.Util.WebApi"]
    App --> Mediator["ArturRios.Mediator"]
    App --> Validation["ArturRios.Validation"]
    App --> Data["ArturRios.Data.PostgreSql"]
    App --> Logging["ArturRios.Logging"]
    Tests["Your test project"] --> TestUtil["ArturRios.Util.Test"]
    TestUtil -.-> WebApi
    WebApi -.-> Transitive["Configuration · Jwt · Util · Extensions · Output"]
```
