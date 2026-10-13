# Roadmap: EDFacts Files from Ed-Fi + EDU/Stadium

Detailed phase text lives in `EDFactsOutputPlan.md` §4; this file is the index. Phase numbering
starts at 04; 01–03 were the P0 project, deleted at the 2026-10-12 split.

| Phase | Dir | Goal | Depends on | Exit criterion |
|---|---|---|---|---|
| 04 | `04-sy2026-27-baseline` | Freeze SY 2026-27 catalog, re-extract, write delta note | owner download | manifest + extraction counts + delta note — done 2026-10-07 |
| 05 | `05-hidden-logic-pass` | Consolidate the six Generate-reading shards into the hidden-logic register with reimplement decisions | — | done 2026-10-07; register deleted 2026-10-12 |
| 06 | `06-spec-seeds-and-macros` | Seed builders, config/xwalk schemas, count + record macros, BRSI tests | 04 (or 2025-26 fallback), 05 | FS052 count query and record render from seeds alone |
| 07 | `07-vertical-slices` | FS052+FS039, FS002/FS089, FS029 end to end on sample Ed-Fi data | 06 | files pass SQL-expressible BRSI checks |
| 08–14 | `08-rollout-*` | One wave per collection group (org, IDEA student, staff, programs, outcomes, assessment, finance) | 07 | per-wave BRSI pass + rule disposition |
| 15 | `15-stadium-deploy` | Package release, partner seeds, export task, rollover var | 08+ | one partner produces Active-set files |
