# Requirements: EDFacts Files from Ed-Fi + EDU/Stadium

**Defined:** 2026-10-07
**Core value:** every rule the spec leaves open is taken from the spec, taken from Generate with
citation, or set as named configuration.

## v1

- [ ] **BASE-01** SY 2026-27 catalog frozen (`wiki/reference/edfacts/2026-27/`, MANIFEST + CATALOG-INVENTORY)
- [ ] **BASE-02** Extraction chain re-run for 2026-27; outputs year-scoped under `tasks/reports/`
- [ ] **BASE-03** `wiki/analysis/EDFacts-2026-27-Delta.md` lists every changed FS/version/category/value/layout
- [x] **HL-01..03** hidden-logic register built (2026-10-07); **deleted 2026-10-12** at the repo split — rules are re-derived per collection from the specs and the Generate wiki
- [ ] **SEED-01** `tasks/build_edfacts_seeds.py` derives category-set, layout, permitted-value, header seeds from `federal-*.csv`, byte-stable on rebuild
- [ ] **SEED-02** `edfacts_config` seed has a column for every SEA policy answer, shaped to the FS5002–FS5029 metadata collections
- [ ] **SEED-03** `xwalk_edfacts_*` seeds exist per category family, pre-filled from Ed-Fi 6.1 default descriptors (`wiki/reference/ed-fi/6.1.0/`)
- [ ] **MAC-01** `edfacts_counts` macro renders the per-set count query for any FS/org level from seeds
- [ ] **MAC-02** `edfacts_record`/`edfacts_header` macros render the fixed-width layout from seeds
- [ ] **TEST-01** permitted-value and SQL-expressible BRSI rules exist as dbt tests
- [ ] **SLICE-01** FS052 (+FS039) file from sample Ed-Fi data passes TEST-01
- [ ] **SLICE-02** FS002/FS089 file passes TEST-01
- [ ] **SLICE-03** FS029 SEA/LEA/school files pass TEST-01
- [ ] **ROLL-01..07** remaining collection waves (plan §4 Phase 4 order)
- [ ] **DEPLOY-01** package versioned; partner `packages.yml` + seeds; export task; reporting-year var

## Out of scope

| Item | Reason |
|---|---|
| Generate/SQL Server/CEDS at runtime | reading source only |
| EDPass submission automation | no public API |
| P0 register waves | stopped (E5); registers deleted 2026-10-12 |

## Traceability

| Requirement | Phase |
|---|---|
| BASE-* | 04 |
| HL-* | 05 |
| SEED-*, MAC-*, TEST-01 | 06 |
| SLICE-* | 07 |
| ROLL-* | 08–14 |
| DEPLOY-01 | 15 |
