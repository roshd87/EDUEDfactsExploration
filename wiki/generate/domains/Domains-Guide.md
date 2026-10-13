---
tags:
  - guide
---

# Domains folder guide

One note per EDFacts collection — 24 notes, one for each `App.Wrapper_Migrate_<Domain>_to_RDS`
wrapper in frozen Generate. [[Home]] carries the full linked table.

Every domain note has the same anatomy:

1. **Seam callout** — which parts are CEDS-specific vs standard-agnostic.
2. **Pipeline table** — wrapper, fact procedure, fact table, per-report views, report codes
   (`c###` ⟷ `FS###`).
3. **Data elements required** — staging columns per federal category-set role.
4. **Ed-Fi coverage (preliminary)** — per-element verdicts against Ed-Fi. Preliminary; they
   predate any pinned Ed-Fi contract.
5. **Citations** — `generate.database/<path>@develop` source paths.

[[ChildCount]] is the reference domain (clearest example of the whole shape). The four legacy
domains — [[CTE]], [[Other]], [[SPPAPR]], [[StudentCounts]] — use the older `RDS.Migrate_*` inlet
instead of `Staging-to-Fact*`; see the warning on [[Home]] and [[Source-Code-Oddities]].
