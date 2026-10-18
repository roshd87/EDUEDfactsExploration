---
tags: [analysis, edfacts, fs002, child-count, south-carolina, sedm, preliminary]
fs_id: FS002
state: SC
repos: [edanalytics/edu_ext_sc, edanalytics/stadium_south_carolina]
edu_ext_sc_commit: eda7cb9
stadium_south_carolina_commit: adf53db
reviewed: 2026-10-17
---

# South Carolina SEDM Child Count vs FS002 (preliminary)

Related: [[FS002 Children with Disabilities (IDEA) School Age|FS002 spec]] · [[FS002 Business Rules]] · [[ChildCount|Generate ChildCount domain]] · [[IDEA Part B Child Count Metadata User Guide]] · [[BRSI Rules Review for dbt Tests]] · [[EDFacts-EdFi-Gap-Analysis|gap analysis]] · [[EDFacts-2026-27-Delta|SY 2026-27 delta]]

> [!abstract] At a glance
> - The SC report (`rpt_sedm__child_count`) is a student-level row list with an IDEA Indicator flag. It produces no counts, no age, no category sets and no SEA, LEA or School aggregation. [[FS002 Children with Disabilities (IDEA) School Age|FS002]] is an aggregated file, so the report is an input list at best.
> - Population is not filtered. Every IEP row is emitted and the indicator is only a flag. Missing: age computed and bounded 5K-21, the kindergarten rule, an enrollment-active-on-date filter, and unduplication across IEPs, schools and LEAs.
> - Likely defect: when `src:program:language_instruction:enabled` is true (stadium_south_carolina sets it), the EL dedup partitions on a null `k_student_program`, so by the SQL most non-EL rows share one partition and collapse to one row. Needs a row-count check.
> - Inner joins to the setting and child-count-date seeds drop IEPs silently. The indicator uses an exclusive end date although the commit message says inclusive, and a null `iep_end_date` gives a null indicator.
> - Environment seed maps to codes FS002 does not permit (4, 7, 9-12, 15), and SC stores the state code rather than computing a percentage of time.
> - Derivable from SC columns (after checking edu_wh): disability (raw), environment (after mapping), sex (raw), race plus Hispanic flag, EL boolean, DOB. Not derivable as-is: age on the date, 5K grade, category sets, subtotals, totals. No row counts were run.

> [!info] Sources
> Two reader reports, plus facts the author checked in the SQL (`models/wh/rpt_sedm__child_count.sql` lines 61-116). Repo-relative paths as named in the reports; not every path was re-opened.
> - `edanalytics/edu_ext_sc`: `models/wh/rpt_sedm__child_count.sql`, `models/wh/_wh.yml` (lines 46-72), `dbt_project.yml` (lines 127-146), `seeds/sedm/xwalk_special_education_setting.csv`, `seeds/sedm/xwalk_child_count_date.csv`, the SEDM base and stage models and `_sedm__base.yml` / `_sedm_stage.yml`.
> - `edanalytics/stadium_south_carolina`: `dbt/packages.yml`, `dbt/dbt_project.yml` (lines 85-87, 188-195), `earthbeam_dag__sedm.py`, `util/earthbeam_dag_factory.py` (line 618), `earthmover/edfi_extensions/sedm/earthmover.yaml`, `sedm__lightbeam.yml`, `airflow_config_prod.yml` (lines 1378-1410), `sedm_inactive_delete.py` (lines 36-61), `edfi_resources.yml`, `edfi_resources_to_snowflake.py` (lines 32-35, 69-75), `external_extract_sedm.py`, `lea_tenant_mapping.yml`.
> - Vault (FS002 side): `wiki/edfacts/FS002/` spec and BRSI notes, `wiki/edfacts/Metadata/` (SY 2025-26 edition), `wiki/generate/` ([[ChildCount]]), `wiki/analysis/EDFacts-EdFi-Gap-Analysis.md`, `wiki/analysis/EDFacts-2026-27-Delta.md`, `edu_ext_edfacts/seeds/` (only FS052 is seeded).

## 1. What the SC report is

- **Grain:** one row per student school association x IEP (student-level detail), materialized in schema `wh`. LEA and school columns attribute each row. No aggregation.
- **Lineage (one line):** PCG SFTP CSVs, then Airflow shards by LEA Code, then external earthmover bundle, then lightbeam POST to each district ODS, then `raw.edfi3`, then base, stage, fct, and finally `rpt_sedm__child_count`.
- **Where it lives:** `edanalytics/edu_ext_sc`, `models/wh/rpt_sedm__child_count.sql`. Not declared in `_wh.yml`.
- **Who built it, per git:** `0fd7e9e` (2026-10-06, "Include tenant_code in final select (#153)") and `d08038d` (2026-10-05, "Feature/sedm child count (#129)"), both Ryan Aguilar. Seeds: `xwalk_child_count_date.csv` gained the SY 2027 date in `65e1bbd` (2026-10-12, Jay Kaiser, "Add child count date for school year 2027 (#155)"); `xwalk_special_education_setting.csv` came in `d08038d`. The SEDM base, stage and fct models date from `2f1bf9f` (2026-05-29, "SEDM (#123)") and were disabled by default in `d0f7006` ("SEDM needs to be disabled by default (#125)").
- **Merge provenance:** no git evidence says the report was merged from stadium_south_carolina. The `d08038d` squash body lists development steps only. stadium_south_carolina consumes edu_ext_sc at git revision `main` (unpinned, `dbt/packages.yml`), so the report reaches SC through the package.
- **Unseen code:** the earthmover bundle that maps SC CSV columns to Ed-Fi JSON (`earthmover_edfi_bundles`, branch `feature/sedm_hotfix_2026`, `edfi_extensions/sedm`) is in neither repo. Any code translation there is unseen. The edu_wh inputs (`dim_student`, `dim_lea`, `dim_school`, `fct_student_school_association`, `fct_student_language_instruction_program_association`) are not cloned, so the derivation of Sex, race and the Hispanic flag is not visible.
- **Ed-Fi resources:** custom `sedm` namespace (StudentIEP, StudentIEPDisabilityCollection, IDEAEvent), descriptor namespace `uri://sedm.sc.gov`. The standard `studentSpecialEducationProgramAssociation` is not used; it appears only as a column on `base_sedm__student_ieps`.
- **Standards references:** no EDFacts or CEDS reference anywhere in the SEDM code.
- **Date handling:** the report has no as-of filter. The child count date is looked up by API year from a seed, and every other date (enrollment, IEP begin and end, exit) is carried through as a column or used only in the indicator.
- **Scope of the indicator:** the IDEA indicator is the only logic that looks at the child count date. Everything that makes a row countable in FS002 (age, grade, enrollment, dedup) sits outside the report.
- **Dependencies on the seeds:** two seeds carry business logic (setting mapping, child count date). Both are maintained in edu_ext_sc, so a change in SC policy reaches the report only through an edu_ext_sc commit that stadium picks up at `main`.
- **Provenance gap:** the reports do not show who in SC reviewed the mapping and date choices, or whether the 2026 and 2027 dates were confirmed with the state. Treat those as unconfirmed until Q5 is answered.

## 2. Comparison matrix

| Concept | FS002 spec | CEDS Generate (ChildCount) | SC dbt report | Verdict |
|---|---|---|---|---|
| Output grain (counts vs student list) | Counts per category set at SEA, LEA, School; 505-character fixed-width record | Counts from DISTINCT student-LEA-school rows with StudentCount 1, aggregated in the view | One row per SSA x IEP; no counts | Differs |
| Levels | SEA, LEA and School (spec defines school level too) | SEA, LEA and School; closed, inactive, future and not-reported-federally LEAs and schools filtered | LEA and school columns on each row only; no aggregate level | Absent in SC |
| Child count date source | State-designated date, Oct 1 to Dec 1; FS5002 SY 2025-26 metadata 10/1/2025 to 12/1/2025 | Month and day from App.ToggleQuestions CHDCTDTE, year = SY - 1; window not enforced | Seed `xwalk_child_count_date` by API year: 2026 = 2025-11-28, 2027 = 2026-10-27; not a dbt var | Partial |
| Child count date window | Between Oct 1 and Dec 1 | Not enforced | 2025-11-28 is inside the 2025-26 window; 2026-10-27 has no FS5002 2026-27 value in the vault | Partial |
| Population basis | IEP or services plan in place on the date | IDEAIndicator = 1, date-effective from Staging.ProgramParticipationSpecialEducation | Every IEP row emitted; `idea_indicator` is a flag only | Differs |
| Active enrollment on date | Enrolled on the child count date | Enrollment span entry to exit (or SY end / today) covers the date | None; exited and future SSA rows included | Absent in SC |
| Age computed and bounded 5K-21 | Discrete age as of the date (34 CFR 300.641(b)); 5 in K through 21 | `RDS.Get_Age` integer; staging keeps 6-21 or 5 with a non-PK grade; view keeps 5-21 | No age computed; DOB output only | Absent in SC |
| Kindergarten age-5 rule | Age 5 only if in kindergarten (AGE05K); ages 3-5 not in K excluded | Age 5 kept in any known non-PK grade, not only KG | No rule; grade is TrueGrade, else entry grade | Absent in SC |
| Age 22+ exclusion | Excluded | Excluded by the 5-21 bound | Not excluded; any age passes | Absent in SC |
| Unduplication across LEAs and schools | Once at SEA; once at one LEA; once at one school | No one-LEA enforcement; a student at two schools counts at each | No dedup across IEPs, schools or LEAs; SSA x IEP fan-out on k_student | Absent in SC |
| LEA and school attribution | LEA responsible for the IEP; school where 50% or more of the day is spent; exact 50/50 goes to the general-ed school | LEA and school from the enrollment row | LEA and school from the SSA row, not IEP ed_org_id | Partial |
| Primary disability selection | Primary disability in the IEP or services plan | IsPrimaryDisability = 1, date-effective | `order_of_disability` = 1 with no tie-break; secondary and third dropped | Partial |
| Disability code mapping | AUT, DB, DD, EMN, HI, ID, MD, OI, SLD, SLI, TBI, VI, OHI, MISSING | Mapped; Deafness and Deaf-blindness both to DB; no row = MISSING | Raw descriptor via `extract_descriptor`, no mapping | Differs |
| Developmental delay age rule | DD only ages 3-9 (state criteria for 6-9) | DD exclusion from CHDCTAGEDD answers (students removed, not recoded) | Not handled | Absent in SC |
| Educational environment codes | RC80, RC79TO40, RC39, SS, RF, HH (not at school level), CF, PPPS (not at school level), MISSING | Stored IDEAEducationalEnvironmentForSchoolAge value | Seed maps state codes; 4 to SC, 7 to H, 9-12 to REC*, 15 to SPL are not FS002 codes; 5 and 13 both SS; 6 and 14 both RF | Differs |
| Percentage-of-time computation | Hours inside / total hours x 100, thresholds for RC codes | None; stored code | None; state code mapped directly | Absent in SC |
| HH and PPPS at school level | Excluded at school level | Not described in the notes read | No school-level exclusion | Absent in SC |
| Sex mapping | F, M, MISSING | M or F, else MISSING | `dim_student.gender` raw | Unknown |
| Race and ethnicity 7-value collapse | AM7, AS7, BL7, HI7, PI7, MU7, WH7, MISSING | HI7 if any Hispanic flag, else MU7 if more than one race, else single code | `dim_student.race_ethnicity` (edu_wh, collapse unverified) plus separate Hispanic boolean | Unknown |
| English learner status | LEP, NLEP, MISSING | EnglishLearnerStatus = 1 gives LEP; everything else, including no row, gives NLEP | Boolean `is_english_language_learner_active`; constant FALSE when var off; null begin gives null | Partial |
| Category sets A-E | Table 2.2-2 (SEA, LEA); Table 2.3-2 (school) | Count view; set logic not detailed in the notes read | None | Absent in SC |
| Subtotals 1-7, EUT, Total Indicator | Subtotals 1-7, EUT, Total Indicator field 22 | Not described in the notes read | None | Absent in SC |
| Zero and -1 / MISSING conventions | Zero for valid combinations at SEA; -1 for missing count; MISSING category | Not described | None | Absent in SC |
| Operational-status and reported-federally filters | Closed, inactive and future LEAs or schools excluded; reported-federally flag | Filters on IsReportedFederally = 0 and status Closed, Future, Inactive, MISSING; flag absent from Ed-Fi | None | Absent in SC |
| IEP status and exit reason | In place on the date | Date-effective | `iep_status` and `reason_exited` ignored; only `not is_deleted` applied in stage | Absent in SC |
| Services plan and parentally placed | Services plan counts; PPPS category | Not described | Not modeled | Absent in SC |
| BRSI rules coverage | 13 active rules (SY 2025-26, v1.04) | Not applicable | None | Absent in SC |
| Tests in dbt | Not applicable | Not applicable | No tests, no column docs; post-hooks only (not null, PK, FK) | Absent in SC |

## 3. Inconsistencies and likely defects in the SC report

1. **Exclusive end date vs stated intent.** The IDEA indicator uses `child_count_date < iep_end_date` (lines 61-78), but commit `d08038d` says "Change date window to be inclusive". A null `iep_end_date` yields a null indicator, not true. Verified in SQL.
2. **Inner joins drop rows silently.** `join xwalk_special_education_setting` (on `special_education_setting = state_descriptor`) and `join xwalk_child_count_date` (on `school_year`) are inner joins. IEPs with a null or unmapped setting, and IEP rows whose API year has no seed row, disappear rather than getting a false indicator. Verified in SQL.
3. **EL dedup collapse (likely).** When `src:program:language_instruction:enabled` is true (set in stadium_south_carolina `dbt_project.yml` lines 188-195), `stu_language_instruction_deduped` deduplicates with `partition_by='k_student_program'`. That key is null for every enrollment row without an EL program, so all non-EL rows fall into one partition and only one survives. By the SQL, most non-EL students would vanish. Row count not run.
4. **EL join fan-out.** The left join to `fct_student_language_instruction_program_association` on `k_student, k_school, school_year` can multiply rows before the dedup in item 3 runs.
5. **Multi-join fan-out.** SSA x IEP joins on `k_student` only; TrueGrade and legal name are also joined on `k_student` only, so any student with more than one matching row multiplies.
6. **No age logic.** No age computation, no 5-21 bound, no kindergarten rule, no 22+ exclusion.
7. **No active-enrollment filter.** Exited and future SSA rows are included; "Exit Date" is output but unused.
8. **No dedup across IEPs, schools or LEAs.** A student with two IEPs, or at two schools, produces two rows.
9. **Secondary and third disabilities dropped.** Only `order_of_disability` = 1 is kept. `is_multiply_disabled` is carried in the fct and never used, so MD is produced only when the source primary says so.
10. **Primary disability has no tie-break** in the dedup ordering (`order_of_disability` asc).
11. **Raw disability descriptor.** `extract_descriptor('value:disabilityDescriptor::string')` passes through with no FS002 mapping. Reader also flags `extract_descriptor` used on a field that may be an integer; type not confirmed.
12. **Environment seed codes not in FS002.** 4 to SC, 7 to H, 9-12 to REC* codes, 15 to SPL are not permitted values. 8a, 8b, 8c to HH and 17 to PPPS are not permitted at school level. 5 and 13 both map to SS, 6 and 14 both map to RF; intent unconfirmed.
13. **Seed type risk.** `xwalk_special_education_setting` has no `column_types` override, so `state_descriptor` type is inferred. Values such as "8a" are strings while others are numeric; a type inference mismatch would break the join silently (item 2).
14. **No percentage-of-time computation.** The state code is stored as the environment.
15. **Copy-paste model.** `fct_student_idea_event` is built from `stg_sedm__student_ieps`, not `stg_sedm__idea_events`. The fct is unused by the report, and `stg_sedm__idea_events` is also unused.
16. **Key reuse and missing PK.** Disabilities are keyed on the same surrogate as IEPs (`k_student_iep`); the disability model has no PK.
17. **Var naming and gating.** Base and stage are gated by `ext_sc:domain:sedm:enabled`, which edu_ext_sc's own `dbt_project.yml` never sets (stadium sets it True at line 194). `edu:sedm:enabled` is used in `_wh.yml`. `src:domain:sedm:enabled` is True in edu_ext_sc. `src:program:language_instruction:enabled` has no default (line 80), so an unset run is unpredictable (not run).
18. **Silent gap for future API years.** Any API year without a `xwalk_child_count_date` row produces zero rows with no error. The SY 2027 row was added on 2026-10-12.
19. **Child count date is a seed, not a var.** Changing the date means a commit to edu_ext_sc.
20. **Fiscal year.** `Fiscal Year` is hard-coded as `concat('FY', school_year-1, '-', right(school_year,2))`. Line 139 has an open TODO: `--is there somewhere to pull fiscal year from?`.
21. **Hard-coded values.** `right(school_id, 4)` for School Code; literals `'TrueGrade'` and `'Legal Name'`; namespace `uri://sedm.sc.gov`.
22. **No tests, no column docs.** Post-hooks only: not null on `k_student_iep`, `k_student`, `k_student_xyear`; PK on `k_student_iep`; FK to `dim_student`; disability FK to IEP association. `rpt_sedm__child_count` is not in `_wh.yml`.
23. **Unpinned dependency.** edu_ext_sc is pulled at `main`, so a push to edu_ext_sc changes stadium output with no SC-side review trail.
24. **Ingest-side overrides.** Tenant override `barnwell45` to `barnwell` (`earthbeam_dag__sedm.py` lines 18-20); 2026 SFTP folder override `/Review/SEDM/sedm_2026` (`external_extract_sedm.py` lines 135, 273-275); hotfix `adf53db` pins the bundle branch and hard-codes the 2026 folder. These are outside the report but change what it reads.
25. **Unverified edu_wh derivations.** Sex, race (7-code collapse) and Hispanic flag come from edu_wh, which is not cloned. Not checkable from this repo.

### 3b. Issues on the FS002 and Generate side

- Generate counts age 5 in any known non-PK grade, not only kindergarten, which FS002 requires.
- Generate does not enforce one-LEA unduplication (FS002 Table 2.2-1).
- Generate maps absent EL status to NLEP. FS002 has a MISSING option; treating absent as NLEP is an assumption to confirm.
- `ChildCount.md` says FS002 is ages 6-21, but the SQL allows 5.
- The vault at-a-glance lists Levels as SEA and LEA; the spec also defines school level.
- Frontmatter says `status_2026_27` is Inactive (frozen 2026-10-07) and Active for SY 2025-26. The spec is v23.0 for SY 2026-27; the delta note says changes are punctuation-level only.
- The Metadata guide in the vault is the SY 2025-26 edition, so the 2026-27 FS5002 and FS5003 values are not in the vault.
- BRSI SY 2025-26 v1.04 marks IDEA-0011 "Changed: Updated threshold" and IDEA-0231 "New". No SY 2026-27 BRSI was available at the freeze.
- Only FS052 is seeded in `edu_ext_edfacts/seeds/`; there are no FS002 seed rows yet.
- Gap analysis: the reported-federally flag is absent from Ed-Fi, and the DD age-band policy is absent (it lives in Generate config and FS5002 metadata).

## 4. Initial results

- **No row counts were run.** Nothing below is measured.
- **The SC report is an input list, not an FS002 file.** It has no counts and no SEA, LEA or School rows, so it cannot be submitted as FS002.
- **Derivable from the SC columns (once edu_wh is checked):**
  - Disability: raw descriptor; needs mapping to the 13 codes plus MISSING.
  - Environment: after mapping; four seed codes have no FS002 equivalent.
  - Sex: raw value; needs mapping to F, M, MISSING.
  - Race plus Hispanic: an edu_wh value, collapse unverified.
  - EL: boolean only; can express LEP and NLEP, not MISSING.
  - DOB: enough to compute age on any date.
- **Not derivable as-is:**
  - Age on the child count date: must be computed from DOB and the date.
  - Grade for AGE05K: the report gives TrueGrade if present, else entry grade; whether TrueGrade is as of the child count date is unknown.
  - Category sets, subtotals, EUT, Total Indicator: none exist.
  - Counts, zeros, -1 and MISSING conventions: none exist.
  - SEA, LEA and School levels, and the reported-federally and operational-status filters: none exist.
- **Dates:** 2025-11-28 (API 2026) falls inside the SY 2025-26 FS5002 window of 10/1/2025 to 12/1/2025. 2026-10-27 (API 2027) has no FS5002 2026-27 value in the vault, so its status is unknown.
- **Ed-Fi path:** the gap analysis maps environment directly to `studentSpecialEducationProgramAssociation`, which SC does not use. SC's custom `sedm` StudentIEP path is the main assumption to test.
- **Dimension check (static, from column names only):**

| FS002 dimension | SC source column | Status from the reports | What is still needed |
|---|---|---|---|
| Disability category | `Primary Disability` (raw descriptor) | Present, unmapped | Descriptor value list (Q7); mapping to 13 codes plus MISSING |
| Educational environment | `Placement` (federal descriptor) | Present, mapped by seed | SC crosswalk (Q6); removal of non-FS002 codes |
| Sex | `Sex` (dim_student.gender) | Present, raw | Value list (Q8); mapping to F, M, MISSING |
| Racial ethnic | `Race Description` plus `Hispanic or Latino Ethnicity` | Present, edu_wh value | Whether edu_wh collapses to seven codes (Q8); precedence rule for HI7 |
| English learner status | `ELL Status Description` | Boolean only | Cannot express MISSING; NLEP for absent is an assumption |
| Age | `Date of Birth` | Present as DOB | Computation on the child count date; 5-21 bound |
| Grade for AGE05K | `Grade Description` | Present, coalesced | Whether TrueGrade is as of the date; kindergarten test |
| Enrollment active on date | `Current Year Enrollment Date`, `Exit Date` | Present, unfiltered | Date filter; exit handling |
| Unduplicated count | none | Absent | One-LEA and one-school rule; dedup key |
| Category sets, subtotals, EUT, Total Indicator | none | Absent | Entire count layer |

- **Preliminary read:** as written, the SC report would need a count model, age and grade logic, dedup, and code mapping layers before it could feed an FS002 file. The EL dedup and inner joins are the first defects to confirm, since they could change row counts before any FS002 logic exists.

## 5. Questions to follow up

1. Is the report meant to feed the state's SEDM vendor (PCG), EDFacts, or both? Who: SC data lead and product owner. Where: stadium_south_carolina requirements or the SEDM vendor spec.
2. What does the external earthmover bundle (`earthmover_edfi_bundles`, branch `feature/sedm_hotfix_2026`, `edfi_extensions/sedm`) do to Placement and PrimaryDisability codes? Who: owner of the bundle. Where: its SEDM mapping files.
3. Is `iep_end_date` ever null in ODS data? Who: data engineering. Where: `raw.edfi3.student_ieps`, count nulls by `api_year`.
4. Expected row counts with and without `src:program:language_instruction:enabled`. Who: someone with SC warehouse access. Where: a dev run of the report, comparing row count to distinct `k_student`.
5. Do the child count dates (2025-11-28 for API 2026, 2026-10-27 for API 2027) match the state's FS5002 metadata answers? Who: SC state reporting contact. Where: state FS5002 metadata submission for SY 2025-26 and 2026-27.
6. Does SC's Placement code list (1-17, 8a-c) have an official SC crosswalk to federal environment codes? Who: SC SPED data contact. Where: SC Placement codebook.
7. What disability descriptor values does SEDM actually emit (namespace `uri://sedm.sc.gov`; commit says "except for disabilityDescriptors")? Who: SC data team. Where: ODS `disabilityDescriptors` endpoint or raw data.
8. Does `dim_student.race_ethnicity` in edu_wh already collapse to the seven codes, and what gender values appear? Who: edu_wh package owner. Where: edu_wh `dim_student`.
9. Do school-level exclusions (HH, PPPS, ages 22+) matter for SC, and will SC submit school-level counts? Who: SC EDFacts coordinator.
10. Should the report use `studentSpecialEducationProgramAssociation` (the standard Ed-Fi resource that Generate and the gap analysis assume) instead of the sedm StudentIEP extension? Who: SC data architect. Where: whether the standard resource is populated in the SC ODS.
11. Is the exclusive end date (item 3.1) intended or a regression from `d08038d`? Who: Ryan Aguilar, the author. Where: `d08038d` diff and PR #129.
12. Where should the fiscal year come from (the TODO on line 139)? Who: report author.
13. Why is the child count date a seed rather than a dbt var, and who owns updating it each year? Who: Jay Kaiser (`65e1bbd`) and the report author.
14. Does SC have a services-plan population (parentally placed, PPPS), and how is it represented in Ed-Fi? Who: SC SPED.
15. Do students appear under both API 2026 and API 2027 in the same run, and does that double count? Who: data engineering. Where: count by `student_unique_id` across `school_year`.
16. Is the SC report expected to be SEA-level only, or does SC also submit LEA and School counts? Who: SC EDFacts coordinator.

## 6. Next steps

- Run row counts on `rpt_sedm__child_count` with the EL var off and on: total rows, distinct `k_student`, rows with null `iep_end_date`, rows dropped by the setting and date-seed joins.
- Draft an FS002 count model in `edu_ext_edfacts`, reusing SC's two seeds as `xwalk_edfacts_*` inputs after the Placement and date questions are answered.
- Add FS002 to the seed builder SPECS allowlist so its category sets and permitted values are seeded from the spec.
- Propose tests to the edu_ext_sc owners (unique `k_student_iep` on the report, accepted values for environment and disability codes). Do not edit edu_ext_sc from this repo.
- Pin edu_ext_sc to a tag in stadium_south_carolina `packages.yml` instead of `main`.
- Declare `rpt_sedm__child_count` in `_wh.yml`.
- Fix the EL dedup key and the inner joins only after the row counts confirm the impact.
- Confirm the disability descriptor value set (Q7) before drafting the disability mapping seed, so the mapping is built from observed values rather than the FS002 list alone.
- Check the environment seed against FS5003 metadata, which declares permitted environments by age band (5K-11, 12-17, 18-21). The age-band answer decides which SC codes can reach FS002 at all.
- Decide how absent EL status is reported (NLEP as Generate does, or MISSING as the spec allows) and record the decision here before building the count model.
- Keep this note as the log: add each answered question and each run's row counts under the matching section, and leave the section 3 claims unchanged until a run or a source confirms them.

### 6a. Verification SQL (Snowflake, not yet run)

`<db>` is the SC warehouse database, `<seeds>` the schema the edu_ext_sc seeds land in. SC runs tenant-sharded, so run per database or union.

Symptom check. If the EL dedup collapse is real, `students_no_el_program` is 1.

```sql
select tenant_code,
       count(*) as rows_total,
       count(distinct "Student ID") as students_total,
       count_if("EL Program Participation Start Date" is null) as rows_no_el_program,
       count(distinct iff("EL Program Participation Start Date" is null, "Student ID", null)) as students_no_el_program,
       count_if("ELL Status Description") as rows_el_active
from <db>.wh.rpt_sedm__child_count
group by tenant_code order by tenant_code;
```

Expected population without the EL branch (the report's row base after the two seed joins).

```sql
with iep as (
    select distinct i.k_student
    from <db>.wh.fct_student_iep_association as i
    join <db>.<seeds>.xwalk_special_education_setting as x on i.special_education_setting = x.state_descriptor
    join <db>.<seeds>.xwalk_child_count_date as d on i.school_year = d.school_year
)
select ssa.tenant_code, count(*) as expected_rows_ssa_x_iep, count(distinct ssa.k_student) as expected_students
from <db>.wh.fct_student_school_association as ssa
join iep on ssa.k_student = iep.k_student
group by ssa.tenant_code order by ssa.tenant_code;
```

Direct reproduction of what `dbt_utils.deduplicate` compiles to. Nulls form one partition, so the `no_program = true` bucket should return one row.

```sql
with joined as (
    select ssa.k_student, l.k_student_program, l.program_enroll_begin_date, l.program_enroll_end_date
    from <db>.wh.fct_student_school_association as ssa
    left join <db>.wh.fct_student_language_instruction_program_association as l
        on ssa.k_student = l.k_student and ssa.k_school = l.k_school and ssa.school_year = l.school_year
)
select k_student_program is null as no_program, count(*) as rows_kept, count(distinct k_student) as students_kept
from joined
qualify row_number() over (partition by k_student_program
                           order by program_enroll_begin_date desc, program_enroll_end_date desc) = 1
group by 1;
```

Side checks for Q3 and the inner-join drop.

```sql
select school_year, count(*) as ieps, count_if(iep_end_date is null) as null_end_dates
from <db>.wh.fct_student_iep_association group by school_year order by school_year;

select count(*) as ieps,
       count_if(x.state_descriptor is null) as unmapped_setting,
       count_if(d.school_year is null) as no_child_count_date
from <db>.wh.fct_student_iep_association as i
left join <db>.<seeds>.xwalk_special_education_setting as x on i.special_education_setting = x.state_descriptor
left join <db>.<seeds>.xwalk_child_count_date as d on i.school_year = d.school_year;
```

## 7. Appendix: SC seeds verbatim

Copied from `edu_ext_sc` at `eda7cb9`.

**`seeds/sedm/xwalk_special_education_setting.csv`** (added in `d08038d`):

```csv
state_descriptor,federal_descriptor
1,RC80
2,RC79TO40
3,RC39
4,SC
5,SS
6,RF
7,H
8,HH
8a,HH
8b,HH
8c,HH
9,REC10YSVCS
10,REC10YOTHLOC
11,REC09YSVCS
12,REC09YOTHLOC
13,SS
14,RF
15,SPL
16,CF
17,PPPS
```

**`seeds/sedm/xwalk_child_count_date.csv`** (`d08038d`, SY 2027 row in `65e1bbd`):

```csv
school_year,child_count_date
2026,2025-11-28
2027,2026-10-27
```

Not in FS002 permitted values: 4, 7, 9, 10, 11, 12, 15 (and 8a-8c and 17 at school level).

## 8. Appendix: SC report output columns

| # | Output column | Source expression |
|---|---|---|
| 1 | tenant_code | SSA |
| 2 | Fiscal Year | `concat('FY', school_year-1, '-', right(school_year,2))` |
| 3 | LEA Name | dim_lea.lea_name |
| 4 | LEA Code | dim_lea.lea_id |
| 5 | School Code | `right(dim_school.school_id, 4)` |
| 6 | School Name | dim_school |
| 7 | Student ID | student_unique_id |
| 8 | First Name | coalesce(legal name, dim_student) |
| 9 | Middle Name | coalesce(legal name, dim_student) |
| 10 | Last Name | coalesce(legal name, dim_student) |
| 11 | Date of Birth | birth_date |
| 12 | Sex | dim_student.gender (raw) |
| 13 | Race Description | dim_student.race_ethnicity (edu_wh value) |
| 14 | Hispanic or Latino Ethnicity | has_hispanic_latino_ethnicity (boolean) |
| 15 | Grade Description | coalesce(TrueGrade indicator_value, ssa.entry_grade_level) |
| 16 | Current Year Enrollment Date | ssa.entry_date |
| 17 | Exit Date | ssa.exit_withdraw_date |
| 18 | Placement | xwalk federal_descriptor |
| 19 | ELL Status Description | is_english_language_learner_active (boolean) |
| 20 | Primary Disability | raw disability_descriptor |
| 21 | EL Program Participation Start Date | fct_language begin |
| 22 | EL Program Participation Exit Date | fct_language end |
| 23 | IEP Program Participation Start Date | iep_begin_date |
| 24 | IEP Program Participation Exit Date | iep_end_date |
| 25 | IDEA Indicator | idea_indicator (boolean) |
