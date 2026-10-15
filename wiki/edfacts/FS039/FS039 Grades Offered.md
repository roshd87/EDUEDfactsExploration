---
fs_id: FS039
title: "Grades Offered"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG18]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [Directory]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS039-v23.0--edfacts-fs039-23-0-dg18-grades-offered-v230-114416.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs039-23-0-dg18-grades-offered-v230-114416.docx"
sha256: 556762b02e811b10b79dd524ecbaf7ae3fe9c6045614321d8abede38f4fa6456
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS039 — Grades Offered (v23.0)

> [!abstract] FS039 at a glance
> **Data groups:** DG18
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** SEA, LEA, School
> **Reporting Period:** Oct 1 - October 1 or the closest school day
> **Categories:** Grades Offered
> **Data record:** 10 fields, 283 characters fixed-width
> **Generate domain:** [[Directory]]
> **Business rules:** [[FS039 Business Rules]] (BRSI SY 2025-26)
> **Metadata guides:** [[CCD Grades Offered Metadata User Guide]]
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS039-v23.0--edfacts-fs039-23-0-dg18-grades-offered-v230-114416.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit EDFacts Data Group 18: Grades offered. The definition for this data group is:

> The grade level(s) offered by the school or district.

The data collected using this file specification are collected under the authority of the Education Sciences Reform Act (ESRA) and are used in the Non-Fiscal Survey of the Common Core of Data (CCD).

The ED data stewarding office/s for this file: NCES/CCD

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than any editorial changes listed in the document history on page ii, there have been no other changes to this file specification.

### Core Requirements for Submitting this File

The following table contains the reporting period, the education units included or excluded, the type of count, and zero count reporting.

**2.2-1: Core Reporting Requirements**

|  | **SEA** | **LEA** | **School** |
|---|---|---|---|
| Reporting Period |  | Oct 1 - October 1 or the closest school day | Oct 1 - October 1 or the closest school day |
| Education units included |  | Operational LEAs | Operational schools |
| Education units <u>not</u> reported |  | Closed, inactive, or future LEAs | Closed, inactive, or future schools<br>OR<br>Operational schools with school type “reportable programs” |
| No students in membership (i.e., instructional services are provided to students counted in membership elsewhere) |  | Report the grades for which instruction is provided. If students served are not assigned to a specific grade, report “Ungraded” | Report the grades for which instruction is provided. If students served are not assigned to a specific grade, report “Ungraded” |
| Zero counts |  |  |  |
| Zero exceptions or Not applicable |  |  |  |
| Missing |  |  |  |
| Related metadata survey |  | FS5017 - CCD Grades Offered Metadata | FS5017 - CCD Grades Offered Metadata |

**Data Packages**

There are file specifications that contain a requirement that the data file and metadata or a related file must be submitted together. FS039 must be submitted together with FS5017 (Grades Offered metadata).

### Required Categories and Totals

This section is not used for this file specification.

### Categories and Permitted Values

This section contains the categories and permitted values used for submitting this file.

**DG18 - Grades offered:**

**Grades Offered**

The grade level(s) offered by the school or district.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                                                                                                                                                                                                          |
|----------------------------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PK                               | Pre-Kindergarten                | A group or class that is part of a public school program and is taught in the year or years preceding kindergarten.                                                                                                                   |
| KG                               | Kindergarten                    |                                                                                                                                                                                                                                       |
| 01                               | Grade 1                         |                                                                                                                                                                                                                                       |
| 02                               | Grade 2                         |                                                                                                                                                                                                                                       |
| 03                               | Grade 3                         |                                                                                                                                                                                                                                       |
| 04                               | Grade 4                         |                                                                                                                                                                                                                                       |
| 05                               | Grade 5                         |                                                                                                                                                                                                                                       |
| 06                               | Grade 6                         |                                                                                                                                                                                                                                       |
| 07                               | Grade 7                         |                                                                                                                                                                                                                                       |
| 08                               | Grade 8                         |                                                                                                                                                                                                                                       |
| 09                               | Grade 9                         |                                                                                                                                                                                                                                       |
| 10                               | Grade 10                        |                                                                                                                                                                                                                                       |
| 11                               | Grade 11                        |                                                                                                                                                                                                                                       |
| 12                               | Grade 12                        |                                                                                                                                                                                                                                       |
| 13                               | Grade 13                        | Grade 13 is usually included for those LEAs or schools that offer a specific program related to earning post-secondary credit, a CTE degree, or CTE certification, that extends beyond the traditional 4 grade high school structure. |
| UG                               | Ungraded                        | Students assigned to a class or program that does not have standard grade designations.                                                                                                                                               |
| AE                               | Adult Education                 | Programs that are usually for students who have dropped out and returned to school for GED preparation.                                                                                                                               |
| NOGRADES                         | No Grades                       | No students and thus no grades at this educational unit. Used by LEAs that provide support services but do not operate schools. Never used for operational schools.                                                                   |

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

**What if no students are enrolled in a grade offered by an education unit?**

A grade may be offered even though there may not be students enrolled in that grade. If a grade is in Grades Offered, a student count in the Membership file (FS052) is required; that count may be zero.

Conversely, a grade should not be reported as offered if it represents a special accommodation made for one student, or a small number of students, whose assigned grade is outside of the EU’s regularly offered grade range.  Examples of special accommodations include:

- a gifted 8th grade student attending a grades 9-12 high school to take classes better matched to her abilities;

- a student in a remote area who cannot easily commute to a school that serves the student's assigned grade;

- a special needs student who is better served in a school that does not normally serve the student's assigned grade.

**Can an education unit have a mix of graded and ungraded students?**

Yes, a school or LEA may have a mix of graded and ungraded students.[^1]

**When should the grades offered file be submitted?**

SEA should always submit files, including updates, in this order because of the database relationship:

- Directory (FS029)

- Grades Offered (FS039)

- Membership (FS052)

**What if a high school offers Pre-K?**

Report all grades offered for that school. When CCD derives the highest and lowest grade offered, PK is only shown as the lowest grade if the school also offers at least kindergarten and first grade.

### Definitions

See the [EDFacts Workbook](https://www.ed.gov/data/edfacts-initiative/edfacts-resources/edfacts-workbook) for the standard definitions. This file specification has no additional definitions.

## File Naming Convention

The following file naming convention is to help identify files to provide technical assistance.

A maximum of 25 characters (including the file extension) is allowed for the file name.

The following is the naming convention for file submissions:

> sslev**filename**vvvvvvv.ext

**Table 3.0-1: File Naming Convention**

| **Where** | **Means** | **Limit in characters** |
|---|---|---|
| ss | USPS State Abbreviation | 2 |
| lev | Abbreviation for level:<br>•<br>LEA for a Local Education Agency level<br>•<br>SCH for a school level | 3 |
| filename | GRADESOFF | 9 |
| vvvvvvv | Alphanumeric string designated by the SEA to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| .ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 4 |

## Fixed or Delimited Files

This section describes the fixed file and delimited file specifications. The fixed file and delimited files contain a header record followed by data records. The file type is specified in the header record.

The “Pop” column in the header and data records is coded as follows:

> M - Mandatory, this field must always be populated
>
> O - Optional, data in this field is optional

### Header Record Definition

The header record is required and is the first record in every file submitted to EDPass. The purpose of the header record is to provide information as to the file type, number of data records in the file, file name, file identifier, and file reporting period.

**Table 4.1–1: Header Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **LEA GRADES OFFERED**<br>**SCHOOL GRADES OFFERED** |
| Total Records In File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 156 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 283 | 1 |  | M |  |  |

Below is an example of a header record.

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | SCHOOL GRADES OFFERED,15,euschGRADESOFFv000001.csv,characters to identify file,2026-2027,¶                                |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide the grades offered for each LEA and School. Each record reports one grade offered, therefore, each LEA and School may have more than one record.

**Table 4.2–1: Data Records**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two-digit American National Standards Institute (ANSI) code for the State, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (State) | 15 | 14 | String | M | The identifier assigned to a local education agency (LEA) by the state education agency (SEA). Also known as State LEA Identification Number (ID). This data element cannot be updated through this file. |  |
| Filler | 29 | 7 | String | M | Leave filler field blank. |   |
| **DG5** School Identifier (State) | 36 | 20 | String | M | The identifier assigned to a school by the state education agency (SEA). Also known as the State School Identification Number (ID). This ID cannot be updated through this file. | LEA level - Blank |
| Filler | 56 | 12 | String | M | Leave filler field blank. |   |
| Grades Offered | 68 | 15 | String | M | The grade level(s) offered by the school or district. | **PK** – Pre-Kindergarten<br>**KG** – Kindergarten<br>**01** – Grade 1<br>**02** – Grade 2<br>**03** – Grade 3<br>**04** – Grade 4<br>**05** – Grade 5<br>**06** – Grade 6<br>**07** – Grade 7<br>**08** – Grade 8<br>**09** – Grade 9<br>**10** – Grade 10<br>**11** – Grade 11<br>**12** – Grade 12<br>**13** – Grade 13<br>**UG** – Ungraded<br>**AE** – Adult Education<br>**NOGRADES** – No Grades |
| Explanation | 83 | 200 | String | O | Text field for state use. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 283 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit.

**Table 4.2–2: Data Record Example – School level**

| Format | File Record Number,State Code,State Agency Number,LEA Identifier (State),Filler,School Identifier (State),Filler,Grades Offered,Explanation,Carriage Return / Line Feed (CRLF) |
|---|---|
| Example of a school with grades offered of grade 1, 2, 3 and 4 | 1,20,01,001000-0000001,,001000-00002,,01,¶<br>1,20,01,001000-0000001,,001000-00002,,02,¶<br>1,20,01,001000-0000001,,001000-00002,,03,¶<br>1,20,01,001000-0000001,,001000-00002,,04,¶ |

## Document History

| **Version Number** | **Date**    | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |             | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | August 2026 | Updated for SY 2026-27:                                                                 |
