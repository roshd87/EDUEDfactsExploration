---
tags: [generate, repo]
---

# Generate Repo and Branches

> [!info] Seam: both
> This note is orientation, not logic. It says where each side of the seam physically lives.

The upstream repo is `CEDS-Collaborative-Exchange/Generate`: ~40,000 files, ~208 MB. About **1,000
of those files are current-state SQL**, and all of them are under `generate.database/`. Everything
else is duplicate, historical, C# shell, or docs.

## Where the canonical logic lives

`generate.database/` is the real application. On `develop`:

| Path | Files | What |
|---|---|---|
| `StoredProcedures/Create/` | 286 | Wrappers, `Staging-to-*`, `RDS.Migrate_*`, report builders |
| `Views/Create/` | 133 | `Debug.vw*` lineage, `RDS.vwDim*` code maps, `App.vwReportCode_*` |
| `Tables/Create/` | 50 | `Staging.*` and six `App.*` tables — **not** the `RDS` schema |
| `Functions/Create/` | 29 | Including `RDS.Get_CountSQL` (7,706 lines) |
| `TableTypes/` | 22 | Table-valued parameter types |
| `Metadata/` | 14 | Seed scripts for the `App` control plane |
| `TestCases/` | ~30 | `App.FS###_TestCase` per file spec |
| `Indexes/`, `Jobs/`, `Scripts/`, `Schemas/` | small | Install/maintenance |

Two things are **not** in the repo and matter:

- **The `RDS` schema has no DDL here.** No `Tables/Create/RDS.*.sql` exists. `RDS` is the CEDS Data
  Warehouse component, installed separately; Generate only reads and writes it. Reconstruct its
  shape from the procedures and from
  `generate.database/Views/Create/RDS.vwCEDS_DataWarehouse_Extended_Properties.View.sql@develop`,
  which reads CEDS element names off SQL extended properties.
- **Several `Staging.*` tables have no DDL here either** — `Staging.IdeaDisabilityType`,
  `Staging.K12PersonRace`, `Staging.K12Organization`, `Staging.SourceSystemReferenceData` are used
  throughout but only exist as C# models under `generate.core/Models/Staging/` (43 files). See
  [[Staging-Layer]].

## The two traps

**`*/VersionUpdates/**`.** About 15 historical snapshots of the same ~290 procedures — roughly
21,000 files. Reading one of these instead of the current file is the most common way to document a
rule that was changed years ago. Never read them except to trace when something changed.

**`generate.web/DatabaseScripts/`.** A near-mirror of `generate.database/`: 15,134 of 15,194 paths
are byte-identical. It is *not* a strict duplicate. **60 files exist only in `generate.database/`,
and 240 current-state files only in `generate.web/`** — and the web-only set is not junk. It holds
newer per-report-code views that have not landed in `generate.database/` yet, including
`RDS.vwAssessment_FactTable_050/113/125/126/137/138/139/210/211`, `RDS.vwChronicAbsenteeism_FactTable_195`,
`Debug.vwStaff_*`, `Debug.vwSchoolPerformanceIndicators_*`, and wrappers
`App.Wrapper_Migrate_ChronicAbsenteeism_to_RDS` / `App.Wrapper_Migrate_SchoolPerformanceIndicators_to_RDS`.
This vault documents `generate.database/` only. When a per-report view seems to be missing, that is
usually why — note the absence, do not invent the file.

`Drop/` folders sit beside every `Create/` and hold teardown DDL only. Never logic.

## Branch state

- **`develop`** — active. 489 commits ahead of `master`, last pushed 2026-08-07. **This vault
  documents `develop`**, cached at commit `37108eb` under `sources/generate/`.
- **`master`** — the released branch, and the repo default. `/blob/main/` URLs 404.

Because `develop` moves, every claim in this vault carries a path citation so it can be re-checked
against upstream. Citation format: `generate.database/<path>@develop`.

## Solution structure

`generate.sln` has twelve C# projects; three matter for orientation. **`generate.web`** is the
ASP.NET application — the UI where an SEA picks school years and report codes, triggers a
migration, reviews counts, and downloads submission files. **`generate.core`** is the domain and
ORM layer: 916 model classes split `Models/IDS` (757), `Models/RDS` (75), `Models/Staging` (43),
`Models/App` (41), plus DTOs, view models, and service interfaces such as
`generate.core/Interfaces/Services/IEdfactsFileService.cs`. The `Models/IDS` bulk is the CEDS
Integrated Data Store schema and contains no reporting rules. **`generate.database`** is where the
reporting logic actually is. The remaining projects (`generate.background`, `generate.console`,
`generate.infrastructure`, `generate.test`, `generate.testdata`, `generate.update`,
`generate.shared`, `generate.filestorage`, `generate.overnighttest`) are scheduling, plumbing, and
test scaffolding. See [[App-Shell]].

## Citations

- `generate.database/Tables/Create/@develop` — 50 files, no `RDS.*`
- `generate.database/Views/Create/RDS.vwCEDS_DataWarehouse_Extended_Properties.View.sql@develop`
- `generate.database/Metadata/@develop` — 14 seed scripts
- `generate.database/Functions/Create/RDS.Get_CountSQL.UserDefinedFunction.sql@develop`
- `sources/gen_tree_develop.txt` — 42,592-path listing of `develop`, used for the duplicate-tree diff
