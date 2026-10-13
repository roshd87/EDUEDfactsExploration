---
milestone: v2.0
milestone_name: edfacts-from-edfi
current_phase: 06
current_phase_name: spec-seeds-and-macros
status: executing
last_updated: "2026-10-12"
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

## Blockers

- Owner decisions E1–E3 (`EDFactsOutputPlan.md` §5); defaults apply until overridden. E5 settled.

## History

2026-10-12: split out of GenerateExplorer. v1.0 (Generate-to-Ed-Fi P0 mapping baseline, phases
01–03) and the hidden-logic register were deleted. GenerateExplorer and its history were deleted
2026-10-13 (no remote); nothing is recoverable.
