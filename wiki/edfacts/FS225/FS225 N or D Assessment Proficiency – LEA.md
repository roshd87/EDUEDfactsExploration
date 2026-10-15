---
fs_id: FS225
title: "N or D Assessment Proficiency – LEA"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG871]
status_2025_26: Optional
status_2026_27: Inactive
generate_domains: [Assessments]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS225-v23.0--edfacts-fs225-23-0-dg871-n-or-d-assessment-proficiency-lea-v230-114547.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs225-23-0-dg871-n-or-d-assessment-proficiency-lea-v230-114547.docx"
sha256: 059a1862f69ac94a78e4827d388fcb4b9593254d03aa6a5c27dc32f7345619b3
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS225 — N or D Assessment Proficiency – LEA (v23.0)

> [!abstract] FS225 at a glance
> **Data groups:** DG871
> **EDPass status:** Optional in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** SEA, LEA, School
> **Reporting Period:** Testing Window - The period when the state administers state-wide academic assessments as described by ESEA
> **Type of count:** Once per academic subject
> **Zero counts:** When an academic subject is reported for an LEA, both values of proficiency status should be reported.
> **Categories:** Academic Subject (Assessment - no science), Proficiency Status
> **Data record:** 12 fields, 310 characters fixed-width
> **Generate domain:** [[Assessments]]
> **Business rules:** [[FS225 Business Rules]] (BRSI SY 2025-26)
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS225-v23.0--edfacts-fs225-23-0-dg871-n-or-d-assessment-proficiency-lea-v230-114547.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit EDFacts Data Group 871: N or D assessment proficiency table - LEA. The definition for this data group is:

> The number of students served by Title I, Part D, Subpart 2 of ESEA, as amended, who participated in a statewide assessment for mathematics and reading.

The data collected using this file specification are collected under the authority of the Elementary and Secondary Education Act of 1965 (ESEA), as amended by the Every Student Succeeds Act (ESSA).

The ED data stewarding office/s for this file: OESE/SSA/Title I, Part D

This file specification is optional.

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than any editorial changes listed in the document history on page ii, there have been no other changes to this file specification.

### Core Requirements for Submitting this File

The following table contains the reporting period, the education units included or excluded, the type of count, and zero count reporting.

**Table 2.2-1: Core Reporting Requirements**

|  | **SEA** | **LEA** | **School** |
|---|---|---|---|
| Reporting Period |  | Testing Window - The period when the state administers state-wide academic assessments as described by ESEA |  |
| Education units included |  | LEAs with programs and facilities funded by Title I, Part D, Subpart 2 |  |
| Education units <u>not</u> reported |  | LEAs that do not have programs or facilities funded by Title I, Part D, Subpart 2, for example, LEAs that have programs solely funded by Title I, Part A |  |
| Type of count |  | Once per academic subject |  |
| Zero counts |  | When an academic subject is reported for an LEA, both values of proficiency status should be reported. |  |
| Zero exceptions and<br>Not applicable |  |  |  |
| Missing |  | Use “-1” to report missing counts.<br>Use “MISSING” when a category is not available. |  |
| Related metadata survey |  |  |  |

Core Reporting Requirements

### Required Categories and Totals

The table below lists the combinations of the categories and totals that are expected to be submitted for the state and each LEA or school that should be included in the file.

- An “X” in the column indicates that the category value must be submitted when reporting that aggregation.

- The total indicator must be “N” (No).

The technical name of the data used in the file is: NDACACLEA

**Table 2.3–1: Required Categories and Totals**

| **Aggregation** | **Academic Subject (Assessment - no science)** | **Proficiency Status** | **Total Indicator** | **Comments** |
|---|---|---|---|---|
| **Category Set A** | X | X | N | Student Count by Academic Subject (Assessment - no science) by Proficiency Status |

Required Categories and Totals

### Categories and Permitted Values

This section contains the categories and permitted values used for submitting this file.

**DG871 - N or D assessment proficiency table - LEA:**

**Academic Subject (Assessment - no science)**

The description of the content or subject area of an assessment.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments** |
|----------------------------------|---------------------------------|--------------|
| M                                | Mathematics                     |              |
| RLA                              | Reading/language arts           |              |

**Proficiency Status**

An indication of whether scores were proficient or above.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                      |
|----------------------------------|---------------------------------|---------------------------------------------------|
| PROFICIENT                       | Attained proficiency            |                                                   |
| NOTPROFICIENT                    | Not proficient                  |                                                   |
| MISSING                          | Missing                         | Use when data are not available by this category. |

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

The questions in this section are based on the following statute and/or regulatory guidance: ESEA sections 1422, 1431 and 1432 (3).

**Which students should be reported in this file?**

Report only students who received Title I, Part D, Subpart 2 services during the reporting period.

**Are programs funded by Title I, Part A reported in this file?**

No. Do not report programs funded solely through Title I, Part A.

**Which programs may receive Title I, Part D Subpart 2 funds?**

Title I, Part D Subpart 2 subgrants are awarded to local educational agencies with high numbers or percentages of children and youth residing in locally operated (including county operated) correctional facilities for children and youth (including facilities involved in community day programs).

**What assessments should be reported?**

Report any assessment reported in FS175 (Academic Achievement in Mathematics) and any assessment reported in FS178 (Academic Achievement in Reading / Language Arts), including alternate assessments based on alternate academic achievement standards. Do not include the results of the Annual English language proficiency assessment taken in lieu of the statewide reading / language arts assessment.

**What if my state assigns non-participants to the lowest level of proficiency?**

Those students are not reported in these files (for reporting academic achievement results).

**Are students who were not enrolled for the full academic year included in this file?**

Yes. Include both students who were enrolled for the full academic year <u>and</u> those who were not enrolled for the full academic year in this file.

### Definitions

See the [EDFacts Workbook](https://www.ed.gov/data/edfacts-initiative/edfacts-resources/edfacts-workbook) for the standard definitions. The following definitions support this file.

***Locally operated correctional facility*** means a facility in which persons are confined as a result of a conviction for a criminal offense, including persons under 21 years of age. The term also includes a local public or private institution and community day program or school not operated by the State that serves delinquent children and youth.

**Community day program**— a regular program of instruction provided by a State agency at a community day school operated specifically for neglected or delinquent children and youth.

**Regular program of instruction** means an educational program (not beyond grade 12) in an institution or a community day program for neglected or delinquent children that consists of classroom instruction in basic school subjects such as reading, mathematics, and career and technical education, and that is supported by non-Federal funds. Neither the manufacture of goods within the institution nor activities related to institutional maintenance are considered classroom instruction.

**At–risk**—The term “at-risk”, when used with respect to a child, youth, or student, means a school aged individual who is at-risk of academic failure, dependency adjudication, or delinquency adjudication, has a drug or alcohol problem, is pregnant or is a parent, has come into contact with the juvenile justice system or child welfare system in the past, is at least 1 year behind the expected grade level for the age of the individual, is an English learner, is a gang member, has dropped out of school in the past, or has a high absenteeism rate at school.

## File Naming Convention

The following file naming convention is to help identify files to provide technical assistance.

A maximum of 25 characters (including the file extension) is allowed for the file name.

The following is the naming convention for file submissions:

> sslev**filename**vvvvvvv.ext

**Table 3.0-1: File Naming Convention**

| **Where** | **Means** | **Limit in characters** |
|---|---|---|
| ss | USPS State Abbreviation | 2 |
| lev | Abbreviation for level:<br>•<br>LEA for a Local Education Agency level | 3 |
| filename | **NDACACLEA** | 9 |
| vvvvvvv | Alphanumeric string designated by the SEA to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| .ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 4 |

File Naming Convention

## Fixed or Delimited Files

This section describes the fixed file and delimited file specifications. The fixed file and delimited files contain a header record followed by data records. The file type is specified in the header record.

The “Pop” column in the header and data records is coded as follows:

> M - Mandatory, this field must always be populated
>
> A - This field is populated in accordance with table 2.3-1 “Required Categories and Totals”
>
> O - Optional, data in this field are optional

### Header Record Definition

The header record is required and is the first record in every file submitted to EDPass. The purpose of the header record is to provide information as to the file type, number of data records in the file, file name, file identifier, and file reporting period.

**Table 4.1–1: Header Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **LEA ND ASSESSMENT PROFICIENCY LEA** |
| Total Records in File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 303 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 430 | 1 |  | M |  |  |

Header Record

Below is an example of a header record.

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | LEA ND ASSESSMENT PROFICIENCY LEA,15,euleaNDACACLEAv000001.csv,characters to identify file,2026-2027,¶                    |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide counts for the specified category sets, subtotals and education unit totals.

**Table 4.2–1: Data Records**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier<br>(State) | 15 | 14 | String | M | The identifier assigned to a local education agency (LEA) by the state education agency (SEA). Also known as State LEA identification number (ID). This data element cannot be updated through this file. |  |
| Filler | 29 | 20 | String | M | Leave filler field blank |  |
| Table Name | 49 | 20 | String | M | See technical name in Section 2.3 Required Categories and Totals. | **NDACACLEA** |
| Academic Subject (Assessment - no science) | 69 | 15 | String | A | The description of the content or subject area of an assessment. | **M** – Mathematics<br>**RLA** – Reading/language arts |
| Proficiency Status | 84 | 15 | String | A | An indication of whether scores were proficient or above. | **PROFICIENT** – Attained proficiency<br>**NOTPROFICIENT** – Not proficient<br>**MISSING** |
| Total Indicator | 99 | 1 | String | M | An indicator that defines the count level – see table 2.3-1 Required Categories and Totals | **N** – Specifies category set |
| Explanation | 100 | 200 | String | O | Text field for state use. |  |
| Student Count | 300 | 10 | Integer | M |  |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 310 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit. See table 2.3-1.

**Table 4.2–2: Data Record Examples – LEA level**

| **Aggregation** | **Example**                                                                                                                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Format          | File Record Number,State Code,State Agency Number,LEA Identifier (State),Filler,Table Name,Academic Subject (Assessment - no science),Proficiency Status, Total Indicator,Explanation,Student Count,Carriage Return / Line Feed (CRLF) |
| Example         | 6,80,01,00605EUPHORIA,,NDACACLEA,RLA,NOTPROFICIENT,N,,100¶                                                                                                                                                                             |

## Document History

| **Version Number** | **Date**       | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |                | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | September 2026 | Updated for SY 2026-27:                                                                 |
