---
fs_id: FS207
title: "State Appropriations for Charter Schools"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG845]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [Directory]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS207-v23.0--edfacts-fs207-23-0-dg845-state-appropriations-charter-schools-v230-114447.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs207-23-0-dg845-state-appropriations-charter-schools-v230-114447.docx"
sha256: a109bca9f20a5feda02e52829c259bee0274ecfd568567760dfde30791186954
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS207 — State Appropriations for Charter Schools (v23.0)

> [!abstract] FS207 at a glance
> **Data groups:** DG845
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** SEA, LEA, School
> **Reporting Period:** School Year (state) - Any 12-month period defined by the state. The state determines whether summer is included in the preceding or following school year
> **Categories:** State Appropriation Methods
> **Data record:** 8 fields, 264 characters fixed-width
> **Generate domain:** [[Directory]]
> **Business rules:** [[FS207 Business Rules]] (BRSI SY 2025-26)
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS207-v23.0--edfacts-fs207-23-0-dg845-state-appropriations-charter-schools-v230-114447.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit EDFacts Data Group 845: State appropriations for charter schools. The definition for this data group is:

> How charter schools receive state appropriations.

The data collected using this file specification are used to distinguish among charter schools by how state appropriations are provided to the charter school.

The data collected using this file specification are collected under the authority of the Elementary and Secondary Education Act of 1965 (ESEA), as amended by the Every Student Succeeds Act (ESSA).

The ED data stewarding office for this file: OESE

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than any editorial changes listed in the document history on page ii, there have been no changes to this file specification.

### Core Requirements for Submitting this File

The following table contains the reporting period, the education units included or excluded, the type of count, and zero count reporting.

**Table 2.2-1: Core Reporting Requirements**

|  | **SEA** | **LEA** | **School** |
|---|---|---|---|
| Reporting Period |  |  | School Year (state) - Any 12-month period defined by the state. The state determines whether summer is included in the preceding or following school year |
| Education units included |  |  | Operational charter schools |
| Education units <u>not</u> reported |  |  | Closed, inactive or future schools<br>Schools that are not charter schools |
| Type of count |  |  |  |
| Zero counts |  |  |  |
| Zero exceptions or<br>Not applicable |  |  |  |
| Missing |  |  | Use MISSING |
| Related metadata survey |  |  |  |

### Required Categories and Totals

This section is not used for this file specification.

### Categories and Permitted Values

This section contains the categories and permitted values used for submitting this file.

**DG845 - State appropriations for charter schools:**

**State Appropriation Methods**

Methods used to provide state appropriations to charter schools.

| **Permitted Value Abbreviation** | **Permitted Value Description**     | **Comments**                                                                                                                                                                                                                                                                                 |
|----------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STEAPRDRCT                       | Direct from state                   | Charter school receives allocations and appropriations directly from the state                                                                                                                                                                                                               |
| STEAPRTHRULEA                    | Through local school district       | Charter school receives appropriations allocated by the state through the local school district with no local school district control on allocation of funds (e.g. passthrough allocations)                                                                                                  |
| STEAPRALLOCLEA                   | Allocation by local school district | Local school district receives appropriation of funds from state and allocates funding to charter school, local school district has similar decision making control on charter school’s use of funds as district has for traditional public schools (e.g. district operated charter school). |
| MISSING                          | Missing                             | Use when data are not available by this category.                                                                                                                                                                                                                                            |

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

**How do I report a charter school if the method of receiving the state appropriation changes?**

Report the method for the fiscal year that most closely aligns with the school year.

**How do I report a charter school if the method of receiving state appropriations is the same for all charter schools?**

Use the same permitted value for all operational charter schools in the state.

**How do I report a charter school if the charter school is under an independent charter district that receives the state appropriations?**

Use the permitted value “Direct from state” (STEAPRDRCT), even though the state appropriations go through the independent charter district.

**Do state appropriations include federal dollars that are allocated through the state?**

No. State appropriations are only dollars from the state and do not include federal pass through dollars.

**Do state appropriations include local dollars such as local property taxes?**

No. State appropriations are only dollars from the state and do not include local dollars.

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
| lev | Abbreviation for level:<br>•<br>SCH for a school level | 3 |
| filename | **CHARSAPRM** | 9 |
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
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SCHOOL CHAR STE APPROPRIATIONS** |
| Total Records In File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 213 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 340 | 1 |  | M |  |  |

Below is an example of a header record.

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | SCHOOL CHAR STE APPROPRIATIONS,15,euschCHARSAPRMv000001.csv,characters to identify file,2026-2027,¶                       |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide counts for the specified category sets, subtotals and education unit totals.

**Table 4.2–1: Data Records**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (State) | 15 | 14 | String | M | The identifier assigned to a local education agency (LEA) by the state education agency (SEA). Also known as State LEA Identification Number (ID). This data element cannot be updated through this file. |  |
| **DG5** School Identifier (State) | 29 | 20 | String | M | The identifier assigned to a school by the state education agency. Also known as the State School Identification Number (ID). This ID cannot be updated through this file. |  |
| State Appropriation Methods | 49 | 15 | String | M | Methods used to provide state appropriations to charter schools. | **STEAPRDRCT** – Direct from state<br>**STEAPRTHRULEA** – Through local school district<br>**STEAPRALLOCLEA** – Allocation by local school district<br>**MISSING** |
| Explanation | 64 | 200 | String | O | Text field for state use. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 264 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit.

**Table 4.2–2: Data Record Examples**

| **Aggregation** | **Example**                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Format          | File Record Number,State Code,State Agency Number,LEA Identifier (State),School Identifier (State),State Appropriation Methods,Explanation,Carriage Return / Line Feed (CRLF) |
| DG 845          | 1,80,01,3400024,8000142,STEAPRDRCT,¶                                                                                                                                          |

## Document History

| **Version Number** | **Date**    | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |             | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | August 2026 | Updated for SY 2026-27:                                                                 |
