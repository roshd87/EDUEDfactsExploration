# Handoff — EDUEDfacts

Updated 2026-10-17 (orientation map, docs checker, BRSI review sheet, lean-up after the over-engineering audit). Read `orientation.md` (repo map) and this file first,
then `EDFactsOutputPlan.md` (the plan) and `CLAUDE.md` (operating guide).

## What this repo is now

**EDFacts file production from Ed-Fi + EDU/Stadium.** Split out of GenerateExplorer on
2026-10-12; its Generate wiki and SQL cache moved here (`wiki/generate/`, `sources/generate/`)
and the repo was deleted on 2026-10-13. The Generate-to-Ed-Fi mapping registers (P0) and the
Generate hidden-logic register were deleted at the split and are not recoverable (no remote).

The target is a dbt extension package (`edu_ext_edfacts`) over `edu_wh` marts: spec-derived seeds for category sets, layouts and permitted values, a
count macro (one GROUP BY per category set, unioned), and a fixed-width record macro. CEDS Generate is a reading source only.

## Done

| Plan phase | Result | Where |
|---|---|---|
| 0 — Freeze SY 2026-27 baseline | 94 specs (all v23.x, all Inactive at freeze) + 43 companion docs, SHA-256 manifest. FS112 dropped, none added | `wiki/reference/edfacts/2026-27/` |
| 0 — Two-year delta | 83 specs editorial only, 11 with guidance changes, no layout changes; "metadata survey" → FS5002–FS5029 metadata collections | `wiki/analysis/EDFacts-2026-27-Delta.md` |
| 1 — Generate hidden-logic pass | 336 rules the specs don't state; 39 SEA policy toggles. Headline kept in `EDFactsOutputPlan.md` Phase 1; register deleted at the split | — |
| Field review (Opus manager + Sonnet workers) | 216 distinct fields, 88 shared (22 universal, 16 family-wide, 50 collection-specific); content reusable, positions per file | `wiki/analysis/EDFacts-2026-27-Shared-Fields.md`, `edfacts-2026-27-shared-fields.csv` |
| 2 — Seeds + macros, FS052 | `tasks/build_edfacts_seeds.py` emits 4 seeds (byte-identical rebuild); `edfacts_counts` (one GROUP BY per category set, labelled and unioned with its zero-fill) and `edfacts_file` (header + fixed-width records); 3 spec tests. Fixture build: 21/21 pass, records 324 bytes, header 459 | `edu_ext_edfacts/` |
| Vault spec notes | 20 specs (18 Active + FS224/FS225 Optional in SY 2025-26) converted from the SY 2026-27 DOCX into Obsidian notes: frontmatter, at-a-glance callout, pipe tables, Generate-domain links, index note. Deterministic rebuild | `wiki/edfacts/<FSnnn>/`, `wiki/edfacts/EDFacts Specs.md`, `tasks/convert_specs_to_vault.py` |
| Vault companion notes | BRSI SY 2025-26 v1.04 (1173 rules; overview + a `<FSnnn> Business Rules` note per spec), Workbook SY 2025-26, and the newest guide for each of the 13 EDPass metadata collections, all cross-linked to the spec notes (FS mentions become wikilinks). No SY 2026-27 BRSI or Workbook existed at the freeze | `wiki/edfacts/{BRSI,Workbook,Metadata}/`, `tasks/convert_companions_to_vault.py` |
| Synopsis page | One-page summary of the three analyses above | `wiki/analysis/EDFacts-2026-27-Findings.html`, published privately at https://claude.ai/artifact/2fVMftrtHYoBwWqYkaRVLa |
| BRSI rules review sheet | 315 rules with a proposed dbt-test handling and pre-set decision each (202 test now, 92 later, 12 not SQL, 9 n/a); linked from the BRSI note and the spec index. Decisions live in a Claude Doc (see On deck) | `wiki/edfacts/BRSI/BRSI Rules Review for dbt Tests.md`, `tasks/build_brsi_review.py` |
| Agent orientation | `orientation.md` maps the repo (generated vs hand-written vs frozen, pipelines, traps); `tasks/check_docs.py` reports paths the orientation docs name that are not on disk, plus missing venvs and frozen docs. Evaluated and rejected skills for refreshing/onboarding: a CLAUDE.md pointer plus the script covers it | `orientation.md`, `tasks/check_docs.py`, `docs/agents/issue-tracker.md` (now matches the real `.planning/` layout) |
| Lean-up (over-engineering audit, 2026-10-17) | Dead driver, flags and duplicate helpers removed from the task scripts; `edfacts_counts` rewritten as one GROUP BY per set (same rows, 21/21 tests); GSD `config.json`, the two template agent docs and the SY 2025-26 `federal-normalized-*` lineage CSVs deleted (git history keeps them); every generated output rebuilt byte-identical | `tasks/`, `edu_ext_edfacts/` |
| SC child count vs FS002 (2026-10-17) | Read `edanalytics/edu_ext_sc` (`rpt_sedm__child_count`, commit `eda7cb9`) and `edanalytics/stadium_south_carolina` (`adf53db`) SEDM code against the FS002 spec, BRSI and Generate notes. The SC report is a student-level IEP list with an IDEA flag, not counts: no age, kindergarten, enrollment-on-date or dedup logic; three likely SQL defects (exclusive IEP end date, inner joins to the two seeds, EL dedup on a null key). 16 follow-up questions, no row counts run | `wiki/analysis/SC-Child-Count-vs-FS002.md` |

## Next steps

1. **Owner decisions E1, E2, E3, E5** (`EDFactsOutputPlan.md` §5). Defaults apply until changed:
   Stadium-private package, Grand Bend sample ODS for validation, seeds for SEA answers +
   earthmover for per-staff/org side-door data. (E5, stop the P0 waves, is settled: registers deleted.)
2. **Finish Phase 2** (`.planning/` phase 06). FS052 is done (see table). Still open:
   - Widen `SPECS` in `tasks/build_edfacts_seeds.py` spec by spec; its asserts flag each new shape
     (FS029's per-level layouts, specs with no Total Indicator, multiple data-record tables).
   - `edfacts_config` shaped to the FS5002–FS5029 metadata collections, one column per SEA policy
     answer. Derive the columns per collection from the specs and the Generate wiki. For FS052
     that means the MEMBERDTE count date and the CCDGRADE13, CCDUNGRADED and ADULTEDU grade
     toggles, which today come in through the `exclude_values` argument.
   - `xwalk_edfacts_*` seeds, pre-filled from the Ed-Fi 6.1 default descriptors in
     `wiki/reference/ed-fi/6.1.0/`.
   - Not implemented yet: `-1` missing counts. LEA/school zero-fill also ignores FS039 grades
     offered, so it emits zero rows for grades a school doesn't offer.
     That belongs in the Phase 3 population model.
3. **Phase 3 — vertical slices:** FS052+FS039, FS002/FS089, FS029 end to end on sample Ed-Fi data.
4. **Apply the SY 2026-27 guidance changes** when building those files: FS118 cumulative count,
   FS195 once-per-shared-time-school, FS113/FS125 program-type zero exceptions, FS127 count type,
   assessment zero counts (`wiki/analysis/EDFacts-2026-27-Delta.md`).
5. **When files go Active:** re-run the fetch (below) for spec revisions and the SY 2026-27 BRSI.

### On deck (vault)

- **Review the BRSI rules, then port them into dbt tests.** The review sheet is
  `wiki/edfacts/BRSI/BRSI Rules Review for dbt Tests.md` (315 rules, each with a proposed handling
  and a pre-set decision; built by `tasks/build_brsi_review.py`) with a live copy that has dropdown
  decisions at https://claude.ai/code/artifact/0d1fae66-f6a9-49f2-8c08-4875755c4d9a. Decisions
  made in the Claude Doc are the record; fold them back into `OVERRIDES` in the script so the vault
  copy matches. Then each "Test now" rule becomes `brsi_<rule id>` in `edu_ext_edfacts`.
- **Derive `edfacts_config` columns from the metadata notes.** The four guides that apply to the
  converted specs (CCD Grades Offered, CCD Staff FTE and Membership, IDEA Part B Child Count,
  IDEA Part C Child Count) list each SEA policy question verbatim under "Responding to FS5xxx".
- **When the SY 2026-27 BRSI and Workbook are published:** refresh the freeze, point
  `BRSI_XLSX` / `WORKBOOK_PDF` in `tasks/convert_companions_to_vault.py` at the new files and
  re-run the three-step vault rebuild. The metadata-guide picker reads the frozen page, so it
  needs no change.
- **If the 75 Inactive specs are ever needed in the vault:** widen the status filter in
  `convert_specs_to_vault.py` (`("Active", "Optional")`); the per-spec rules notes follow
  automatically.
- Not carried into the vault: screenshots and figures in the PDFs, the EDPass general user and
  account guides (`general/`), and prior-version companions the pages still link.

## Gotchas

- **ed.gov refuses every non-browser client** (curl, PowerShell, headless Chrome, WebFetch → 403
  or a WAF page). Refresh with `tasks/fetch_edgov_via_chrome.ps1` (visible Chrome over the
  DevTools protocol, launched from WSL via `powershell.exe Start-Process` with
  `--remote-debugging-port=9223`), pacing ~4 s per file, then `tasks/freeze_edfacts_catalog.py <year>`.
  Never hand-edit files under `wiki/reference/` (checksummed).
- **Remote:** https://github.com/roshd87/EDUEDfactsExploration (public, added 2026-10-13; local-only before that). The frozen federal documents under `wiki/reference/edfacts/<year>/`, the Ed-Fi schema tarball, and `sources/generate/` are git-ignored and live only on disk (manifests and READMEs stay tracked). The pre-reset history that contained them is kept only under the local tag `archive/main-pre-reset` (never push it); `main` is the published snapshot history.
- **dbt package macros:** a root project only sees them namespaced (`edu_ext_edfacts.x`), and
  that holds for calls between the package's own macros too. Each `ref()` must run at parse time,
  outside any `if execute` guard, or dbt can't infer the dependency.
- Generate defects that make files empty or wrong as shipped are catalogued in
  `wiki/generate/repo/Source-Code-Oddities.md`; check there before porting
  Generate logic.
- **Vault conversion tooling** (details in `CLAUDE.md` § Tooling): system Python is externally
  managed, so PDF/XLSX libraries live in `~/.venvs/edfacts-tools`; pandoc emits HTML tables for
  any DOCX table with multi-paragraph cells, which the spec converter flattens to pipe tables;
  Obsidian needs `\|` for the alias pipe of a wikilink inside a table cell.
- **Companion picker in `convert_specs_to_vault.py` globs `BRSI SY *.md`** for the inventory note; the
  review sheet shares the folder and sorts first, which once swapped the index link (fixed 2026-10-17).
- **Vault rebuild order matters:** specs → companions → specs. The spec notes read the companion
  notes' frontmatter for back-links; the companions read the spec catalog for link targets.

## Rebuild commands

```sh
python3 tasks/extract_federal_table_cells.py --year 2026-27  # tasks/reports/2026-27/federal-{table-cells,document-blocks}.csv
python3 tasks/build_federal_delta.py 2025-26 2026-27
python3 tasks/reports/field-review/validate_shards.py
python3 tasks/reports/field-review/consolidate_shared_fields.py
python3 tasks/build_edfacts_seeds.py --year 2026-27  # seeds; then dbt build per edu_ext_edfacts/README.md
python3 tasks/convert_specs_to_vault.py              # wiki/edfacts/ Obsidian spec notes (needs pandoc)
~/.venvs/edfacts-tools/bin/python tasks/convert_companions_to_vault.py  # BRSI/Workbook/metadata notes (venv: pip install openpyxl pymupdf4llm)
python3 tasks/convert_specs_to_vault.py              # again: spec notes read the companion notes for back-links
~/.venvs/edfacts-tools/bin/python tasks/build_brsi_review.py            # wiki/edfacts/BRSI/BRSI Rules Review for dbt Tests.md
```
