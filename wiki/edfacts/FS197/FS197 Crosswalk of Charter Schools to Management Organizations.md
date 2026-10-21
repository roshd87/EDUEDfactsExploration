---
fs_id: FS197
title: "Crosswalk of Charter Schools to Management Organizations"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG833]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [Directory]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS197-v23.0--edfacts-fs197-23-0-dg833-crosswalk-of-charter-schools-management-organizations-v230-114444.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs197-23-0-dg833-crosswalk-of-charter-schools-management-organizations-v230-114444.docx"
sha256: 18fdb8172826cfe6601a3ad3c871ce23f18fd9cd8e87ff0558d39ec8635529f2
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS197 — Crosswalk of Charter Schools to Management Organizations (v23.0)

> [!abstract] FS197 at a glance
> **Data groups:** DG833
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** School
> **Reporting Period:** School Year (state) - Any 12-month period defined by the state. The state determines whether summer is included in the preceding or following school year
> **Data record:** 11 fields, 301 characters fixed-width
> **Generate domain:** [[Directory]]
> **Business rules:** [[FS197 Business Rules]] (BRSI SY 2025-26)
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS197-v23.0--edfacts-fs197-23-0-dg833-crosswalk-of-charter-schools-management-organizations-v230-114444.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit EDFacts Data Group 833: Management organization EIN. The definition for this data group is:

> The identification number issued by the IRS in order for the entity (charter management organization) to pay federal taxes to the U.S. Treasury and report wages to the IRS and Social Security Administration.

The data collected using this file specification are collected under the authority of the Elementary and Secondary Education Act of 1965 (ESEA), as amended by the Every Student Succeeds Act (ESSA).

The ED data stewarding office/s for this file: OESE

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than any editorial changes listed in the document history on page ii, there have been no other changes to this file specification.

### Core Requirements for Submitting this File

**Table 2.2-1: Core Reporting Requirements**

|                                     | **SEA** | **LEA** | **School**                                                                                                                                                |
|-------------------------------------|---------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reporting Period                    |         |         | School Year (state) - Any 12-month period defined by the state. The state determines whether summer is included in the preceding or following school year |
| Education units included            |         |         | Any charter schools that used a management organization                                                                                                   |
| Education units <u>not</u> reported |         |         | Schools that are not charter schools. Charter schools that did not use a management organization.                                                         |

**Data Packages**

There are file specifications that contain a requirement that the data file and metadata or a related file must be submitted together. FS197 must be submitted together with FS196 (Multiple DGs) — Management Organization for Charter Schools Roster.

### Required Categories and Totals

This section is not used for this file specification.

### Categories and Permitted Values

This file specification does not use any categories and permitted values.

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

All responses in this section are technical clarifications to assist data submitters and are not associated with statutory, regulatory, or policy guidance.

**In what order is this file submitted?**

To prevent submission system errors, files should be submitted in the following order.

1.  School level directory file (FS029)

2.  Management Organization Directory file (FS196)

3.  Crosswalk of Charter Schools to Management Organizations file (FS197)

**Can a management organization be associated with more than one charter school?**

Yes

**Can a charter school be associated with more than one management organization?**

Yes, if the charter school changed management organizations during the school year.

**What is the format for Employer Identification Number (EIN) (DG833)?**

An Employer Identification Number (EIN) is a nine-digit number that the IRS assigns in the following format: XX-XXXXXXX.

**What if the Employer Identification Number changes?**

If the Employer Identification Number changes, report the prior EIN in DG833 and the new EIN in DG833N. If the management organization for the charter school has not changed since the beginning of the school year, leave DG833N blank.

### Definitions

The following definitions support this file:

**Charter Management Organization**

The definition of a Charter Management Organization from [ESEA of 1965, as amended by ESSA, Section 4310(3):](https://www2.ed.gov/documents/essa-act-of-1965.pdf) *The term ‘‘charter management organization’’ means a nonprofit organization that operates or manages a network of charter schools linked by centralized support, operations, and oversight*.

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
| filename | **CHARMOCWK** | 9 |
| vvvvvvv | Alphanumeric string designated by the SEA to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| .ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 4 |

## Fixed or Delimited Files

This section describes the fixed file and delimited file specifications. The fixed file and delimited files contain a header record followed by data records. The file type is specified in the header record.

The “Pop” column in the header and data records is coded as follows:

> M - Mandatory, this field must always be populated
>
> O - Optional
>
> C - Used when charter management organization changes

### Header Record Definition

The header record is required and is the first record in every file submitted to EDPass. The purpose of the header record is to provide information as to the file type, number of data records in the file, file name, file identifier, and file reporting period.

**Table 4.1–1: Header Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SCH CHAR ORG CROSSWALK** |
| Total Records In File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 333 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 460 | 1 |  | M |  |  |

Below is an example of a header record.

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | SCH CHAR ORG CROSSWALK,15,euschCHARMOCWKv000001.csv,characters to identify file,2026-2027,¶                               |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide other data for the education units.

**Table 4.2–1: Data Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (State) | 15 | 14 | String | M | The identifier assigned to a local education agency (LEA) by the state education agency (SEA). Also known as State LEA Identification Number (ID). This data element cannot be updated through this file. |  |
| **DG1** LEA Identifier (NCES) | 29 | 7 | String | M | The seven-digit unique identifier assigned to the LEA by NCES. Also known as NCES LEA ID.<br>This ID cannot be updated through this file. | Two–digit state code followed by a five–digit local education agency (LEA) code. |
| **DG5** School Identifier (State) | 36 | 20 | String | M | The identifier assigned to a school by the state education agency (SEA). Also known as the State School Identification Number (ID). This ID cannot be updated through this file. |  |
| **DG529** School Identifier (NCES) | 56 | 5 | String | M | Include only the unique 5 digits assigned by NCES<br>This ID cannot be updated through this file. |  |
| **DG833** Management Organization EIN | 61 | 20 | String | M | The identification number issued by the IRS in order for the entity (charter management organization) to pay federal taxes to the U.S. Treasury and report wages to the IRS and Social Security Administration. | Format: XX-XXXXXXX |
| **DG833N** Management Organization EIN New<br>(previously referred to as “Updated”) | 81 | 20 | String | C | The new (updated) identification number issued by the IRS in order for the entity (charter management organization) to pay federal taxes to the U.S. Treasury and report wages to the IRS and Social Security Administration, if changed since the beginning of the school year.<br>**Population of this field -** Use only if updating the Management Organization EIN.. | Format: XX-XXXXXXX<br>If the management organization for the charter school has not changed since the beginning of the school year, leave this field blank. |
| Explanation | 101 | 200 | String | O | Text field for state use. |  |
| Carriage Return / Line Feed (CRLF) | 301 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each connection.

**Table 4.2–2: Data Record Example**

| Format  | File Record Number, State Code, State Agency Number, LEA Identifier (State), LEA Identifier (NCES), School Identifier (State), School Identifier (NCES),Management organization EIN,Management organization EIN New,Explanation,Carriage Return / Line Feed (CRLF) |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Example | 1,80,01,3400024,8000142,278A,32405,84-1270214,,¶                                                                                                                                                                                                                   |

## Document History

| **Version Number** | **Date**    | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |             | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | August 2026 | Updated for SY 2026-27:                                                                 |
