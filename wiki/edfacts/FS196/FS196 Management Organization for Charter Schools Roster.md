---
fs_id: FS196
title: "Management Organization for Charter Schools Roster"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG825, DG826, DG827, DG828, DG829]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [Directory]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS196-v23.0--edfacts-fs196-23-0-dg825-dg826-dg827-dg828-dg829-management-organization-charter-schools-roster-v230-114443.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs196-23-0-dg825-dg826-dg827-dg828-dg829-management-organization-charter-schools-roster-v230-114443.docx"
sha256: e696c453eb682c6f6e834db72abc03167434b04d456e3cfcb85065b07a9d59a7
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS196 — Management Organization for Charter Schools Roster (v23.0)

> [!abstract] FS196 at a glance
> **Data groups:** DG825, DG826, DG827, DG828, DG829
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** Management Organizations
> **Reporting Period:** School Year (state) - Any 12-month period defined by the state. The state determines whether summer is included in the preceding or following school year
> **Categories:** Management Organization Type
> **Data record:** 24 fields, 791 characters fixed-width
> **Generate domain:** [[Directory]]
> **Business rules:** [[FS196 Business Rules]] (BRSI SY 2025-26)
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS196-v23.0--edfacts-fs196-23-0-dg825-dg826-dg827-dg828-dg829-management-organization-charter-schools-roster-v230-114443.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit the following EDFacts data groups:

**Table 1.0-1: EDFacts data groups**

| **Data Group Name**                  | **DG** | **Definition**                                                                                                                                                                |
|--------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Management organization name         | 825    | The full legally accepted name of the management organization.                                                                                                                |
| Employer identification number (EIN) | 826    | The identification number issued by the IRS in order for the entity to pay federal taxes to the U.S. Treasury and report wages to the IRS and Social Security Administration. |
| Organization address location        | 827    | The set of elements that describes the physical location of the management organization, including the street address, city, state, ZIP Code, and ZIP Code + 4.               |
| Organization address mailing         | 828    | The set of elements that describes the mailing address of the management organization, including the mailing address, city, state, ZIP Code and ZIP Code + 4.                 |
| Management organization type         | 829    | The type of management organization.                                                                                                                                          |

In the school level files for the Directory (FS029), states mark schools as charter schools. In this file, states submit the list of organizations that manage one or more charter school in the state. If a state has reported schools in the FS029 School Directory file that were managed by a Management Organization, then the state is expected to report the Management Organization in this file.

The data collected using this file specification are gathered to provide the Charter School Programs (CSP) Office of the U.S. Department of Education (Department) insight into the extent and scope of the relationships between management organizations and charter schools. The federal grant funds provided to states are allocated to schools that work with such non-profit and for-profit organizations, which assist in directly managing and overseeing the charter schools, without always having accountability to a district or the state. Funds may be provided to non-profit charter management organizations (CMOs) directly through CSP Replication and Expansion grants. It is important that the Department begins to form a roster of these organizations to provide stronger oversight and accountability for federal funds.

The data collected using this file specification are collected under the authority of the Elementary and Secondary Education Act of 1965 (ESEA), as amended by the Every Student Succeeds Act (ESSA).

The ED data stewarding office/s for this file: OESE

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than any editorial changes listed in the document history on page ii, there have been no other changes to this file specification.

### Core Requirements for Submitting this File

**Table 2.2-1: Core Reporting Requirements**

|                                     | **Management Organizations**                                                                                                                              |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reporting Period                    | School Year (state) - Any 12-month period defined by the state. The state determines whether summer is included in the preceding or following school year |
| Education units included            | Any entity that managed operational, future, or inactive charter schools reported in FS029 Directory                                                      |
| Education units <u>not</u> reported | Management organizations that did not manage charter schools reported in FS029 Directory                                                                  |

**Data Packages**

There are file specifications that contain a requirement that the data file and metadata or a related file must be submitted together. FS196 must be submitted together with FS197 (DG833) — Crosswalk of Charter Schools to Management Organizations.

### Required Categories and Totals

This section is not used for this file specification.

### Categories and Permitted Values

This section contains the categories and permitted values used for submitting this file.

**DG829 - Management organization type:**

**Management Organization Type**

The type of management organization.

| **Permitted Value Abbreviation** | **Permitted Value Description**         | **Comments**                                                                                                                                                                                  |
|----------------------------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CHARCMO                          | Charter Management Organization (CMO)   | A non-profit organization that operates or manages a network of charter schools (either through a contract or as the charter holder) linked by centralized support, operations, and oversight |
| CHAREMO                          | Education Management Organization (EMO) | A for-profit entity that operates or manages a network of charter schools (either through a contract or as the charter holder) linked by centralized support, operations, and oversight.      |
| CHARSMNP                         | Single Management (non-profit)          | A non-profit organization that is not a CMO or EMO and that provides management services to one charter school.                                                                               |
| CHARSMFP                         | Single Management (for-profit)          | A for-profit entity that is not a CMO or EMO and that provides management services to one charter school.                                                                                     |

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

All responses in this section are technical clarifications to assist data submitters and are not associated with statutory, regulatory, or policy guidance.

#### Management Organization Type (DG829)

**We do not have any Management Organizations operating in our state. Do we still need to report these data?**

Any charter school with a management organization would need to be identified for this data collection. However, if there are no management organizations operating charter schools in your state (i.e., every charter school is an independent, single, stand-alone entity), then the state is not required to submit these data. Please refer to the definition of Management Organization in Section 2.6.

#### Employer Identification Number (EIN) (DG826)

An Employer Identification Number (EIN) is a nine-digit number that the IRS assigns in the following format: XX-XXXXXXX.

#### Organization Address Location (DG827)

In the file, the location address is divided into the following fields:

- Address Location 1

- Address Location 2

- Address Location 3

- City Location

- State Abbreviation Location

<!-- -->

- ZIP Code Location

- ZIP Code Plus 4 Location

The field “Address Location 1” should only be left blank if 1) it is the same as the mailing address **AND** 2) the mailing address does not contain “PO Box” in it; otherwise the Location Address must also be reported.

When a Location Address is provided, it must be a complete address consisting of a minimum of the following fields:

- Address Location 1

- City Location

- State Abbreviation Location

- ZIP Code Location

If any of the fields listed above is provided, all four must be provided.

Location Address Lines 1, 2, and 3 cannot be a Post Office Box.  Any combination of “PO Box”, “P.O. Box” or “Post Office Box” is invalid.  However, a rural route number, with or without a box number (e.g., RR 3, Box 25), will be accepted.

#### Organization Address Mailing (DG828)

In the file, the mailing address is divided into the following fields:

- Address Mailing 1

- Address Mailing 2

- Address Mailing 3

- City Mailing

- State Abbreviation Mailing

- ZIP Code Mailing

- ZIP Code plus 4 Mailing

The field “Address Mailing 1” is required. If a street address, Post Office box, or rural route is not available, the phrase “No Street Address” should be provided in the field Address Mailing 1 along with a valid city, state abbreviation and ZIP code.

### Definitions

The following definitions support this file:

**Authorized Public Chartering Agency**

The definition of an Authorized Public Chartering Agency from ESEA of 1965, [as amended by ESSA, Section 4310(1)](https://www2.ed.gov/documents/essa-act-of-1965.pdf): *The term ‘‘authorized public chartering agency’’ means a State educational agency, local educational agency, or other public entity that has the authority pursuant to State law and approved by the Secretary to authorize or approve a charter school*. For further clarification about Authorized Public Chartering Agency, see permitted values for Charter Authorizer Type in FS190 (DG807).

**Charter Management Organization**

The definition of a Charter Management Organization from [ESEA of 1965, as amended by ESSA, Section 4310(3):](https://www2.ed.gov/documents/essa-act-of-1965.pdf) *The term ‘‘charter management organization’’ means a nonprofit organization that operates or manages a network of charter schools linked by centralized support, operations, and oversight*.

**Non-Profit Organization**

A non-profit organization is an organization that has:

1)  Proof that the Internal Revenue Service currently recognizes the applicants as an organization to which contributions are tax-deductible under section 501(c)(3) of the Internal Revenue Code;

2)  A statement from a State taxing body or the State attorney general certifying that:

<!-- -->

1.  The organization is a non-profit organization operating within the State; and

2.  No part of its net earnings may lawfully benefit any private shareholder or individual;

<!-- -->

3)  A certified copy of the certificate of incorporation or similar document if it clearly establishes the non-profit status of the applicant; or

4)  Any item described above if that item applies to a State or national parent organization, together with a statement by the State or parent organization that the organization is a local non-profit affiliate.

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
| lev | Abbreviation for level:<br>•<br>SEA for the list of organizations in the state | 3 |
| filename | **CHARMAORG** | 9 |
| vvvvvvv | Alphanumeric string designated by the SEA to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| .ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 4 |

## Fixed or Delimited Files

This section describes the fixed file and delimited file specifications. The fixed file and delimited files contain a header record followed by data records. The file type is specified in the header record.

The “Pop” column in the header and data records is coded as follows:

> M - Mandatory, this field must always be populated
>
> A - If one field marked with ‘A’ is provided, all other fields marked with ‘A’ must be provided
>
> O - Optional, data in this field are optional

### Header Record Definition

The header record is required and is the first record in every file submitted to EDPass. The purpose of the header record is to provide information as to the file type, number of data records in the file, file name, file identifier, and file reporting period.

**Table 4.1–1: Header Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **CHARTER MANAGE ORG** |
| Total Records in File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 333 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF)or Line Feed (LF) | 460 | 1 |  | M |  |  |

Below is an example of a header record.

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | CHARTER MANAGE ORG,15,EUSEACHARMAORGver0007.CSV,characters to identify file,2026-2027,¶                                   |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide information for the management organizations.

**Table 4.2–1: Data Records**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| Filler | 15 | 14 | String | M | Leave filler field blank. |  |
| Filler | 29 | 20 | String | M | Leave filler field blank. |  |
| **DG825** Management | 49 | 60 | String | M | The full legally accepted name of the management organization. |  |
| **DG826** Employer Identification Number (EIN) | 109 | 20 | String | M | The identification number issued by the IRS in order for the entity to pay federal taxes to the U.S. Treasury and report wages to the IRS and Social Security Administration. | Format: XX-XXXXXXX |
| **DG827** Address Location 1 | 129 | 60 | String | A | The street address that describes the physical location. |  |
| **DG827** Address Location 2 | 189 | 60 | String | O | Additional address information that describes the physical location. |  |
| **DG827** Address Location 3 | 249 | 60 | String | O | Additional address information that describes the physical location. |  |
| **DG827** City Location | 309 | 30 | String | A | The name of the city that describes the physical location. |  |
| **DG827** State Abbreviation Location | 339 | 2 | String | A | The state abbreviation for the location address. | Two-character USPS standard state abbreviation<br>(See FS029 Appendix A for list of state abbreviations) |
| **DG827** ZIP Code Location | 341 | 5 | String | A | The five–digit ZIP Code for the location address. | All 5 digits (cannot be 00000 or 99999 or less than 00600) |
| **DG827** ZIP Code Plus 4 Location | 346 | 4 | String | O | The four–digit extension of the ZIP Code for the location address. | All 4 digits (cannot be 0000) |
| **DG828** Address Mailing 1 | 350 | 60 | String | M | The mailing street name and number or Post Office Box. |  |
| **DG828** Address Mailing 2 | 410 | 60 | String | O | Additional mailing street address information. |  |
| **DG828** Address Mailing 3 | 470 | 60 | String | O | Additional mailing street address information. |  |
| **DG828** City Mailing | 530 | 30 | String | M | The mailing address city. |  |
| **DG828** State Abbreviation Mailing | 560 | 2 | String | M | The state abbreviation for the mailing address. | Two-character USPS standard state abbreviation<br>(See FS029 Appendix A for list of state abbreviations) |
| **DG828** ZIP Code Mailing | 562 | 5 | String | M | The five–digit ZIP Code for the mailing address. | All 5 digits (cannot be 00000 or 99999 or less than 00600) |
| **DG828** ZIP Code Plus 4 Mailing | 567 | 4 | String | O | The four–digit extension of the ZIP Code for the mailing address. | All 4 digits (cannot be 0000) |
| **DG829** Management Organization Type | 571 | 20 | String | M | The type of management organization. | **CHARCMO** - Charter Management Organization (CMO)<br>**CHAREMO** - Education Management Organization (EMO)<br>**CHARSMNP –** Single Management (non-profit)<br>**CHARSMFP** – Single Management (for-profit) |
| Explanation | 591 | 200 | String | O | Text field for state use. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 791 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit.

**Table 4.2–2: Data Record Example – Management Organizations**

| Format                                                       | File Record Number,State Code,State Agency Number,Filter,Filler,Management Organization Name, Employer Identification Number (EIN),Address Location 1,Address Location 2,Address Location 3,City Location,State Abbreviation Location,ZIP Code Location,ZIP Code Plus 4 Location,Address Mailing 1,Address Mailing 2,Address Mailing 3,City Mailing,State Abbreviation Mailing,ZIP Code Mailing,ZIP Code Plus 4 Mailing,Management Organization Type,Explanation,Carriage Return / Line Feed (CRLF) |
|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Example - Mailing address is the same as location address    | 1,27,01,,,Heritage Academies,75-0040987,,,,,,,,3850 Broadmoor Ave SE,Suite 201,,Grand Rapids,MI,49512,,CHAREMO,¶                                                                                                                                                                                                                                                                                                                                                                                    |
| Example - Mailing address is different than location address | 1,27,01,,,Heritage Academies,75-0040987,3850 Broadmoor Ave SE,Suite 201,,Grand Rapids,MI,49512,,3850 Broadmoor Ave SE,Suite 201,,Grand Rapids,MI,49512,,CHAREMO,¶                                                                                                                                                                                                                                                                                                                                   |

## Document History

| **Version Number** | **Date**    | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |             | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | August 2026 | Updated for SY 2026-27:                                                                 |
