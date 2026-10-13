# Worker 1 element inventory

Domains: ChildCount, Exiting, Discipline, Assessments, SPPAPR, Other

## Contradictions found

- Brief said (Exiting): "The reportable element is the exit reason — `Staging.K12Enrollment.ExitOrWithdrawalType` mapped through `Staging.SourceSystemReferenceData`." The source disagrees: `Staging.K12Enrollment.ExitOrWithdrawalType` does not appear anywhere in `Staging.Staging-to-FactK12StudentCounts_Exiting.StoredProcedure.sql` or `Debug.vwExiting_StagingTables.View.sql`. The actual exit-reason element is `Staging.ProgramParticipationSpecialEducation.SpecialEducationExitReason`, translated via `Staging.SourceSystemReferenceData` (`TableName = 'RefSpecialEducationExitReason'`) into `rds.DimIdeaStatuses.SpecialEducationExitReasonCode` / `...EdFactsCode` (see `generate.database/Views/Create/RDS.vwDimIdeaStatuses.View.sql@develop`). `ExitOrWithdrawalType` is the general K12Enrollment exit code used by Membership/Dropout-family reporting, not by the IDEA Exiting fact procedure.
- Brief said (Other): "`studentfederalprogramsparticipation` and `studentmultifedprogsparticipation` cross-tabulate participation across Title I, Title III, MEP, NorD and special education." The source's fixed `@reportCounts` schema in `generate.database/StoredProcedures/Create/RDS.Create_StudentFederalProgramsReportData.StoredProcedure.sql@develop` (lines ~236–244) declares these cross-tab columns instead: `HOMELESSNESSSTATUS`, `ENGLISHLEARNERSTATUS`, `MIGRANTSTATUS`, `CTEPROGRAM`, `ELIGIBILITYSTATUSFORSCHOOLFOODSERVICEPROGRAM`, `TITLEIIIIMMIGRANTPARTICIPATIONSTATUS`, `SECTION504STATUS`, `FOSTERCAREPROGRAM`, `TITLEISCHOOLSTATUS`, plus `IDEAINDICATOR` used only as a filter (`WDIS`/`WODIS`) and explicitly excluded from the dimension list. No `NorD`/neglected-or-delinquent column, filter, or string appears anywhere in that procedure (`grep -i "nord\|neglected"` returns nothing) — Section 504, foster care, and school-food-service are cross-tabbed instead of NorD.
- Brief said (worker-wide, via the "Category set role" instructions and echoed by `wiki/components/App-Metadata-Layer.md`): a category's `<CATEGORYCODE>` looks like "e.g., RACE, SEX, AGE, IDEADISAB, ELSTATUS". The source disagrees on two counts, checked against the full 260-row dump in `generate.database/Metadata/App.Categories.Metadata.sql@develop`: (1) **`IDEADISAB` is not a `CategoryCode` at all** — it is `App.TableTypes.TableTypeAbbrv = 'IDEADISAB'` ("Children with Disabilities (IDEA) School Age Tables", a file-spec grouping, `generate.database/Metadata/App.TableTypes.Metadata.sql@develop` line 238), a different metadata table with a different meaning; it only appears to "exist" elsewhere because it string-matches inside `IdeaDisabilityType`/`DimIdeaDisabilityTypes` identifiers. The real disaggregation codes are `DISABCATIDEA` ("Disability Category (IDEA)"), `DISABSTATIDEA` ("Disability Status (IDEA)"), and file-spec-specific variants like `DISABCATIDEAEXIT` ("Disability Category (IDEA) Exiting"). (2) **Generic `RACE`/`AGE`/`ELSTATUS` codes do not exist either** — ED's own EDENDB category list (which this file mirrors verbatim, unfiltered by report code) names every category with a purpose suffix, e.g. `AGEEXITSPED` ("Age (Exiting)"), not `AGE`; `SEX` exists as literally `'SEX'` but only meaning "Sex (Membership)"; no `RACE` or `ELSTATUS` row exists under any spelling. Below, `category: RACE`/`SEX`/`AGE`/`ELSTATUS` are used as descriptive role labels matching this brief's own example vocabulary, not verified literal `CategoryCode` values — `App.Category_Dimensions` and `App.CategorySet_Categories` (the tables that would pin an exact code to a specific report) have no seed script in `Metadata/` to check them against (confirmed in `wiki/components/App-Metadata-Layer.md`). Only `DISABCATIDEA`, `DISABSTATIDEA`, `DISABCATIDEAEXIT`, `AGEEXITSPED`, and `BASISEXIT` below are verified literal codes.

---

## ChildCount

Fact type: `childcount` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c002`, `c089`, `yeartoyearenvironmentcount`, `yeartoyearchildcount`, `yeartoyearremovalcount`, `studentssummary`
File specs: FS002, FS089

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_student.studentUniqueId` | |
| LEA identifier | `Staging.K12Enrollment.LEAIdentifierSeaAccountability` | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId` | |
| School identifier | `Staging.K12Enrollment.SchoolIdentifierSea` | organization | Direct | `edFi_school.schoolId` | |
| Age at count date | `Staging.K12Enrollment.Birthdate` | category: AGE | Derivable | from `edFi_student.birthDate` computed as of the count date | Count date itself comes from `App.ToggleQuestions/ToggleResponses` ('CHDCTDTE'), not from staging |
| Sex | `Staging.K12Enrollment.Sex` | category: SEX | Direct | `edFi_studentEducationOrganizationAssociation.sexDescriptor` | |
| Race/ethnicity (unduplicated) | `Staging.K12PersonRace.RaceType`, `Staging.K12Enrollment.HispanicLatinoEthnicity` | category: RACE | Direct | `edFi_studentEducationOrganizationAssociationRace.raceDescriptor` + `.hispanicLatinoEthnicity` | 7-category unduplicated bucketing is Generate-side logic regardless of source standard |
| IDEA indicator | `Staging.ProgramParticipationSpecialEducation.IdeaIndicator` | filter | Direct | `edFi_studentSpecialEducationProgramEligibilityAssociation.ideaIndicator` | |
| IDEA educational environment | `Staging.ProgramParticipationSpecialEducation.IDEAEducationalEnvironmentForSchoolAge` / `...ForEarlyChildhood` | category: IDEAEDUCENV | Direct | `edFi_studentSpecialEducationProgramAssociation.specialEducationSettingDescriptor` | Generate splits school-age vs. early-childhood columns; Ed-Fi uses one descriptor |
| Primary disability type | `Staging.IdeaDisabilityType.IdeaDisabilityTypeCode` where `IsPrimaryDisability = 1` | category: DISABCATIDEA | Derivable | `edFi_studentSpecialEducationProgramAssociationDisability.disabilityDescriptor` where `orderOfDisability = 1` | |
| English learner status | `Staging.PersonStatus.EnglishLearnerStatus` | category: ELSTATUS | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | |
| Grade level | `Staging.K12Enrollment.GradeLevel` | filter | Direct | `edFi_studentSchoolAssociation.entryGradeLevelDescriptor` | Drives the age-5/PK inclusion rule for C002 |
| Enrollment span | `Staging.K12Enrollment.EnrollmentEntryDate` / `EnrollmentExitDate` | filter | Derivable | from `edFi_studentSchoolAssociation.entryDate` + `.exitWithdrawDate` — enrolled if the count date falls in the span | |
| LEA/school operational status | `Staging.K12Organization.LEA_OperationalStatus` / `School_OperationalStatus` | filter | Direct | `edFi_school.operationalStatusDescriptor` / `edFi_localEducationAgency.operationalStatusDescriptor` | C002 only |
| LEA/school federal-reporting flag | `Staging.K12Organization.LEA_IsReportedFederally` / `School_IsReportedFederally` | filter | Absent | no core boolean marks federal-reporting inclusion | C002 only |
| Developmental-delay age-band answer | `App.ToggleResponses` for `EmapsQuestionAbbrv = 'CHDCTAGEDD'` | filter | Absent | SEA policy answer, not a student/org data element | Excludes `DD` students outside the SEA's answered ages, C002 only |
| Student count | one row per matched student | measure | Derivable | count of matched rows; not a stored element | |

---

## Exiting

Fact type: `exiting` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `c009`, `exitspecialeducation`, `yeartoyearexitcount`
File specs: FS009

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.K12Enrollment.StudentIdentifierState` | identifier | Direct | `edFi_student.studentUniqueId` | |
| LEA identifier | `Staging.K12Enrollment.LEAIdentifierSeaAccountability` | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId` | |
| School identifier | `Staging.K12Enrollment.SchoolIdentifierSea` | organization | Direct | `edFi_school.schoolId` | |
| Exit date | `Staging.ProgramParticipationSpecialEducation.ProgramParticipationEndDate` | filter | Direct | `edFi_studentSpecialEducationProgramAssociation.specialEducationExitDate` | Required not null; drives the reporting-period and age-reference-date logic |
| Age at exit | `Staging.K12Enrollment.Birthdate` | category: AGEEXITSPED | Derivable | from `edFi_student.birthDate` computed as of the exit date | |
| Sex | `Staging.K12Enrollment.Sex` | category: SEX | Direct | `edFi_studentEducationOrganizationAssociation.sexDescriptor` | |
| Race/ethnicity (unduplicated) | `Staging.K12PersonRace.RaceType`, `Staging.K12Enrollment.HispanicLatinoEthnicity` | category: RACE | Direct | `edFi_studentEducationOrganizationAssociationRace.raceDescriptor` + `.hispanicLatinoEthnicity` | |
| Exit reason | `Staging.ProgramParticipationSpecialEducation.SpecialEducationExitReason` | category: BASISEXIT | Direct | `edFi_studentSpecialEducationProgramAssociation.specialEducationExitReasonDescriptor` | Descriptor value-set coverage of IDEA-specific reasons not verifiable from swagger alone |
| Primary disability type | `Staging.IdeaDisabilityType.IdeaDisabilityTypeCode` where `IsPrimaryDisability = 1` | category: DISABCATIDEAEXIT | Derivable | `edFi_studentSpecialEducationProgramAssociationDisability.disabilityDescriptor` where `orderOfDisability = 1` | |
| English learner status | `Staging.PersonStatus.EnglishLearnerStatus` | category: ELSTATUS | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | |
| IDEA indicator (eligibility gate) | `Staging.ProgramParticipationSpecialEducation.IdeaIndicator` | filter | Direct | `edFi_studentSpecialEducationProgramEligibilityAssociation.ideaIndicator` | Must resolve to `IdeaIndicatorCode = 'Yes'` |
| Student count | one row per matched exit | measure | Derivable | count of matched rows; not a stored element | |

---

## Discipline

Fact type: `discipline` | Fact table: `RDS.FactK12StudentDisciplines` | Report codes: `c005`, `c006`, `c007`, `c086`, `c088`, `c143`, `c144`, `studentdiscipline`, `indicator4a`, `indicator4b`, `disciplinaryremovals`
File specs: FS005, FS006, FS007, FS086, FS088, FS143, FS144

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.Discipline.StudentIdentifierState` | identifier | Direct | `edFi_student.studentUniqueId` | |
| LEA identifier | `Staging.Discipline.LeaIdentifierSeaAccountability` | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId` | |
| School identifier | `Staging.Discipline.SchoolIdentifierSea` | organization | Direct | `edFi_school.schoolId` | |
| Incident identifier | `Staging.Discipline.IncidentIdentifier` | identifier | Direct | `edFi_disciplineIncident.incidentIdentifier` | Incident-level, secondary key |
| Disciplinary action start date | `Staging.Discipline.DisciplinaryActionStartDate` | filter | Direct | `edFi_disciplineAction.disciplineDate` | Anchors every effective-dated join |
| Duration of disciplinary action | `Staging.Discipline.DurationOfDisciplinaryAction` | measure | Direct | `edFi_disciplineAction.disciplineActionLength` | Also `.actualDisciplineActionLength`; stored directly on the fact row (decimal days), not a dimension |
| Disciplinary action taken | `Staging.Discipline.DisciplinaryActionTaken` | category: action type | Direct | `edFi_disciplineActionDiscipline.disciplineDescriptor` | Feeds FS006 |
| IDEA interim removal | `Staging.Discipline.IdeaInterimRemoval` | category: interim removal | Absent | no interim-alternative-educational-setting concept in core Ed-Fi | Feeds FS005 |
| IDEA interim removal reason | `Staging.Discipline.IdeaInterimRemovalReason` | category: interim removal reason | Absent | no interim-alternative-educational-setting concept in core Ed-Fi | Feeds FS007 |
| Discipline method for children with disabilities | `Staging.Discipline.DisciplineMethodOfCwd` | category: CWD removal setting | Derivable | from `disciplineDescriptor` plus an active `edFi_studentSpecialEducationProgramAssociation` on the same date | Feeds FS088/FS143; no CWD-specific split field in Ed-Fi |
| Educational services after removal | `Staging.Discipline.EducationalServicesAfterRemoval` | category: services during removal | Absent | no property represents continued-service status during/after a removal | Feeds FS144 |
| Firearm/weapon type | `Staging.Discipline.FirearmType` | category: firearm type | Direct | `edFi_disciplineIncidentWeapon.weaponDescriptor` | Feeds FS086 (all students, not IDEA-gated) |
| Firearm discipline method | `Staging.Discipline.DisciplineMethodFirearm`, `.IDEADisciplineMethodFirearm` | category: firearm discipline method | Derivable | same derivation as CWD method, scoped to incidents with a weapon association | Feeds FS086 |
| Primary disability type | `Staging.IdeaDisabilityType.IdeaDisabilityTypeCode` where `IsPrimaryDisability = 1` | category: DISABCATIDEA | Derivable | `edFi_studentSpecialEducationProgramAssociationDisability.disabilityDescriptor` where `orderOfDisability = 1` | |
| IDEA indicator | `Staging.ProgramParticipationSpecialEducation.IdeaIndicator` | filter | Direct | `edFi_studentSpecialEducationProgramEligibilityAssociation.ideaIndicator` | Gates six of seven specs; FS086 is not IDEA-gated |
| Race/ethnicity (unduplicated) | `Staging.K12PersonRace.RaceType`, `Staging.K12Enrollment.HispanicLatinoEthnicity` | category: RACE | Direct | `edFi_studentEducationOrganizationAssociationRace.raceDescriptor` + `.hispanicLatinoEthnicity` | |
| Sex | `Staging.K12Enrollment.Sex` | category: SEX | Direct | `edFi_studentEducationOrganizationAssociation.sexDescriptor` | |
| Age at count date | `Staging.K12Enrollment.Birthdate` | category: AGE | Derivable | from `edFi_student.birthDate` | |
| Grade level | `Staging.K12Enrollment.GradeLevel` | filter | Direct | `edFi_studentSchoolAssociation.entryGradeLevelDescriptor` | |
| English learner status | `Staging.PersonStatus.EnglishLearnerStatus` | category: ELSTATUS | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | |
| Discipline count | one row per matched discipline action | measure | Derivable | count of matched rows; not a stored element | |

---

## Assessments

Fact type: `assessment` | Fact table: `RDS.FactK12StudentAssessments` (+ `RDS.BridgeK12StudentAssessmentRaces`, `RDS.BridgeK12StudentAssessmentAccommodations`) | Report codes: `c050`, `c113`, `c125`, `c126`, `c137`, `c138`, `c139`, `c142`, `c157`, `c175`, `c178`, `c179`, `c185`, `c188`, `c189`, `c224`, `c225`, `stateassessmentsperformance`, `yeartoyearprogress`, `yeartoyearattendance`
File specs: FS175, FS178, FS179, FS185, FS188, FS189, FS224, FS225

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `Staging.AssessmentResult.StudentIdentifierState` | identifier | Direct | `edFi_student.studentUniqueId` | |
| LEA identifier | `Staging.AssessmentResult.LEAIdentifierSeaAccountability` | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId` | |
| School identifier | `Staging.AssessmentResult.SchoolIdentifierSea` | organization | Direct | `edFi_school.schoolId` | |
| Assessment identifier/title | `Staging.Assessment.AssessmentIdentifier`, `.AssessmentTitle` | identifier | Direct | `edFi_assessment.assessmentIdentifier` / `.assessmentTitle` | Identifies the instrument, not the student |
| Academic subject | `Staging.Assessment.AssessmentAcademicSubject` | category: subject | Direct | `edFi_assessmentAcademicSubject.academicSubjectDescriptor` | |
| Assessment type / type administered | `Staging.Assessment.AssessmentType`, `.AssessmentTypeAdministered`, `.AssessmentTypeAdministeredToEnglishLearners` | category: assessment type | Derivable | `edFi_assessment.assessmentCategoryDescriptor` plus accommodations/registration context | |
| Administration dates | `Staging.AssessmentResult.AssessmentAdministrationStartDate`, `.AssessmentAdministrationFinishDate` | filter | Direct | `edFi_studentAssessment.administrationDate` / `.administrationEndDate` | School-year and enrollment-span anchor |
| Grade level when assessed | `Staging.K12Enrollment.GradeLevel` | category: grade level | Direct | `edFi_studentAssessment.whenAssessedGradeLevelDescriptor` | |
| Assessment performance level | `Staging.AssessmentResult.AssessmentPerformanceLevelIdentifier` (+ label) | category: performance level | Direct | `edFi_studentAssessmentPerformanceLevel.performanceLevelDescriptor` | Load-bearing for C224/C225 PROFICIENT/NOTPROFICIENT, itself driven by SEA-configured `App.ToggleAssessments.ProficientOrAboveLevel` |
| Raw score value | `Staging.AssessmentResult.ScoreValue` | measure | Direct | `edFi_studentAssessmentScoreResult.result` + `.resultDatatypeTypeDescriptor` | Scale/percentile/T/Z/ACT/SAT columns exist on the fact table but are hardcoded -1, unpopulated |
| Participation status | `Staging.AssessmentResult.AssessmentRegistrationParticipationIndicator`, `.ReasonNotCompleting`, `.ReasonNotTested` | filter | Direct | `edFi_studentAssessment.reasonNotTestedDescriptor` | Participation itself is Derivable from whether a scored record exists |
| Race/ethnicity (many-to-many) | `Staging.K12PersonRace.RaceType`, `Staging.K12Enrollment.HispanicLatinoEthnicity` | category: RACE | Direct | `edFi_studentEducationOrganizationAssociationRace.raceDescriptor` + `.hispanicLatinoEthnicity` | |
| Sex | `Staging.K12Enrollment.Sex` | category: SEX | Direct | `edFi_studentEducationOrganizationAssociation.sexDescriptor` | |
| IDEA indicator | `Staging.ProgramParticipationSpecialEducation.IdeaIndicator` | category: DISABSTATIDEA | Direct | `edFi_studentSpecialEducationProgramEligibilityAssociation.ideaIndicator` | |
| English learner status | `Staging.PersonStatus.EnglishLearnerStatus` | category: ELSTATUS | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | |
| Economically disadvantaged / foster care status | `Staging.PersonStatus.EconomicDisadvantageStatus`, `.ProgramType_FosterCare` | category: various | Derivable | `edFi_studentEducationOrganizationAssociationStudentCharacteristic.studentCharacteristicDescriptor` | Generic bucket; neither has a dedicated core property |
| Migrant / homeless / military-connected status | `Staging.PersonStatus.MigrantStatus`, `.HomelessnessStatus`, `.MilitaryConnectedStudentIndicator` | category: various | Direct | presence of `edFi_studentMigrantEducationProgramAssociation` / `edFi_studentHomelessProgramAssociation` / `edFi_studentEducationOrganizationAssociation.supporterMilitaryConnectionDescriptor` | |
| Neglected-or-delinquent status + subpart | `Staging.ProgramParticipationNorD.NeglectedOrDelinquentStatus`, `.NeglectedOrDelinquentProgramEnrollmentSubpart` | category: NORD subpart | Direct | `edFi_studentNeglectedOrDelinquentProgramAssociation.neglectedOrDelinquentProgramDescriptor` | Subpart 1 vs. 2 is exactly the C224/C225 split |
| Accommodation (many-to-many) | `RDS.BridgeK12StudentAssessmentAccommodations` | category: accommodation | Direct | `edFi_studentAssessmentAccommodation.accommodationDescriptor` | Gated on `AssessmentTypeAdministeredCode = 'REGASSWACC'` |
| Assessment count | one row per matched student/assessment/result | measure | Derivable | count of matched rows; not a stored element | |

---

## SPPAPR

Fact type: `sppapr` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `indicator9`, `indicator10`
File specs: None — IDEA SPP/APR indicators, submitted separately from EDFacts

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Student identifier | `RDS.DimPeople` (from `Staging.K12Enrollment`, via shared dim loader) | identifier | Direct | `edFi_student.studentUniqueId` | No dedicated Staging-to-Fact* procedure; reads only already-populated RDS dims |
| LEA identifier | `RDS.DimLeas` (from `Staging.K12Organization`, via shared dim loader) | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId` | |
| IDEA indicator | `RDS.DimIdeaStatuses` (from `Staging.ProgramParticipationSpecialEducation.IdeaIndicator`) | filter | Direct | `edFi_studentSpecialEducationProgramEligibilityAssociation.ideaIndicator` | |
| Primary disability type | `RDS.DimIdeaDisabilityTypes` (from `Staging.IdeaDisabilityType.IdeaDisabilityTypeCode`, `IsPrimaryDisability = 1`) | category: DISABCATIDEA | Derivable | `edFi_studentSpecialEducationProgramAssociationDisability.disabilityDescriptor` where `orderOfDisability = 1` | Indicator10 only |
| Race/ethnicity | `RDS.DimRaces` (from `Staging.K12PersonRace.RaceType`, `Staging.K12Enrollment.HispanicLatinoEthnicity`) | category: RACE | Direct | `edFi_studentEducationOrganizationAssociationRace.raceDescriptor` + `.hispanicLatinoEthnicity` | |
| Disproportionate-representation ratio | not a stored column; computed at report-generation time | measure | Absent | a computed policy metric; no standard stores it directly | Percent of LEAs, not a headcount |

---

## Other

Fact type: `other` | Fact table: `RDS.FactK12StudentCounts` | Report codes: `studentfederalprogramsparticipation`, `studentmultifedprogsparticipation`, `edenvironmentdisabilitiesage3-5`, `edenvironmentdisabilitiesage6-21`
File specs: None — cross-program analysis reports, not EDFacts submissions

| Element | Staging source | Category set role | Ed-Fi verdict | Ed-Fi binding | Note |
|---|---|---|---|---|---|
| Organization identifiers (SEA/LEA) | `RDS.Dim*` (from `Staging.K12Organization`, via shared dim loaders) | organization | Direct | `edFi_localEducationAgency.localEducationAgencyId` / `edFi_school.schoolId` | |
| Title I school status | see TitleI domain (not in this worker's set) | category: TITLEISCHOOLSTATUS | Direct | presence of `edFi_studentTitleIPartAProgramAssociation` | |
| Title III immigrant participation status | see Immigrant domain (not in this worker's set) | category: TITLEIIIIMMIGRANTPARTICIPATIONSTATUS | Absent | no "immigrant" property or schema anywhere in core Ed-Fi 5.2.0 | |
| Migrant status | see MigrantEducationProgram domain (not in this worker's set) | category: MIGRANTSTATUS | Direct | presence of `edFi_studentMigrantEducationProgramAssociation` | |
| CTE program participation | see CTE domain (not in this worker's set) | category: CTEPROGRAM | Direct | presence of `edFi_studentCTEProgramAssociation` | |
| School food service eligibility (NSLP) | `Staging.PersonStatus` (column outside this domain's assigned reads) | category: ELIGIBILITYSTATUSFORSCHOOLFOODSERVICEPROGRAM | Direct | presence of `edFi_studentSchoolFoodServiceProgramAssociation` | |
| Section 504 status | `Staging.PersonStatus` (column outside this domain's assigned reads) | category: SECTION504STATUS | Direct | presence of `edFi_studentSection504ProgramAssociation` | |
| Foster care status | `Staging.PersonStatus.ProgramType_FosterCare` | category: FOSTERCAREPROGRAM | Derivable | `edFi_studentEducationOrganizationAssociationStudentCharacteristic.studentCharacteristicDescriptor` | Generic bucket, no dedicated core property |
| Homelessness status | see Homeless domain (not in this worker's set) | category: HOMELESSNESSSTATUS | Direct | presence of `edFi_studentHomelessProgramAssociation` | |
| English learner status | `Staging.PersonStatus.EnglishLearnerStatus` | category: ELSTATUS | Direct | `edFi_studentEducationOrganizationAssociation.limitedEnglishProficiencyDescriptor` | |
| IDEA indicator | `Staging.ProgramParticipationSpecialEducation.IdeaIndicator` | filter | Direct | `edFi_studentSpecialEducationProgramEligibilityAssociation.ideaIndicator` | `WDIS`/`WODIS`; excluded from the cross-tab dimension list itself |
| IDEA educational environment (age 3-5 / 6-21) | same as ChildCount | category: IDEAEDUCENV | Direct | `edFi_studentSpecialEducationProgramAssociation.specialEducationSettingDescriptor` | Pivoted by age band |
| Primary disability type | same as ChildCount | category: DISABCATIDEA | Derivable | `edFi_studentSpecialEducationProgramAssociationDisability.disabilityDescriptor` where `orderOfDisability = 1` | |
| Student count | one row per matched combination | measure | Derivable | count of matched rows; not a stored element | |
