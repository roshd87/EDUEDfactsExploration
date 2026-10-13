---
tags: [analysis, edfacts, edfi, gap-analysis, preliminary]
data_standard: "Ed-Fi 5.2.0"
---

# EDFacts ↔ Ed-Fi Gap Analysis (Preliminary)

> [!info] Seam: standard-agnostic
> This note compares the **element requirements** that CEDS Generate reads out of its staging
> contract against **Ed-Fi Data Standard 5.2.0 core**. It says nothing about how Generate is built;
> it says what an Ed-Fi-sourced re-implementation would and would not be able to supply.

**Scope.** Ed-Fi Data Standard **5.2.0**, as published in the ODS/API 7.3 resources swagger
(`sources/edfi/swagger-canonical.json`, 989 schemas, 471 `edFi_*` core schemas — see
`sources/edfi/VERSION.txt`). Derived from the 24 domain notes in the Generate wiki (`wiki/generate/domains/`;
domain names in this note refer to them), which were written against `generate.database@develop` (`37108eb`). **Preliminary and element-level.** Each verdict
answers "does core Ed-Fi carry this concept", not "does the descriptor value set line up".

**Method.** Each of the 24 domain notes carries an *Ed-Fi coverage* table. Those 232 rows were
consolidated: 17 elements recur across domains and are given one canonical row here; the remaining
103 are domain-specific. Where workers assigned different verdicts to the same canonical element,
the conflict was re-adjudicated against the swagger during review — see `wiki/generate/repo/Source-Code-Oddities.md`.

## Headline

| Verdict | Unique elements | Share |
|---|---:|---:|
| **Direct** — one core Ed-Fi property carries the same meaning | 70 | 58% |
| **Derivable** — computable from core Ed-Fi elements | 20 | 17% |
| **Absent** — not in core 5.2.0 | 30 | 25% |
| **Total unique elements** | **120** | |

Before dedupe the same tables hold 232 rows (166 Direct / 34 Derivable / 32 Absent); the shift is
because the widely-shared elements are almost all Direct, so collapsing them raises the Absent share.

**The shape of the gap is not uniform.** Student-level demographic and program-participation
reporting is nearly fully covered. The gaps cluster in three places: **staff qualifications**
(FS070/FS099/FS112), **organization characteristics and governance** (FS129/FS130/FS190/FS196–FS198),
and **federal funding amounts** (FS035/FS193). Those three clusters account for 19 of the 30 Absent
elements.

## Shared elements (canonical rows)

These recur across many domains. Each domain note repeats them for local completeness; this is the
single authoritative row. Domain counts are of the 24 domain notes.

| Element | Domains | Verdict | Ed-Fi binding |
|---|---:|---|---|
| Student identifier | 21 | Direct | `edFi_student.studentUniqueId` |
| Organization identifier (SEA/LEA/school) | 15 | Direct | `edFi_stateEducationAgency.stateEducationAgencyId`, `edFi_localEducationAgency.localEducationAgencyId`, `edFi_school.schoolId` |
| IDEA indicator | 13 | Direct | `edFi_studentSpecialEducationProgramEligibilityAssociation.ideaIndicator` |
| Race / ethnicity | 11 | Direct | `edFi_studentEducationOrganizationAssociationRace.raceDescriptor` + `.hispanicLatinoEthnicity` |
| English learner status | 11 | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` |
| Grade level | 10 | Direct | `edFi_studentSchoolAssociation.entryGradeLevelDescriptor` |
| Primary IDEA disability type | 7 | **Derivable** | `edFi_studentSpecialEducationProgramAssociationDisability.disabilityDescriptor` where `orderOfDisability = 1` |
| Sex | 6 | Direct | `edFi_studentEducationOrganizationAssociation.sexDescriptor` |
| Age at a reference date | 5 | **Derivable** | computed from `edFi_student.birthDate`; Ed-Fi stores no age |
| Count measure | 4 | **Derivable** | count of matched rows; not a stored element in any standard |
| Migrant status | 4 | Direct | presence of `edFi_studentMigrantEducationProgramAssociation` |
| Foster care status | 3 | **Absent** | no foster-care association or characteristic in core; see ranked list |
| Section 504 status | 3 | Direct | `edFi_studentSection504ProgramAssociation` (`section504Eligibility`) |
| Economic disadvantage | 2 | **Derivable** | active `edFi_studentSchoolFoodServiceProgramAssociation`; no single boolean |
| IDEA educational environment | 2 | Direct | `edFi_studentSpecialEducationProgramAssociation.specialEducationSettingDescriptor` |
| Homelessness status | 2 | Direct | presence of `edFi_studentHomelessProgramAssociation` |
| Native language | 2 | Direct | `edFi_studentEducationOrganizationAssociation.languages` |

Three of these were re-adjudicated in review: **primary disability type** is Derivable, not Direct —
`edFi_studentSpecialEducationProgramEligibilityAssociation` carries `ideaIndicator` but **no**
disability collection, so "primary" requires filtering `orderOfDisability = 1` on a different
schema. **Age** is Derivable everywhere (`birthDate` is Direct; age is not). **Foster care** is
Absent, not Derivable — a generic `studentCharacteristicDescriptor` with no shipped foster-care
value is an extension point, not coverage.

## Absent elements, ranked

Ranked by blast radius: elements blocking more file specs and more domains first.

| # | Element / cluster | Domain | File specs blocked | Why absent |
|---:|---|---|---|---|
| 1 | **Staff qualification & certification** — EdFacts certification status, special-ed teacher qualification status, paraprofessional qualification status, special-ed staff category, special-ed age group taught | Staff | FS070, FS099, FS112 | `edFi_credential` names a credential *type*; core has no certified/qualified *determination*, no special-ed staff sub-category, and no age-band-served property. Five of the six reported elements are missing, so these specs are effectively unbuildable from core |
| 2 | **Charter school governance** — primary & secondary authorizer, management organization, contract ID | Directory | FS190, FS196, FS197, FS198 | `edFi_school.charterStatusDescriptor` says *whether* a school is a charter; core models no authorizing organization, no management-organization reference, and no contract identifier |
| 3 | **Federal program funding** — program code, funding allocation, Title I parental-involvement reservation, Section 1003 school-improvement funds | Directory, CTE | FS035, FS193, `c132` | `edFi_localEducationAgencyFederalFunds` exposes a fixed set of named allocation fields, not a generic (program code, amount) pair |
| 4 | **School characteristic statuses** — NSLP status, shared-time indicator, virtual school status, dangerous-school status, state poverty designation | Directory | FS129, FS130 | No core property for any of the five; `edFi_school` covers type, magnet emphasis and operational status only |
| 5 | **IDEA removal semantics** — interim removal, interim removal reason, educational services after removal | Discipline | FS005, FS007, FS144 | Core discipline covers incidents, actions and weapons, but has no interim-alternative-educational-setting concept and nothing representing continued services during or after a removal |
| 6 | **Foster care status** | TitleI, Graduationrate, Assessments, Other | FS037, FS134, FS150, FS151 + assessment specs | Only `edFi_studentHomelessProgramAssociation.awaitingFosterCare`, scoped to McKinney-Vento awaiting-placement |
| 7 | **Perkins CTE subpopulations** — single-parent / single-pregnant-woman, displaced homemaker, graduation-rate inclusion type, LEP-Perkins status | CTE | FS154, FS155, FS156 | No core property for any; Perkins subpopulation vocabulary is not modelled |
| 8 | **Adjusted cohort & cohort membership** | Graduationrate, GraduatesCompleters | FS150, FS151 | `edFi_studentEducationOrganizationAssociationCohortYear` names a cohort year but no maintained four-year adjusted cohort. Note Generate does not implement this either — see Source-Code-Oddities |
| 9 | **Immigrant program participation** | Immigrant, Other | FS165 | No `immigrant`-named property in any of the 471 core `edFi_*` schemas |
| 10 | **N-or-D facility / institution type** | NeglectedOrDelinquent | FS119, FS127 | No facility or institution concept in core 5.2.0 |
| 11 | **Progress-toward-ELP indicator** (organization level) | Directory | FS205, FS206 | Core has no organization-level English-language-proficiency-progress property |
| 12 | **McKinney-Vento subgrant recipient** | Directory | FS170 | No subgrant-recipient property on `edFi_localEducationAgency` |
| 13 | **MEP enrollment type** | MigrantEducationProgram | FS054, FS121, FS122, FS145 | Only the generic `programParticipationStatuses` collection; no MEP-specific enrolment-type descriptor |
| 14 | **Teacher out-of-field status** | Staff | FS070, FS099 | No out-of-field property in core |
| 15 | **Attendance rate (pre-computed)** | Chronic | FS195 | No stored rate element; only the underlying attendance events (see Derivable) |
| 16 | **Generate-internal flags** — reported-federally flag, DD age-band policy answer, disproportionate-representation ratio | ChildCount, Directory, SPPAPR | FS002, FS089 | Not data elements at all: SEA policy answers and Generate's own reporting-scope switches. No standard should carry them |

Items 1–4 are the load-bearing ones. Items 15–16 are cheap: one is a computation, the other is
configuration that belongs outside the data standard.

## Derivable elements and their rules

Twenty distinct elements need computation rather than a lookup. These are the implementation work
an Ed-Fi binding must do.

| Element | Domains | Derivation rule |
|---|---|---|
| Primary IDEA disability type | 7 | `edFi_studentSpecialEducationProgramAssociationDisability.disabilityDescriptor` where `orderOfDisability = 1` |
| Age at a reference date | 5 | `edFi_student.birthDate` differenced against the report's reference date (child-count date, exit date, MEP performance period) |
| Count measure | 4 | count of matched rows after all filters; never stored |
| Economic disadvantage | 2 | active `edFi_studentSchoolFoodServiceProgramAssociation` participation |
| Enrollment span / membership as-of count | 2 | student is in membership if the configured count date falls between `edFi_studentSchoolAssociation.entryDate` and `.exitWithdrawDate` |
| Chronic absenteeism flag | 1 | aggregate `edFi_studentSchoolAttendanceEvent` per student per year; chronically absent when the absence share crosses the state threshold (Generate documents 10%) |
| "Is this a dropout" | 1 | a state convention over `edFi_studentSchoolAssociation.exitWithdrawTypeDescriptor` values — structurally identical to CEDS's SSRD translation step |
| Postsecondary enrollment | 1 | `edFi_postSecondaryEvent` (`postSecondaryEventCategoryDescriptor` + `eventDate` + `postSecondaryInstitutionReference`), filtered to enrolment-category events |
| Cohort entry / graduation year | 1 | `edFi_studentEducationOrganizationAssociationCohortYear` (`cohortYearTypeDescriptor` + `schoolYearTypeReference`) assembled per student |
| Immigrant statutory facts | 1 | `edFi_student.birthDate` (age 3–21) + `.birthCountryDescriptor` (not born in a US state) + earliest `edFi_studentSchoolAssociation.entryDate` (under three full academic years) |
| NCES identifier (LEA / school) | 1 | `identificationCodes[]` on `edFi_localEducationAgency` / `edFi_school`, filtered to the NCES system descriptor |
| Comprehensive / targeted support identification | 1 | `edFi_school.indicators[]` (`indicatorDescriptor` / `indicatorValue`) — a generic extensibility slot; CSI/TSI vocabulary is not built in |
| CTE concentrator / participant status | 1 | `edFi_studentCTEProgramAssociation.programParticipationStatuses[].participationStatusDescriptor`; concentrator thresholds are state-defined |
| Discipline method for children with disabilities | 1 | `disciplineDescriptor` plus an active `edFi_studentSpecialEducationProgramAssociation` on the same date |
| Firearm discipline method | 1 | as above, scoped to incidents carrying an `edFi_disciplineIncidentWeapon` association |
| Assessment type administered | 1 | `edFi_assessment.assessmentCategoryDescriptor` plus accommodation and registration context |
| Homeless serviced indicator | 1 | `edFi_studentHomelessProgramAssociation.homelessProgramServices[]` non-empty, or the linked program's funding source being a McKinney-Vento subgrant |
| Teacher inexperienced status | 1 | `edFi_staff.yearsOfPriorTeachingExperience` against a state-defined threshold |
| Title III teacher status | 1 | `edFi_staffProgramAssociation.programReference` → `edFi_program.programTypeDescriptor` (Title III / language instruction) combined with a Teacher `staffClassificationDescriptor` |
| Section 504 status *(where treated as derived)* | 1 | active `edFi_studentSection504ProgramAssociation` spanning the reference date — canonically Direct, listed here because date-scoping is still required |

Two patterns recur and are worth pulling out. **Date-scoping**: Ed-Fi models most statuses as dated
associations, while EDFacts wants an as-of-date or any-time-in-year answer — nearly every "Direct"
element still needs a span filter. **State convention**: dropout, CTE concentrator, and inexperienced
teacher all bottom out in a threshold or code list the state defines, not the standard. Generate has
the same problem and solves it with `Staging.SourceSystemReferenceData`; an Ed-Fi binding needs an
equivalent translation layer.

## Caveats

1. **Element-level, not value-level.** A Direct verdict means the concept exists as a property. It
   does **not** mean the descriptor's value set covers the EDFacts permitted values. Descriptor-level
   reconciliation — especially IDEA disability categories, exit reasons, educational environments
   and grade levels — is unstarted and is where the next real work is.
2. **Core Ed-Fi 5.2.0 only.** `tpdm_*` (TPDM 1.1.0) schemas are in the same swagger but are an
   extension; they never count as Direct. Where a worker cited an extension it appears as
   corroboration inside an Absent verdict, not as coverage. Domain-specific extensions could close
   many Absent items — that is a programme decision, not a data-standard fact.
3. **Some elements never touch the documented seam.** For CTE, Other, SPPAPR,
   StudentCounts and the `organizationstatus` fact type behind FS199–FS202, Generate sources
   category data from the CEDS IDS (`dbo.*`) rather than from `Staging.*` — 58 of 67
   `RDS.Migrate_Dim*` procedures read `dbo.*` exclusively. Those elements were inventoried from the
   IDS tables, so their staging column references are nominal. See Source-Code-Oddities.
4. **Some of Generate's own logic is unimplemented.** Adjusted-cohort computation, the
   postsecondary-enrolment filter, the chronic-absence threshold, Title III teacher status and
   several funding amounts are declared but never populated. Where the target behaviour was taken
   from the file spec rather than from Generate, the note says so. A re-implementation that matches
   Generate byte-for-byte would inherit these gaps.
5. **Verdict counts are of concepts, not of file-spec fields.** One Absent element can block an
   entire file spec (see rank 1) while five Direct elements may be trivial identifiers. Read the
   ranked table, not the percentages.
6. **`App.CategorySets` seeds are partial.** The cached metadata does not contain category sets for
   every report code and year, so a few domain notes infer category roles from lineage views. Those
   are flagged in the notes themselves.

## Sources

- Per-domain detail: the 24 notes linked from `wiki/generate/Home.md`
- Worker inventories: `tasks/inventories/worker-{1..4}.md`
- Verified anomalies: `wiki/generate/repo/Source-Code-Oddities.md`
- Ed-Fi: `sources/edfi/swagger-canonical.json`, `sources/edfi/VERSION.txt` (DS 5.2.0, ODS/API 7.3)
- Generate: `generate.database@develop` (`37108eb`), cached at `sources/generate/`
