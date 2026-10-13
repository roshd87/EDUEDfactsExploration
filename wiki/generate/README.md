# Reading CEDS Generate

Operating guide for the Generate source cache (`sources/generate/`, 515 canonical `.sql` files at
`develop` commit 37108eb) that the notes in this folder cite. Moved from the retired
`GenerateExplorer` repo on 2026-10-13. Start with [[Home]] for the architecture.

## Reading the Generate repo

**Read `sources/generate/` first** — a local cache of `generate.database/` at branch `develop`
(commit 37108eb, 2026-08-07): all 515 canonical `.sql` files, grep-able. The wiki baseline is **`develop`** (the active line,
~489 commits ahead of `master`, the released version).

There is no full clone — 208 MB, 40,405 files. For anything outside the cache use `gh api`.
The default branch is **`master`**; `/blob/main/` URLs 404.

Fetch the file tree once per session and grep it locally instead of paging the contents API:

```sh
gh api repos/CEDS-Collaborative-Exchange/Generate/git/trees/master?recursive=1 \
  --jq '.tree[].path' > /tmp/gen_tree.txt

gh api repos/CEDS-Collaborative-Exchange/Generate/contents/<path> --jq '.content' | base64 -d
```

One call gets all 40,405 paths. Paging `contents/` directory by directory instead is the main way
to waste a session here.

## Where the logic actually is

**~97% of the repo is duplicate or historical.** Of 40,405 files, about 1,000 are current-state
SQL. Everything canonical lives under `generate.database/`:

| Path | `.sql` files |
|---|---|
| `StoredProcedures/Create/` | 286 |
| `Views/Create/` | 133 |
| `Tables/Create/` | 50 |
| `Functions/Create/` | 29 |
| `TableTypes/` | 22 |
| `Metadata/` | 14 |

Two traps:

- **`*/VersionUpdates/**`** holds ~15 historical snapshots of those same ~290 procedures (~21K
  files). Never read these unless you are specifically tracing when a rule changed.
- **`generate.web/DatabaseScripts/`** mirrors `generate.database/` — 15,134 of 15,194 paths are
  identical. Treat it as a duplicate, but not a strict one: 60 files exist only under
  `generate.database/`, and 240 current-state files only under `generate.web/`. If a procedure
  seems missing, check the other tree before concluding it doesn't exist.

`Drop/` folders next to every `Create/` are teardown DDL — never logic. The C# (`generate.core`,
`generate.web`) is the app shell; `generate.core/Models/IDS` alone is 757 ORM model files and
contains no reporting rules.

## Pipeline architecture

Schemas: `Staging`, `RDS`, `App`, `Debug`, `CEDS`, `Upgrade`, `EDENDB`.

Data moves **`Staging` → `RDS` (star schema) → report rows → EDFacts file**. Per EDFacts domain,
`App.Wrapper_Migrate_<Domain>_to_RDS` is the entry point — reading the wrapper for a domain is the
fastest way to find that domain's real logic. There are ~24, one per collection (ChildCount,
Exiting, Discipline, Assessment, Membership, Dropout, GraduatesCompleters, Homeless, Chronic, CTE,
TitleIIIELOct, SPPAPR, …).

A wrapper's actual shape, from `App.Wrapper_Migrate_ChildCount_to_RDS`:

1. `Staging.Staging-to-Dim*` — load shared dimensions (`DimPeople_K12Students`, `DimSeas`,
   `DimLeas`, `DimK12Schools`). 20 of these.
2. `RDS.Empty_RDS '<domain>'` — clear the domain's prior load.
3. `Staging.Staging-to-Fact*` — load the domain's fact table. 32 of these.

Two corrections to naive readings of that shape (verified during the wiki build): **four wrappers
are a different generation** — CTE, Other, SPPAPR, StudentCounts call `rds.Migrate_Dim*` /
`rds.Migrate_StudentCounts` directly, with no `Staging-to-Fact*` step; and **58 of the 67
`RDS.Migrate_Dim*` procedures read `dbo.*` (the CEDS IDS) rather than `Staging.*`** — the staging
seam is not the only data path into RDS. Report rows are produced by two generators selected per
report via `GenerateReports.UseLegacyReportMigration`: legacy `RDS.Create_ReportData` →
`Get_CountSQL`, and current `RDS.Insert_CountsIntoReportTable` counting off per-report-code views
(`rds.vw<Domain>_FactTable_C###`) — those views are the cleanest statement of each report's rules.

**Orchestration is metadata-driven, not statically wired.** `App.Migrate_Data` builds procedure
names at runtime and calls them via `sp_executesql`. Grepping for static `EXEC` chains will not
reveal the full call graph — the `App` metadata tables do.

Useful shortcut: `Debug.vw<Domain>_FactTable` and `Debug.vw<Domain>_StagingTables` are per-domain
lineage views. They are effectively a pre-built map from staging columns to fact columns, and are
much faster to read than the procedures that populate them.

## The seam (why this project exists)

CEDS coupling and EDFacts output shape live in different places, and the whole extraction depends
on that separation:

- **CEDS-specific:** the `Staging.*` tables and the `Staging-to-Dim*` / `Staging-to-Fact*`
  procedures. This is the replaceable half.
- **Standard-agnostic:** the `RDS` star schema, and the `App` metadata that declares the staging
  contract and maps it to EDFacts layouts — `App.GenerateStagingTables`,
  `App.GenerateStagingColumns`, `App.GenerateReport_GenerateStagingTablesXREF`,
  `App.FactType_ReportsXREF`, plus the `App.vwReportCode_*` views (`FileColumns`,
  `CategoryOptions`, `StagingTables`). This is the reusable half.

**Every vault note should make clear which side of that line it documents** —
a note that blurs the two is worse than no note, because it hides the thing being extracted.

One honest caveat to that thesis, found during the wiki build: some fact types bypass `Staging.*`
entirely and read `dbo.*` (the CEDS IDS) directly — CTE program participation and Directory's
organization status among them. The seam is real but not airtight; the wiki's Home note carries the
details.

