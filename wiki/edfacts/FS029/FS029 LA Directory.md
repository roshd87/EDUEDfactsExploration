---
fs_id: FS029
title: "LA Directory"
version: "v23.1"
school_year: "SY 2026-27"
data_groups: []
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [Directory]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS029-v23.1--edfacts-fs029-la-23-1-dgs-multiple-la-directory-v231-114415.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs029-la-23-1-dgs-multiple-la-directory-v231-114415.docx"
sha256: ba758ec239106399e1b8413ed3b43dfb810f080aa7802840a93baa2702940b0c
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS029 — LA Directory (v23.1)

> [!abstract] FS029 at a glance
> **Data groups:** multiple
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** DG
> **Data record:** 31 fields, 1080 characters fixed-width
> **Generate domain:** [[Directory]]
> **Business rules:** [[FS029 Business Rules]] (BRSI SY 2025-26)
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS029-v23.1--edfacts-fs029-la-23-1-dgs-multiple-la-directory-v231-114415.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

The purpose of the Directory is to identify Lead Agencies that received an Individuals with Disabilities Education Act (IDEA) Part C formula grant. It serves as the basis of official statistics that provides information on the implementation of IDEA Part C early intervention services.

This document contains technical instructions for building files used to upload and submit the Lead Agency (LA) Directory.

The data collected using this file specification are collected under the authority of the. Education Sciences Reform Act (ESRA). The data submitted in this file specification serve as the backbone for all other reporting.

The ED data stewarding office/s for this file: OSEP

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

1.

2.

### Changes from the SY 2025-26 File Specifications

Other than the editorial changes listed in the document history on page ii, there have been no other changes to this file specification.

### Core Requirements for Submitting this File

This section describes the data submitted for the LA directory. LA Directory data can be organized into the following content areas: unique identifiers and contact information. The table below identifies the data groups submitted for the LA directory.

**Table 2.2-1: Data Groups in the Directory and Type**

| **Type**            | **DG**                       |
|---------------------|------------------------------|
|                     | DG# Name of data group       |
| Unique Identifier   | 559 State Code               |
| Unique Identifier   | 7 Education entity name - LA |
| Unique Identifier   | 570 Lead agency number       |
| Contact Information | 8 Address mailing - LA       |
| Contact Information | 9 Address location - LA      |
| Contact Information | 10 Telephone – LA            |
| Contact Information | 11 Web site address - LA     |

#### Upload of the Directory Files

The LA directory data is rolled over from the previous school year and does not have to be uploaded.

- The LA Directory file only needs to be uploaded if the LA directory data changed.

- The LA directory data from the previous year is rolled over unless replaced with a new LA Directory file.

### Unique Identifiers

The unique identifiers are identifiers and names.

#### State Code (DG559)

Definition - The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States.

Appendix A contains a list of the State Codes.

#### Education Entity Name - LA (DG7)

Definition - The full registered name of the LA reporting Part C data.

Abbreviations should not be used if the full name can be entered in 60 characters. If the name is longer than 60 characters, it will need to be abbreviated.

| ***TIP!*** Appendix B contains a list of recommended abbreviations. |
|--------------------------------------------------------------------------------------------------|

#### Lead Agency Number (DG570)

Definition - A number used to uniquely identify state agencies.

The Lead Agency number assigned to each LA is “02.” This ID cannot be updated through the Directory file.

The directory data for the LA is the directory data for the state agency that administers the Part C IDEA programs regardless of whether other state agencies are involved in coordinating and supervising early intervention services and supports.

#### Address Mailing - LA (DG8)

Definition - The set of elements that describes the mailing address of the Part C LA, including the mailing address, city, state, ZIP Code and ZIP Code + 4.

In the file, the mailing address is divided into the following fields:

| Field | Population | Guidance |
|---|---|---|
| Address Mailing 1 - LA | Required | If a street address, Post Office box, or rural route is not available, use “No Street Address”<br>Include the correct street suffix (Ave, St, Rd)<br>Use only USPS recognized street suffix abbreviations when abbreviating street suffixes. See the [USPS web site](https://pe.usps.com/text/pub28/28apc_002.htm) for those recognized street suffix abbreviations.<br>Include any directional descriptor (North, South, East, West) |
| Address Mailing 2 – LA | Optional |  |
| Address Mailing 3 – LA | Optional |  |
| City Mailing – LA | Required |  |
| State Abbreviation Mailing – LA | Required | If state doesn’t match to the state code for the LA, mark Out-Of-State Indicator as “YES.” |
| ZIP Code Mailing – LA | Required |  |
| ZIP Code plus 4 Mailing – LA | Optional |  |

#### Address Location - LA (DG9)

Definition - The set of elements that describes the physical location of the education entity, including the street address, city, state, ZIP Code and ZIP Code + 4.

The location address is not required. It can be left blank when it is the same as the mailing address. When the mailing address is a post office box, the location must be provided.

In the file, the location address is divided into the following fields:

| Field | When provided | Guidance |
|---|---|---|
| Address Location 1 | Must be included | Include the correct street suffix (Ave, St, Rd)<br>Use only USPS recognized street suffix abbreviations when abbreviating street suffixes. See the [USPS web site](https://pe.usps.com/text/pub28/28apc_002.htm) for those recognized street suffix abbreviations.<br>Include any directional descriptor (North, South, East, West) |
| Address Location 2 | Optional |  |
| Address Location 3 | Optional |  |
| City Location | Must be included |  |
| State Abbreviation Location | Must be included | If state doesn’t match to the state code for the LA, mark Out-Of-State Indicator as “YES.” |
| ZIP Code Location | Must be included |  |
| ZIP Code plus 4 Location | Optional |  |

Location Address Lines 1, 2, and 3 cannot be a Post Office Box. Any combination of “PO Box”, “P.O. Box” or “Post Office Box” is invalid. However, a rural route number, with or without a box number (e.g., RR 3, Box 25), will be accepted.

#### Telephone - LA (DG10)

Definition - The 10-digit telephone number, including the area code, for the LA.

Do not include hyphens, blanks, periods or parentheses.

#### Web Site Address - LA (DG11)

Definition - The Uniform Resource Locator (URL) for the unique address of a Web page of a LA.

Note: This field has a limit of 100 characters.

This field is optional. If a URL is not available or the entity does not have a URL, leave this field blank.

### Required Categories and Totals

This section is not used for this file specification.

### Categories and Permitted Values

This file specification does not use any categories and permitted values.

### Definitions

See the [EDFacts Workbook](https://www.ed.gov/edfacts-workbook) for the standard definitions. This file specification has no additional definitions.

## File Naming Convention

The following file naming convention is to help identify files to provide technical assistance.

A maximum of 25 characters (including the file extension) is allowed for the file name.

The following is the naming convention for file submissions:

> sslevf**ilename**vvvvvvv.ext

**Table 3.0-1: File Naming Convention**

| **Where** | **Means** | **Limit in characters** |
|---|---|---|
| ss | USPS State Abbreviation | 2 |
| lev | Abbreviation for level:<br>•<br>LA for a Lead Agency level | 3 |
| filename | **DIRECTORY** | 9 |
| vvvvvvv | Alphanumeric string designated by the LA to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| .ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 4 |

## Fixed or Delimited Files

This section describes the fixed file and delimited file specifications. The fixed file and delimited files contain a header record followed by data records. The file type is specified in the header record.

The “Pop” column in the header and data records is coded as follows:

> M - Mandatory, this field must always be populated
>
> A - This field is populated in accordance with table 2.3-1 “Required Categories and Totals”
>
> O - Optional, data in this field may not be required

3.

4.

### Header Record Definition

The header record is required and is the first record in every file submitted to EDPass. The purpose of the header record is to provide information as to the file type, number of data records in the file, file name, file identifier, and file reporting period.

**Table 4.1–1: Header Record**

| **Data Element Name** | **Start**<br>**Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SEA DIRECTORY INFO** |
| Total Records In File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the LA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 333 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) | 460 | 1 |  | M |  |  |

Below is an example of a header record.

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | SEA DIRECTORY INFO,15,LADIRECTORYver0007.CSV,characters to identify file,2026-2027,¶                                      |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide counts for the specified category sets, subtotals and education unit totals.

**Table 4.2–1: Data Records**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the Lead Agency that is unique to each row entry within the file. | This will only be “1” for the LA directory |
| **DG559** State Code | 11 | 2 | String | M | See section 2.3.1<br>The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the Appendix A |
| **DG570** Lead Agency Number | 13 | 2 | String | M | See section 2.3.3<br>A number used to uniquely identify lead agencies.<br>This ID cannot be updated through this file. | **02** – Lead Agency |
| Filler | 15 | 14 | String | M | Leave filler fields blank. |  |
| Filler | 29 | 7 | String | M | Leave filler fields blank. |  |
| Filler | 36 | 20 | String | M | Leave filler fields blank. |  |
| Filler | 56 | 12 | String | M | Leave filler fields blank. |  |
| **DG7** Education Entity Name - LA | 68 | 60 | String | M | See section 2.3.2<br>The full registered name of the LA reporting education data. |  |
| **DG11** Web Site Address - LA | 128 | 100 | String | O | See section 2.3.6<br>The Uniform Resource Locator (URL) for the unique address of a Web page of an LA. |  |
| **DG10** Telephone – LA | 228 | 10 | String | M | See section 2.3.5<br>The 10-digit telephone number, including the area code, for the LA.<br>Do not include hyphens, blanks, or parentheses. | Cannot be between 00000000000–2000000000 or 9900000000–9999999999. |
| **DG8** Address Mailing 1 - LA | 238 | 60 | String | M | See section 2.3.4<br>The mailing street name and number or Post Office Box for the LA |  |
| **DG8** Address Mailing 2 - LA | 298 | 60 | String | O | See section 2.3.4<br>Additional mailing street address information for the LA |  |
| **DG8** Address Mailing 3 - LA | 358 | 60 | String | O | See section 2.3.4<br>Additional mailing street address information for the LA |  |
| **DG8** City Mailing - LA | 418 | 30 | String | M | See section 2.3.4<br>The mailing address city for the LA |  |
| **DG8** State Abbreviation Mailing - LA | 448 | 2 | String | M | See section 2.3.4<br>The state abbreviation for the mailing address for the LA | For a list of valid USPS State Abbreviations, refer to Appendix A. |
| **DG8** ZIP Code Mailing – LA | 450 | 5 | String | M | See section 2.3.4<br>The five–digit ZIP Code for the mailing address for the LA | All 5 digits (cannot be 00000 or 99999 or less than 00600) |
| **DG8** ZIP Code Plus 4 Mailing - LA | 455 | 4 | String | O | See section 2.3.4<br>The four–digit extension of the ZIP Code for the mailing address for the LA | If included, all 4 digits (cannot be 0000) |
| **DG9** Address Location 1 - LA | 459 | 60 | String | O | See section 2.4.2.The street address that describes the physical location of the LA |  |
| **DG9** Address Location 2 - LA | 519 | 60 | String | O | See section 2.4.2<br>Additional address information that describes the physical location of the LA |  |
| **DG9** Address Location 3 - LA | 579 | 60 | String | O | See section 2.4.2<br>Additional address information that describes the physical location of the LA |  |
| **DG9** City Location - LA | 639 | 30 | String | O | See section 2.4.2<br>The name of the city that describes the physical location of the LA |  |
| **DG9** State Abbreviation Location – LA | 669 | 2 | String | O | See section 2.4.2The state abbreviation for location address of the LA | For a list of valid USPS State Abbreviations, refer to Appendix A |
| **DG9** ZIP Code Location - LA | 671 | 5 | String | O | See section 2.4.2<br>The five–digit ZIP Code for the location address of the LA | All 5 digits (cannot be 00000 or 99999 or less than 00600) |
| **DG9** ZIP Code Plus 4 Location - LA | 676 | 4 | String | O | See section 2.4.2<br>The four–digit extension of the ZIP Code for the location address of the LA | If included, all 4 digits (cannot be 0000) |
| Filler | 680 | 30 | String | M | Leave filler fields blank. |  |
| Filler | 710 | 30 | String | M | Leave filler fields blank. |  |
| Filler | 740 | 50 | String | M | Leave filler fields blank. |  |
| Filler | 790 | 10 | String | M | Leave filler fields blank. |  |
| Filler | 800 | 80 | String | M | Leave filler fields blank. |  |
| Explanation | 880 | 200 | String | O | Text field for state use. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 1080 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each LA.

**Table D.1.3–2: LA Data Record Example**

| Format  | File Record Number,State Code,State Agency Number,Filler,Filler,Filler,Filler, Education Entity Name - LA,Web Site Address - LA,Telephone - LA,Address Mailing 1 - LA,Address Mailing 2 - LA,Address Mailing 3 - LA,City Mailing - LA,State Abbreviation Mailing - LA,ZIP Code Mailing – LA,ZIP Code Plus 4 Mailing - LA, Address Location 1 - LA,Address Location 2 - LA,Address Location 3 - LA,City Location - LA,State Abbreviation Location - LA,ZIP Code Location – LA,ZIP Code Plus 4 Location - LA,Filler,Filler,Filler,Filler,Filler,Filler,Explanation,Carriage Return / Line Feed (CRLF) |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Example | 1,80,02,,,,,Euphoria Lead Agency,www.doe.k12.eu.us,5552104958,PO Box 1650,Drawer 300,Bin 5,Commons Station,EU,12345,1234,,,,,,,,,,,,,explanation¶                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

SEA data record exampleformat, example

## Appendix A: State Abbreviations and Codes

This Appendix defines the state abbreviations and the two-digit American National Standards Institute (ANSI) codes (01-78). These codes were formerly known as Federal Information Processing Standards (FIPS) codes.

> **Table A-1: State Abbreviations and ANSI Codes**

| **State name**           | **ANSI** | **State abbreviation**            |
|--------------------------|----------|-----------------------------------|
| ALABAMA                  | 01       | AL                                |
| ALASKA                   | 02       | AK                                |
| ARIZONA                  | 04       | AZ                                |
| ARKANSAS                 | 05       | AR                                |
| CALIFORNIA               | 06       | CA                                |
| COLORADO                 | 08       | CO                                |
| CONNECTICUT              | 09       | CT                                |
| DELAWARE                 | 10       | DE                                |
| DISTRICT OF COLUMBIA     | 11       | DC                                |
| FLORIDA                  | 12       | FL                                |
| GEORGIA                  | 13       | GA                                |
| HAWAII                   | 15       | HI                                |
| IDAHO                    | 16       | ID                                |
| ILLINOIS                 | 17       | IL                                |
| INDIANA                  | 18       | IN                                |
| IOWA                     | 19       | IA                                |
| KANSAS                   | 20       | KS                                |
| KENTUCKY                 | 21       | KY                                |
| LOUISIANA                | 22       | LA                                |
| MAINE                    | 23       | ME                                |
| MARYLAND                 | 24       | MD                                |
| MASSACHUSETTS            | 25       | MA                                |
| MICHIGAN                 | 26       | MI                                |
| MINNESOTA                | 27       | MN                                |
| MISSISSIPPI              | 28       | MS                                |
| MISSOURI                 | 29       | MO                                |
| MONTANA                  | 30       | MT                                |
| NEBRASKA                 | 31       | NE                                |
| NEVADA                   | 32       | NV                                |
| NEW HAMPSHIRE            | 33       | NH                                |
| NEW JERSEY               | 34       | NJ                                |
| NEW MEXICO               | 35       | NM                                |
| NEW YORK                 | 36       | NY                                |
| NORTH CAROLINA           | 37       | NC                                |
| NORTH DAKOTA             | 38       | ND                                |
| OHIO                     | 39       | OH                                |
| OKLAHOMA                 | 40       | OK                                |
| OREGON                   | 41       | OR                                |
| PENNSYLVANIA             | 42       | PA                                |
| RHODE ISLAND             | 44       | RI                                |
| SOUTH CAROLINA           | 45       | SC                                |
| SOUTH DAKOTA             | 46       | SD                                |
| TENNESSEE                | 47       | TN                                |
| TEXAS                    | 48       | TX                                |
| UTAH                     | 49       | UT                                |
| VERMONT                  | 50       | VT                                |
| VIRGINIA                 | 51       | VA                                |
| WASHINGTON               | 53       | WA                                |
| WEST VIRGINIA            | 54       | WV                                |
| WISCONSIN                | 55       | WI                                |
| WYOMING                  | 56       | WY                                |
| AMERICAN SAMOA           | 60       | AS                                |
| BUREAU OF INDIAN AFFAIRS | 59       | State where BIE school is located |
| GUAM                     | 66       | GU                                |
| MARSHALL ISLANDS         | 68       | MH                                |
| MICRONESIA               | 64       | FM                                |
| NORTHERN MARIANAS        | 69       | MP                                |
| PUERTO RICO              | 72       | PR                                |
| REPUBLIC OF PALAU        | 70       | PW                                |
| VIRGIN ISLANDS           | 78       | VI                                |

## Appendix B: Recommended Abbreviations

Below is a list of recommended abbreviations.

> **Table B-1: Recommended Abbreviations**

| **Abbreviation** | **Description**                  |
|------------------|----------------------------------|
| ACAD             | Academic                         |
| ADM              | Administration or Administrative |
| AG               | Agriculture                      |
| AGY              | Agency                           |
| BD               | Board                            |
| BOR              | Borough                          |
| CAR              | Career                           |
| CLD              | Child                            |
| CLDN             | Children                         |
| CMTE             | Committee                        |
| CNSM             | Consortium                       |
| CNT              | Central                          |
| CTE              | Career and Technical Education   |
| CTR              | Center                           |
| COM              | Community                        |
| COMM             | Commission                       |
| COMP             | Computer                         |
| COMPHEN          | Comprehensive                    |
| CON              | Consolidated                     |
| COOP             | Cooperative                      |
| CORP             | Corporation                      |
| CORR             | Correction                       |
| CO               | County                           |
| CUR              | Curriculum                       |
| DEPT             | Department                       |
| DIST             | District                         |
| DVL              | Development                      |
| ED               | Education                        |
| EDL              | Educational                      |
| EIS              | Early Intervention Services      |
| ELEM             | Elementary                       |
| ELEMSCH          | Elementary School                |
| EXM              | Exempted                         |
| FAM              | Family                           |
| HLT              | Health                           |
| HM               | Home                             |
| HS               | High School                      |
| IMP              | Improvement                      |
| IND              | Independent                      |
| INST             | Institution                      |
| JCT              | Junction                         |
| JHS              | Junior High School               |
| JR               | Junior                           |
| LA               | Lead Agency                      |
| LOC              | Local                            |
| LRN              | Learning                         |
| MIDSCH           | Middle School                    |
| METRO            | Metropolitan                     |
| MUL              | Multi                            |
| MUN              | Municipal                        |
| NRS              | Nursing                          |
| OP               | Operations                       |
| ORG              | Organization                     |
| PAR              | Parish                           |
| PLT              | Plantation                       |
| PROG             | Program                          |
| PUB              | Public                           |
| REORG            | Reorganized                      |
| RES              | Resource                         |
| RGN              | Region                           |
| RGNL             | Regional                         |
| SCH              | School                           |
| SEC              | Secondary                        |
| SEP              | Separate                         |
| SOC              | Social                           |
| SPEC             | Special                          |
| SR               | Senior                           |
| SRV              | Service                          |
| ST               | State                            |
| SUPT             | Superintendent                   |
| SUPV             | Supervisor                       |
| TECH             | Technical                        |
| TERR             | Territory                        |
| TRD              | Trade                            |
| TRN              | Training                         |
| TWN              | Township                         |
| UNF              | Unified                          |
| UNIV             | University                       |
| UNORG            | Unorganized                      |
| UNT              | United                           |
| VIL              | Village                          |
| VLY              | Valley                           |
| YTH              | Youth                            |

## Document History

| **Version Number** | **Date**       | **Summary of Change**                                                                         |
|---|---|---|
| 1.0 - 22.0         |                | Versions 1.0 through 22.0 are used to build files for prior school years prior to SY 2026-27. |
| 23.0               | August 2026    | Updated for SY 2026-27:                                                                       |
| 23.1               | September 2026 | Corrected typo in table Table D.1.3–2: LA Data Record Example                                 |
