---
title: ArturRios.Data
linkTitle: Data
weight: 100
description: >-
  A modular data-access toolkit — nine packages covering EF Core, Dapper, MongoDB, DynamoDB and file export.
---

[![Docs](https://img.shields.io/badge/docs-website-blue)](https://artur-rios.github.io/dotnet-data)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/artur-rios/dotnet-data/blob/main/LICENSE)
[![Relational.Core](https://img.shields.io/nuget/v/ArturRios.Data.Relational.Core.svg?label=Relational.Core)](https://www.nuget.org/packages/ArturRios.Data.Relational.Core)
[![MongoDb](https://img.shields.io/nuget/v/ArturRios.Data.MongoDb.svg?label=MongoDb)](https://www.nuget.org/packages/ArturRios.Data.MongoDb)
[![Export](https://img.shields.io/nuget/v/ArturRios.Data.Export.svg?label=Export)](https://www.nuget.org/packages/ArturRios.Data.Export)

The largest library in the family: one consistent, envelope-based repository style across **relational**
databases (EF Core over PostgreSQL, MySQL and SQLite, plus a Dapper read path), **NoSQL** stores
(**MongoDB**, **DynamoDB**), and **file export** writers (CSV, JSON, TXT, MessagePack, Excel).

Every operation returns a `DataOutput` / `ProcessOutput` envelope from [`ArturRios.Output`](../output/), so
infrastructure failures — including optimistic-concurrency conflicts — surface as errors on the result
instead of unhandled exceptions.

## The nine packages

Each backend is its own package, so installing SQLite support does not pull in the MongoDB or AWS SDKs.

| Package | Backend | Depends on |
|---|---|---|
| [`ArturRios.Data.Relational.Core`](https://www.nuget.org/packages/ArturRios.Data.Relational.Core) | EF Core abstractions — repository and unit-of-work contracts, `EfRepository`, `BaseDbContext`, provider seam | `ArturRios.Output`, EF Core |
| [`ArturRios.Data.PostgreSql`](https://www.nuget.org/packages/ArturRios.Data.PostgreSql) | PostgreSQL (Npgsql) | Relational.Core |
| [`ArturRios.Data.Sqlite`](https://www.nuget.org/packages/ArturRios.Data.Sqlite) | SQLite | Relational.Core |
| [`ArturRios.Data.MySql`](https://www.nuget.org/packages/ArturRios.Data.MySql) | MySQL (Pomelo) — *deferred* | Relational.Core |
| [`ArturRios.Data.Dapper`](https://www.nuget.org/packages/ArturRios.Data.Dapper) | Raw-SQL reads over the EF connection | Relational.Core, Dapper |
| [`ArturRios.Data.MongoDb`](https://www.nuget.org/packages/ArturRios.Data.MongoDb) | MongoDB document store | `ArturRios.Output`, MongoDB.Driver |
| [`ArturRios.Data.DynamoDb`](https://www.nuget.org/packages/ArturRios.Data.DynamoDb) | AWS DynamoDB | `ArturRios.Output`, AWSSDK.DynamoDBv2 |
| [`ArturRios.Data.Export`](https://www.nuget.org/packages/ArturRios.Data.Export) | CSV / JSON / TXT / MessagePack writers | `ArturRios.Output`, MessagePack |
| [`ArturRios.Data.Export.Excel`](https://www.nuget.org/packages/ArturRios.Data.Export.Excel) | Excel `.xlsx` add-on | Export, ClosedXML |

See the [dependency graph](../../dependencies/#inside-arturriosdata) for how these fit together.

## Install

```bash
dotnet add package ArturRios.Data.PostgreSql
```

## Family dependencies

- [`ArturRios.Output`](../output/) 3.1.0 — every package in the set depends on it, directly or through
  `Relational.Core` / `Export`.

Current package versions: `Relational.Core` 4.0.0, `Dapper` 4.0.0, `PostgreSql` 3.0.1, `Sqlite` 3.0.1,
`MySql` 1.0, `MongoDb` 2.0.0, `DynamoDb` 2.0.0, `Export` 2.0.0, `Export.Excel` 2.0.0.

## Links

- **Documentation:** <https://artur-rios.github.io/dotnet-data>
- **Architecture and diagrams:** <https://artur-rios.github.io/dotnet-data/architecture/>
- **Guides:** [Relational](https://artur-rios.github.io/dotnet-data/relational/) ·
  [MongoDB](https://artur-rios.github.io/dotnet-data/mongodb/) ·
  [DynamoDB](https://artur-rios.github.io/dotnet-data/dynamodb/) ·
  [Export](https://artur-rios.github.io/dotnet-data/export/)
- **Repository:** <https://github.com/artur-rios/dotnet-data>
