---
fs_id: FS190
title: "Charter Authorizer Directory"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG798, DG805, DG806, DG807, DG808]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [Directory]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS190-v23.0--edfacts-fs190-23-0-dg798-dg805-dg806-dg807-dg808-charter-authorizer-directory-v230-114440.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs190-23-0-dg798-dg805-dg806-dg807-dg808-charter-authorizer-directory-v230-114440.docx"
sha256: b05ff159029eda66c2941573077e5232b4f1666a31a2110bddc8ad545ad560d3
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS190 — Charter Authorizer Directory (v23.0)

> [!abstract] FS190 at a glance
> **Data groups:** DG798, DG805, DG806, DG807, DG808
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** Charter Authorizers
> **Reporting Period:** School Year (state) - Any 12-month period defined by the state. The state determines whether summer is included in the preceding or following school year
> **Categories:** Charter Authorizer Type
> **Data record:** 23 fields, 586 characters fixed-width
> **Generate domain:** [[Directory]]
> **Business rules:** [[FS190 Business Rules]] (BRSI SY 2025-26)
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS190-v23.0--edfacts-fs190-23-0-dg798-dg805-dg806-dg807-dg808-charter-authorizer-directory-v230-114440.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit the following EDFacts data groups:

**Table 1.0-1: EDFacts data groups**

| **Data Group Name**                   | **DG** | **Definition**                                                                                                                                                             |
|---------------------------------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Charter authorizer name               | 798    | The full legally accepted name of the authorized public chartering agency that currently oversees the charter school.                                                      |
| Charter authorizer address location   | 805    | The set of elements that describes the physical location of the authorized public chartering agency, including the street address, city, state, ZIP Code and ZIP Code + 4. |
| Charter authorizer address mailing    | 806    | The set of elements that describes the mailing address of the authorized public chartering agency, including the mailing address, city, state, ZIP Code and ZIP Code + 4.  |
| Charter authorizer type               | 807    | The type of organization.                                                                                                                                                  |
| Charter authorizer identifier (state) | 808    | The unique identifier assigned to an authorized public chartering agency by the SEA.                                                                                       |

The data collected using this file specification are collected under the authority of the Elementary and Secondary Education Act of 1965 (ESEA), as amended by the Every Student Succeeds Act (ESSA).

The ED data stewarding office/s for this file: OESE

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than any editorial changes listed in the document history on page ii, there have been no other changes to this file specification.

### Core Requirements for Submitting this File

**Table 2.2-1: Core Reporting Requirements**

|                                     | **Charter Authorizers**                                                                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reporting Period                    | School Year (state) - Any 12-month period defined by the state. The state determines whether summer is included in the preceding or following school year     |
| Education units included            | Authorized public chartering agencies that are associated with a charter schools reported in FS029 Directory that is operational, future, inactive or closed. |
| Education units <u>not</u> reported | Authorized public chartering agencies that is not associated with a charter school in FS029 Directory                                                         |

### Required Categories and Totals

This section is not used for this file specification.

### Categories and Permitted Values

This section contains the categories and permitted values used for submitting this file.

**DG807 - Charter authorizer type:**

**Charter Authorizer Type**

The organization types that authorize charters.

| **Permitted Value Abbreviation** | **Permitted Value Description**     | **Comments**                  |
|----------------------------------|-------------------------------------|-------------------------------|
| SEA                              | State department of education       |                               |
| SBE                              | State board of education            |                               |
| PCSB                             | Public charter school board         |                               |
| LEA                              | Local education agency              |                               |
| UNI                              | University                          |                               |
| CC                               | Community college                   |                               |
| NONPROFIT                        | Not for profit organization         |                               |
| GOVTENT                          | Non educational government entities | For example, a mayor's office |
| OTH                              | Other                               |                               |

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

All responses in this section are technical clarifications to assist data submitters and are not associated with statutory, regulatory, or policy guidance.

**Do any other file specifications collect related data?**

The purpose in collecting the identifier is to easily link charter schools reported in the Directory (FS029) file to their respective authorizers. There are two fields for charter authorizer identifiers in the Directory. These fields should be filled for each charter school submitted in the Directory file. In the Directory file, if the charter only has one authorizer, only fill out the first field and leave the second field blank. The identifiers in the Directory file and this file specification should match. If the charter school has multiple authorizers, each authorizer should be reported in the Charter Authorizer Directory separately.

#### Charter Authorizer Name (DG798)

**Can abbreviations be used in the name?**

Abbreviations should not be used if the full name can be entered in 60 characters. If the name is longer than 60 characters, it will need to be abbreviated. Appendix B in the FS029 Directory File Specifications contains a list of recommended abbreviations.

#### Charter Authorizer Identifier (State) (DG808)

**Does the state create the charter authorizer identifier or does the authorizer itself create that ID?**

The state is able to create any number they want for this identifier, as long as it is unique within the state. If the authorizer is already an established LEA, the state may use the NCES LEA ID as the charter authorizer identifier.

#### Charter Authorizer Address Mailing (DG806)

In the file, the mailing address is divided into the following fields:

- Address Mailing 1

- Address Mailing 2

- Address Mailing 3

- City Mailing

- State Abbreviation Mailing

- ZIP Code Mailing

- ZIP Code Plus 4 Mailing

The field “Address Mailing 1” is required. If a street address, Post Office box, or rural route is not available, the phrase “No Street Address” should be provided in the field Address Mailing 1 along with a valid city, state abbreviation and ZIP Code.

#### Charter Authorizer Address Location (DG805)

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

If any of the fields listed above are provided, all four must be provided.

Location Address Lines 1, 2, and 3 cannot be a Post Office Box. Any combination of “PO Box”, “P.O. Box” or “Post Office Box” is invalid. However, a rural route number, with or without a box number (e.g., RR 3, Box 25), will be accepted.

### Definitions

The following definitions support this file:

**Authorized Public Chartering Agency**[^1] – An authorized public chartering agency (aka charter authorizer) is a state educational agency, local educational agency, specialized charter granting entity or Independent Public Charter School Board, Higher Education Institute, Non-profit entity, state, county or local governmental entity, or other entity that has the authority pursuant to state law to authorize or approve a charter school, and to decide to renew, not renew, or revoke charter contracts.

**Public Charter School Board** – A public charter school board is an independent, special purpose board that has been delegated the power to authorize charter schools within a state (ex. the District of Columbia Public Charter School Board; Indiana Charter School Board).

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
| lev | Abbreviation for level:<br>•<br>SEA for the list of authorizers in the state | 3 |
| filename | **CHARAUTOR** | 9 |
| vvvvvvv | Alphanumeric string designated by the SEA to uniquely identify the individual submission (*e.g.,* ver1901, v010803) | 7 |
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

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SEA CHARTER AUTHORIZER** |
| Total Records in File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 273 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF)or Line Feed (LF) | 400 | 1 |  | M |  |  |

Below is an example of a header record.**

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | SEA CHARTER AUTHORIZER,15,euseaCHARAUTORv000001.csv,characters to identify file,2026-2027,¶                               |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide the statuses and other data for the education units.

**Table 4.2–1: Data Records**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| Filler | 15 | 14 | String | M | Filler field leave blank |  |
| Filler | 29 | 20 | String | M | Filler field leave blank |  |
| **DG 798** Charter authorizer name | 49 | 60 | String | M | The full legally accepted name of the authorized public chartering agency that currently oversees the charter school. |  |
| **DG 808** Charter authorizer identifier (state) | 109 | 20 | String | M | The unique identifier assigned to an authorized public chartering agency by the SEA. |  |
| **DG806** Address Mailing 1 | 129 | 60 | String | M | The mailing street name and number or Post Office Box. |  |
| **DG806** Address Mailing 2 | 189 | 60 | String | O | Additional mailing street address information. |  |
| **DG806** Address Mailing 3 | 249 | 60 | String | O | Additional mailing street address information. |  |
| **DG806** City Mailing | 309 | 30 | String | M | The mailing address city. |  |
| **DG806** State Abbreviation Mailing | 339 | 2 | String | M | The state abbreviation for the mailing address. | Two-character USPS standard state abbreviation<br>(See FS029 Appendix A for list of state abbreviations) |
| **DG806** ZIP Code Mailing | 341 | 5 | String | M | The five–digit ZIP Code for the mailing address. | All 5 digits (cannot be 00000 or 99999 or less than 00600) |
| **DG806** ZIP Code Plus 4 Mailing | 346 | 4 | String | O | The four–digit extension of the ZIP Code for the mailing address. | All 4 digits (cannot be 0000) |
| **DG805** Address Location 1 | 350 | 60 | String | A | The street address that describes the physical location. |  |
| **DG805** Address Location 2 | 410 | 60 | String | O | Additional address information that describes the physical location. |  |
| **DG805** Address Location 3 | 470 | 60 | String | O | Additional address information that describes the physical location. |  |
| **DG805** City Location | 530 | 30 | String | A | The name of the city that describes the physical location. |  |
| **DG805** State Abbreviation Location | 560 | 2 | String | A | The state abbreviation for the location address. | Two-character USPS standard state abbreviation<br>(See FS029 Appendix A for list of state abbreviations) |
| **DG805** ZIP Code Location | 562 | 5 | String | A | The five–digit ZIP Code for the location address. | All 5 digits (cannot be 00000 or 99999 or less than 00600) |
| **DG805** ZIP Code Plus 4 Location | 567 | 4 | String | O | The four digit extension of the ZIP Code for the location address. | All 4 digits (cannot be 0000) |
| **DG807** Charter Authorizer Type | 571 | 15 | String | M | The type of organization. | **SEA** - State department of education<br>**SBE** - State board of education<br>**PCSB** - Public charter school board<br>**LEA** - Local educational agency<br>**UNI** - University<br>**CC** - Community college<br>**NONPROFIT** – Not for profit organization<br>**GOVTENT** – Non educational government entities<br>**OTH** – Other |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 586 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit.

**Table 4.2–2: Data Record Example**

| Format                                                    | File Record Number,State Code,State Agency Number,Filler,Filler,Charter Authorizer Name,Charter Authorizer Identifier (State),Address Mailing 1,Address Mailing 2,Address Mailing 3,City Mailing,State Abbreviation Mailing,ZIP Code Mailing,ZIP Code Plus 4 Mailing,Address Location 1,Address Location 2,Address Location 3,City Location,State Abbreviation Location,ZIP Code Location,ZIP Code Plus 4 Location,Charter Authorizer Type,Carriage Return / Line Feed (CRLF) |
|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Example – Mailing address same as location address        | 1,80,01,,,North Townville County Charterization Center,CHART001,711 Pilcrow Ct,,,Townville,HA,99998,,,,,,,,,PCSB¶                                                                                                                                                                                                                                                                                                                                                             |
| Example – Mailing address different from location address | 1,80,01,,,North Townville County Charterization Center,CHART001,PO Box 345,,,Pilcrow,CT,99987,0345,5711 Pilcrow Ct,,,Townville,HA,99998,PCSB¶                                                                                                                                                                                                                                                                                                                                 |

## Document History

| **Version Number** | **Date**    | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |             | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | August 2026 | Updated for SY 2026-27:                                                                 |
