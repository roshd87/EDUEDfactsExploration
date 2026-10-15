---
fs_id: FS207
title: FS207 Business Rules
brsi: SY 2025-26 v1.04
rules: 3
discontinued: 0
source: business-rules/edfacts-business-rules-single-inventory-sy-2025-26-v104-113313.xlsx
sha256: 94a0bd49aa8a715f41e501b84d0cb828384ca2ce42c9b3e40b01d9961784aab8
frozen: 2026-10-07
tags: [edfacts, brsi, business-rules]
---

# FS207 Business Rules (SY 2025-26 v1.04)

> [!abstract] At a glance
> **Spec:** [[FS207 State Appropriations for Charter Schools]]
> **Rules naming FS207:** 3 active, 0 discontinued or suspended
> **Also applies:** the cross-file rules in [[BRSI SY 2025-26#Rules that apply across files|BRSI SY 2025-26]]
> **Columns:** Phase is the EDPass data-quality phase; Levels is where the rule runs; Files lists every spec the rule reads, so a rule can appear in several notes.

> [!info] Source
> Converted by `tasks/convert_companions_to_vault.py` from the frozen SY 2026-27 catalog copy of the BRSI workbook (`wiki/reference/edfacts/2026-27/business-rules/edfacts-business-rules-single-inventory-sy-2025-26-v104-113313.xlsx`). The original remains the authority.

## Active rules

| Rule ID | Legacy ID | Phase | Objective | Failure | Levels | Files | DGs | Definition | Rule logic | Error message | Threshold | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **CHAR-0007** | Charter-017, S207-R01 | Pre-submission | Directory and rosters | Rule Failure | SCH | [[FS029 Directory\|029]], [[FS207 State Appropriations for Charter Schools\|207]] | 27, 845 | Non-charter schools must not be included in State Appropriations for Charter Schools. | Fails when [[FS029 Directory\|FS029]]/DG27 Charter Status equals NO or NA and [[FS207 State Appropriations for Charter Schools\|FS207]]/DG845 State Appropriations for Charter is reported. | Charter Status equals NO or NA, but State Appropriations for Charter was reported.<br>*Condition: Charter Status, State Appropriation Method* |  |  |
| **CHAR-0008** | Charter-018 | Pre-submission | Directory and rosters | Rule Failure | SCH | [[FS029 Directory\|029]], [[FS207 State Appropriations for Charter Schools\|207]] | 27, 531, 845 | State Appropriations for Charter are expected to be reported for charter schools. | Fails when:<br>1) [[FS029 Directory\|FS029]]/DG27 Charter Status equals YES, and <br>2) [[FS029 Directory\|FS029]]/DG531 Operational Status - School Effective is operational, and<br>3) [[FS207 State Appropriations for Charter Schools\|FS207]]/DG845 State Appropriations for Charter is not reported | Charter Status equals YES, but State Appropriations for Charter was not reported.<br>*Condition: Charter Status, Operational Status* |  |  |
| **FMTE-0001** | ER-59, ER-103 | Pre-submission | Format and Validation | Format Error | SEA, LEA, SCH | [[FS029 Directory\|029]], [[FS059 Staff FTE\|059]], 103, [[FS129 CCD School\|129]], 130, 131, 132, 163, 165, 169, [[FS197 Crosswalk of Charter Schools to Management Organizations\|197]], 205, 206, [[FS207 State Appropriations for Charter Schools\|207]], [[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|231]], [[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|232]], [[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|233]], [[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|234]], [[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|236]], [[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|237]] | 4, 5, 559, 570, 833, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 910, 911, 912, 913 | The State Code, State Agency Number, LEA Identifier (State) (LEA and SCH level), and School Identifier (State) (SCH level) must be unique within the uploaded file. | Fails when the uploaded file contains more than one row of data for the combination of the DG559 State Code, DG570 State Agency Number, DG4 LEA Identifier (State) (LEA and SCH level), and DG5 School Identifier (State) (SCH level). | The uploaded file contained more than one row of data for the combination of the State Code, State Agency Number, LEA Identifier (State) (LEA and SCH level), and School Identifier (State) (SCH level).<br>*Condition: State Code, State Agency Number, LEA Identifier (State), School Identifier (State)* |  |  |
