---
tags: [analysis, edfacts, catalog, delta]
baseline: "EDFacts SY 2026-27 catalog frozen 2026-10-07 vs SY 2025-26 frozen 2026-08-08"
---

# EDFacts SY 2026-27 Delta

> [!info] Seam: standard-agnostic
> Federal specification changes only. Nothing here depends on Generate or on any source standard.

Compares the SY 2026-27 file specifications (`wiki/reference/edfacts/2026-27/`, 94 DOCX, all
v23.x) with the SY 2025-26 set (`../2025-26/`, 95 DOCX, v22.x). Three sources of evidence, in
increasing depth: the catalog inventories, each document's own history table, and a normalized
cell-by-cell diff of both years' Pandoc extractions
(`tasks/build_federal_delta.py` → `tasks/reports/2026-27/federal-delta-2025-26-to-2026-27.csv`,
197 rows across 53 specs; year strings, version numbers and dash variants are normalized away).

## Catalog

| | SY 2025-26 | SY 2026-27 |
|---|---:|---:|
| DOCX in catalog | 95 | 94 |
| Distinct FS ids | 94 | 93 |
| Versions | 84 × v22.0, 10 × v22.1, 1 × v2.0 | 93 × v23.0, 1 × v23.1 (FS029 LA Directory) |
| Active / Inactive / Optional at freeze | 18 / 75 / 2 | 0 / 94 / 0 ("There are no active files at this time") |

- **Dropped:** FS112 (DG647) Special Education Paraprofessionals. Not linked and not mentioned
  anywhere on the SY 2026-27 page. Its Generate report `c112` is now historical.
- **Added:** none.
- FS045 moves from the odd `v2.0` to `v23.0`; FS040's title loses its slash ("Graduates
  Completers").
- FS224/FS225 are listed as plain Inactive, no longer flagged Optional.

## What each document says changed (document history, v23.0 row)

83 of 94 documents carry an empty "Updated for SY 2026-27" entry: editorial only. Eleven carry a
description:

| Spec | Stated change |
|---|---|
| FS175, FS178, FS179 | Revised Table 2.2-1 zero-count guidance; revised §2.2 data-package guidance; revised every §2.4 table's comments on MISSING and on state-used permitted values; revised §2.5; §2.6 adds definitions for assessments with and without accommodations |
| FS185, FS188, FS189 | Same as above minus the §2.6 accommodation definitions |
| FS113, FS125 | Table 2.2-1 zero-exceptions reporting revised |
| FS127 | Table 2.2-1 type of count revised |
| FS118 | New §2.5 guidance on counting homeless students enrolled at any time in the year |
| FS195 | New §2.5 guidance on reporting students |
| FS029 v23.1 | Typo fix in Table D.1.3-2 (LA data record example) |

## What the cell diff shows (substantive, by collection)

**Assessment files (FS175/FS178/FS179/FS185/FS188/FS189).** The largest diff by volume, mostly
relocation: the §2.4 and §2.6 content moved under headings now prefixed "Revised!", so the diff
counts them as removed-then-added. The real changes inside: the core requirement is now "required
for all applicable combinations for the state" (was "all valid combinations"); every reference to
the "assessment metadata survey" becomes the "assessment metadata collection" with explicit
metadata file ids (FS5005 significant medical emergency, FS5006 math, FS5007 RLA, FS5008
science); the related-files table lists those FS5xxx data groups; a new "data packages" paragraph
points at the EDPass Academic Assessment metadata user guide; grade-level and assessment-type
comments say "if used by the state" and "do not use with HS for the same assessment"; the
unknown-race/sex guidance ("leave these students out of the relevant category set, keep them in
the subtotal") is restated.

**N or D (FS113/FS125/FS127/FS119).** FS113/FS125 zero-exceptions cell changes from "if a state
does not have programs under a program type, leave those counts out" to "Revised! None", so every
program type is now expected. FS127's count becomes "once for each type of delinquent or at-risk
program"; the facility-type definitions (group home, long-term secure, ranch/wilderness camp…) are
revised in FS119/FS127.

**Homeless (FS118).** New Q&A: SEAs that receive point-in-time enrollment reports more than once a
year must compile a cumulative, unduplicated count of homeless students enrolled at any time during
the school year.

**Chronic absenteeism (FS195).** New Q&A on shared-time schools: a student is counted once at each
school where they meet the chronic-absence definition. The header-record file-name text was
simplified to the SEA line.

**Directory (FS029).** Operational-status special-situation examples roll forward (school years
2034-35/2036-37 replace 2015-16/2035-36); one data-record example cell changes (the v23.1 typo
fix).

**Membership (FS052), Child Count (FS002).** Punctuation-level only (race-code list formatting;
"IEP or service plan" parenthesis).

**Part C and dispute resolution (FS901–FS908, FS227–FS230), FS210/FS211, FS218–FS221, FS160,
FS206.** Under 20 normalized cell changes each; wording of reporting-period phrases
("school years" → "reporting years") and metadata-collection references.

## Consequences for the plan

1. **The SEA policy answers now travel as EDPass metadata files (FS5002–FS5029).** The 2026-27
   specs reference "metadata collection FS5xxx" 57 times versus 9 residual "survey" mentions. The
   `edfacts_config` seed proposed in `EDFactsOutputPlan.md` Phase 2 should be shaped to those
   FS5xxx collections (the 28 metadata user guides are cached under `../reference/edfacts/2026-27/metadata/`),
   so the same seed can emit the metadata files and drive the data files.
2. **Drop FS112** from every rollout list.
3. **Rules changed by the new guidance:** FS118 cumulative count (Generate's "homelessness starts
   during the enrollment" filter is now explicitly wrong); FS195 once-per-school counting;
   FS113/FS125 program-type zero exceptions; FS127 count type; assessment zero-count and
   state-used-value comments.
4. **No layout changes were detected** in any Data Record Definition or Header Record Definition
   beyond formatting, so the Phase 2 layout seeds can be built from either year's extraction.
5. The SY 2026-27 BRSI is not published yet; the Business Rules page links SY 2025-26 v1.04 (the
   2025-26 cache holds v1.03). Re-check when the files go Active.

## Citations

- `wiki/reference/edfacts/2026-27/file-specifications/CATALOG-INVENTORY.tsv`, `MANIFEST.csv`
- `wiki/reference/edfacts/2025-26/file-specifications/CATALOG-INVENTORY.tsv`
- `tasks/reports/2026-27/federal-table-cells.csv`, `federal-document-blocks.csv` (all 94 specs)
- `tasks/reports/2025-26/federal-table-cells.csv`, `federal-document-blocks.csv` (all 95 specs)
- `tasks/reports/2026-27/federal-delta-2025-26-to-2026-27.csv`
