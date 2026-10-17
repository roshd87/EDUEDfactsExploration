---
tags: [edfacts, spec, moc]
source_year: "2026-27"
filter_year: "2025-26"
---

# EDFacts File Specifications — SY 2026-27

The file specifications that were **Active or Optional in the SY 2025-26 EDPass catalog**, converted from the SY 2026-27 frozen DOCX files (`wiki/reference/edfacts/2026-27/`). At the 2026-10-07 freeze every SY 2026-27 spec was still Inactive ("no active files at this time"), so the SY 2025-26 status is the working filter. Regenerate with `python3 tasks/convert_specs_to_vault.py`.

Related: [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]] · [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]] · [[generate/Home|CEDS Generate wiki]] · [[Domains-Guide|Generate domains]]

| Spec | Title | Data groups | SY 2025-26 | Generate domain | Business rules | Metadata guides |
|---|---|---|---|---|---|---|
| [[FS002 Children with Disabilities (IDEA) School Age\|FS002]] | Children with Disabilities (IDEA) School Age | DG74 | Active | [[ChildCount]] | [[FS002 Business Rules\|rules]] | [[IDEA Part B Child Count Metadata User Guide\|IDEA Part B Child Count]] |
| [[FS029 Directory\|FS029]] | Directory | multiple | Active | [[Directory]] | [[FS029 Business Rules\|rules]] | — |
| [[FS029 LA Directory\|FS029 LA]] | LA Directory | multiple | Active | [[Directory]] | [[FS029 Business Rules\|rules]] | — |
| [[FS033 Free and Reduced Price Lunch\|FS033]] | Free and Reduced Price Lunch | DG565, DG813 | Active | [[Membership]] | [[FS033 Business Rules\|rules]] | — |
| [[FS039 Grades Offered\|FS039]] | Grades Offered | DG18 | Active | [[Directory]] | [[FS039 Business Rules\|rules]] | [[CCD Grades Offered Metadata User Guide\|CCD Grades Offered]] |
| [[FS052 Membership\|FS052]] | Membership | DG39 | Active | [[Membership]] | [[FS052 Business Rules\|rules]] | [[CCD Grades Offered Metadata User Guide\|CCD Grades Offered]], [[CCD Staff FTE and Membership Metadata User Guide\|CCD Staff FTE and Membership]] |
| [[FS059 Staff FTE\|FS059]] | Staff FTE | DG528, DG644 | Active | [[Staff]] | [[FS059 Business Rules\|rules]] | [[CCD Staff FTE and Membership Metadata User Guide\|CCD Staff FTE and Membership]] |
| [[FS089 Children with Disabilities (IDEA) Early Childhood\|FS089]] | Children with Disabilities (IDEA) Early Childhood | DG613 | Active | [[ChildCount]] | [[FS089 Business Rules\|rules]] | [[IDEA Part B Child Count Metadata User Guide\|IDEA Part B Child Count]] |
| [[FS129 CCD School\|FS129]] | CCD School | DG573, DG791, DG803 | Active | [[Directory]] | [[FS129 Business Rules\|rules]] | — |
| [[FS190 Charter Authorizer Directory\|FS190]] | Charter Authorizer Directory | DG798, DG805, DG806, DG807, DG808 | Active | [[Directory]] | [[FS190 Business Rules\|rules]] | — |
| [[FS196 Management Organization for Charter Schools Roster\|FS196]] | Management Organization for Charter Schools Roster | DG825, DG826, DG827, DG828, DG829 | Active | [[Directory]] | [[FS196 Business Rules\|rules]] | — |
| [[FS197 Crosswalk of Charter Schools to Management Organizations\|FS197]] | Crosswalk of Charter Schools to Management Organizations | DG833 | Active | [[Directory]] | [[FS197 Business Rules\|rules]] | — |
| [[FS198 Charter Contracts\|FS198]] | Charter Contracts | DG830, DG831, DG832 | Active | [[Directory]] | [[FS198 Business Rules\|rules]] | — |
| [[FS207 State Appropriations for Charter Schools\|FS207]] | State Appropriations for Charter Schools | DG845 | Active | [[Directory]] | [[FS207 Business Rules\|rules]] | — |
| [[FS224 N or D Assessment Proficiency – State Agency\|FS224]] | N or D Assessment Proficiency – State Agency | DG868 | Optional | [[Assessments]] | [[FS224 Business Rules\|rules]] | — |
| [[FS225 N or D Assessment Proficiency – LEA\|FS225]] | N or D Assessment Proficiency – LEA | DG871 | Optional | [[Assessments]] | [[FS225 Business Rules\|rules]] | — |
| [[FS902 Infants and Toddlers with Disabilities (IDEA Part C) Early Intervention\|FS902]] | Infants and Toddlers with Disabilities (IDEA Part C) Early Intervention | DG5023 | Active | — | [[FS902 Business Rules\|rules]] | [[IDEA Part C Child Count Metadata User Guide\|IDEA Part C Child Count]] |
| [[FS903 Children with Disabilities (IDEA Part C) Continuing Early Intervention\|FS903]] | Children with Disabilities (IDEA Part C) Continuing Early Intervention | DG5024 | Active | — | [[FS903 Business Rules\|rules]] | [[IDEA Part C Child Count Metadata User Guide\|IDEA Part C Child Count]] |
| [[FS904 At Risk Infants and Toddlers with Disabilities (IDEA Part C)\|FS904]] | At Risk Infants and Toddlers with Disabilities (IDEA Part C) | DG5025 | Active | — | [[FS904 Business Rules\|rules]] | [[IDEA Part C Child Count Metadata User Guide\|IDEA Part C Child Count]] |
| [[FS905 Infants and Toddlers with Disabilities (IDEA Part C) Cumulative Count\|FS905]] | Infants and Toddlers with Disabilities (IDEA Part C) Cumulative Count | DG5026 | Active | — | [[FS905 Business Rules\|rules]] | [[IDEA Part C Child Count Metadata User Guide\|IDEA Part C Child Count]] |

## Companion documents

Converted by `tasks/convert_companions_to_vault.py`. The BRSI and Workbook are the SY 2025-26 editions, the newest published at the freeze; each metadata guide is the newest version the EDPass metadata page links.

- [[EDFacts Workbook SY 2025-26]] — EDPass roles, directory upload order, program-area file lists, FAQs, standard definitions, glossary
- [[BRSI Rules Review for dbt Tests]] — Business Rules Single Inventory: scope, cross-file rules, version history; per-spec rules in the table above

| Metadata collection | Version | Year | Metadata specs | Applies to |
|---|---|---|---|---|
| [[Academic Assessment Metadata User Guide\|Academic Assessment]] | v3.0 | SY 2024-25 | FS5005, FS5006, FS5007, FS5008 | none of the converted specs |
| [[Accountability Metadata User Guide\|Accountability]] | v2.0 | SY 2024-25 | FS5019, FS5020, FS5021, FS5022, FS5023, FS5025 | none of the converted specs |
| [[CCD Dropouts Graduates Completers Metadata User Guide\|CCD Dropouts Graduates Completers]] | v2.0 | SY 2024-25 | FS5015, FS5016 | none of the converted specs |
| [[CCD Grades Offered Metadata User Guide\|CCD Grades Offered]] | v3.0 | SY 2025-26 | FS5017 | [[FS039 Grades Offered\|FS039]], [[FS052 Membership\|FS052]] |
| [[CCD Staff FTE and Membership Metadata User Guide\|CCD Staff FTE and Membership]] | v3.0 | SY 2025-26 | FS5018, FS5024 | [[FS052 Membership\|FS052]], [[FS059 Staff FTE\|FS059]] |
| [[English Assessment Metadata User Guide\|English Assessment]] | v3.0 | SY 2024-25 | FS5009 | none of the converted specs |
| [[Gun-Free School Act Metadata User Guide\|Gun-Free School Act]] | v2.0 | SY 2024-25 | FS5010 | none of the converted specs |
| [[IDEA Discipline Exiting Staffing Metadata User Guide\|IDEA Discipline Exiting Staffing]] | v2.0 | SY 2024-25 | FS5012, FS5013, FS5014 | none of the converted specs |
| [[IDEA Part B Child Count Metadata User Guide\|IDEA Part B Child Count]] | v3.0 | SY 2025-26 | FS5002, FS5003, FS5004 | [[FS002 Children with Disabilities (IDEA) School Age\|FS002]], [[FS089 Children with Disabilities (IDEA) Early Childhood\|FS089]] |
| [[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|IDEA Part B MOE CEIS CCEIS]] | v2.0 | SY 2024-25 | FS231, FS232, FS233, FS234, FS235, FS236, FS237, FS238, FS5029 | none of the converted specs |
| [[IDEA Part C Child Count Metadata User Guide\|IDEA Part C Child Count]] | v3.0 | SY 2025-26 | FS5027 | [[FS902 Infants and Toddlers with Disabilities (IDEA Part C) Early Intervention\|FS902]], [[FS903 Children with Disabilities (IDEA Part C) Continuing Early Intervention\|FS903]], [[FS904 At Risk Infants and Toddlers with Disabilities (IDEA Part C)\|FS904]], [[FS905 Infants and Toddlers with Disabilities (IDEA Part C) Cumulative Count\|FS905]] |
| [[IDEA Part C Dispute Resolution Metadata User Guide\|IDEA Part C Dispute Resolution]] | v2.0 | SY 2025-26 | FS906, FS907, FS908 | none of the converted specs |
| [[IDEA Part C Exiting Metadata User Guide\|IDEA Part C Exiting]] | v2.0 | SY 2024-25 | FS5026 | none of the converted specs |
