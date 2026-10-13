---
tags:
  - guide
---

# Components folder guide

One note per architectural layer of the Generate pipeline
(`Staging → RDS star schema → report rows → EDFacts file`). [[Home]] lists all seven with
one-line summaries and seam sides; read them in the order given there.

Each note follows the vault conventions: a seam callout under the H1 (`CEDS-specific`,
`standard-agnostic`, or `both`), at most one mermaid flowchart, and a closing `## Citations`
list of `generate.database/<path>@develop` paths.

| Note | Layer |
|---|---|
| [[Staging-Layer]] | CEDS-aligned landing tables (the replaceable half) |
| [[App-Metadata-Layer]] | Metadata control plane — reports, category sets, file layouts |
| [[RDS-Star-Schema]] | Dimensions, facts, report tables |
| [[Staging-to-RDS-Migration]] | The 24 domain wrappers and their procedures |
| [[Report-Data-Generation]] | Facts → EDFacts count rows (legacy and current generators) |
| [[File-Generation]] | Report rows → fixed-width submission file |
| [[App-Shell]] | The C# application shell (out of extraction scope) |
