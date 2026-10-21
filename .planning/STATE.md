---
milestone: v2.0
milestone_name: edfacts-from-edfi
current_phase: 06
current_phase_name: spec-seeds-and-macros
status: executing
last_updated: "2026-10-21"
---

# Project State

See `.planning/PROJECT.md` and `EDFactsOutputPlan.md`.


## Current Position

- Phase 04 (SY 2026-27 baseline): **done 2026-10-07** via Chrome-driven fetch
  (`tasks/fetch_edgov_via_chrome.ps1`) + `tasks/freeze_edfacts_catalog.py`; delta note
  `wiki/analysis/EDFacts-2026-27-Delta.md`.
- Phase 05 (hidden-logic pass): **done 2026-10-07**, 336 rules; register **deleted 2026-10-12** at
  the repo split (owner decision). Headline kept in `EDFactsOutputPlan.md` Phase 1.
- Field review of all 94 SY 2026-27 specs: **done 2026-10-07** — `wiki/analysis/EDFacts-2026-27-Shared-Fields.md`.
- Synopsis published: `wiki/analysis/EDFacts-2026-27-Findings.html`.
- Phase 06 (spec seeds + macros): **in progress**. FS052 renders from seeds alone in `edu_ext_edfacts/`
  (2026-10-09); remaining: widen spec allowlist, `edfacts_config`, `xwalk_edfacts_*`. See `HANDOFF.md`.
- Proposed Plan 1 (2026-10-21): FS029 precursor → FS039 → FS052 sequence plus a 40-element completeness
  evaluation against current `edu_wh`/`edu_edfi_source` (20 ready / 10 crosswalk / 5 build gap / 5 manual).
  `EDFactsOutputPlan.md` §4a; runbook `wiki/analysis/EDFacts-Plan1-FS039-FS052-Runbook.html`. **Gate G1 open.**

## Blockers

- **Start gate G1 / decisions E6 and E7:** Proposed Plan 1 (`EDFactsOutputPlan.md` §4a) and the status
  and year-change tracking approach (`wiki/analysis/Status-and-Year-Change-Tracking.md`) must both be
  decided before Phase 07 starts. No defaults.
- Owner decisions E1–E3 (`EDFactsOutputPlan.md` §5); defaults apply until overridden. E5 settled.

## History

2026-10-12: split out of GenerateExplorer. v1.0 (Generate-to-Ed-Fi P0 mapping baseline, phases
01–03) and the hidden-logic register were deleted. GenerateExplorer and its history were deleted
2026-10-13 (no remote); nothing is recoverable.
