---
fs_id: FS904
title: FS904 Business Rules
brsi: SY 2025-26 v1.04
rules: 6
discontinued: 0
source: business-rules/edfacts-business-rules-single-inventory-sy-2025-26-v104-113313.xlsx
sha256: 94a0bd49aa8a715f41e501b84d0cb828384ca2ce42c9b3e40b01d9961784aab8
frozen: 2026-10-07
tags: [edfacts, brsi, business-rules]
---

# FS904 Business Rules (SY 2025-26 v1.04)

> [!abstract] At a glance
> **Spec:** [[FS904 At Risk Infants and Toddlers with Disabilities (IDEA Part C)]]
> **Rules naming FS904:** 6 active, 0 discontinued or suspended
> **Also applies:** the cross-file rules in [[BRSI SY 2025-26#Rules that apply across files|BRSI SY 2025-26]]
> **Columns:** Phase is the EDPass data-quality phase; Levels is where the rule runs; Files lists every spec the rule reads, so a rule can appear in several notes.

> [!info] Source
> Converted by `tasks/convert_companions_to_vault.py` from the frozen SY 2026-27 catalog copy of the BRSI workbook (`wiki/reference/edfacts/2026-27/business-rules/edfacts-business-rules-single-inventory-sy-2025-26-v104-113313.xlsx`). The original remains the authority.

## Active rules

| Rule ID | Legacy ID | Phase | Objective | Failure | Levels | Files | DGs | Definition | Rule logic | Error message | Threshold | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **IDEA-0102** |  | Pre-submission | Completeness | Data Error | SEA | [[FS904 At Risk Infants and Toddlers with Disabilities (IDEA Part C)\|904]] | 5025 | The At Risk Infants and Toddlers with Disabilities (IDEA Part C) file must contain meaningful data. | Fails when all -1s are reported for DG5025 At risk infants and toddlers table for all of the following category sets/subtotals:<br>- Category Set A - Infants and Toddlers Count by Racial Ethnic by Age (EI)<br>- Category Set B - Infants and Toddlers Count by Age (EI)<br>- Education Unit Total - Education Unit Total of Infants and Toddlers Count | The At Risk Infants and Toddlers with Disabilities (IDEA Part C) file contained all -1s. |  |  |
| **IDEA-0106** |  | Pre-submission | Completeness | Rule Failure | SEA | [[FS904 At Risk Infants and Toddlers with Disabilities (IDEA Part C)\|904]] | 5025 | All permitted value combinations are expected for At Risk Infants and Toddlers with Disabilities (IDEA Part C) because zero reporting is required. | Fails when counts for DG5025 At risk infants and toddlers table are not reported for all permitted value combinations for all category sets and subtotals in the following category sets/subtotals: <br>- Category Set A - Infants and Toddlers Count by Racial Ethnic by Age (EI)<br>- Category Set B - Infants and Toddlers Count by Age (EI) | A count of At Risk Infants and Toddlers with Disabilities (IDEA Part C) was not reported for one or more permitted value combinations.<br>*Condition: Category Set/Subtotal, PV Combination* |  |  |
| **IDEA-0110** | PartC-CC-044 | Pre-submission | Accuracy | Rule Failure | SEA | [[FS904 At Risk Infants and Toddlers with Disabilities (IDEA Part C)\|904]] | 5025 | The sum of At Risk Infants and Toddlers with Disabilities (IDEA Part C) for category sets and subtotals that include all infants and toddlers are expected to equal the EUT. | Fails when the sum of one or more of the following category sets / subtotals for DG5025 At risk infants and toddlers table < the EUT, and the \|difference\|, divided by EUT, is > Threshold %.<br>- Category Set A - Infants and Toddlers Count by Racial Ethnic by Age (EI)<br>- Category Set B - Infants and Toddlers Count by Age (EI) | The sum of At Risk Infants and Toddlers with Disabilities (IDEA Part C) in one or more category sets or subtotals that include all students did not equal the EUT.<br>*Condition: Category Set/Subtotal, Category Set/Subtotal Sum, EUT* | 1 |  |
| **IDEA-0235** |  | Pre-submission | Completeness | Rule Failure | SEA | [[FS904 At Risk Infants and Toddlers with Disabilities (IDEA Part C)\|904]] | 5025 | Children are expected to be reported for all permitted values of Racial Ethnic for At Risk Infants and Toddlers with Disabilities (IDEA Part C). | For SEA level,<br>Fails when, for any permitted value combination of DG5025 At Risk Infants and Toddlers with Disabilities (IDEA Part C) Racial Ethnic (Category Set A):<br>The count of children in the SEA = 0. | The count of children was reported as zero for one or more permitted value where children are expected to be reported for At Risk Infants and Toddlers with Disabilities (IDEA Part C).<br>*Condition: Category Set/Subtotal, PV, Count* |  | New |
| **IDEA-0239** | PartC-CC-031 | Pre-submission | Longitudinal | Rule Failure | SEA | [[FS904 At Risk Infants and Toddlers with Disabilities (IDEA Part C)\|904]] | 5025 | The child count for all Age (EI) and Racial Ethnic permitted values reported in the current SY is expected to be similar to the prior SY. | For any Racial Ethnic (Category Set A) or Age (EI) (Category Set B) permitted value, fails when: <br>A1) The prior SY PV <> 0; and <br>A2) The prior SY PV minus the current SY PV (\|PY-CY\|) > Threshold Base and prior SY PV minus current SY PV divided by prior year PV (\|PY-CY\|/PY)*100 > Threshold %<br>OR<br>B1) The prior SY PV = 0; and <br>B2) The prior SY PV minus the current SY PV (\|PY-CY\|) > Threshold Base | The child count for one or more Racial Ethnic and Age (EI) permitted values reported in the current SY varied significantly from the prior SY.<br>*Condition: Category Set [Subtotal], PV, Current SY Count, Prior SY Count, Difference, % Difference* | 50 30 | New: New YTY Rule |
| **IDEA-0243** | PartC-CC-033 | Pre-submission | Longitudinal | Rule Failure | SEA | [[FS904 At Risk Infants and Toddlers with Disabilities (IDEA Part C)\|904]] | 5025 | The file reported for the current SY is not expected to be identical to the file reported for the prior SY. | Fails when:<br>1) the sum of all values reported for the current SY is identical to the sum of all values reported for the prior SY, and<br>2) The sum of all values in the following category sets/EUT is identical to the sum of all values reported for the prior SY:<br>- Category Set A - Infants and Toddlers Count by Racial Ethnic<br>- Category Set B - Infants and Toddlers Count by Age (EI)<br>- Education Unit Total - Education Unit Total of Infants and Toddlers Count | The file reported for the current SY was identical to the file reported for the prior SY. |  | New: New YTY Rule |
