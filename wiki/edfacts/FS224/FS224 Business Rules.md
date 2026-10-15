---
fs_id: FS224
title: FS224 Business Rules
brsi: SY 2025-26 v1.04
rules: 2
discontinued: 0
source: business-rules/edfacts-business-rules-single-inventory-sy-2025-26-v104-113313.xlsx
sha256: 94a0bd49aa8a715f41e501b84d0cb828384ca2ce42c9b3e40b01d9961784aab8
frozen: 2026-10-07
tags: [edfacts, brsi, business-rules]
---

# FS224 Business Rules (SY 2025-26 v1.04)

> [!abstract] At a glance
> **Spec:** [[FS224 N or D Assessment Proficiency – State Agency]]
> **Rules naming FS224:** 2 active, 0 discontinued or suspended
> **Also applies:** the cross-file rules in [[BRSI SY 2025-26#Rules that apply across files|BRSI SY 2025-26]]
> **Columns:** Phase is the EDPass data-quality phase; Levels is where the rule runs; Files lists every spec the rule reads, so a rule can appear in several notes.

> [!info] Source
> Converted by `tasks/convert_companions_to_vault.py` from the frozen SY 2026-27 catalog copy of the BRSI workbook (`wiki/reference/edfacts/2026-27/business-rules/edfacts-business-rules-single-inventory-sy-2025-26-v104-113313.xlsx`). The original remains the authority.

## Active rules

| Rule ID | Legacy ID | Phase | Objective | Failure | Levels | Files | DGs | Definition | Rule logic | Error message | Threshold | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ND-0030** |  | Pre-submission | Completeness | Rule Failure | SEA | [[FS224 N or D Assessment Proficiency – State Agency\|224]] | 868 | The N or D Assessment Proficiency – State Agency file must contain meaningful data. | Fails when all zeros are reported for DG868 N or D Assessment Proficiency Table – State Agency for all of the following category sets:<br>-Category Set A - Student Count by Academic Subject (Assessment – no science) by Proficiency Status | The N or D Assessment Proficiency – State Agency file contained all zeros. |  |  |
| **ND-0031** |  | Pre-submission | Completeness | Data Error | SEA | [[FS224 N or D Assessment Proficiency – State Agency\|224]] | 868 | The N or D Assessment Proficiency – State Agency file must contain meaningful data. | Fails when all -1s are reported for DG868 N or D Assessment Proficiency Table – State Agency for all of the following category sets:<br>-Category Set A - Student Count by Academic Subject (Assessment – no science) by Proficiency Status | The N or D Assessment Proficiency – State Agency file contained all -1s. |  |  |
