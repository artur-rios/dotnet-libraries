---
title: Dotnet Libraries
linkTitle: Home
---

{{< blocks/cover title="Dotnet Libraries" height="auto" color="primary" >}}
<p class="lead mt-4">
Twelve small, focused <strong>ArturRios.*</strong> packages for .NET 10 — result envelopes, configuration,
data access, validation, JWT, logging, messaging, mediation and web API plumbing — built to compose with
each other and usable one at a time.
</p>
<a class="btn btn-lg btn-secondary me-3 mb-4" href="docs/">
  Documentation <i class="fas fa-arrow-alt-circle-right ms-2"></i>
</a>
<a class="btn btn-lg btn-secondary me-3 mb-4" href="docs/libraries/">
  Libraries <i class="fas fa-book ms-2"></i>
</a>
<a class="btn btn-lg btn-secondary me-3 mb-4" href="https://github.com/artur-rios">
  GitHub <i class="fab fa-github ms-2"></i>
</a>
{{< /blocks/cover >}}

{{% blocks/lead color="light" %}}
Every library follows the same conventions: `net10.0`, the Artur Rios Attribution License, one repository per library, its own Docsy
documentation site, and — where an operation can fail — an `ArturRios.Output` envelope instead of an
exception.
{{% /blocks/lead %}}

{{< blocks/section color="white" type="row" >}}

{{% blocks/feature icon="fas fa-cubes" title="One library per repository" url="docs/repositories/" %}}
Each library is developed, versioned, tested and published on its own. Pick the ones you need — nothing
drags in the rest of the family.
{{% /blocks/feature %}}

{{% blocks/feature icon="fas fa-project-diagram" title="A deliberate dependency graph" url="docs/dependencies/" %}}
`ArturRios.Output` sits at the root; everything else layers on top of it. See the full graph, including
which package depends on which.
{{% /blocks/feature %}}

{{% blocks/feature icon="fas fa-drafting-compass" title="Shared patterns" url="docs/patterns/" %}}
Output envelopes, provider-per-package modularity, fluent validation, CQRS mediation and
convention-driven CI — the ideas that repeat across the family.
{{% /blocks/feature %}}

{{< /blocks/section >}}

{{% blocks/section color="light" %}}
## Other documentation sites

Every documentation site of the family is served from `docs.artur-rios.tech`, one path each. This site is the index
of them: the bare address of the host comes here.

### The libraries

Each library has its own site, with its API reference, guides and coverage report.

- [dotnet-output docs](https://docs.artur-rios.tech/dotnet-output/) — Output
- [dotnet-util docs](https://docs.artur-rios.tech/dotnet-util/) — Util
- [dotnet-extensions docs](https://docs.artur-rios.tech/dotnet-extensions/) — Extensions
- [dotnet-configuration docs](https://docs.artur-rios.tech/dotnet-configuration/) — Configuration
- [dotnet-logging docs](https://docs.artur-rios.tech/dotnet-logging/) — Logging
- [dotnet-jwt docs](https://docs.artur-rios.tech/dotnet-jwt/) — JWT
- [dotnet-validation docs](https://docs.artur-rios.tech/dotnet-validation/) — Validation
- [dotnet-mediator docs](https://docs.artur-rios.tech/dotnet-mediator/) — Mediator
- [dotnet-messaging docs](https://docs.artur-rios.tech/dotnet-messaging/) — Messaging
- [dotnet-data docs](https://docs.artur-rios.tech/dotnet-data/) — Data
- [dotnet-webapi-util docs](https://docs.artur-rios.tech/dotnet-webapi-util/) — Web API Util
- [dotnet-test-util docs](https://docs.artur-rios.tech/dotnet-test-util/) — Test Util

### Everything else

The documentation sites of the other projects.

- [Heimdall API docs](https://docs.artur-rios.tech/heimdall-api/)
- [Heimdall docs](https://docs.artur-rios.tech/heimdall-docs/)
- [Fortuna docs](https://docs.artur-rios.tech/fortuna-docs/)
- [Alexandria docs](https://docs.artur-rios.tech/alexandria-docs/)
- [Orpheus docs](https://docs.artur-rios.tech/orpheus/)
{{% /blocks/section %}}
