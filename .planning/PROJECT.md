# EDFacts Files from Ed-Fi + EDU/Stadium

## What This Is

Produce EDPass-submittable EDFacts files from an EDU warehouse (`edu_wh` over Ed-Fi ODS data) as a
dbt extension package deployable to any Stadium partner. CEDS Generate is read, never run, via the
Generate wiki in `wiki/generate/`, for business rules the federal file
specifications leave unstated. Full plan: `EDFactsOutputPlan.md`.

Split out of GenerateExplorer on 2026-10-12. The previous Generate-to-Ed-Fi mapping register
project (phases 01–03) and the hidden-logic register were deleted at the split.

## Core Value

A state on Stadium produces every EDFacts file it owes from its own warehouse, with each rule the
spec leaves open either taken from the spec, taken from Generate with citation, or set as named
configuration. No rule is invented silently.

## Requirements

### Validated

- ✓ Spec extraction chain and normalized grain/layout/value CSVs (SY 2025-26) — existing
- ✓ 24 Generate domain notes + verified defect list — `wiki/generate/`

### Active

- [ ] **BASE-01**: SY 2026-27 federal baseline frozen with manifest, extraction, and delta note
- [ ] **SEED-01**: Category-set, layout, permitted-value, and header seeds regenerate from the
  federal CSVs
- [ ] **SEED-02**: `edfacts_config` and `xwalk_edfacts_*` seed schemas cover every SEA policy
  answer the FS5002–FS5029 metadata collections and the built specs need
- [ ] **MAC-01**: Count macro (one GROUP BY per category set, unioned) and record macro render FS052 from seeds alone
- [ ] **SLICE-01..03**: Membership (FS052+FS039), Child Count (FS002/FS089), Directory (FS029)
  files pass SQL-expressible BRSI checks on sample Ed-Fi data
- [ ] **ROLL-01..07**: remaining collections by wave (see plan §4 Phase 4)
- [ ] **DEPLOY-01**: one Stadium partner produces its Active-set files

### Out of Scope

- Running Generate / SQL Server / CEDS at runtime
- EDPass submission automation
- Non-EDFacts state files
- Continuing the P0 register adjudication waves (decision E5: stopped; registers deleted)

## Context

- Evidence caches: `wiki/reference/` (Ed-Fi 6.1, EDFacts 2025-26 and 2026-27), `sources/edfi/`
  (Ed-Fi DS 5.2 swagger), Generate wiki in `wiki/generate/` + SQL cache in `sources/generate/`,
  sibling vault `/mnt/c/Repos/EDUAPIExplorer/wiki/` (EDU/Stadium model map).
- `www.ed.gov` blocks non-browser fetches (403); refresh with `tasks/fetch_edgov_via_chrome.ps1`
  then `tasks/freeze_edfacts_catalog.py`.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Regenerate category sets/layouts/values from the specs, not from Generate `App` metadata | spec is the authority; extraction chain already exists | — Pending E-series |
| Per-set GROUP BY + UNION ALL replaces a count-SQL generator (GROUPING SETS until 2026-10-17) | native SQL does what `Get_CountSQL` hand-built | — Pending |
| SEA policy toggles become seeds | they are EDPass metadata survey answers the state already holds | — Pending |

*Last updated: 2026-10-07 at pivot*
