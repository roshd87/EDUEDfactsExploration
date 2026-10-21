---
fs_id: FS033
title: "Free and Reduced Price Lunch"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG565, DG813]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [Membership]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS033-v23.0--edfacts-fs033-23-0-dg565-dg813-free-and-reduced-price-lunch-v230-114525.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs033-23-0-dg565-dg813-free-and-reduced-price-lunch-v230-114525.docx"
sha256: 88810b6c51fff98cf1958f8b438806dd3949ad25ea637df84950ccce11b654dd
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS033 — Free and Reduced Price Lunch (v23.0)

> [!abstract] FS033 at a glance
> **Data groups:** DG565, DG813
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** School
> **Reporting Period:** October 1 (or closest school day) or USDA reporting period
> **Type of count:** Students are counted at only one school
> **Zero counts:** Either DG 565 or DG 813 are required. Both can be submitted
> **Categories:** Lunch Program Status
> **Data record:** 11 fields, 295 characters fixed-width
> **Generate domain:** [[Membership]]
> **Business rules:** [[FS033 Business Rules]] (BRSI SY 2025-26)
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS033-v23.0--edfacts-fs033-23-0-dg565-dg813-free-and-reduced-price-lunch-v230-114525.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit the following EDFacts Data Groups:

**Table 1.0-1: EDFacts Data Groups**

| **Data Group Name**                | **DG** | **Definition**                                                                                                                                                      |
|------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Free and reduced-price lunch table | 565    | The unduplicated number of students who are eligible to participate in the Free Lunch and Reduced-Price Lunch Programs under the National School Lunch Act of 1946. |
| Direct certification               | 813    | The unduplicated number of students in membership whose National School Lunch Program (NSLP) eligibility has been determined through direct certification.          |

EDFacts data groups

The data collected using this file specification are collected under the authority of the Education Sciences Reform Act (PL 107-279) and are used primarily for the Non-Fiscal Survey of the Common Core of Data (CCD).

The ED data stewarding office/s for this file: NCES

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than the editorial changes listed in the document history on page ii, there have been no other changes to this file specification.

### Core Requirements for Submitting this File

The following tables contain the reporting period, the education units included or excluded, the type of count, and zero count reporting for each data group.

**Table 2.2-1: Core Reporting Requirements – DG 565 Free and Reduced-price Lunch Table and DG 813 Direct Certification**

|  | **SEA** | **LEA** | **School** |
|---|---|---|---|
| Reporting Period |  |  | October 1 (or closest school day) or USDA reporting period |
| Education units included |  |  | Operational schools with membership (FS 052) greater than zero and with NSLP (FS129) Status that is not “No.” |
| Education units not reported |  |  | Inactive, closed or future schools.<br>Schools with no membership or membership equal to zero (FS 052).<br>Schools with NSLP Status that is “No.” |
| Type of count |  |  | Students are counted at only one school. |
| Zero counts |  |  | Either DG 565 or DG 813 are required.<br>Both can be submitted. |
| Zero exceptions and Not applicable |  |  | None |
| Missing |  |  | Use “-1” to report missing counts, that is, when the value is not known. |
| Related metadata survey |  |  |  |

### Required Categories and Totals

The table below lists the combinations of the categories and totals that are expected to be submitted for each school that should be included in the file.

- An “X” in the column indicates that the category value must be submitted when reporting that aggregation.

- The total indicator must be either “Y” (Yes) or “N” (No).

  - If the record is for a category set, specify an “N” (No).

  - If the record is for a subtotal or education unit total, specify a “Y” (Yes).

**Table 2.3-1: Required Categories and Totals**

| **Category Set**                                                        | **Lunch Program Status** | **Total Indicator** | **Comments**                                                   |
|-------------------------------------------------------------------------|--------------------------|---------------------|----------------------------------------------------------------|
| Free and reduced-price lunch table (DG 565) Category Set A              | X                        | N                   | Student Count by Lunch Program Status                          |
| Free and reduced-price lunch table (DG 565) Total of the Education Unit |                          | Y                   | Total of the Educational Unit for Free and reduced-price lunch |
| Direct Certification (DG 813) Total of the Education Unit               |                          | Y                   | Total of the Educational Unit for Direct certification         |

The following table contains the table names used for this file’s data groups.

**Table 2.3-2 Free and Reduced Price Lunch Table Names Used in Files**

| **DG#** | **DG Name**                        | **Table Name used in file** |
|---------|------------------------------------|-----------------------------|
| 565     | Free and reduced-price lunch table | LUNCHFREERED                |
| 813     | Direct certification               | DIRECTCERT                  |

### Categories and Permitted Values

This section contains the categories and permitted values used for submitting this file.

**DG565 – Free and reduced-price lunch table:**

**Lunch Program Status**

An indication of students’ qualification for free or reduced-price lunch.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                                                                                                                                                                 |
|----------------------------------|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FL                               | Free lunch qualified            | Students who are eligible to participate in the Free Lunch Program under the National School Lunch Act of 1946. This definition **EXCLUDES** students eligible only for reduced-price lunch. |
| RPL                              | Reduced-price lunch qualified   | Students who are eligible to participate in the Reduced-Price Lunch Program under the National Schools Lunch Act of 1946.                                                                    |
| MISSING                          | Missing                         | FL and RPL counts are unknown                                                                                                                                                                |

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

**What is the relationship between DG565 (Free and reduced-price lunch) and DG813 (Direct certification)?**

Free and reduced-price lunch (DG565) includes students who are directly certified plus students who qualified for free or reduced-price lunch by completing an application. As such, the number of students reported for Direct certification (DG813) should always be lower than the number of students reported for Free lunch (DG565). Additional information can be found in the NCES blog post titled [Understanding School Lunch Eligibility in the Common Core of Data.](https://nces.ed.gov/blogs/nces/post/understanding-school-lunch-eligibility-in-the-common-core-of-data)

**Are both DGs required?**

No. States are required to submit <u>either</u> DG565 (Free and reduced-price lunch) or DG813 (direct certification) data for operational schools with membership (FS 052) greater than zero and with NSLP Status that is not “No.”

**If we have both DGs, does ED prefer that we submit both?**

If both data elements are available, ED prefers that the state provide data for both. Both values are useful for data quality checks and provide valuable information for data users to understand the difference between free and reduced-price lunch and direct certification data.

**How are schools that certify for the NSLP participation without collecting eligibility data or certifying students each year reported?**

Schools participating in the NSLP under Provisions 2 or 3 or the Community Eligibility Option (CEO) are not required to collect eligibility data and certify students each year.  Report current headcounts of free and reduced-price lunch students, when possible.  If the data are not available due to schools implementing the NSLP provisions, estimate the count of students by multiplying current year membership by the percentage of eligible students in the most recent year for which the school collected that information.

**Are records required for both free and reduced-price lunch?**

If detailed records are submitted for category set A, records must be submitted for each school for both free and reduced-price lunch. Submission errors will be triggered if records are submitted for one but not the other.

**How to report DG565 (Free and reduced-price lunch) when students cannot be disaggregated between free and reduced-price lunch?**

If students cannot be disaggregated between free and reduce-price lunch, report only the total count for Total of Education Unit. Do not include records for Category Set A. Below is an example of the record. Additionally, please provide a data note in EDPass.

| **Aggregation** | **Example** |
|---|---|
| Format | File Record Number,State Code,State Agency Number,LEA Identifier (state),School Identifier (state),Table Name,Lunch Program Status,Total Indicator,Explanation,Student Count,Carriage Return / Line Feed (CRLF) |
| DG 565<br>Total of education unit | 3,99,01,LEA001,SCH001,LUNCHFREERED,,Y,,{insert total number of students here} |

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
| filename | **PRICELNCH** | 9 |
| vvvvvvv | Alphanumeric string designated by the SEA to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| .ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 4 |

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
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SCHOOL FREE AND REDUCED PRICE LUNCH** |
| Total Records In File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 168 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 295 | 1 |  | M |  |  |

Below is an example of a header record.

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | SCHOOL FREE AND REDUCED PRICE LUNCH,15,EUSCHPRICELNCHver0007.CSV,characters to identify file,2026-2027,¶                  |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide counts for the specified category sets, subtotals and education unit totals.

**Table 4.2–1: Data Records**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two–digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (state) | 15 | 14 | String | M | The identifier assigned to a local education agency (LEA) by the state education agency (SEA). Also known as State LEA Identification Number (ID). This data element cannot be updated through this file. |  |
| **DG5** School Identifier (state) | 29 | 20 | String | M | The identifier assigned to a school by the state education agency (SEA). Also known as the State School Identification Number (ID). This ID cannot be updated through this file. |  |
| Table Name | 49 | 20 | String | M | See technical names in Section 2.3 Required Categories and Totals | **LUNCHFREERED**<br>**DIRECTCERT** |
| Lunch Program Status | 69 | 15 | String | A | An indication of students' qualification for free or reduced-price lunch. | **FL –** Free lunch qualified<br>**RPL –** Reduced-price lunch qualified<br>**MISSING** |
| Total Indicator | 84 | 1 | String | M | An indicator that defines the count level – see table 2.3-1 “Required Categories and Totals” | **N** – Specifies category set<br>**Y** – Specifies subtotal or total of the education unit |
| Explanation | 85 | 200 | String | O | Text field for state use. |  |
| Student Count | 285 | 10 | Integer | M |  |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 295 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit. See table 2.3-1.

**Table 4.2–2: Data Record Example – School level**

| **Aggregation** | **Example** |
|---|---|
| Format | File Record Number,State Code,State Agency Number,LEA Identifier (state),School Identifier (state),Table Name,Lunch Program Status,Total Indicator,Explanation,Student Count,Carriage Return / Line Feed (CRLF) |
| DG 565<br>Category Set A<br>Reduced Price Lunch | 1,99,01,LEA001,SCH001,LUNCHFREERED,RPL,N,,150¶ |
| DG 565<br>Category Set A<br>Free Lunch | 2,99,01,LEA001,SCH001,LUNCHFREERED,FL,N,,250¶ |
| DG 565<br>Total of education unit | 3,99,01,LEA001,SCH001,LUNCHFREERED,,Y,,400¶ |
| DG 813<br>Total of education unit | 1,99,01,LEA001,SCH001,DIRECTCERT,,Y,,75¶ |

## Document History

| **Version Number** | **Date**       | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |                | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | September 2026 | Updated for SY 2026-27.                                                                 |
