---
fs_id: FS198
title: FS198 Business Rules
brsi: SY 2025-26 v1.04
rules: 4
discontinued: 1
source: business-rules/edfacts-business-rules-single-inventory-sy-2025-26-v104-113313.xlsx
sha256: 94a0bd49aa8a715f41e501b84d0cb828384ca2ce42c9b3e40b01d9961784aab8
frozen: 2026-10-07
tags: [edfacts, brsi, business-rules]
---

# FS198 Business Rules (SY 2025-26 v1.04)

> [!abstract] At a glance
> **Spec:** [[FS198 Charter Contracts]]
> **Rules naming FS198:** 4 active, 1 discontinued or suspended
> **Also applies:** the cross-file rules in [[BRSI SY 2025-26#Rules that apply across files|BRSI SY 2025-26]]
> **Columns:** Phase is the EDPass data-quality phase; Levels is where the rule runs; Files lists every spec the rule reads, so a rule can appear in several notes.

> [!info] Source
> Converted by `tasks/convert_companions_to_vault.py` from the frozen SY 2026-27 catalog copy of the BRSI workbook (`wiki/reference/edfacts/2026-27/business-rules/edfacts-business-rules-single-inventory-sy-2025-26-v104-113313.xlsx`). The original remains the authority.

## Active rules

| Rule ID | Legacy ID | Phase | Objective | Failure | Levels | Files | DGs | Definition | Rule logic | Error message | Threshold | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **CHAR-0001** | Charter-002a | Pre-submission | Directory and rosters | Rule Failure | SCH, Other (C) | [[FS029 Directory\|029]], [[FS198 Charter Contracts\|198]] | 27, 531, 830 | Charter contracts are expected to be reported for charter schools. | Fails when:<br>1) [[FS029 Directory\|FS029]]/DG27 Charter Status equals YES, and<br>2) [[FS029 Directory\|FS029]]/DG531 Operational Status - School Effective is operational, and<br>3) [[FS198 Charter Contracts\|FS198]]/DG830 Charter Contract is not reported | Charter Status equals YES, but Charter Contract was not reported.<br>*Condition: Charter Status, Operational Status* |  |  |
| **CHAR-0002** | Charter-002b | Pre-submission | Directory and rosters | Rule Failure | SCH, Other (C) | [[FS029 Directory\|029]], [[FS198 Charter Contracts\|198]] | 27, 830 | Charter contracts are not expected to be reported for non-charter schools. | Fails when [[FS029 Directory\|FS029]]/DG27 Charter Status equals NO or NA and [[FS198 Charter Contracts\|FS198]]/DG830 Charter Contract is reported. | Charter Status equals NO or NA but Charter Contract was reported.<br>*Condition: Charter Status, Charter Contract ID Number* |  |  |
| **CHAR-0005** | Charter-013, S198-R04 | Pre-submission | Directory and rosters | Rule Failure | SCH, Other (C) | [[FS198 Charter Contracts\|198]] | 831, 832 | The Charter Contract Approval date must be prior to the Charter Contract Renewal date. | Fails when the DG831 Charter Contract Approval Date is not prior to the DG832 Charter Contract Renewal Date. | The Charter Contract Approval Date is not prior to the Charter Contract Renewal Date.<br>*Condition: Charter Contract Approval Date, Charter Contract Renewal Date* |  |  |
| **FERR-0011** | ER-132 | Pre-submission | Format and validation | File Error | LEA, SCH | [[FS029 Directory\|029]], [[FS198 Charter Contracts\|198]] | 831, 832, 571 | Date fields must be in the correct format (YYYY-MM-DD). | Fails when a date field is not in the correct format (YYYY-MM-DD). | A date field was not in the correct format (YYYY-MM-DD).<br>*Condition: Date* |  |  |

## Discontinued or suspended rules

| Rule ID | Legacy ID | Phase | Objective | Failure | Levels | Files | DGs | Definition | Rule logic | Error message | Threshold | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **CHAR-0006** | Charter-016, S198-R03 | Pre-submission | Directory and rosters | Rule Failure | SCH, Other (C) | [[FS198 Charter Contracts\|198]] | 831, 832 | The Charter Contract Approval date and the Charter Contract Renewal date are not expected to have more than a 5 year difference. | Fails when the time period between DG831 Charter Contract Approval Date and DG832 Charter Contract Renewal Date is greater than 5 years. | The time period between Charter Contract Approval Date and Charter Contract Renewal Date is greater than 5 years.<br>*Condition: Charter Contract Approval Date, Charter Contract Renewal Date* | 5 | Suspended: Suspended - threshold years under review |
