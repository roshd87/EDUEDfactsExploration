---
fs_id: FS198
title: "Charter Contracts"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG830, DG831, DG832]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [Directory]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS198-v23.0--edfacts-fs198-23-0-dg830-dg831-dg832-charter-contracts-v230-114445.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs198-23-0-dg830-dg831-dg832-charter-contracts-v230-114445.docx"
sha256: 242f76d9720c8cec8e37fd0f94ab29b4292381c6998267aafd29002d5b7c4d9d
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS198 — Charter Contracts (v23.0)

> [!abstract] FS198 at a glance
> **Data groups:** DG830, DG831, DG832
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** School
> **Reporting Period:** School Year (state) - Any 12-month period defined by the state. The state determines whether summer is included in the preceding or following school year
> **Data record:** 10 fields, 289 characters fixed-width
> **Generate domain:** [[Directory]]
> **Business rules:** [[FS198 Business Rules]] (BRSI SY 2025-26)
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS198-v23.0--edfacts-fs198-23-0-dg830-dg831-dg832-charter-contracts-v230-114445.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit the following EDFacts data groups:

**Table 1.0-1: EDFacts data groups**

| **Data Group Name**            | **DG** | **Definition**                                                                                                                                                                                                  |
|--------------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Charter contract ID number     | 830    | The unique number an SEA assigns to the contract (or charter).                                                                                                                                                  |
| Charter contract approval date | 831    | The effective date of the contract (or charter) issued by approved charter school authorizer authorizing the charter school to operate in the state under the state's charter school legislation.               |
| Charter contract renewal date  | 832    | The date by which the charter school must renew its contract (or charter) with an approved charter school authorizer in order to continue to operate in the state under the state’s charter school legislation. |

The data collected using this file specification are to enable the Department’s Office of Elementary and Secondary Education, Charter School Programs Office (OESE/CSP) to obtain a complete list of charter schools in the United States. OESE/CSP goes through a complex reconciliation process to compile a directory of all charter schools that are in operation across the nation. These data will fill in the data gaps so that, for each school year, OESE/CSP has a complete and accurate directory of charter schools.

The data collected using this file specification are collected under the authority of the Elementary and Secondary Education Act of 1965 (ESEA), as amended by the Every Student Succeeds Act (ESSA).

The ED data stewarding office(s) for this file: OESE.

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than any editorial changes listed in the document history on page ii, there have been no changes to this file specification.

### Core Requirements for Submitting the File

***
***

**Table 2.2-1: Core Reporting Requirements**

|  | **SEA** | **LEA** | **School** |
|---|---|---|---|
| Reporting Period |  |  | School Year (state) - Any 12-month period defined by the state. The state determines whether summer is included in the preceding or following school year |
| Education units included |  |  | Operational charter schools (required); Inactive or Future charter schools (optional) |
| Education units <u>not</u> reported |  |  | Closed charter schools |
| Type of count |  |  |  |
| Zero counts |  |  |  |
| Zero exceptions or<br>Not applicable |  |  |  |
| Missing |  |  | When the contract information is missing, the charter school is left out of the file. |
| Related metadata survey |  |  |  |

### Required Categories and Totals

This section is not used for this file specification.

### Categories and Permitted Values

This file specification does not use any categories and permitted values.

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

**Are all charter schools included in this file?**

No. The state must report a charter contract that has an ID number, an approval date and a renewal date for all operational charter schools. The state may optionally report a charter contract for inactive or future schools.

#### Charter Contract ID Number (DG830)

**When a state does not assign identification codes to charter schools, can the School ID or NCES ID be used for reporting?** **Why?**

No. States should assign a unique identifier that corresponds to each separate and distinct charter contract and enter this unique number in the Charter contract ID number field. These data will enable the Department and other stakeholders to understand the full universe of charters which are executed by authorized public chartering agencies in each state.

The purpose of the charter contract ID number (DG830) is to assign a unique identifier to each charter or contract between an authorized public chartering agency (see definition in Section 2.6) and the organization that holds the charter. In some cases, each charter contract corresponds to one and only one charter school. However, in many cases, a single charter contract captures two or more charter schools.

**If there is no change in the charter contract approval or renewal date, is it necessary to report these data each year?**

Yes. While some dates will not change, it is possible that some event may occur that could result in changes to these dates.

**Is the contract approval date the first date the contract was signed, or the most recent date the contract was renewed?**

The purpose of the “Charter Contract Approval Date” is to capture and maintain the date of execution of a charter school’s current contract with its authorizer. For a relatively new school, which has not reached its renewal date, this date will correspond with the effective date of the school’s current contract with its authorizer. For a charter school that has a contract that has been renewed, the “Charter Contract Approval Date” will correspond with that renewal date, as that date would represent the effective date of the charter school’s current charter or contract with the authorizer. In that case, the “Charter Contract Renewal Date” would represent the new renewal date for the current contract.

### Definitions

**Authorized Public Chartering Agency**

The definition of an Authorized Public Chartering Agency from ESEA of 1965, [as amended by ESSA, Section 4310(1)](https://www2.ed.gov/documents/essa-act-of-1965.pdf): *The term ‘‘authorized public chartering agency’’ means a State educational agency, local educational agency, or other public entity that has the authority pursuant to State law and approved by the Secretary to authorize or approve a charter school*. For further clarification about Authorized Public Chartering Agency, see permitted values for Charter Authorizer Type in FS190 (DG807).

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
| filename | **CHARCONTR** | 9 |
| vvvvvvv | Alphanumeric string designated by the SEA to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 4 |

## Fixed or Delimited Files

This section describes the fixed file and delimited file specifications. The fixed file and delimited files contain a header record followed by data records. The file type is specified in the header record.

The “Pop” column in the header and data records is coded as follows:

> M - Mandatory, this field must always be populated
>
> O - Optional, data in this field are optional

### Header Record Definition

The header record is required and is the first record in every file submitted to EDPass. The purpose of the header record is to provide information as to the file type, number of data records in the file, file name, file identifier, and file reporting period.

**Table 4.1–1: Header Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SCH CHAR CONTRACTS** |
| Total Records In File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 333 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 460 | 1 |  | M |  |  |

Below is an example of a header record.

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CLRF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | SCH CHAR CONTRACTS,15,euschCHARCONTRv000001.csv,characters to identify file,2026-2027,¶                                   |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide the statuses and other data for the education units.

**Table 4.2–1: Data Records**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (State) | 15 | 14 | String | M | The identifier assigned to a local education agency (LEA) by the state education agency (SEA). Also known as State LEA Identification Number (ID). This data element cannot be updated through this file. |  |
| **DG5** School Identifier (State) | 29 | 20 | String | M | The identifier assigned to a school by the state education agency (SEA). Also known as the State School Identification Number (ID). This ID cannot be updated through this file. |  |
| **DG830** Charter Contract ID Number | 49 | 20 | String | M | The unique number an SEA assigns to the contract (or charter). |  |
| **DG831** Charter Contract Approval Date | 69 | 10 | String | M | The effective date of the contract (or charter) issued by approved charter school authorizer authorizing the charter school to operate in the state under the state's charter school legislation. | YYYY-MM-DD |
| **DG832** Charter Contract Renewal Date | 79 | 10 | String | M | The date by which the charter school must renew its contract (or charter) with an approved charter school authorizer in order to continue to operate in the state under the state’s charter school legislation. | YYYY-MM-DD |
| Explanation | 89 | 200 | String | O | Text field for state use. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 289 | 1 |  | M |  |  |

Below is an example of a data record. This is the set of data that should be submitted for each education unit.

**Table 4.2–2: Data Record Example – School level**

| Format  | File Record Number,State Code,State Agency Number,LEA Identifier (State),School Identifier (State),Charter Contract ID Number,Charter Contract Approval Date,Charter Contract Renewal Date,Explanation,Carriage Return / Line Feed (CRLF) |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Example | 1,80,01,00620LEA,00000000000000000010,HAMN2005--710,2016-05-16,2031-05-16,¶                                                                                                                                                               |

## Document History

| **Version Number** | **Date**    | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |             | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | August 2026 | Updated for SY 2026-27:                                                                 |
