# Worker 4 element inventory

Domains: Directory, Staff, CTE, DataPopulation, StudentCounts, Homeless

## Contradictions found

- Brief says (Directory notes): "Repo bug to flag, not fix: `Views/Create/Debug.vwDirectoryLiteSEA_FactTable.View.sql` declares `CREATE VIEW [Debug].[vwDirectorySEA_FactTable]` — the filename and the object name disagree." Confirmed verbatim in the source: `generate.database/Views/Create/Debug.vwDirectoryLiteSEA_FactTable.View.sql@develop` line 1 reads `CREATE VIEW [Debug].[vwDirectorySEA_FactTable]` (no "Lite"). Not a contradiction of the brief — the brief was right — recorded here per the brief's own instruction to log it.
- Brief lists `Tables/Create/Staging.OrganizationSchoolComprehensiveAndTargetedSupport.Table.sql` as relevant stale DDL for Directory's comprehensive/targeted support elements. The actual loader, `Staging.Staging-to-FactOrganizationCounts_ComprehensiveAndTargetedSupport.StoredProcedure.sql`, does not read that table at all — it reads two differently-named tables, `Staging.K12SchoolComprehensiveSupportIdentificationType` and `Staging.K12SchoolTargetedSupportIdentificationType`, which have their own (non-stale-flagged) DDL in `Tables/Create/` and were not mentioned in the brief.
- Brief lists `Tables/Create/Staging.OrganizationSchoolIndicatorStatus.Table.sql` as relevant stale DDL for Directory. In fact `RDS.Migrate_OrganizationStatusCounts.StoredProcedure.sql` (the `organizationstatus` fact type's loader, covering FS199–FS202) reads no `Staging.*` table at all — it reads `dbo.K12SchoolIndicatorStatus`, `dbo.RefIndicatorStatusType`, and `dbo.RefIndicatorStatusCustomType`. `Staging.OrganizationSchoolIndicatorStatus` is used only by the CEDS IDS path (`Staging.Migrate_StagingToIDS_Organization.StoredProcedure.sql`) and index-maintenance utilities, never by the EDFacts/RDS path. The `organizationstatus` fact type has no `Staging`-schema seam — worth flagging for the Ed-Fi re-implementation since there is no CEDS-aligned landing table to replace here, only Generate's own `dbo` operational tables.
- Brief says (CTE notes): "Staging tables it reads: Not separately declared — trace `RDS.Migrate_StudentCounts` and `Staging.ProgramParticipationCTE`," and lists `Tables/Create/Staging.ProgramParticipationCTE.Table.sql` as relevant DDL. In fact the CTE-specific categorical data is loaded by `RDS.Migrate_DimCteStatuses.StoredProcedure.sql` (called from `RDS.Migrate_StudentCounts` when `@factTypeCode = 'cte'`), which reads `dbo.PersonProgramParticipation` joined to `dbo.ProgramParticipationCte`, `dbo.OrganizationProgramType`, `dbo.OrganizationPersonRole`, `dbo.RefNonTraditionalGenderStatus`, and `dbo.PersonStatus` — never `Staging.ProgramParticipationCTE`. Confirmed by grep: the only referrers of `Staging.ProgramParticipationCTE` in `generate.database` are the CEDS IDS path (`Staging.Migrate_StagingToIDS_ProgramParticipationCTE.StoredProcedure.sql`) and index-maintenance utilities. Same pattern as the Directory/organizationstatus contradiction above: this fact type's category data has no `Staging`-schema seam.
- Brief says (StudentCounts notes): "note it calls `exec [rds].[Empty_RDS] 'submission', 'studentcounts'` with two arguments, while `RDS.Empty_RDS` declares only one parameter — verify this yourself." Confirmed exactly: `generate.database/StoredProcedures/Create/App.Wrapper_Migrate_StudentCounts_to_RDS.StoredProcedure.sql@develop` line 43 calls `exec [rds].[Empty_RDS] 'submission', 'studentcounts'`; `generate.database/StoredProcedures/Create/RDS.Empty_RDS.StoredProcedure.sql@develop` line 1–2 declares `CREATE PROCEDURE [RDS].[Empty_RDS] @factTypeCode as varchar(50)` — one parameter only. This is a real arity mismatch that would raise a SQL Server error at call time. Not a contradiction of the brief — the brief was right — recorded here per the brief's own instruction.
- Brief says (StudentCounts notes): "`RDS.Create_Reports` has no `if @factTypeCode = 'submission'` branch. Verify this yourself and say so in the note." Confirmed: grepping `generate.database/StoredProcedures/Create/RDS.Create_Reports.StoredProcedure.sql@develop` for `submission` (case-insensitive) returns only `DataMigrationHistoryMessage` log strings prefixed `'Submission Reports - c###'` for other fact types' report codes — never an `if @factTypeCode = 'submission'` block. Not a contradiction — recorded per instruction.

---

## Directory

Fact type: `directory` (+ `organizationstatus`) | Fact table: `RDS.FactOrganizationCounts` (+ `RDS.FactOrganizationStatusCounts`) | Report codes: `c029`, `c035`, `c039`, `c103`, `c129`, `c130`, `c131`, `c163`, `c170`, `c190`, `c193`, `c196`, `c197`, `c198`, `c205`, `c206`, `c207`, `c199`, `c200`, `c201`, `c202`
File specs: FS029, FS035, FS039, FS103, FS129, FS130, FS131, FS163, FS170, FS190, FS193, FS196, FS197, FS198, FS205, FS206, FS207, FS199, FS200, FS201, FS202

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| SEA identifier | `Staging.StateDetail.SeaOrganizationIdentifierSea` | identifier | Direct | `edFi_stateEducationAgency.stateEducationAgencyId` | |
| LEA identifier | `Staging.K12Organization.LeaIdentifierSea` | identifier | Direct | `edFi_localEducationAgency.localEducationAgencyId` | |
| School identifier | `Staging.K12Organization.SchoolIdentifierSea` | identifier | Direct | `edFi_school.schoolId` | |
| Organization name | `Staging.K12Organization.NameOfInstitution` | identifier | Direct | `edFi_school.nameOfInstitution` | FS029/FS039 |
| Organization address | `Staging.OrganizationAddress` | identifier | Direct | `edFi_school.addresses` | FS029/FS039 |
| Organization phone | `Staging.OrganizationPhone` | identifier | Direct | `edFi_school.institutionTelephones` | FS029/FS039 |
| NCES ID, LEA | `Staging.K12Organization.LEAIdentifierNCES` | identifier | Derivable | from `edFi_localEducationAgency.identificationCodes[]`, filtered to the entry whose system descriptor is NCES | FS029 |
| NCES ID, school | `Staging.K12Organization.SchoolIdentifierNCES` | identifier | Derivable | from `edFi_school.identificationCodes[]`, filtered to the entry whose system descriptor is NCES | FS039 |
| Grades offered | `Staging.OrganizationGradeOffered.GradeOffered` | category: GRADESOFFERED | Direct | `edFi_school.gradeLevels` | FS039 |
| Charter school indicator | `Staging.K12Organization.School_CharterSchoolIndicator` | filter | Direct | `edFi_school.charterStatusDescriptor` | FS190/FS198 |
| Charter primary authorizer | `Staging.K12Organization.School_CharterPrimaryAuthorizer` | category: CHARTERAUTH | Absent | no authorizing-organization reference in core | FS190 |
| Charter secondary authorizer | `Staging.K12Organization.School_CharterSecondaryAuthorizer` | category: CHARTERAUTH | Absent | no authorizing-organization reference in core | FS190 |
| Charter management organization | `Staging.CharterSchoolManagementOrganization` | category: CHARTERMGMT | Absent | no management-organization property in core | FS196/FS197 |
| Charter contract ID | `Staging.K12Organization.CharterSchoolContractIdNumber` | identifier | Absent | no contract-identifier property in core | FS198 |
| School type | `Staging.K12Organization.SchoolTypeCode` | category: SCHOOLTYPE | Direct | `edFi_school.schoolTypeDescriptor` | FS129/FS130 |
| Magnet/special-program-emphasis status | `Staging.K12Organization.School_MagnetOrSpecialProgramEmphasisSchool` | category: MAGNET | Direct | `edFi_school.magnetSpecialProgramEmphasisSchoolDescriptor` | FS129/FS130 |
| National School Lunch Program status | `Staging.K12Organization.School_NationalSchoolLunchProgramStatus` | category: SCHOOLSTATUS | Absent | no core property | FS129/FS130 |
| Shared-time indicator | `Staging.K12Organization.School_SharedTimeIndicator` | category: SCHOOLSTATUS | Absent | no core property | FS129/FS130 |
| Virtual school status | `Staging.K12Organization.School_VirtualSchoolStatus` | category: SCHOOLSTATUS | Absent | no core property | FS129/FS130 |
| School dangerous status | `Staging.K12Organization.School_SchoolDangerousStatus` | category: SCHOOLSTATUS | Absent | no core property | FS129/FS130 |
| State poverty designation | `Staging.K12Organization.School_StatePovertyDesignation` | category: SCHOOLSTATUS | Absent | no core property | FS129/FS130 |
| Progress-toward-ELP indicator | `Staging.K12Organization.School_ProgressAchievingEnglishLanguageProficiencyIndicatorType` | category: ELPPROGRESS | Absent | no organization-level ELP-progress property in core | FS205/FS206 |
| Comprehensive support identification | `Staging.K12SchoolComprehensiveSupportIdentificationType` | category: CSI/TSI | Derivable | from `edFi_school.indicators[]`, a generic extensibility slot; CSI vocabulary is not built in | FS207/compsupport, not wrapper-called |
| Targeted support identification | `Staging.K12SchoolTargetedSupportIdentificationType` | category: CSI/TSI | Derivable | from `edFi_school.indicators[]`, a generic extensibility slot; TSI vocabulary is not built in | FS207/compsupport, not wrapper-called |
| Federal program code | `Staging.OrganizationFederalFunding.FederalProgramCode` | measure | Absent | `edFi_localEducationAgencyFederalFunds` has fixed named categories, not a generic program code | FS035/FS193 |
| Federal program funding allocation | `Staging.OrganizationFederalFunding.FederalProgramsFundingAllocation` | measure | Absent | same as above | FS035/FS193 |
| Title I parental-involvement reservation | `Staging.OrganizationFederalFunding.ParentalInvolvementReservationFunds` | measure | Absent | no matching field in core | FS193 |
| School-improvement funds | `RDS.FactOrganizationCounts.SchoolImprovementFunds` | measure | Direct | `edFi_localEducationAgencyFederalFunds.schoolImprovementAllocation` | FS035; hardcoded -1/NULL by `Staging-to-FactOrganizationCounts` |
| GFSA reporting status | `Staging.K12Organization.School_GunFreeSchoolsActReportingStatus` | category: GFSASTATUS | Direct | `edFi_localEducationAgencyAccountability.gunFreeSchoolsActReportingStatusDescriptor` | FS163, organizationstatus |
| McKinney-Vento subgrant recipient | `Staging.K12Organization.LEA_McKinneyVentoSubgrantRecipient` | category: MVSUBGRANT | Absent | no subgrant-recipient property in core | FS170, organizationstatus |
| LEA operational status | `RDS.DimLeas.LeaOperationalStatus` | category: OPSTATUS | Direct | `edFi_localEducationAgency.operationalStatusDescriptor` | |
| School operational status | `RDS.DimK12Schools.SchoolOperationalStatus` | category: OPSTATUS | Direct | `edFi_school.operationalStatusDescriptor` | |
| Reported-federally flag | `RDS.DimLeas.ReportedFederally` / `RDS.DimK12Schools.ReportedFederally` | filter | Absent | Generate-internal reporting-scope flag | |
| State-defined indicator status | `dbo.K12SchoolIndicatorStatus.IndicatorStatus` | category: state-defined status | Absent | SEA-custom, no fixed Ed-Fi equivalent | organizationstatus only; not sourced from `Staging` — see Contradictions |

---

## Staff

Fact type: `staff` | Fact table: `RDS.FactK12StaffCounts` | Report codes: `c059`, `c067`, `c070`, `c099`, `c112`, `c203`
File specs: FS059, FS067, FS070, FS099, FS112, FS203

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Staff identifier | `Staging.K12StaffAssignment.StaffMemberIdentifierState` | identifier | Direct | `edFi_staff.staffUniqueId` | |
| LEA identifier | `Staging.K12StaffAssignment.LeaIdentifierSea` | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId` | via assignment association's org reference |
| School identifier | `Staging.K12StaffAssignment.SchoolIdentifierSea` | organization | Direct | `edFi_school.schoolId` | via assignment association's org reference |
| Staff name & birthdate | `Staging.K12StaffAssignment.FirstName`, `.LastOrSurname`, `.MiddleName`, `.BirthDate` | identifier | Direct | `edFi_staff.firstName` + `.lastSurname` + `.middleName` + `.birthDate` | used as a DimPeople match key, not just descriptive |
| Full-time equivalency | `Staging.K12StaffAssignment.FullTimeEquivalency` | measure | Direct | `edFi_staffEducationOrganizationAssignmentAssociation.fullTimeEquivalency` | the measure for FS059/070/099/112/203 |
| Staff classification | `Staging.K12StaffAssignment.K12StaffClassification` | category: K12STAFFCLASS | Direct | `edFi_staffEducationOrganizationAssignmentAssociation.staffClassificationDescriptor` | FS059/FS203 |
| Special education staff category | `Staging.K12StaffAssignment.SpecialEducationStaffCategory` | category: SPECEDSTAFFCAT | Absent | no special-education staff sub-category property in core | FS099 |
| Title I program staff category | `Staging.K12StaffAssignment.TitleIProgramStaffCategory` | category: TITLEISTAFFCAT | Absent | no Title I staff-role property in core | |
| Special education age group taught | `Staging.K12StaffAssignment.SpecialEducationAgeGroupTaught` | category: AGEGROUP | Absent | no age-band-served property for staff in core | FS070/FS099/FS112 |
| EdFacts certification status | `Staging.K12StaffAssignment.EdFactsCertificationStatus` | category: CERTSTATUS | Absent | `credentialTypeDescriptor` names a credential type, not a certified/not-certified determination | FS070/FS099/FS112 |
| Special education teacher qualification status | `Staging.K12StaffAssignment.SpecialEducationTeacherQualificationStatus` | category: QUALSTATUS | Absent | no qualification-status property in core | FS070/FS099 |
| Paraprofessional qualification status | `Staging.K12StaffAssignment.ParaprofessionalQualificationStatus` | category: PARAQUALSTATUS | Absent | no paraprofessional-specific property in core | FS112 |
| Teaching credential type | `Staging.K12StaffAssignment.TeachingCredentialType` | category: CREDTYPE | Direct | `edFi_credential.teachingCredentialDescriptor`, via `staffEducationOrganizationAssignmentAssociation.credentialReference` | |
| Credential issuance date | `Staging.K12StaffAssignment.CredentialIssuanceDate` | measure | Direct | `edFi_credential.issuanceDate` | |
| Credential expiration date | `Staging.K12StaffAssignment.CredentialExpirationDate` | measure | Direct | `edFi_credential.expirationDate` | |
| Highly-qualified teacher indicator | `Staging.K12StaffAssignment.HighlyQualifiedTeacherIndicator` | category: HQSTATUS | Direct | `edFi_staff.highlyQualifiedTeacher` | |
| Teacher inexperienced status | `Staging.K12StaffAssignment.EdFactsTeacherInexperiencedStatus` | category: EXPSTATUS | Derivable | from `edFi_staff.yearsOfPriorTeachingExperience` compared to a state-defined threshold | |
| Teacher out-of-field status | `Staging.K12StaffAssignment.EDFactsTeacherOutOfFieldStatus` | category: OOFSTATUS | Absent | no out-of-field property in core | |
| Assignment start date | `Staging.K12StaffAssignment.AssignmentStartDate` | filter | Direct | `edFi_staffEducationOrganizationAssignmentAssociation.beginDate` | must span the child-count date |
| Assignment end date | `Staging.K12StaffAssignment.AssignmentEndDate` | filter | Direct | `edFi_staffEducationOrganizationAssignmentAssociation.endDate` | |
| Title III teacher status | `RDS.FactK12StaffCounts.TitleIIIStatusId` | category: TITLEIIISTATUS | Derivable | from `edFi_staffProgramAssociation.programReference` → `edFi_program.programTypeDescriptor` (Title III/Language Instruction) + `staffClassificationDescriptor` = Teacher | FS067; hardcoded -1 in `Staging-to-FactK12StaffCounts` — Generate itself has no populating source for this column |

---

## CTE

Fact type: `cte` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c082`, `c083`, `c132`, `c154`, `c155`, `c156`, `c158`, `c169`
File specs: FS082, FS083, FS132, FS154, FS155, FS156, FS158, FS169

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | shared `DimK12Students` load, ultimately `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_studentReference.studentUniqueId` | |
| LEA identifier | shared `DimLeas` load | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId` | |
| School identifier | shared `DimK12Schools` load | organization | Direct | `edFi_school.schoolId` | |
| CTE concentrator status | `dbo.ProgramParticipationCte.CteConcentrator` | category: CTESTATUS | Derivable | from `edFi_studentCTEProgramAssociation.programParticipationStatuses[].participationStatusDescriptor` — a generic status slot; concentrator/participant thresholds are state-defined | not from `Staging.ProgramParticipationCTE` — see Contradictions |
| CTE participant status | `dbo.ProgramParticipationCte.CteParticipant` | category: CTESTATUS | Derivable | same as above | not from `Staging.ProgramParticipationCTE` — see Contradictions |
| CTE completer | `dbo.ProgramParticipationCte.CteCompleter` | category: CTESTATUS | Direct | `edFi_studentAcademicRecordDiploma.cteCompleter` | |
| Single-parent / single-pregnant-woman status | `dbo.ProgramParticipationCte.SingleParentOrSinglePregnantWoman` | category: CTESUBPOP | Absent | no core property | FS155/FS156 |
| Displaced-homemaker indicator | `dbo.ProgramParticipationCte.DisplacedHomemakerIndicator` | category: CTESUBPOP | Absent | no core property | FS155/FS156 |
| Non-traditional gender status (participation) | `dbo.ProgramParticipationCte.RefNonTraditionalGenderStatusId` | category: CTENONTRAD | Direct | `edFi_studentCTEProgramAssociation.nonTraditionalGenderStatus` | FS155 |
| Non-traditional completion | `dbo.ProgramParticipationCte.CteNonTraditionalCompletion` | category: CTENONTRAD | Direct | `edFi_studentCTEProgramAssociation.nonTraditionalGenderStatus` | FS156 |
| Graduation-rate inclusion type | `dbo.ProgramParticipationCte.InclusionType` | category: CTEGRADINCL | Absent | no core property ties a CTE concentrator to graduation-rate-cohort inclusion | FS154 |
| LEP-Perkins status | `dbo.PersonStatus` filtered to `RefPersonStatusType.Code = 'Perkins LEP'` | category: LEPPERKINS | Absent | no core property distinguishes a Perkins-specific LEP status from general English-learner status | |
| CTE program entry date | `dbo.OrganizationPersonRole.EntryDate` | filter | Direct | `edFi_studentCTEProgramAssociation.beginDate` | |
| CTE program exit date | `dbo.OrganizationPersonRole.ExitDate` | filter | Direct | `edFi_studentCTEProgramAssociation.endDate` | FS082/FS083/FS158/FS169 use this to determine exiters |
| Section 1003 school-improvement funds | organization-level; routed via `Create_OrganizationReportData`, not the student-count path | measure | Absent | `edFi_localEducationAgencyFederalFunds` has fixed named categories, not a generic program-code/amount pair | `c132`; same gap as Directory's federal funding |

---

## DataPopulation

Fact type: `datapopulation` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `studentcount`, `studentsex`, `studentdisability`, `studentrace`, `studentsubpopulation` (no `c###` form)
File specs: None — UI-only data-quality summary, not an EDFacts submission

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_studentReference.studentUniqueId` | |
| LEA identifier | `Staging.K12Enrollment.LeaIdentifierSeaAccountability` | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId` | |
| School identifier | `Staging.K12Enrollment.SchoolIdentifierSea` | organization | Direct | `edFi_school.schoolId` | |
| Sex | `Staging.K12Enrollment.Sex` | category: SEX | Direct | `edFi_student.sexDescriptor` | duplicates Membership |
| Race/ethnicity (unduplicated) | `Staging.K12Enrollment.HispanicLatinoEthnicity`, `Staging.K12PersonRace` (via `RDS.vwUnduplicatedRaceMap`) | category: RACE | Direct | `edFi_studentEducationOrganizationAssociation.races[]` + `.hispanicLatinoEthnicity` | duplicates Membership |
| Grade level | `Staging.K12Enrollment.GradeLevel` | category: GRADELEVEL | Direct | `edFi_studentSchoolAssociation.entryGradeLevelDescriptor` | duplicates Membership |
| Primary IDEA disability type | `Staging.IdeaDisabilityType.IdeaDisabilityTypeCode` where `IsPrimaryDisability = 1` | category: IDEADISAB | Direct | `edFi_studentSpecialEducationProgramEligibilityAssociation.disabilities[]`, primary flag | duplicates ChildCount |
| Title I program status | `Staging.K12Organization.LEA_TitleIProgramType`, `.LEA_TitleIinstructionalService`, `.LEA_K12LeaTitleISupportService`, `.School_TitleIPartASchoolDesignation` | category: TITLEISTATUS | Direct | see TitleI for the element-level binding | LEA/school-level designation, not per-student participation |

Note: despite the `studentsubpopulation` report code, `Staging.Staging-to-FactK12StudentCounts_DataPopulation` hardcodes EL, homeless, migrant, foster-care, economically-disadvantaged, Title III, CTE, N-or-D, cohort, and attendance status to `-1` on every row — this procedure does not populate them. They are not listed as elements here because this domain's own code supplies no binding for them; they are populated only by other domains' fact procedures writing the same shared `RDS.FactK12StudentCounts` table.

---

## StudentCounts

Fact type: `submission` | Fact table: `RDS.FactK12StudentCounts` | Report codes: None — no `if @factTypeCode = 'submission'` branch exists in `RDS.Create_Reports`
File specs: None

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | not separately declared — resolved through the shared `Migrate_DimK12Students` load | identifier | Direct | `edFi_studentReference.studentUniqueId` | generic skeleton every fact type gets from `RDS.Migrate_StudentCounts` |
| LEA identifier | not separately declared — shared `DimLeas` load | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId` | |
| School identifier | not separately declared — shared `DimK12Schools` load | organization | Direct | `edFi_school.schoolId` | |

Note: a count-date filter is not listed as an element because which dimensions (if any) attach to the `submission` fact type is metadata-driven via `rds.DimFactType_DimensionTables`, and nothing in this cache confirms a count-date rule is registered for it — see the domain note.

---

## Homeless

Fact type: `homeless` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c118`, `c194`
File specs: FS118, FS194

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_studentReference.studentUniqueId` | |
| LEA identifier | `Staging.K12Enrollment.LeaIdentifierSeaAccountability` | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId` | |
| School identifier | `Staging.K12Enrollment.SchoolIdentifierSea` | organization | Direct | `edFi_school.schoolId` | |
| Homelessness status | `Staging.PersonStatus.HomelessnessStatus` | filter | Direct | presence of an `edFi_studentHomelessProgramAssociation` record spanning the count date | fact procedure requires `= 1` |
| Homeless primary nighttime residence type | `Staging.PersonStatus.HomelessNightTimeResidence` | category: NIGHTRESIDENCE | Direct | `edFi_studentHomelessProgramAssociation.homelessPrimaryNighttimeResidenceDescriptor` | distinct element from the homelessness flag — do not collapse |
| Homeless unaccompanied-youth status | `Staging.PersonStatus.HomelessUnaccompaniedYouth` | category: UNACCOMPANIED | Direct | `edFi_studentHomelessProgramAssociation.homelessUnaccompaniedYouth` | distinct element from the homelessness flag — do not collapse |
| Homeless serviced indicator | `Staging.PersonStatus.HomelessServicedIndicator` | category: SERVICED | Derivable | from `edFi_studentHomelessProgramAssociation.homelessProgramServices[]` non-empty, or the linked program's funding source being a McKinney-Vento subgrant | FS194-specific |
| IDEA indicator | `Staging.ProgramParticipationSpecialEducation.IDEAIndicator` | category: IDEADISAB | Direct | `edFi_studentSpecialEducationProgramEligibilityAssociation.ideaIndicator` | |
| Primary disability type | `Staging.IdeaDisabilityType.IdeaDisabilityTypeCode` where `IsPrimaryDisability = 1` | category: IDEADISAB | Direct | `edFi_studentSpecialEducationProgramEligibilityAssociation.disabilities[]`, primary flag | |
| English learner status | `Staging.PersonStatus.EnglishLearnerStatus` | category: ELSTATUS | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | |
| Migrant status | `Staging.PersonStatus.MigrantStatus` | category: MIGRANTSTATUS | Direct | presence of an `edFi_studentMigrantEducationProgramAssociation` record | |
| Race/ethnicity (unduplicated) | `Staging.K12Enrollment.HispanicLatinoEthnicity`, `Staging.K12PersonRace` | category: RACE | Direct | `edFi_studentEducationOrganizationAssociation.races[]` + `.hispanicLatinoEthnicity` | |
| Grade level | `Staging.K12Enrollment.GradeLevel` | category: GRADELEVEL | Direct | `edFi_studentSchoolAssociation.entryGradeLevelDescriptor` | |
| Age | `Staging.K12Enrollment.Birthdate` (via `RDS.Get_Age`) | category: AGE | Derivable | from `edFi_student.birthDate` vs. the count date | |
