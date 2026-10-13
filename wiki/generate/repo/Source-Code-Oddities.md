---
tags: [repo, oddities, verified]
---

# Source-Code Oddities

> [!info] Seam: both
> Findings that change how the pipeline should be read. Each was flagged by a worker against the
> brief, then re-verified against `sources/generate/` during the Phase D review.

Every item below was checked directly in the cached `develop` source. They fall into three groups:
**architecture** (the seam is not where it looked), **unimplemented logic** (code that reads as a
rule but does not run), and **inconsistencies** (metadata that disagrees with itself).

## Architecture

### The CEDS IDS is a second inlet into RDS

The seam story — "replace `Staging.*` and everything downstream still works" — holds for the 20
modern domains and fails for the rest. Generate has an older route:
`Staging` → `Staging.Migrate_StagingToIDS_*` → the CEDS **Integrated Data Store** (`dbo.*`) →
`RDS.Migrate_Dim*` → `RDS`.

**58 of 67 `RDS.Migrate_Dim*` procedures read `dbo.*` and never read `Staging.*`; 4 read both; none
read `Staging.*` alone.** The `dbo.*` names map 1:1 onto `generate.core/Models/IDS/*.cs`, which is
what identifies them as the IDS. Consequences:

- `RDS.Migrate_DimCteStatuses` reads `dbo.ProgramParticipationCte`, `dbo.PersonProgramParticipation`,
  `dbo.OrganizationPersonRole`, `dbo.RefNonTraditionalGenderStatus`. The CEDS-aligned
  `Staging.ProgramParticipationCTE` is read only by the IDS loader and by index maintenance — never
  on the EDFacts path. So [[CTE]]'s categorical data has no staging seam.
- `RDS.Migrate_OrganizationStatusCounts` (the `organizationstatus` fact type, FS199–FS202) reads
  `dbo.K12SchoolIndicatorStatus`, `dbo.RefIndicatorStatusType`, `dbo.RefIndicatorStatusCustomType`
  and no `Staging.*` table at all. See [[Directory]].
- `RDS.Migrate_StudentCounts` — the fact loader for [[CTE]], [[Other]], [[SPPAPR]] and
  [[StudentCounts]] — references only `rds.*` and `dbo.*`.

An Ed-Fi binding that replaces only the staging contract leaves this layer unfed. Either the IDS
shape must also be supplied, or `RDS.Migrate_Dim*` must be replaced outright.

### Two generations of nearly everything

Wrappers (`Staging-to-Fact*` vs. `rds.Migrate_StudentCounts`), report generators
(`RDS.Create_ReportData` + `Get_CountSQL` vs. `RDS.Insert_CountsIntoReportTable`), and lineage views
(`Debug.vw<Domain>_*` vs. `RDS.vw<Domain>_FactTable_<C###>`) each exist in an old and a new form,
both live, selected per report by `App.GenerateReports.UseLegacyReportMigration`. See
[[Staging-to-RDS-Migration]] and [[Report-Data-Generation]].

### FS052 membership counts depend on FS039 report output

The legacy generator builds c052's LEA/school counts by inner-joining students to a `#Grades` temp
table loaded from `rds.ReportEDFactsOrganizationCounts where ReportCode = 'C039'`
(`RDS.Get_CountSQL` lines 537–545, joins at 607 and 622). FS052 therefore cannot be reproduced
without first reproducing FS039 — report generation is order-dependent across file specs, not just
across fact loads. See [[Membership]].

## Unimplemented logic

Code that looks like a rule but does not execute. Each of these means a re-implementation should
follow the *file spec*, not Generate's behaviour.

| Finding | Where | Effect |
|---|---|---|
| Adjusted-cohort logic absent | `Staging-to-FactK12StudentCounts_GraduationRate` line 163 sets `CohortStatusId = -1`; the `RDS.DimCohortStatuses` join is commented out with "Mapping above needs research… the dimension doesn't exist yet" | FS150/FS151 ACGR has **no** transfer-in/transfer-out adjustment; `Get_CountSQL` divides by a plain `sum(StudentCount)`. See [[Graduationrate]] |
| Postsecondary enrolment never filtered | `Staging-to-FactK12StudentCounts_HSGradPSEnroll` references neither `PostSecondaryEnrollment` nor `DiplomaOrCredentialAwardDate`, has no `WHERE` clause, `LEFT JOIN`s an unused `Staging.PsStudentEnrollment`, and hardcodes `K12EnrollmentStatusId = -1` (line 136) — the very column report generation gates on | FS160 loads one row per enrolled student, not per postsecondary-enrolled graduate. See [[HsGradPSEnroll]] |
| Chronic-absence threshold not in the load | `AttendanceRate < 0.9` appears only in `Debug.vwChronic_StagingTables.View.sql` line 79; the fact procedure never references `AttendanceRate` | Every enrolled student gets a FS195 fact row; the 90% threshold is documentation, not logic. See [[Chronic]] |
| `TitleIIIStatusId` hardcoded | `Staging-to-FactK12StaffCounts` line 97 writes `-1` | FS067's Title III teacher status has no populating source. See [[Staff]] |
| `SchoolImprovementFunds` hardcoded | `Staging-to-FactOrganizationCounts` | FS035's school-improvement allocation is never populated. See [[Directory]] |
| DataPopulation status columns hardcoded | `Staging-to-FactK12StudentCounts_DataPopulation` writes `-1` for EL, homeless, migrant, foster care, economic disadvantage, Title III, CTE, N-or-D, cohort and attendance | Those slices are populated only by other domains writing the same shared fact table. See [[DataPopulation]] |
| Assessment score columns hardcoded | `Staging-to-FactK12StudentAssessments` — scale/percentile/T/Z/ACT/SAT columns set to `-1` | Only `ScoreValue` is real. See [[Assessments]] |
| `cohortgraduationrate` reads phantom objects | `RDS.Create_CustomReportData` lines 909–1005 read `rds.FactStudentCounts` / `rds.DimStudents.Cohort` — neither has DDL nor a populating procedure anywhere in the repo | The report cannot produce rows as shipped. See [[GraduatesCompleters]] |
| c089 age predicate excludes ages 3–4 | `RDS.vwChildCount_FactTable_C089.sql` lines 27–31 filter `AgeEdFactsCode IN ('3','4','5')` and then require age 5 with grade `PK`/`MISSING` — the inverse of the working c002 exclusion (`RDS.vwChildCount_FactTable_C002.sql` lines 54–58) | FS089, the ages 3–5 count, can never count ages 3–4 through the current-generation view. See [[ChildCount]] |
| c089 staging view cannot compile | `Staging.vwChildCount_StagingTables_C089.View.sql` line 78 joins CTE `excludeDD`, which the view never defines (the c002 twin defines it at line 16); lines 82–85 also require `GradeLevel IS NULL AND GradeLevel IN ('PK','PK_1')`, which is never true | The c089 current-generation staging path is dead as shipped. See [[ChildCount]] |
| Grades Offered staging join reads nonexistent columns | `Staging-to-DimK12Schools` lines 487–495 join `sogo.RecordStartDateTime`, `sogo.RecordEndDateTime`, `sogo.SchoolYear`; the frozen DDL (`Tables/Create/Staging.OrganizationGradesOffered.Table.sql` lines 2–9) declares none of them — and that file creates `Staging.OrganizationGradeOffered`, singular, despite its plural filename | The frozen grades-offered staging path cannot compile against its own DDL; another stale-DDL case — trust the procedures. See [[Directory]] |
| CSI/TSI and charter-status FKs are permanent `-1` sentinels | The wrapper-called `Staging-to-FactOrganizationCounts` hardcodes `ComprehensiveAndTargetedSupportId` and `CharterSchoolStatusId` to `-1` at every level (lines 151–152, 245–246, 398–399); the only real writer, `Staging-to-FactOrganizationCounts_ComprehensiveAndTargetedSupport`, has no caller in the tree; the alternative `RDS.Migrate_OrganizationCounts` is itself dead code with its `Migrate_DimComprehensiveAndTargetedSupport_School` call commented out (lines 623–638) | FS206's CSI/TSI/ATSI fields never carry a real per-school value at this commit. See [[Directory]] |
| `rds.DimCharterSchoolStatuses` does not exist | Referenced only at `RDS.Create_OrganizationReportData` lines 1362, 1368–1369 (c207's `AppropriationMethodEdFactsCode`); no `CREATE TABLE`, view, or populating procedure anywhere in the cached tree | FS207's appropriation method has no data source; c206 additionally `INNER JOIN`s its support dimension on the always-`-1` key (lines 1326–1327), so its output is structurally empty or constant |
| c130 computes `ImprovementStatus` that is never emitted | `RDS.Create_OrganizationReportData` lines 664, 682 build the column; `App.FileSubmissions.Metadata.sql` has no `ImprovementStatus` file column anywhere | Dead computation on the persistently-dangerous path. See [[Directory]] |
| c033 and c059 are active but unreachable by both generators | Zero `App.CategorySets` rows for either code (`App.CategorySets.Metadata.sql` lines 12206–12212, 17759–17765) against hard `ReportCode` joins in `RDS.Create_ReportData` (lines 90–95, 140–157, 207–211); no `rds.vw*_C033`/`_C059` view exists for the current generator; both registered `IsActive = 1` (`App.GenerateReports.Metadata.sql` lines 388–394, 496–502) | FS033 and FS059 cannot emit rows at this commit; the c033 branch logic in `Get_CountSQL` (e.g. lines 5823–5880) is dead code |
| c033 merges Free and Reduced-Price Lunch | `RDS.Get_CountSQL` lines 5861–5862 bucket only `DIRECTCERT` vs `LUNCHFREERED`; the line-5873 filter collapses `FREE` and `REDUCEDPRICE` into one bucket | FS033's record layout requires the two categories separately; no lineage exists at the required grain |
| Charter-authorizer staging loader reads undeclared columns | `Staging-to-DimCharterSchoolAuthorizers` lines 77–87 select `AddressApartmentRoomOrSuiteNumber`, `StateAbbreviation`, `AddressCountyAnsiCodeCode` from aliases bound to `Staging.OrganizationAddress` (lines 107, 111); the DDL (`Tables/Create/Staging.OrganizationAddress.Table.sql` lines 1–15) declares `AddressApartmentRoomOrSuite`, `RefStateId`/`AddressStateANSICode`, and no county column | The c190 address staging path cannot resolve as written — another stale-DDL case |
| c190 operational-status filter disabled | `RDS.Create_OrganizationReportData` lines 967–971 and 1004–1008: the commented-out `DimK12Schools` join ("JW 6/26/2023 Not sure of this join") disables both UNION arms' `SchoolOperationalStatus not in ('Closed','FutureSchool','Inactive','MISSING')` filter | Closed and inactive schools' authorizers are not excluded from FS190 |

## Inconsistencies

| Finding | Evidence | Status |
|---|---|---|
| **`C225` is gated on `c226`'s flag** | `RDS.Create_Reports` wraps the `C225` call in `if exists (… ReportCode = 'c226' and IsLocked = 1 …)`; the log line inside says `'Submission Reports - c225'` | Almost certainly a copy-paste bug. FS225 generates only when FS226 is locked. See [[Assessments]] |
| **`c045` dispatched under two fact types** | `RDS.Create_Reports` lines 339–347 (`graduatescompleters`) and 408–416 (`titleIIIELSY`); neither commented out | `RDS.Get_FactTypeByReport` returns exactly one fact type per report code, so `App.GenerateReport_FactType` silently decides which branch is correct and the other counts the wrong fact slice. Unresolved — see [[GraduatesCompleters]], [[TitleIIIELSY]] |
| **`App.CedsConnections` titles disagree with the code** | FS165 is titled "Migratory Data" though `c165` is dispatched only under `immigrant`; FS045 is titled "Immigrant" under both branches that dispatch it | `CedsConnections` is a CEDS Connect documentation link, not a mapping — treat the procedure headers and `RDS.Create_Reports` as authoritative. See [[Immigrant]] |
| **`IDEADISAB` is not a category code** | Zero rows in `App.Categories`; it is an `App.TableTypes.TableTypeAbbrv` (a file-spec grouping). Real codes are purpose-suffixed: `DISABCATIDEA`, `DISABSTATIDEA`, `DISABCATIDEAEXIT`, `AGEEXITSPED`, `GRADELVMEM`, `RACEETHNIC`, `SEX`, `LEPONLY`, `BASISEXIT` | Corrected across the vault. No bare `RACE`, `AGE` or `ELSTATUS` code exists. See [[App-Metadata-Layer]] |
| **Exiting's exit reason is not `ExitOrWithdrawalType`** | `Staging.K12Enrollment.ExitOrWithdrawalType` appears nowhere in the Exiting fact procedure; the element is `Staging.ProgramParticipationSpecialEducation.SpecialEducationExitReason` | `ExitOrWithdrawalType` belongs to [[Dropout]] / [[Membership]], not [[Exiting]] |
| **`Empty_RDS` arity mismatch** | `App.Wrapper_Migrate_StudentCounts_to_RDS` line 43 calls `exec [rds].[Empty_RDS] 'submission', 'studentcounts'`; `RDS.Empty_RDS` declares one parameter | Would raise at call time. See [[StudentCounts]] |
| **`c204` retired in code** | `RDS.Create_Reports` lines 419–427 fully commented under `-- This report is retired --` | Metadata rows persist. See [[TitleIIIELSY]] |
| **Filename/object mismatch** | `Views/Create/Debug.vwDirectoryLiteSEA_FactTable.View.sql` declares `CREATE VIEW [Debug].[vwDirectorySEA_FactTable]` | Deploying both files installs one view twice. See [[Directory]] |
| **Stale staging DDL** | `Tables/Create/Staging.K12Enrollment.sql` declares `Student_Identifier_State`; live code uses `StudentIdentifierState` / `LEAIdentifierSeaAccountability`. Four hot tables have no DDL at all | Read column names from `Debug.vw*_StagingTables`. See [[Staging-Layer]] |
| **c089 report view selects the school-age environment column** | `RDS.vwChildCount_FactTable_C089.sql` line 23 selects `IdeaEducationalEnvironmentForSchoolAgeEdFactsCode`; the legacy generator picks `IDEAEducationalEnvironmentForEarlyChildhood` for c089 (`RDS.Get_CountSQL` lines 7223–7231) | Early-childhood educational environment comes from the wrong column on the current-generation path. See [[ChildCount]] |
| **Current-generation dispatch passes removed parameters** | Eight `exec [RDS].[Insert_CountsIntoReportTable]` sites in `RDS.Create_Reports` (lines 304, 459, 562, 578, 594, 610, 1014, 1030) pass `@ReportTableName`/`@CountColumn`; the procedure comments both out of its signature (lines 4–6) and derives them internally from `App.FactType_ReportsXREF` (lines 11–15) | Every such call errors at runtime; as shipped, only legacy-dispatched reports can generate. See [[Report-Data-Generation]] |
| **EL status can never be `MISSING`** | `Staging.vwChildCount_StagingTables_C089.View.sql` lines 71–74: unconditional `ELSE 'NLEP'` (c002 twin identical) | Absent EL data is reported as non-EL; the federal `MISSING` value is unreachable from this path. See [[ChildCount]] |
| **`Deafness` collapsed into `DB`** | `Staging.vwChildCount_StagingTables_C089.View.sql` lines 19–20 and 33–34 map `Deafblindness`, `Deafness`, and both `_1` variants all to `DB` | A hearing-disability category is misreported as deaf-blindness on the current-generation path. See [[ChildCount]] |
| **State ANSI code emitted as parent-org identifier** | `RDS.Get_CountSQL` line 6482: `lea.StateANSICode as ParentOrganizationIdentifierSea` at LEA level | The legacy generator writes a state code where the SEA parent-organization identifier belongs |
| **c052 unduplicates on the dimension surrogate, not the student identifier** | `RDS.Get_CountSQL` lines 6116–6125: C052 uses `count(distinct cs.dimStudentId)` while c002/c089 use `count(distinct cs.K12StudentStudentIdentifierState)` | A student split across `DimPeople` rows (name/birthdate/span changes) inflates the FS052 count. See [[Membership]] |

## Citations

- `generate.database/StoredProcedures/Create/RDS.Migrate_DimCteStatuses.StoredProcedure.sql@develop`
- `generate.database/StoredProcedures/Create/RDS.Migrate_OrganizationStatusCounts.StoredProcedure.sql@develop`
- `generate.database/StoredProcedures/Create/RDS.Migrate_StudentCounts.StoredProcedure.sql@develop`
- `generate.database/StoredProcedures/Create/RDS.Create_Reports.StoredProcedure.sql@develop` lines 339–347, 408–416, 419–427, 1023–1037
- `generate.database/StoredProcedures/Create/Staging.Staging-to-FactK12StudentCounts_GraduationRate.StoredProcedure.sql@develop` lines 163, 247–254
- `generate.database/StoredProcedures/Create/Staging.Staging-to-FactK12StudentCounts_HSGradPSEnroll.StoredProcedure.sql@develop` lines 136, 159
- `generate.database/Views/Create/Debug.vwChronic_StagingTables.View.sql@develop` line 79
- `generate.database/StoredProcedures/Create/Staging.Staging-to-FactK12StaffCounts.StoredProcedure.sql@develop` line 97
- `generate.database/StoredProcedures/Create/RDS.Create_CustomReportData.StoredProcedure.sql@develop` lines 909–1005
- `generate.database/StoredProcedures/Create/App.Wrapper_Migrate_StudentCounts_to_RDS.StoredProcedure.sql@develop` line 43
- `generate.database/Metadata/App.Categories.Metadata.sql@develop`, `generate.database/Metadata/App.TableTypes.Metadata.sql@develop`
- `generate.database/Metadata/App.CedsConnections.Metadata.sql@develop`
- `generate.database/Views/Create/Debug.vwDirectoryLiteSEA_FactTable.View.sql@develop` line 1
- `generate.database/Views/Create/RDS.vwChildCount_FactTable_C089.sql@develop` lines 23, 27–31
- `generate.database/Views/Create/RDS.vwChildCount_FactTable_C002.sql@develop` lines 54–58
- `generate.database/Views/Create/Staging.vwChildCount_StagingTables_C089.View.sql@develop` lines 19–34, 71–74, 78–85
- `generate.database/Views/Create/Staging.vwChildCount_StagingTables_C002.View.sql@develop` line 16
- `generate.database/Functions/Create/RDS.Get_CountSQL.UserDefinedFunction.sql@develop` lines 6482, 7198–7231
- `generate.database/StoredProcedures/Create/RDS.Insert_CountsIntoReportTable.StoredProcedure.sql@develop` lines 1–15
- `generate.database/StoredProcedures/Create/RDS.Create_Reports.StoredProcedure.sql@develop` lines 304–311, 459, 562–610, 1014–1030
- `generate.database/Functions/Create/RDS.Get_CountSQL.UserDefinedFunction.sql@develop` lines 537–545, 607, 622, 6116–6125
- `generate.database/StoredProcedures/Create/Staging.Staging-to-DimK12Schools.StoredProcedure.sql@develop` lines 487–495
- `generate.database/Tables/Create/Staging.OrganizationGradesOffered.Table.sql@develop` lines 2–9
