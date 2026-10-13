# CLAUDE.md

## What this is

Produce EDPass-submittable EDFacts files from an **Ed-Fi + EDU/Stadium** warehouse (`edu_wh` dbt
marts) as a dbt extension package, `edu_ext_edfacts/`: spec-derived seeds (category sets, layouts,
permitted values), a GROUPING SETS count macro, and a fixed-width record macro. Plan:
`EDFactsOutputPlan.md`. Status and next steps: `HANDOFF.md`. Tracker: `.planning/` (see
`docs/agents/issue-tracker.md`). Split out of `GenerateExplorer` on 2026-10-12 (that repo was deleted 2026-10-13). The
read-only wiki of how CEDS Generate works lives here at `wiki/generate/` (moved 2026-10-13; reading
guide in `wiki/generate/README.md`) — use
it for business rules the specs leave unstated; its SQL citations point at
`sources/generate/`.

## Sources of truth

- **EDFacts file specifications** (SY 2026-27, plus Workbook, BRSI, EDPass metadata guides) are the
  authority on file content. Frozen under `wiki/reference/edfacts/<year>/` (checksummed — never
  hand-edit) with full-text extractions in `tasks/reports/<year>/`. SY 2025-26 is kept as lineage.
- **Ed-Fi:** `wiki/reference/ed-fi/6.1.0/` (pinned schemas + descriptors), `sources/edfi/` (DS 5.2.0
  swagger cited by `wiki/analysis/EDFacts-EdFi-Gap-Analysis.md`).
- The EDU/Stadium model map lives in `/mnt/c/Repos/EDUAPIExplorer/wiki/`.

## Refreshing the spec catalog

`www.ed.gov` returns 403 to every non-browser client (curl, PowerShell, headless Chrome, WebFetch).
Refresh only with `tasks/fetch_edgov_via_chrome.ps1` (drives a visible Windows Chrome over the
DevTools protocol from WSL), then `tasks/freeze_edfacts_catalog.py <year>`.

## Build

```sh
python3 tasks/build_edfacts_seeds.py --year 2026-27   # byte-identical rebuild of edu_ext_edfacts/seeds
```
Then `dbt build` per `edu_ext_edfacts/README.md`. Full rebuild list in `HANDOFF.md`.

## Agent skills

- Issue tracker: `.planning/` phase plans, local-only repo. See `docs/agents/issue-tracker.md`.
- Triage labels: `docs/agents/triage-labels.md`. Domain docs: `docs/agents/domain.md`.
