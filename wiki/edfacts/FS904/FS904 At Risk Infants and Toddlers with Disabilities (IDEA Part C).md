---
fs_id: FS904
title: "At Risk Infants and Toddlers with Disabilities (IDEA Part C)"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG5025]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: []
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS904-v23.0--edfacts-fs904-23-0-dg5025-risk-infants-and-toddlers-disabilities-idea-part-c-v230-114556.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs904-23-0-dg5025-risk-infants-and-toddlers-disabilities-idea-part-c-v230-114556.docx"
sha256: c198d146df61b46130d81b2890890dc57b3ba338a195e4f58251d6c7ef672a8f
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS904 — At Risk Infants and Toddlers with Disabilities (IDEA Part C) (v23.0)

> [!abstract] FS904 at a glance
> **Data groups:** DG5025
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** State
> **Reporting Period:** Child Count Date
> **Data record:** 13 fields, 325 characters fixed-width
> **Business rules:** [[FS904 Business Rules]] (BRSI SY 2025-26)
> **Metadata guides:** [[IDEA Part C Child Count Metadata User Guide]]
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS904-v23.0--edfacts-fs904-23-0-dg5025-risk-infants-and-toddlers-disabilities-idea-part-c-v230-114556.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit EDFacts Data Group 5025: At risk infants and toddlers table. The definition for this data group is:

> The unduplicated number of infants and toddlers, ages birth through 2, who were determined to be at risk of experiencing substantial developmental delays if early intervention services were not provided and who have an active IFSP in place on the child count date.

The data collected using this file specification are collected under the authority of the Individuals with Disabilities Education Act (IDEA), 20 U.S.C. 1418(a)(1)(C) and (a)(3).

The ED data stewarding office/s for this file: OSERS/OSEP.

## Guidance for Submitting this File

This section contains changes from the previous reporting year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than any editorial changes listed in the document history on page ii, there have been no other changes to this file specification.

### Core Requirements for Submitting this File

The following table contains the reporting period, the education units included or excluded, the type of count, and zero count reporting.

**Table 2.2-1: Core Reporting Requirements**

|                                   | State                                                                              |
|-----------------------------------|------------------------------------------------------------------------------------|
| Reporting Period                  | Child Count Date                                                                   |
| Type of Count                     | Once                                                                               |
| Zero Counts                       | Required                                                                           |
| Zero Exceptions or Not Applicable | None                                                                               |
| Missing                           | Use “-1” to report missing counts. Use “MISSING” when a category is not available. |
| Related Metadata Survey           | FS5027 - Infants and Toddlers with Disabilities (IDEA Part C) Count Metadata       |

### Required Categories and Totals

The table below lists the combinations of the categories and totals that are expected to be submitted for the state.

- An “X” in the column indicates that the category value must be submitted when reporting that aggregation.

- The total indicator must be either “Y” (Yes) or “N” (No).

  - If the record is for a category set, specify an “N” (No).

  - If the record is for a subtotal or education unit total, specify a “Y” (Yes).

The technical name of the data used in the file is: ATRSKIT

**Table 2.3–1: Required Categories and Totals**

| Aggregation | Racial Ethnic | Age (EI) | Total<br>Indicator | Comments |
|---|---|---|---|---|
| Category Set A | X |  | N | Infants and Toddlers Count by Racial Ethnic |
| Category Set B |  | X | N | Infants and Toddlers Count by Age (EI) |
| Total of the Education Unit |  |  | Y | Total of the Education Unit |

### Categories and Permitted Values

This section contains the categories and permitted values used for submitting this file.

#### Age (EI)

The discrete age of infants and toddlers on the child count date.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                      |
|----------------------------------|---------------------------------|---------------------------------------------------|
| AGEB                             | Birth                           | Birth to 1                                        |
| AGE1                             | Age 1                           | Age 1 to 2                                        |
| AGE2                             | Age 2                           | Age 2 to 3                                        |
| MISSING                          | Missing                         | Use when data are not available by this category. |

#### Racial Ethnic

The general racial category that most clearly reflects individuals' recognition of their community or with which the individuals most identify.

| Permitted Value Abbreviation | Permitted Value Description               | Comments                                          |
|------------------------------|-------------------------------------------|---------------------------------------------------|
| AM7                          | American Indian or Alaska Native          |                                                   |
| AS7                          | Asian                                     |                                                   |
| BL7                          | Black or African American                 |                                                   |
| HI7                          | Hispanic/Latino                           |                                                   |
| PI7                          | Native Hawaiian or Other Pacific Islander |                                                   |
| MU7                          | Two or more races                         |                                                   |
| WH7                          | White                                     |                                                   |
| MISSING                      | Missing                                   | Use when data are not available by this category. |

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

**Which states report this data?**

Only states that have elected under 20 U.S.C. 1432(5)(B)(i) to serve at-risk infants and toddlers. States that do not have an extended Part C option should NOT provide counts of children age three or older.

### Definitions

See the [EDFacts Workbook](https://www.ed.gov/edfacts-workbook) for the standard definitions.

**Early Intervention Services** – Development services that:

1)  are provided in conformity with an IFSP;

2)  are provided under public supervision (i.e., Federal, State, or local funds are used in connection with the provision of services). This includes children receiving services through a program funded by public monies as well as children receiving services from a private provider, but whose services are supervised or paid for by a public agency;

3)  are provided at no cost except where Federal or State law provides for a system of payments by families, including a schedule of sliding fees;

4)  are designed to meet the developmental needs of an infant or toddler with a disability (as defined in 20 U.S.C. 1432(5));

5)  meet the standards of the State and the requirements of IDEA; and

6)  are provided, to the maximum extent appropriate, in natural environments.

More detailed information about the definition of early intervention services can be found in 20 U.S.C. 1432(4) and in 34 C.F.R. §§ 303.13 and 303.16.

## File Naming Convention

The following file naming convention is to help identify files to provide technical assistance.

A maximum of 25 characters (including the file extension) is allowed for the file name.

The following is the naming convention for file submissions:

> sslev**filename**vvvvvvv.ext

**Table 3.0-1: File Naming Convention**

| Where | Means | Limit in characters |
|---|---|---|
| ss | USPS State Abbreviation | 2 |
| lev | Abbreviation for level:<br>SEA for a State Agency level | 3 |
| filename | IDEACARIT | 9 |
| vvvvvvv | Alphanumeric string designated by the state agency to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| .ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 4 |

## Fixed or Delimited Files

This section describes the fixed file and delimited file specifications. The fixed file and delimited files contain a header record followed by data records. The file type is specified in the header record.

The “Pop” column in the header and data records is coded as follows:

> M - Mandatory, this field must always be populated
>
> A - This field is populated in accordance with table 2.3-1 “Required Categories and Totals”

O - Optional, data in this field are optional

### Header Record Definition

The header record is required and is the first record in every file submitted to EDPass. The purpose of the header record is to provide information as to the file type, number of data records in the file, file name, file identifier, and file reporting period.

**Table 4.1–1: Header Record**

| Data Element Name | Start Position | Length | Type | Pop | Definition / Comments | Permitted Values<br>Abbreviation |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SEA AT RISK INFANT TODD IDEA C** |
| Total Records in File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the lead agency (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 378 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 505 | 1 |  | M |  |  |

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | SEA AT RISK INFANT TODD IDEA C,13,eulaIDEACARITv000001.csv,characters to identify file,2026-2027,¶                        |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide counts for the specified category sets, subtotals and education unit totals.

**Table 4.2–1: Data Records**

| Data Element Name | Start Position | Length | Type | Pop | Definition / Comments | Permitted Values<br>Abbreviations |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| DG559<br>State Code | 11 | 2 | String | M | The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| DG570<br>Lead Agency Number | 13 | 2 | String | M | A number used to uniquely identify lead agencies. This ID cannot be updated through this file. | 02 – Lead Agency |
| Filler | 15 | 14 | String | M | Leave filler field blank. |  |
| Filler | 29 | 20 | String | M | Leave filler field blank. |  |
| Table Name | 49 | 20 | String | M | See technical name in Section 2.3 Required Categories and Totals. | ATRSKIT |
| Filler | 69 | 15 | String | M | Leave filler field blank. |  |
| Age (EI) | 84 | 15 | String | A | The discrete age of children on the child count date. | AGEB – Birth<br>AGE1 – Age 1<br>AGE2 – Age 2<br>MISSING |
| Racial Ethnic | 99 | 15 | String | A | The general racial category that most clearly reflects individuals' recognition of their community or with which the individuals most identify. | AM7 – American Indian or Alaska Native<br>AS7 – Asian<br>BL7 – Black or African American<br>HI7 – Hispanic/Latino<br>PI7 – Native Hawaiian or Other Pacific Islander<br>WH7 – White<br>MU7 – Two or more races<br>MISSING |
| Total Indicator | 114 | 1 | String | M | An indicator that defines the count level – see table 2.3-1 “Required Categories and Totals” | N – specifies detail level<br>Y – specifies a subtotal or total of the education unit level |
| Explanation | 115 | 200 | String | O | Text field for state use. |  |
| Infants and Toddlers Count | 315 | 10 | Integer | M |  |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 325 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit. See table 2.3-1.

**Table 4.2–2: Data Record Example**

| Aggregation                 | Example                                                              | Data Record                                                                                                                                                                                       |
|-----------------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Format                      |                                                                      | File Record Number,State Code,Lead Agency Number,Filler,Filler,Table Name,Filler,Age (EI),Racial Ethnic,Total Indicator,Explanation,Infants and Toddlers Count,Carriage Return / Line Feed (CRLF) |
| Category Set A              |  5 children who are American Indian or Alaska Native who are at risk | 1,80,02,,,ATRSKIT,,,AM7,N,,5¶                                                                                                                                                                     |
| Category Set B              |  12 children who are ages birth to 1 who are at risk                 | 6,80,02,,,ATRSKIT,,AGEB,,N,,12¶                                                                                                                                                                   |
| Total of the Education Unit |  1,112 children who are at risk                                      | 31,80,02,,,ATRSKIT,,,,Y,,1112¶                                                                                                                                                                    |

## Document History

| **Version Number** | **Date**       | **Summary of Change**                                                                      |
|---|---|---|
| 1.0 – 22.0         |                | Versions 1.0 through 22.0 are used to build files for reporting years prior to SY 2026-27. |
| 23.0               | September 2026 | Updated for SY 2026-27:                                                                    |
