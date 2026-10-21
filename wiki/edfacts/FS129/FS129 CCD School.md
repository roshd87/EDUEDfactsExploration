---
fs_id: FS129
title: "CCD School"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG573, DG791, DG803]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [Directory]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS129-v23.0--edfacts-fs129-23-0-dg573-dg791-dg803-ccd-school-v230-114535.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs129-23-0-dg573-dg791-dg803-ccd-school-v230-114535.docx"
sha256: a614a3c557cfb01503b21a39ddc80b7a7d9313eceaed8df5cf124408c32b8353
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS129 — CCD School (v23.0)

> [!abstract] FS129 at a glance
> **Data groups:** DG573, DG791, DG803
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** School
> **Reporting Period:** See section 2.5
> **Categories:** Shared Time Status, NSLP Status, Virtual School Status
> **Data record:** 12 fields, 324 characters fixed-width
> **Generate domain:** [[Directory]]
> **Business rules:** [[FS129 Business Rules]] (BRSI SY 2025-26)
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS129-v23.0--edfacts-fs129-23-0-dg573-dg791-dg803-ccd-school-v230-114535.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit the following EDFacts Data Groups:

**Table 1.0-1: EDFacts Data Groups**

| **Data Group Name**   | **DG** | **Definition**                                                                                                                                                                                                                    |
|-----------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shared time status    | 573    | An indication that a school offers career and technical education or other educational services in which some or all students are enrolled at a separate school of record and attend the shared-time school on a part-time basis. |
| NSLP status           | 791    | The classification of participation by a school in the National School Lunch Program (NSLP).                                                                                                                                      |
| Virtual school status | 803    | An indication of the extent to which a public school offers instruction in which students and teachers are separated by time and/or location, and interaction occurs via computers and/or telecommunications technologies.        |

The data collected using this file specification are collected under the authority of the Education Sciences Reform Act (ESRA) for the Non-Fiscal Survey of the Common Core of Data (CCD) and the Every Student Succeeds Act (ESSA).

The ED data stewarding office for this file: NCES

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than any editorial changes listed in the document history on page ii, there have been no changes to this file specification.

### Core Requirements for Submitting this File

The following table contains the reporting period, the education units included or excluded, the type of count, and zero count reporting.

**Table 2.2-1: Core Reporting Requirements**

|  | **SEA** | **LEA** | **School** |
|---|---|---|---|
| Reporting Period |  |  | See section 2.5 |
| Education units included |  |  | Schools other than reportable programs that were operational on October 1 |
| Education units <u>not</u> reported |  |  | Closed, inactive, or future schools<br>Schools that opened after October 1st<br>Schools with school type of "reportable program" |
| Type of Count |  |  |  |
| Zero Counts |  |  |  |
| Zero Exceptions and Not Applicable |  |  | None |
| Missing |  |  | Use “MISSING” when a status is not available. |
| Related metadata survey |  |  |  |

### Required Categories and Totals

This section is not used for this file specification.

### Categories and Permitted Values

This section contains the categories and permitted values used for submitting this file.

**DG573 - Shared time status:**

**Shared Time Status**

An indication that a school offers career and technical education or other educational services in which some or all students are enrolled at a separate school of record and attend the shared-time school on a part-time basis.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                                                                                                                                                                                                                                 |
|----------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NO                               | Is not a shared-time school     | School does not offer educational services in which some or all students are enrolled in separate schools.                                                                                                                                                   |
| YES                              | Is a shared-time school         | School offers vocational/technical education or other educational services in which some or all students are enrolled in separate schools of record and attend this school on a part-time basis (i.e., students are reported in FS052 under another school). |
| MISSING                          | Missing                         | Use when data are not available by this category.                                                                                                                                                                                                            |

**DG791 - NSLP status:**

**NSLP Status**

The statuses describing participation in the National School Lunch Program (NSLP).

| **Permitted Value Abbreviation** | **Permitted Value Description**                           | **Comments**                                      |
|----------------------------------|-----------------------------------------------------------|---------------------------------------------------|
| NSLPWOPRO                        | Yes, participating without using any Provision or the CEO |                                                   |
| NSLPPRO1                         | Yes, under Provision 1                                    |                                                   |
| NSLPPRO2                         | Yes, under Provision 2                                    |                                                   |
| NSLPPRO3                         | Yes, under Provision 3                                    |                                                   |
| NSLPCEO                          | Yes, under Community Eligibility Option (CEO)             |                                                   |
| NSLPNO                           | No                                                        |                                                   |
| MISSING                          | Missing                                                   | Use when data are not available by this category. |

**DG803 - Virtual school status:**

**Virtual School Status**

The statuses describing the extent to which a public school offers instruction in which students and teachers are separated by time and/or location and interaction occurs via computers and /or telecommunication technologies.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                                                                                                                                                                                                            |
|----------------------------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FULLVIRTUAL                      | Exclusively virtual             | All instruction offered by the school is virtual. This does not exclude students and teachers meeting in person for field trips, school-sponsored social events or assessment purposes. All students receive all instruction virtually. |
| FACEVIRTUAL                      | Primarily virtual               | The school’s major purpose is to provide virtual instruction to students, but some traditional classroom instruction is also provided. Most students receive all instruction virtually.                                                 |
| SUPPVIRTUAL                      | Supplemental Virtual            | Instruction is directed by teachers in a traditional classroom setting; virtual instruction supplements face-to-face instruction by teachers. Students vary in the extent to which their instruction is virtual.                        |
| NOTVIRTUAL                       | No virtual instruction          | The school does not offer any virtual instruction. No students receive any virtual instruction.                                                                                                                                         |
| MISSING                          | Missing                         | Use when data are not available by this category.                                                                                                                                                                                       |

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

**What is the reporting period for each data group?**

**Table 2.5-1: Reporting Period for Each Data Group**

| **Data Group Name**   | **DG** | **Reporting Period**                                               |
|-----------------------|--------|--------------------------------------------------------------------|
| Shared time status    | 573    | Oct 1 - October 1 or closest school day                            |
| NSLP status           | 791    | November 30 – November 30 or the closest school day to November 30 |
| Virtual school status | 803    | Oct 1 - October 1 or closest school day                            |

### Definitions

See the [EDFacts Workbook](https://www.ed.gov/data/edfacts-initiative/edfacts-resources/edfacts-workbook) for the standard definitions.

## File Naming Convention

The following file naming convention is to help identify files to provide technical assistance.

A maximum of 25 characters (including the file extension) is allowed for the file name.

The following is the naming convention for file submissions:

> sslev**filename**vvvvvvv.ext

**Table 3.0-1: File Naming Convention**

| **Where** | **Means** | **Limit in characters** |
|---|---|---|
| ss | USPS State Abbreviation | 2 |
| lev | Abbreviation for level:<br>•<br>SCH for a school level | 3 |
| filename | CCDSCHOOL | 9 |
| vvvvvvv | Alphanumeric string designated by the SEA to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| .ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 4 |

## Fixed or Delimited Files

This section describes the fixed file and delimited file specifications. The fixed file and delimited files contain a header record followed by data records. The file type is specified in the header record.

The “Pop” column in the header and data records is coded as follows:

> M - Mandatory, this field must always be populated
>
> O - Optional, data in this field are optional

### Header Record Definition

The header record is required and is the first record in every file submitted to EDPass. The purpose of the header record is to provide information as to the file type, number of data records in the file, file name, file identifier, and file reporting period.

**Table 4.1–1: Header Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **CCD SCHOOL** |
| Total Records in File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 182 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 309 | 1 |  | M |  |  |

Below is an example of a header record.

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File File Name,File Identifier,File Reporting Period,Filler, Carriage Return / Line Feed (CRLF) |
|---------|----------------------------------------------------------------------------------------------------------------------------|
| Example | CCD SCHOOL,15,euschCCDSCHOOLv000001.csv,characters to identify file,2026-2027,¶                                            |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide the statuses for the education units.

**Table 4.2–1: Data Records**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (state) | 15 | 14 | String | M | The identifier assigned to a local education agency (LEA) by the state education agency (SEA). Also known as State LEA Identification Number (ID). This data element cannot be updated through this file. |  |
| **DG5** School Identifier (state) | 29 | 20 | String | M | The identifier assigned to a school by the state education agency (SEA). Also known as the State School Identification Number (ID). This ID cannot be updated through this file. |  |
| Shared Time Status | 49 | 15 | String | M | An indication that a school offers career and technical education or other educational services in which some or all students are enrolled at a separate school of record and attend the shared-time school on a part-time basis. | **NO** – Is not a shared-time school<br>**YES** – Is a shared-time school<br>**MISSING** |
| Filler | 64 | 15 | String | M | Leave filler field blank. |  |
| Filler | 79 | 15 | String | M | Leave filler field blank. |  |
| NSLP Status | 94 | 15 | String | M | The statuses describing participation in the National School Lunch Program (NSLP). | **NSLPWOPRO** – Yes, participating without using any Provision or the CEO<br>**NSLPPRO1** – Yes, under Provision 1<br>**NSLPPRO2** – Yes, under Provision 2<br>**NSLPPRO3** – Yes, under Provision 3<br>**NSLPCEO** – Yes, under Community Eligibility Option (CEO)<br>**NSLPNO** – No<br>**MISSING** |
| Virtual School Status | 109 | 15 | String | M | The statuses describing the extent to which a public school offers instruction in which students and teachers are separated by time and/or location and interaction occurs via computers and /or telecommunication technologies. | **FULLVIRTUAL** – Exclusively virtual<br>**FACEVIRTUAL** – Primarily virtual<br>**SUPPVIRTUAL** – Supplemental Virtual<br>**NOTVIRTUAL** – No virtual instruction<br>**MISSING** |
| Explanation | 124 | 200 | String | O | Text field for state use. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 324 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit.

**Table 4.2–2: Data Record Example – School level**

| Format  | File Record Number,State Code,State Agency Number,LEA Identifier (state),School Identifier (state),Shared Time Status,,,NSLP Status,Virtual School Status,Explanation,Carriage Return / Line Feed (CRLF) |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Example | 1,80,01,00619PSCLEA,00000000000000000123,YES,,,NSLPCEO,FULLVIRTUAL,¶                                                                                                                                     |

## Document History

| **Version Number** | **Date**       | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |                | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | September 2026 | Updated for SY 2026-27:                                                                 |
