# Worker 3 element inventory

Domains: Membership, Dropout, GraduatesCompleters, Graduationrate, HsGradPSEnroll, Chronic

## Contradictions found

- Brief (GraduatesCompleters) lists `cohortgraduationrate` as needing `CohortYear`,
  `CohortGraduationYear`, `CohortDescription` on `Staging.K12Enrollment`. Source:
  `RDS.Create_CustomReportData`'s `cohortgraduationrate` branch reads `rds.DimStudents.Cohort` off
  `rds.FactStudentCounts` — a table/dimension pair with no DDL and no populating procedure anywhere
  under `sources/generate`. The `Staging.K12Enrollment` cohort columns are instead consumed by
  `Staging.Staging-to-FactK12StudentCounts_GraduationRate` (the Graduationrate domain), not by
  `cohortgraduationrate`. See `generate.database/StoredProcedures/Create/RDS.Create_CustomReportData.StoredProcedure.sql@develop`
  lines 909–1005.
- Brief (GraduatesCompleters) records the known `c045` collision (`graduatescompleters` vs.
  `titleIIIELSY`) without resolving it, correctly. Additionally: `App.CedsConnections.Metadata.sql`
  gives FS045's CEDS Connect title as "Immigrant" (e.g. `'FS045 Immigrant SY 2020-21 (Generate)'`),
  matching neither factType branch it is dispatched under. Not resolved, per brief instruction.
- Brief (Graduationrate) says "'Adjusted' means transfers in and out modify the denominator — find
  where that adjustment happens and cite it." Source: no such adjustment is visible anywhere.
  `Staging.Staging-to-FactK12StudentCounts_GraduationRate` hardcodes `CohortStatusId = -1` for every
  row and comments out the `RDS.DimCohortStatuses` join with "Mapping above needs research... the
  dimension doesn't exist yet." `RDS.Get_CountSQL`'s `ADJUSTEDCOHORTGRADUATIONRATE` divides by a
  plain `sum(StudentCount)` with no transfer-adjustment join. See
  `generate.database/StoredProcedures/Create/Staging.Staging-to-FactK12StudentCounts_GraduationRate.StoredProcedure.sql@develop`
  lines 163, 247–254.
- Brief (HsGradPSEnroll) says "The element is `Staging.K12Enrollment.PostSecondaryEnrollment` (a bit)
  combined with `DiplomaOrCredentialAwardDate`." Source: neither column is referenced anywhere in
  `Staging.Staging-to-FactK12StudentCounts_HSGradPSEnroll`. The procedure `LEFT JOIN`s an unused,
  undocumented `Staging.PsStudentEnrollment` table and has no `WHERE` clause at all — it loads one
  row per enrolled student, not per postsecondary-enrolled graduate. Report generation
  (`RDS.Get_CountSQL`, `c160`) actually gates on `K12EnrollmentStatusId` →
  `PostSecondaryEnrollmentStatusEdFactsCode <> 'MISSING'`, but the fact procedure hardcodes
  `K12EnrollmentStatusId = -1`. See
  `generate.database/StoredProcedures/Create/Staging.Staging-to-FactK12StudentCounts_HSGradPSEnroll.StoredProcedure.sql@develop`
  lines 136, 159–162, 217–226.
- Brief (Chronic) says "Find the threshold in the fact procedure and cite the line — do not assume
  10%." Source: the threshold (`AttendanceRate < 0.9`) exists only in
  `Debug.vwChronic_StagingTables.View.sql@develop` line 79. `Staging.Staging-to-FactK12StudentCounts_Chronic`
  has no `WHERE` clause narrowing by attendance at all — every enrolled student gets a fact row.

---

## Membership

Fact type: `membership` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c033`, `c052`, `c226`
File specs: FS033, FS052, FS226

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_student.studentUniqueId` | |
| Organization (SEA/LEA/school) | `LEAIdentifierSeaAccountability`, `SchoolIdentifierSea` | organization | Direct | `edFi_school.schoolId`, `edFi_localEducationAgency.localEducationAgencyId` | |
| Membership (as-of) count date | EMAPS toggle `MEMBERDTE` vs. `EnrollmentEntryDate`/`EnrollmentExitDate` | filter | Derivable | `edFi_studentSchoolAssociation.entryDate` + `.exitWithdrawDate` | count date is a config value, not a stored element |
| Sex | `Staging.K12Enrollment.Sex` | category: SEX | Direct | `edFi_studentEducationOrganizationAssociation.sexDescriptor` | |
| Grade level | `Staging.K12Enrollment.GradeLevel` | category: GRADELVMEM | Direct | `edFi_studentSchoolAssociation.entryGradeLevelDescriptor` | |
| Race/ethnicity | `Staging.K12PersonRace.RaceType`, `HispanicLatinoEthnicity` | category: RACEETHNIC | Direct | `edFi_studentEducationOrganizationAssociation.races`, `.hispanicLatinoEthnicity` | |
| NSLP direct certification | `Staging.PersonStatus.NationalSchoolLunchProgramDirectCertificationIndicator` | category: LUNCHPROG | Direct | `edFi_studentSchoolFoodServiceProgramAssociation.directCertification` | feeds c033 |
| FRL eligibility status | `Staging.PersonStatus.EligibilityStatusForSchoolFoodServicePrograms` | category: LUNCHPROG | Derivable | `edFi_studentSchoolFoodServiceProgramAssociation` participation/service type | feeds c033 |
| Economic disadvantage (overall) | `Staging.PersonStatus.EconomicDisadvantageStatus` | category: ECODIS | Derivable | active `edFi_studentSchoolFoodServiceProgramAssociation` | feeds c226 |
| Title I program type | `Staging.K12Organization.LEA_TitleIProgramType` | category: TITLEIPROG | Direct | active `edFi_studentTitleIPartAProgramAssociation` | |
| School operational status | `Staging.K12Organization.School_OperationalStatus` | filter | Direct | `edFi_school.operationalStatusDescriptor` | c226 eligibility only |
| School type | `Staging.K12Organization.School_Type` | filter | Direct | `edFi_school.schoolTypeDescriptor` | c226 eligibility only |

---

## Dropout

Fact type: `dropout` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c032`
File specs: FS032

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_student.studentUniqueId` | |
| Organization (LEA/school) | `LEAIdentifierSeaAccountability`, `SchoolIdentifierSea` | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId`, `edFi_school.schoolId` | |
| Exit/withdrawal reason | `Staging.K12Enrollment.ExitOrWithdrawalType` → SSRD `RefExitOrWithdrawalType` | filter (defines "dropout") | Direct | `edFi_studentSchoolAssociation.exitWithdrawTypeDescriptor` | fact procedure recognizes only CEDS code `01927`; debug view lists `01925`/`01927`/`01931` |
| "Is this a dropout" | derived from the code above | filter | Derivable | state convention over `exitWithdrawTypeDescriptor` values | not a stored fact in either system |
| Grade level (exit) | `Staging.K12Enrollment.GradeLevel` | category: GRADELDROP | Direct | `edFi_studentSchoolAssociation.entryGradeLevelDescriptor` (exit grade needs `nextYearGradeLevelDescriptor`) | |
| Sex | `Staging.K12Enrollment.Sex` | category: SEX | Direct | `edFi_studentEducationOrganizationAssociation.sexDescriptor` | |
| Race/ethnicity | `Staging.K12PersonRace.RaceType`, `HispanicLatinoEthnicity` | category: RACEETHNIC | Direct | `edFi_studentEducationOrganizationAssociation.races`, `.hispanicLatinoEthnicity` | |
| IDEA indicator | `Staging.ProgramParticipationSpecialEducation.IDEAIndicator` | category: DISABSTATIDEA | Direct | `edFi_studentSpecialEducationProgramAssociation.ideaEligibility` | |
| Section 504 status | `Staging.Disability.DisabilityStatus`, `Section504Status` | category: SEC504STATUS | Derivable | active `edFi_studentSection504ProgramAssociation` | |
| Migrant status | `Staging.PersonStatus.MigrantStatus` | category: MIGRNTSTATUS | Direct | active `edFi_studentMigrantEducationProgramAssociation` | |
| English learner status | `Staging.PersonStatus.EnglishLearnerStatus` | category: ELSTATUS | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | |
| Economic disadvantage | `Staging.PersonStatus.EconomicDisadvantageStatus` | category: ECODIS | Derivable | active `edFi_studentSchoolFoodServiceProgramAssociation` | |
| Homelessness | `Staging.PersonStatus.HomelessnessStatus` | category: HOMELESS | Direct | active `edFi_studentHomelessProgramAssociation` | |

---

## GraduatesCompleters

Fact type: `graduatescompleters` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c040`, `c045`, `cohortgraduationrate`
File specs: FS040

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_student.studentUniqueId` | |
| Organization (LEA/school) | `LEAIdentifierSeaAccountability`, `SchoolIdentifierSea` | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId`, `edFi_school.schoolId` | |
| Diploma/credential type | `Staging.K12Enrollment.HighSchoolDiplomaType` | identifier (defines "completer") + category: DIPLCREDTYPE | Direct | `edFi_studentAcademicRecordDiploma.diplomaTypeDescriptor` | fact procedure filter is simply "not blank" |
| Diploma award date | `Staging.K12Enrollment` (reporting window 10/1–9/30, no dedicated award-date column read) | filter | Direct | `edFi_studentAcademicRecordDiploma.diplomaAwardDate` | |
| CTE completer | not read by this fact procedure | n/a | Direct | `edFi_studentAcademicRecordDiploma.cteCompleter` | see CTE (worker 4) |
| Sex | `Staging.K12Enrollment.Sex` | category: SEX | Direct | `edFi_studentEducationOrganizationAssociation.sexDescriptor` | |
| Race/ethnicity | `Staging.K12PersonRace.RaceType`, `HispanicLatinoEthnicity` | category: RACEETHNIC | Direct | `edFi_studentEducationOrganizationAssociation.races`, `.hispanicLatinoEthnicity` | |
| IDEA indicator | `Staging.ProgramParticipationSpecialEducation.IDEAIndicator` | category: DISABSTATIDEA | Direct | `edFi_studentSpecialEducationProgramAssociation.ideaEligibility` | |
| English learner status | `Staging.PersonStatus.EnglishLearnerStatus` | category: ELSTATUS | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | |
| Homelessness | `Staging.PersonStatus.HomelessnessStatus` | category: HOMELESS | Direct | active `edFi_studentHomelessProgramAssociation` | |
| Migrant status | `Staging.Migrant` / `PersonStatus.MigrantStatus` | category: MIGRNTSTATUS | Direct | active `edFi_studentMigrantEducationProgramAssociation` | |
| Economic disadvantage | `Staging.PersonStatus.EconomicDisadvantageStatus` | category: ECODIS | Derivable | active `edFi_studentSchoolFoodServiceProgramAssociation` | |
| Cohort membership (`cohortgraduationrate` only) | `rds.DimStudents.Cohort` (legacy, undocumented — see Contradictions) | identifier | Absent | no cohort-year role concept on the diploma record | see `generate.database/StoredProcedures/Create/RDS.Create_CustomReportData.StoredProcedure.sql@develop` |

---

## Graduationrate

Fact type: `graduationrate` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c150`, `c151`
File specs: FS150, FS151

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_student.studentUniqueId` | |
| Organization (LEA/school) | `LEAIdentifierSeaAccountability`, `SchoolIdentifierSea` | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId`, `edFi_school.schoolId` | 12th-grade-only filter applied at report time |
| Cohort entry year | `Staging.K12Enrollment.CohortYear` | identifier (defines the cohort) | Derivable | `edFi_studentEducationOrganizationAssociationCohortYear` (`cohortYearTypeDescriptor` + `schoolYearTypeReference`) | |
| Cohort graduation year | `Staging.K12Enrollment.CohortGraduationYear` | measure (rate window) | Derivable | same as above, different `cohortYearTypeDescriptor` value | |
| Cohort status/description | `Staging.K12Enrollment.CohortDescription` | category: COHSTATUS | Absent | not mapped in Generate itself — `CohortStatusId` is hardcoded `-1` (see Contradictions) | |
| Adjusted cohort (transfers in/out) | none found | measure | Absent | no maintained four-year adjusted-cohort concept in core Ed-Fi | compute from `edFi_studentSchoolAssociation` spans across the cohort span |
| Graduated with regular diploma | `Staging.K12Enrollment.HighSchoolDiplomaType` (via GraduatesCompleters dimension) | measure (numerator) | Direct | `edFi_studentAcademicRecordDiploma.diplomaTypeDescriptor` + `.diplomaAwardDate` | |
| Sex | `Staging.K12Enrollment.Sex` | category: SEX | Direct | `edFi_studentEducationOrganizationAssociation.sexDescriptor` | |
| Race/ethnicity | `Staging.K12PersonRace.RaceType`, `HispanicLatinoEthnicity` | category: RACEETHNIC | Direct | `edFi_studentEducationOrganizationAssociation.races`, `.hispanicLatinoEthnicity` | |
| IDEA indicator | `Staging.ProgramParticipationSpecialEducation.IDEAIndicator` | category: DISABSTATIDEA | Direct | `edFi_studentSpecialEducationProgramAssociation.ideaEligibility` | |
| Homelessness | `Staging.PersonStatus.HomelessnessStatus` | category: HOMELESS | Direct | active `edFi_studentHomelessProgramAssociation` | |
| Foster care status | `Staging.PersonStatus.ProgramType_FosterCare` | filter | Absent | no foster-care program association in core Ed-Fi 5.2.0 | |
| Economic disadvantage | `Staging.PersonStatus.EconomicDisadvantageStatus` | category: ECODIS | Derivable | active `edFi_studentSchoolFoodServiceProgramAssociation` | |

---

## HsGradPSEnroll

Fact type: `hsgradpsenroll` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c160`
File specs: FS160

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_student.studentUniqueId` | |
| Organization (LEA/school) | `LEAIdentifierSeaAccountability`, `SchoolIdentifierSea` | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId`, `edFi_school.schoolId` | |
| Postsecondary enrollment flag | `Staging.K12Enrollment.PostSecondaryEnrollment` (declared; unused by the fact procedure) | identifier (intended) | Derivable | `edFi_postSecondaryEvent` (`postSecondaryEventCategoryDescriptor` + `eventDate` + `postSecondaryInstitutionReference`) | see Contradictions — not wired in Generate |
| Diploma award date | `Staging.K12Enrollment.DiplomaOrCredentialAwardDate` (declared; unused) | filter (intended) | Direct | `edFi_studentAcademicRecordDiploma.diplomaAwardDate` | |
| Enrollment status (report-time gate) | `RDS.DimK12EnrollmentStatuses.PostSecondaryEnrollmentStatusEdFactsCode` | filter | Derivable | `edFi_postSecondaryEvent.postSecondaryEventCategoryDescriptor` value set (enrolled vs. not) | dimension never populated for this fact type — see Contradictions |

---

## Chronic

Fact type: `chronic` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c195`
File specs: FS195

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_student.studentUniqueId` | |
| Organization (LEA/school) | `LEAIdentifierSeaAccountability`, `SchoolIdentifierSea` | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId`, `edFi_school.schoolId` | |
| Attendance rate | `Staging.K12Enrollment.AttendanceRate` | filter (`< 0.9` defines "chronically absent") | Absent | no stored rate element in core Ed-Fi | threshold applied only in `Debug.vwChronic_StagingTables`, not the fact procedure — see Contradictions |
| Days absent / school days | `Staging.K12Enrollment.NumberOfDaysAbsent`, `.NumberOfSchoolDays` | measure (rate inputs) | Derivable | aggregate `edFi_studentSchoolAttendanceEvent` (`attendanceEventCategoryDescriptor`, `eventDate`) per student per year | |
| Sex | `Staging.K12Enrollment.Sex` | category: SEX | Direct | `edFi_studentEducationOrganizationAssociation.sexDescriptor` | |
| Race/ethnicity | `Staging.K12PersonRace.RaceType`, `HispanicLatinoEthnicity` | category: RACEETHNIC | Direct | `edFi_studentEducationOrganizationAssociation.races`, `.hispanicLatinoEthnicity` | |
| IDEA indicator | `Staging.ProgramParticipationSpecialEducation.IDEAIndicator` | category: DISABSTATIDEA | Direct | `edFi_studentSpecialEducationProgramAssociation.ideaEligibility` | |
| Section 504 status | `Staging.Disability.DisabilityStatus`, `Section504Status` | category: SEC504STATUS | Derivable | active `edFi_studentSection504ProgramAssociation` | distinct from IDEA; not `Staging.IdeaDisabilityType` |
| English learner status | `Staging.PersonStatus.EnglishLearnerStatus` | category: ELSTATUS | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | |
| Homelessness | `Staging.PersonStatus.HomelessnessStatus` | category: HOMELESS | Direct | active `edFi_studentHomelessProgramAssociation` | |
| Economic disadvantage | `Staging.PersonStatus.EconomicDisadvantageStatus` | category: ECODIS | Derivable | active `edFi_studentSchoolFoodServiceProgramAssociation` | |
