# Worker 2 element inventory

Domains: TitleI, TitleIIIELOct, TitleIIIELSY, Immigrant, MigrantEducationProgram, NeglectedOrDelinquent

## Contradictions found

- Brief said `c045` is dispatched under both `titleIIIELSY` and `graduatescompleters` (Worker 3's
  domain) — confirmed exactly by source, not a disagreement: `RDS.Create_Reports.StoredProcedure.sql`
  dispatches `ReportCode = 'c045'` under `@factTypeCode = 'graduatescompleters'` (lines 339–347)
  *and* under `@factTypeCode = 'titleIIIELSY'` (lines 408–416). Logged here per the brief's
  instruction; not resolved.
- Brief said Immigrant's file spec is FS165. `Metadata/App.CedsConnections.Metadata.sql` labels
  FS165 **"Migratory Data"** in every cached school-year snapshot (lines 7488, 11610, 13194, 14400,
  15732 — SY2017-18 through SY2021-22), which would suggest Migrant, not Immigrant. This
  contradicts the brief. Followed the brief anyway, because two independent code sources agree
  with it and with each other: `Staging.Staging-to-FactK12StudentCounts_Immigrant.StoredProcedure.sql`'s
  own header ("Migrates Immigrant Data... processes files: 165") and
  `RDS.Create_Reports.StoredProcedure.sql`, which dispatches `c165` only under
  `@factTypeCode = 'immigrant'` (never under `migranteducationprogram`, which uses `c054`/`c121`/
  `c122`/`c145` instead). Treated the CedsConnections text as a stale/mislabeled CEDS Connect
  use-case entry — see `wiki/generate/domains/Immigrant.md` for the full note.

---

## TitleI

Fact type: `titleI` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c037`, `c134`, `C222`, `studentswdtitle1`
File specs: FS037, FS134, FS222

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_studentReference.studentUniqueId` | |
| LEA identifier | `Staging.K12Enrollment.LEAIdentifierSeaAccountability` | organization | Direct | `edFi_localEducationAgencyReference.localEducationAgencyId` | |
| School identifier | `Staging.K12Enrollment.SchoolIdentifierSea` | organization | Direct | `edFi_schoolReference.schoolId` | |
| Title I participation | `Staging.ProgramParticipationTitleI.TitleIIndicator` | filter | Direct | `edFi_studentTitleIPartAProgramAssociation.titleIPartAParticipantDescriptor` | |
| School Title I status (SWP/TAS) | `Staging.K12Organization.School_TitleISchoolStatus` | filter | Direct | `edFi_school.titleIPartASchoolDesignationDescriptor` | Core property, not an extension |
| Foster care status | `Staging.PersonStatus.ProgramType_FosterCare` | filter | Absent | | Only `edFi_studentHomelessProgramAssociation.awaitingFosterCare` exists, scoped to McKinney-Vento awaiting-placement |
| IDEA indicator | `Staging.ProgramParticipationSpecialEducation.IDEAIndicator` | category: IDEADISAB | Direct | `edFi_studentEducationOrganizationAssociationDisability.designations` | |
| English learner status | `Staging.PersonStatus.EnglishLearnerStatus` | category: ELSTATUS | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | |
| Race/ethnicity | `Staging.K12PersonRace.RaceType` | category: RACE | Direct | `edFi_studentEducationOrganizationAssociation.races` | |

---

## TitleIIIELOct

Fact type: `titleIIIELOct` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c141`
File specs: FS141

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_studentReference.studentUniqueId` | |
| LEA / School identifier | `Staging.K12Enrollment.LEAIdentifierSeaAccountability` / `SchoolIdentifierSea` | organization | Direct | `edFi_localEducationAgencyReference.localEducationAgencyId`, `edFi_schoolReference.schoolId` | |
| English learner status (Oct-1 snapshot) | `Staging.PersonStatus.EnglishLearnerStatus` | filter | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | |
| Native language | `Staging.PersonStatus.ISO_639_2_NativeLanguage` | category: LANGUAGE | Direct | `edFi_studentEducationOrganizationAssociation.languages` | |
| IDEA indicator | `Staging.ProgramParticipationSpecialEducation.IDEAIndicator` | category: IDEADISAB | Direct | `edFi_studentEducationOrganizationAssociationDisability.designations` | |
| Race/ethnicity | `Staging.K12PersonRace.RaceType` | category: RACE | Direct | `edFi_studentEducationOrganizationAssociation.races` | |
| Grade level | `Staging.K12Enrollment.GradeLevel` | category: GRADELEVEL | Direct | `edFi_studentSchoolAssociation.entryGradeLevelDescriptor` | |
| Title III program participation | `Staging.ProgramParticipationTitleIII.EnglishLearnerParticipation` | filter | Direct | `edFi_studentLanguageInstructionProgramAssociation.englishLearnerParticipation` | `Debug.vwTitleIIIELOct_StagingTables` requires this; the fact procedure does not gate on it |

---

## TitleIIIELSY

Fact type: `titleIIIELSY` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c116`, `c045`, `c204`
File specs: FS116, FS045, FS204

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_studentReference.studentUniqueId` | |
| LEA / School identifier | `Staging.K12Enrollment.LEAIdentifierSeaAccountability` / `SchoolIdentifierSea` | organization | Direct | `edFi_localEducationAgencyReference.localEducationAgencyId`, `edFi_schoolReference.schoolId` | |
| English learner status (any time in SY) | `Staging.PersonStatus.EnglishLearnerStatus` | filter | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | Date rule changed at SY2023 — see domain note |
| Title III language instruction program type | `Staging.ProgramParticipationTitleIII.TitleIIILanguageInstructionProgramType` | category: LANGINSTPROG | Direct | `edFi_studentLanguageInstructionProgramAssociationLanguageInstructionProgramService.languageInstructionProgramServiceDescriptor` | |
| Title III EL participation flag | `Staging.ProgramParticipationTitleIII.EnglishLearnerParticipation` | filter | Direct | `edFi_studentLanguageInstructionProgramAssociation.englishLearnerParticipation` | Lineage view gates on this; fact procedure only left-joins it |
| Race/ethnicity | `Staging.K12PersonRace.RaceType` | category: RACE | Direct | `edFi_studentEducationOrganizationAssociation.races` | |
| Grade level | `Staging.K12Enrollment.GradeLevel` | category: GRADELEVEL | Direct | `edFi_studentSchoolAssociation.entryGradeLevelDescriptor` | |

---

## Immigrant

Fact type: `immigrant` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c165`
File specs: FS165

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_studentReference.studentUniqueId` | |
| LEA / School identifier | `Staging.K12Enrollment.LEAIdentifierSeaAccountability` / `SchoolIdentifierSea` | organization | Direct | `edFi_localEducationAgencyReference.localEducationAgencyId`, `edFi_schoolReference.schoolId` | |
| Immigrant program participation | `Staging.PersonStatus.ProgramType_Immigrant` | filter | Absent | | No `immigrant`-named property in any of 471 core `edFi_*` schemas |
| Immigrant statutory facts (age, birth jurisdiction, years in US schools) | not separately staged — folded into the flag above | filter | Derivable | `edFi_student.birthDate` + `.birthCountryDescriptor` + earliest `edFi_studentSchoolAssociation.entryDate` | Approximation only; no stored "years in US schools" field |
| English learner status | `Staging.PersonStatus.EnglishLearnerStatus` | category: ELSTATUS | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | |
| Native language | `Staging.PersonStatus.ISO_639_2_NativeLanguage` | category: LANGUAGE | Direct | `edFi_studentEducationOrganizationAssociation.languages` | |
| Grade level | `Staging.K12Enrollment.GradeLevel` | category: GRADELEVEL | Direct | `edFi_studentSchoolAssociation.entryGradeLevelDescriptor` | |

---

## MigrantEducationProgram

Fact type: `migranteducationprogram` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c054`, `c121`, `c122`, `c145`
File specs: FS054, FS121, FS122, FS145

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_studentReference.studentUniqueId` | |
| LEA / School identifier | `Staging.K12Enrollment.LEAIdentifierSeaAccountability` / `SchoolIdentifierSea` | organization | Direct | `edFi_localEducationAgencyReference.localEducationAgencyId`, `edFi_schoolReference.schoolId` | |
| Migrant status (eligibility) | `Staging.Migrant.MigrantStatus` | filter | Direct | Presence of `edFi_studentMigrantEducationProgramAssociation` | |
| Qualifying arrival date | `Staging.Migrant.MigrantStudentQualifyingArrivalDate` | filter | Direct | `edFi_studentMigrantEducationProgramAssociation.qualifyingArrivalDate` | |
| Last qualifying move date | `Staging.Migrant.LastQualifyingMoveDate` | filter | Direct | `edFi_studentMigrantEducationProgramAssociation.lastQualifyingMove` | |
| Continuation-of-services reason | `Staging.Migrant.ContinuationOfServicesReason` | category: MEPCONTSERV | Direct | `edFi_studentMigrantEducationProgramAssociation.continuationOfServicesReasonDescriptor` | |
| Priority for services | `Staging.Migrant.MigrantPrioritizedForServices` | category: MEPPRIORITY | Direct | `edFi_studentMigrantEducationProgramAssociation.priorityForServices` | |
| MEP services type | `Staging.Migrant.MigrantEducationProgramServicesType` | category: MEPSERVICE | Direct | `edFi_studentMigrantEducationProgramAssociationMigrantEducationProgramService.migrantEducationProgramServiceDescriptor` | |
| MEP enrollment type | `Staging.Migrant.MigrantEducationProgramEnrollmentType` | category: MEPENROLL | Absent | | Only the generic `programParticipationStatuses` collection exists; no MEP-specific enrollment-type descriptor |
| Age (MEP performance-period) | `Staging.K12Enrollment.BirthDate` | category: AGE | Direct | `edFi_student.birthDate` | |

---

## NeglectedOrDelinquent

Fact type: `neglectedordelinquent` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c119`, `c127`, `C218`, `C219`, `C220`, `C221`
File specs: FS119, FS127, FS218, FS219, FS220, FS221 (FS180/FS181 also appear in `RDS.Get_FactTypeByReport`'s legacy map)

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_studentReference.studentUniqueId` | |
| LEA identifier | `Staging.K12Enrollment.LEAIdentifierSeaAccountability` | organization | Direct | `edFi_localEducationAgencyReference.localEducationAgencyId` | |
| N or D status flag | `Staging.ProgramParticipationNorD.NeglectedOrDelinquentStatus` | filter | Direct | Presence of `edFi_studentNeglectedOrDelinquentProgramAssociation` | |
| Subpart (state agency vs. LEA) | `Staging.ProgramParticipationNorD.NeglectedOrDelinquentProgramEnrollmentSubpart` | filter | Direct | `edFi_studentNeglectedOrDelinquentProgramAssociation.neglectedOrDelinquentProgramDescriptor` | Selects C218/C220 vs. C219/C221 |
| N or D program type | `Staging.ProgramParticipationNorD.NeglectedOrDelinquentProgramType` | category | Direct | `edFi_studentNeglectedOrDelinquentProgramAssociation.neglectedOrDelinquentProgramDescriptor` | FS119/FS127 (legacy) only; current C218–C221 default this to MISSING |
| Academic/CTE outcome type | `Staging.ProgramParticipationNorD.EdFactsAcademicOrCareerAndTechnicalOutcomeType` | category | Direct | `edFi_studentNeglectedOrDelinquentProgramAssociation.neglectedOrDelinquentProgramServices` | C218/C219's disaggregation |
| Academic/CTE outcome exit type | `Staging.ProgramParticipationNorD.EdFactsAcademicOrCareerAndTechnicalOutcomeExitType` | category | Direct | `edFi_studentNeglectedOrDelinquentProgramAssociation.neglectedOrDelinquentProgramServices` | C220/C221's disaggregation |
| Reading progress level | `Staging.ProgramParticipationNorD.ProgressLevel_Reading` | category | Direct | `edFi_studentNeglectedOrDelinquentProgramAssociation.elaProgressLevelDescriptor` | |
| Math progress level | `Staging.ProgramParticipationNorD.ProgressLevel_Math` | category | Direct | `edFi_studentNeglectedOrDelinquentProgramAssociation.mathematicsProgressLevelDescriptor` | |
| Facility/institution type | not staged as a discrete element | filter | Absent | | No facility or institution concept in core 5.2.0 (471 schemas searched) |
| LEA operational status | `Staging.K12Organization.LEA_OperationalStatus` | filter | Direct | `edFi_localEducationAgency.operationalStatusDescriptor` | Excludes closed/inactive/future LEAs |
