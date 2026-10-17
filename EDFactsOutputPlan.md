# EDFacts Files from Ed-Fi + EDU/Stadium — Execution Plan

> **Split 2026-10-12.** Carved out of `GenerateExplorer`. The P0 mapping registers and the
> Generate hidden-logic register were deleted, not moved. GenerateExplorer itself (and its git
> history, which had no remote) was deleted on 2026-10-13 after its wiki and SQL cache moved
> here; the registers are **not recoverable** and must be re-derived if needed.


Status: Draft for owner review, 2026-10-07
Baselines: Generate `37108eb4` (read-only lineage), Ed-Fi Data Standard 6.1.0 (pinned), EDFacts
SY 2026-27 catalog (frozen 2026-10-07; SY 2025-26 retained as lineage)

## 1. Objective

Produce EDPass-submittable EDFacts files from an EDU warehouse (`edu_wh` dims/facts over Ed-Fi
ODS data), deployable to any Stadium partner as a dbt extension package plus one file-export task.
CEDS Generate is used only as a **reading source**: it tells us which business rules a working
EDFacts producer applies that the federal file specifications do not state. Nothing from Generate
runs at runtime.

The EDFacts file specifications (the per-FS DOCX documents linked from the SY 2026-27 file
specifications page, plus the EDFacts Workbook, the Business Rules Single Inventory (BRSI), and the
EDPass metadata guides linked from the EDFacts Resources page) are the authority on **what** a file
contains. Generate is the authority on **how a state has actually computed it** where the spec is
silent.

## 2. What this repo already settles

| Asset | Where | Reuse |
|---|---|---|
| Spec-derived category sets, record layouts and permitted values (SY 2026-27, from the Pandoc cells) | `edu_ext_edfacts/seeds/` via `tasks/build_edfacts_seeds.py` | the count engine's metadata, the fixed-width writer, `accepted_values` tests and xwalk targets (the SY 2025-26 `federal-normalized-*.csv` lineage was removed 2026-10-17; git history keeps it) |
| Element-level Ed-Fi gap clusters: staff qualifications, org governance/finance, foster care | `wiki/analysis/EDFacts-EdFi-Gap-Analysis.md` | scope of side-door data |
| 24 domain notes: every Generate wrapper's inputs, filters, report codes | `wiki/generate/domains/` | the per-collection rule inventory |
| Verified Generate defects and dead paths | `wiki/generate/repo/Source-Code-Oddities.md` | what **not** to port |
| Pandoc extraction for DOCX specs | `tasks/extract_federal_table_cells.py` | every catalog spec of a year to `tasks/reports/<year>/`; the 2025-26 normalizer was P0 tooling and is gone |
| EDU warehouse model map (sibling vault) | `/mnt/c/Repos/EDUAPIExplorer/wiki/repos/edu-wh/` | source models per EDFacts input |

The seam thesis from the P0 work carries over unchanged: Generate's `App` metadata half
(category sets, layouts, permitted values) is standard-agnostic and is **regenerated from the
specs**, not ported. Generate's `Staging`/IDS half is replaced by `edu_wh` + xwalk seeds.

## 3. Target architecture (lazy version)

```mermaid
flowchart LR
  ODS["Ed-Fi ODS (state/LEA)"] -->|edu_edfi_airflow| RAW["raw / stg_ef3__*"]
  RAW -->|edu_wh| WH["dim_* / fct_* / msr_*"]
  SIDE["Non-ODS inputs: staff certification, org governance, finance, SEA policy answers"] -->|earthmover / seeds| WH
  WH --> POP["edfacts_pop__fs###: one row per student/staff/org with EDFacts category columns"]
  SPEC["Spec seeds: category sets, layouts, permitted values (from federal-*.csv)"] --> CNT
  CFG["edfacts_config seeds: count dates, age bands, SEA toggle answers; xwalk_edfacts_* value maps"] --> POP
  POP --> CNT["edfacts_count__fs###: one GROUP BY per category set, unioned → count rows incl. totals"]
  CNT --> REC["edfacts_file__fs###: header + fixed-width records (RPAD/LPAD), ordered"]
  REC -->|COPY INTO stage / Airflow task| FILE["FS###.txt → EDPass"]
  BRSI["BRSI edit checks as dbt tests"] -.-> CNT
```

One dbt package, working name `edu_ext_edfacts`, following the `edu_ext_*` extension pattern
(reads `edu_wh` marts and its own seeds, defines no sources). Three model layers per file spec,
one macro family, four seed families, and a single export task. Deliberate omissions:

- **No generic count-SQL generator.** One `GROUP BY` per category set from the seed, unioned with
  its zero-fill, produces every combination and total natively (GROUPING SETS was the first cut;
  the per-set union is shorter and labels each row directly). Generate's 7,706-line
  `RDS.Get_CountSQL` exists because SQL Server 2008-era code built the SQL text by hand.
- **No report-row star schema.** `edfacts_count__*` tables are the report rows. No equivalent of
  `RDS.ReportEDFacts*` is needed because nothing else reads them.
- **No app shell, no toggle UI.** SEA policy answers are seed rows (they are EDPass metadata
  survey answers already, so the state has them in writing).
- **No XML rendering** until a spec requires it (SY 2025-26 specs are fixed-width or delimited).

## 4. Phases

Each phase ends with a commit and a one-line entry in `.planning/STATE.md`. Phases 1 and 2 run in
parallel; 3 depends on both; 4+ repeat 3's shape.

### Phase 0 — Freeze the SY 2026-27 federal baseline (done 2026-10-07)

`www.ed.gov` returns 403 to every non-browser client (curl, PowerShell, headless Chrome) and the
Wayback Machine held no capture. A real Chrome window driven over the DevTools protocol
(`tasks/fetch_edgov_via_chrome.ps1`, run from WSL via `powershell.exe`) fetched the pages and every
linked document; `tasks/freeze_edfacts_catalog.py 2026-27` renamed, checksummed and inventoried
them into `wiki/reference/edfacts/2026-27/` (94 DOCX, 43 companion documents, `MANIFEST.csv`).

**Outcome:** 93 FS ids, all v23.x, all Inactive at freeze; FS112 dropped, none added; 83 specs
editorial-only, 11 with guidance changes, no record-layout changes. Full account:
`wiki/analysis/EDFacts-2026-27-Delta.md`. Both years are now extracted in full under
`tasks/reports/2025-26/` and `tasks/reports/2026-27/` (`extract_federal_table_cells.py --year …`).

**New fact that reshapes Phase 2:** the specs now cite EDPass metadata *collections* FS5002–FS5029
instead of a survey. The SEA policy answers Generate held as toggles are themselves EDFacts files;
`edfacts_config` should be shaped to those collections.

### Phase 1 — Final Generate pass: business logic not evident in the specs (done 2026-10-07)

Six parallel reads of Generate's SQL, one per domain group (IDEA student, CCD/outcomes, programs,
Directory+Staff, Assessments+legacy inlet, shared machinery), consolidated into a register of rules
with a reimplement decision each (`adopt`, `adopt-as-config`, `follow-spec-instead`, `drop`).

**Outcome (2026-10-07):** 336 rules — 91 spec-silent, 54 implied, 28 stated-differently,
67 contradicting, 96 defects; decisions 71 adopt / 90 adopt-as-config / 108 follow-spec-instead /
67 drop. 39 SEA policy toggles catalogued (13 of them dead in Generate but still needed by the
spec). Headline for the architecture: **a port is not possible** — Generate has no single-
organization assignment for IDEA counts, no reporting-period filters for exiting or discipline,
no highest-score selection for assessments, and dropout/graduate/ACGR/chronic definitions that
collapse to source codes.

**Register deleted 2026-10-12** (owner decision at the repo split). The headline above stands; the
per-rule rows do not. Re-derive individual rules from the Generate wiki
(`wiki/generate/`) and the specs as each collection is built.

### Phase 2 — Spec-driven metadata seeds and the count/write macros

1. `tasks/build_edfacts_seeds.py` — derive four seed CSV families from `federal-*.csv`:
   `edfacts_category_sets` (FS, org level, category set, category, data group), `edfacts_layouts`
   (FS, org level, position, length, type, element), `edfacts_permitted_values` (FS, category,
   code, label), `edfacts_file_headers` (File Type, reporting period, identifier rules). Re-runnable
   for any reporting year.
2. `edfacts_config` seed schema, shaped to the FS5002–FS5029 metadata collections: count dates per collection (child count date,
   membership date, EL date, effective date, state school-year start/end, inclusion period),
   age-band answers (DD age band, homeless ages), per-state yes/no toggles, CTE program-year
   window, assessment-type answers.
3. `xwalk_edfacts_*` seeds: Ed-Fi descriptor value → EDFacts permitted value, one per category
   family (race/ethnicity, sex, grade level, disability category, educational environment, exit
   basis, EL status, discipline action, removal reason, staff classification …). Pre-fill from
   the Ed-Fi 6.1 default descriptor sets (`wiki/reference/ed-fi/6.1.0/`); leave state-specific
   rows blank for the partner.
4. Macros: `edfacts_counts(pop_model, fs, org_level)` emitting one GROUP BY per category set from the
   category-set seed, including zero-fill for required combinations and the Total Indicator rows;
   `edfacts_record(fs, org_level)` emitting the fixed-width concatenation from the layout seed;
   `edfacts_header(fs)`.
5. Tests: `accepted_values` against permitted values; BRSI checks that are expressible in SQL
   (subtotal = sum of parts, required categories present, no negative counts).

**Done when:** `dbt seed && dbt run-operation` renders a count query and a record for FS052 from
seeds alone, and the seeds rebuild byte-identical from the federal CSVs.

### Phase 3 — Vertical slices

Three population models, chosen to exercise the three input shapes:

| Slice | Specs | Input shape | edu_wh sources |
|---|---|---|---|
| Membership | FS052 (+FS039 Grades Offered, which FS052 depends on) | point-in-time student enrollment on a count date | `fct_student_school_association`, `dim_student`, `dim_school`, `bld_ef3__stu_grade_level`, school grade spans |
| IDEA Child Count | FS002, FS089 | student × program eligibility on a count date, with policy exclusions | `fct_student_special_education_program_association` (`is_idea_eligible`, `primary_disability_type`, `special_education_setting`), `dim_student` (birth date → age), `fct_student_school_association` |
| Directory | FS029 (SEA/LEA/school) | organization attributes, operational status transitions | `dim_lea`, `dim_school`, `bld_ef3__wide_ids_*`, calendar windows |

For each slice: population model → counts → record → file in a local dbt project against sample
Ed-Fi data (the Ed-Fi "Grand Bend" sample ODS loaded through `edu_edfi_source`/`edu_wh` is enough;
no partner data needed). Validate the file with the BRSI tests and, where a partner can supply one,
a Generate-produced or previously-submitted file for the same year.

**Done when:** the three files pass every SQL-expressible BRSI rule, record lengths match the
layout seed, and the slice's Phase-1 rules are each either implemented or logged as
`follow-spec-instead` with the spec citation.

### Phase 4 — Roll out by collection, in EDPass unlock order

Group the remaining Generate-covered specs by shared population model and ship a group per wave,
reusing the Phase 3 shape. Suggested order, by the SY 2025-26 catalog's Active set and by shared
inputs:

1. CCD organization: FS129, FS130, FS131, FS190, FS196–FS198, FS207, FS163, FS170, FS205, FS206,
   FS212, FS223 (Directory population + org status side-door).
2. IDEA student: FS009 Exiting; FS005/FS006/FS007/FS088/FS143/FS144 Discipline; FS086 Firearms.
3. CCD staff: FS059, FS203; IDEA staff FS070, FS099, FS067 (FS112 left the catalog in SY 2026-27) — **gated on a staff
   qualification side-door** (Ed-Fi core has no certified/qualified determination).
4. Program participation: FS118/FS194 Homeless, FS045/FS165 Immigrant, FS054/FS121/FS145 MEP,
   FS134/FS137 Title I, FS116/FS126/FS141/FS210/FS211 Title III, FS113/FS119/FS125/FS127/
   FS218–FS221 N-or-D, FS222 Foster care, FS226 Economically disadvantaged, FS033 FRL.
5. Outcomes: FS032 Dropout, FS040 Graduates, FS150/FS151 ACGR (implement the adjusted cohort from
   the spec; Generate never did), FS160 Postsecondary enrollment, FS195 Chronic absenteeism (from
   `msr_student_cumulative_attendance`; threshold from the spec, not Generate).
6. Assessment: FS175/FS178/FS179/FS185/FS188/FS189, FS137–FS139, FS050, FS224/FS225.
7. Finance and governance: FS035, FS132, FS193 (amounts are non-Ed-Fi inputs → seeds or side-door).

The 12 specs Generate never covered (FS227–FS230 dispute resolution, FS901–FS908 Part C) have no
Ed-Fi student data behind them at all; they are SEA administrative counts and belong in a plain
seed-to-file path, last.

**Done when (per wave):** every spec in the wave has a population model, passes BRSI tests, and
its Phase-1 rules are dispositioned.

### Phase 5 — Stadium deployment

1. Publish `edu_ext_edfacts` as a versioned dbt package; a partner adds it to `packages.yml` and
   fills `edfacts_config` and `xwalk_edfacts_*` seeds (same mechanics as every other `xwalk_*`).
2. One Airflow task in the partner's `stadium_*` DAG repo: run the `edfacts` tag, then export each
   `edfacts_file__*` model to the state's drop location (Snowflake `COPY INTO @stage` with
   `FILE_FORMAT = (TYPE = CSV FIELD_DELIMITER = NONE …)` for fixed-width, or a small Python
   export for Databricks).
3. Submission-year rollover: a single `edfacts:reporting_year` var selects the seed year.

**Done when:** one partner produces its Active-set files from its own warehouse and they pass
EDPass validation.

## 5. Decisions needed from the owner

| # | Decision | Default if silent |
|---|---|---|
| E1 | Package home: public EDU org (PolyForm) vs. Stadium-private | Stadium-private until Phase 3 proves the shape, then propose publishing |
| E2 | First partner / first state for Phase 3 validation data | Grand Bend sample ODS only; no partner data |
| E3 | Where non-Ed-Fi inputs (staff certification, org governance, finance, SEA policy answers) enter | seeds for SEA-level answers; earthmover bundles for anything per-staff or per-org |
| E4 | ~~Baseline: wait for SY 2026-27 artifacts~~ resolved: SY 2026-27 frozen 2026-10-07 | — |
| E5 | Fate of the P0 register waves (Phases 4+ of the old plan: 4,731 unadjudicated rows) | stop; spec seeds replace them. Registers deleted 2026-10-12 |

## 6. Out of scope

- Running Generate, SQL Server, or any CEDS artifact at runtime.
- EDPass submission automation beyond producing the file (EDPass has no public API).
- State-specific files that are not EDFacts (those stay in each `stadium_*` repo's `state_files`).
- Ed-Fi ODS/API changes; if a state's ODS lacks an element, the side-door path supplies it.

## 7. Repo housekeeping

- 2026-10-12: split out of GenerateExplorer into this repo. `.planning/` phases continue at `06`;
  phases `01`–`03` (P0) and the P0 archive were deleted.
- Decisions: E1–E5 in §5; record new ones there and in `HANDOFF.md`.
