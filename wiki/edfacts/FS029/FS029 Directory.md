---
fs_id: FS029
title: "Directory"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: []
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [Directory]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS029-v23.0--edfacts-fs029-23-0-dgs-multiple-directory-v230-114414.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs029-23-0-dgs-multiple-directory-v230-114414.docx"
sha256: 2f2e9b761ab973a6b37531479ad2192c242fbf3216dc349a57ef80a15d457951
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS029 — Directory (v23.0)

> [!abstract] FS029 at a glance
> **Data groups:** multiple
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Data record:** 31 fields, 1080 characters fixed-width
> **Generate domain:** [[Directory]]
> **Business rules:** [[FS029 Business Rules]] (BRSI SY 2025-26)
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS029-v23.0--edfacts-fs029-23-0-dgs-multiple-directory-v230-114414.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

The purpose of the Directory is to identify all governmental entities providing publicly funded education at the elementary and secondary levels. It serves as the basis of official statistics that provides information on the condition of education.

This document contains technical instructions for building files used to upload and submit the Directory for each education level.

The Directory is a unique file. Therefore, the Directory file specification document is slightly different from the other file specification documents.

| Section | Description                                        |
|---------|----------------------------------------------------|
| 2.1     | Lists the changes from prior school year           |
| 2.2     | Core requirements for the Directory files          |
| 2.3     | Reporting guidelines for unique identifiers        |
| 2.4     | Reporting guidelines for contact information       |
| 2.5     | Reporting guidelines for descriptive information   |
| 2.6     | Reporting guidelines for charters                  |
| 3.0     | Naming convention                                  |
| 4.0     | Guidance on changes to LEAs and schools            |
| 5.0     | Changing state identifiers                         |
| 6.0     | Updating operational status during the school year |

In addition, this document contains several appendices:

| Appendix | Description                                |
|----------|--------------------------------------------|
| A        | State abbreviations and codes              |
| B        | Recommended abbreviations for entity names |
| C        | Charts on operational status               |
| D        | Record layouts and examples                |

Throughout this document, technical hints and explanations are provided in boxes.

The directory is the cornerstone of your EDPass data submissions. Therefore, you are encouraged to review this entire document before uploading and submitting the Directory files for SY 2026-27.

You are also encouraged to review Attachment B Directory Records for the EDFacts Data Set. Attachment B of the EDFacts Information Collection includes an explanation of the directory.

Attachment B can be found on [reginfo.gov](https://www.reginfo.gov/public/do/PRAViewIC?ref_nbr=202505-1850-001&icID=217323). It is listed as:

- Document Type – “Other-Directory”

- Instrument File – “Attachment B Directory EDFacts 2025-26 to 2027-28.docx”

The data collected using this file specification are collected under the authority of the Education Sciences Reform Act (ESRA) and are used in the Non-Fiscal Survey of the Common Core of Data (CCD). The data submitted in this file specification serve as the backbone for all other reporting.

The ED data stewarding office for this file is NCES*,* except for the following data groups for which OESE is the steward:

- Charter LEA Status (DG653)

- Charter Status (DG27)

- Charter Authorizer Identifier (State) (DG804)

## Guidance for Submitting this File

This section contains changes from the previous school year and guidance for submitting this year’s file.

### Changes from the SY 2025-26 File Specification

Other than the guidance/instruction changes listed in the document history on page ii, there have been no other changes to this file specification.

### Core Requirements

An accurate directory must exist for every state at the SEA, LEA and school levels.

#### Data Submitted in the Directory

This section describes the data submitted for the directory. Directory data can be organized into the following content areas: unique identifiers, contact information, descriptive information, and charters. The tables below identify the data groups submitted for each level of the directory.

**Table 2.2.1-1: Data Groups in the Directory by Education Level and Type – Unique Identifiers**

These DGs are explained in section 2.3.

| **SEA**                    | **LEA**                                     | **School**                   |
|----------------------------|---------------------------------------------|------------------------------|
| **DG# Name of data group** | **DG# Name of data group**                  | **DG# Name of data group**   |
| 559 State code             | 559 State code                              | 559 State code               |
| 7 Education entity name    | 7 Education entity name                     | 7 Education entity name      |
| 570 State agency number    | 570 State agency number                     | 570 State agency number      |
|                            | 551 Supervisory union identification number |                              |
|                            | 4 LEA identifier (state)                    | 4 LEA identifier (state)     |
|                            | 1 LEA identifier (NCES)                     | 1 LEA identifier (NCES)      |
|                            |                                             | 5 School identifier (state)  |
|                            |                                             | 529 School identifier (NCES) |

**Table 2.2.1-2: Data Groups in the Directory by Education Level and Type – Contact Information**

These DGs are explained in section 2.4.

| **SEA**                         | **LEA**                         | **School**                      |
|---------------------------------|---------------------------------|---------------------------------|
| **DG# Name of data group**      | **DG# Name of data group**      | **DG# Name of data group**      |
| 8 Address mailing               | 8 Address mailing               | 8 Address mailing               |
| 9 Address location              | 9 Address location              | 9 Address location              |
| 10 Telephone - education entity | 10 Telephone - education entity | 10 Telephone - education entity |
| 11 Web site address             | 11 Web site address             | 11 Web site address             |
|                                 | 669 Out of state indicator      | 669 Out of state indicator      |

**Table 2.2.1-3: Data Groups in the Directory by Education Level and Type – Descriptive Information**

These DGs are explained in section 2.4.

| **SEA** | **LEA** | **School** |
|---|---|---|
| **DG# Name of data group** | **DG# Name of data group** | **DG# Name of data group** |
|  | 16 Operational status – LEA | 531 Operational status – school |
|  | 571 Effective Date | 571 Effective Date |
|  | 453 Local education agency (LEA) type | 21 School type |
|  |  | 743 Reconstituted status |

**Table 2.2.1-4: Data Groups in the Directory by Education Level and Type – Charter Information**

These DGs are explained in section 2.5

| **SEA**                    | **LEA**                    | **School**                                |
|----------------------------|----------------------------|-------------------------------------------|
| **DG# Name of data group** | **DG# Name of data group** | **DG# Name of data group**                |
|                            | 653 Charter LEA status     | 27 Charter status                         |
|                            |                            | 804 Charter authorizer identifier (state) |

Occasionally, an SEA needs to change the state identifiers for its LEAs and schools. The table below lists the data groups used to change state identifiers.

**Table 2.2.1-5: Data Groups Used for Changes to State Identifiers**

These DGs are explained in section 5.0.

|  | **LEA** | **School** |
|---|---|---|
| **Explanation** | **DG# Name of data group** | **DG# Name of data group** |
| Previous state identifier for the LEA | 4P LEA identifier (state) | 4P LEA identifier (state) |
| New state identifier for the LEA | 4N LEA identifier (state) | 4N LEA identifier (state) |
| Previous state identifier for the school |  | 5P School identifier (state) |
| New state identifier for the school |  | 5N School identifier (state) |

#### Reporting Period

The directory data should be reported as of October 1 or the closest school day to coincide with the data reported in FS052 Membership.

If an SEA needs to report that an LEA or school had a different operational status later in the school year, the SEA includes the effective date of the change in operational status as the reporting period. (If the SEA reported the wrong operational status for the start of the school year, that would be a correction of the operational status and not reporting a new or updated operational status.)

The table below lists the data groups used to report a change in operational status.

**Table 2.2.2-1: Data Groups Used for Changes to Operational Status**

These DGs are explained in section 6.0.

|  | **LEA** | **School** |
|---|---|---|
| **Explanation** | **DG# Name of data group** | **DG# Name of data group** |
| New or updated operational status | 16 N Operational status – LEA | 531 N Operational status – school |
| Reporting period for the change of the operational status | 571 Effective Date | 571 Effective Date |

#### Upload of the Directory Files

The SEA directory data is rolled over from the previous school year and does not have to be uploaded. The directory data for the LEA and school levels are school-year specific and will not roll over from the previous school year.

SEA

- The Directory file is uploaded only if the SEA directory data changed.

- The directory data from the previous year is rolled over unless replaced with a new Directory file.

LEA

- The entire LEA Directory must be uploaded for each school year.

- The LEA Directory file must be uploaded **<u>before</u>** the School Directory file is uploaded.

- Records on supervisory unions (LEA Type (DG453) with code “3”) must be uploaded first in an LEA Directory file, which must be processed before records on component LEAs (LEA Type (DG453) with code “2”) are uploaded in a second LEA Directory file.

- After uploading the LEA Directory file, upload the LEA Grades Offered file (FS039).

School

- The entire school Directory must be uploaded for each school year.

- The school Directory file must be uploaded **<u>after</u>** the LEA Directory file is uploaded. After uploading the school Directory file, upload the school Grades Offered file (FS039).

#### Data Packages

There are file specifications that contain a requirement that the data file and metadata or a related file must be submitted together. FS029 must be submitted together with FS190 (Multiple DGs) — Charter Authorizer Directory.

### Unique Identifiers

The unique identifiers are identifiers and names. Care should be taken to validate identifiers since the leading cause of duplicate LEAs and schools is submitting an incorrect NCES ID with an updated state ID and adding or removing leading zeros in state IDs and NCES IDs.

#### State Code (DG559)

Definition - The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States.

[[#APPENDIX A: STATE ABBREVIATIONS AND CODES|Appendix A]] contains a list of the State Codes.

#### Education Entity Name (DG7)

Definition - The full registered name of the school, LEA, SEA, or other entity reporting education data.

Abbreviations should not be used if the full name can be entered in 60 characters. If the name is longer than 60 characters, it will need to be abbreviated.

| ***TIP!*** Appendix B contains a list of recommended abbreviations. |
|--------------------------------------------------------------------------------------------------|

The primary identifiers—NCES and state identifiers—are used in combination with the education unit name and addresses to identify duplicates. It is imperative that each education unit be included only once in the state’s directory.

To avoid confusion,

- Report the LEA name differently from any school names associated with the LEA. For example, add the word “Agency” to the LEA.

- Include the types of grades served in the school name. For example, “Jones School” should be specified as “Jones Elementary School,” “Jones Middle School,” or “Jones High School.”

#### State Agency Number (DG570)

Definition - A number used to uniquely identify state agencies.

The State Agency number assigned to each SEA is “01.” This ID cannot be updated through the Directory file.

The directory data for the SEA is the directory data for the state agency that administers the ESEA programs regardless of whether other state agencies are involved in “coordinating and supervising public elementary and secondary instruction.”

#### LEA Identifier (State) (DG4) and School Identifier (State) (DG5)

Definition DG4 - The identifier assigned to an LEA by the SEA. Also known as the State LEA Identification Number (ID).

Definition DG5 - The identifier assigned to a school by the SEA. Also known as the State School Identification Number (ID).

LEA identifiers (State) submitted to EDPass must be consistent across LEA and school files because they are used to connect LEAs with their schools.

**Tech Tip!** Because the fields for the state identifier are alphanumeric, EDPass views the identifier “0011” as different from “11.” If a state submitted records for an LEA or school where some records use “0011” and other use “11,” EDPass will not link the two and will instead create two separate records. SEAs must be consistent about the use of leading zeros in LEA and school identifiers.

If a state includes leading zeros in the IDs, then the state must always use leading zeros in the IDs.

If a state does not include leading zeros in the IDs, then the state can never use leading zeros in the IDs.

#### LEA Identifier (NCES) (DG1) and School Identifier (NCES) (DG529)

Definition DG1 - The seven-digit unique identifier assigned to the LEA by NCES consisting of the two-digit ANSI state code and a five-digit code unique within the state.

Definition DG529 –The seven-digit unique identifier assigned to the school by NCES consisting of the two-digit ANSI state code and a five-digit code unique within the state.  This identifier can also be presented in a twelve-digit format (consisting of the two-digit ANSI state code, the unique five-digit code for the LEA and the unique five-digit code for the school).

An incomplete NCES identifier will result in an error that prevents the file from be processed.

**Tech Tip!** If a state inadvertently uploads an incorrect NCES identifier to EDPass, update the source file with the correct NCES identifier and reupload the entire directory file using the ‘replace’ option on the upload screen.

All schools and LEAs must have NCES identifiers in the Directory file **UNLESS** the school or LEA has one of the following operational statuses (DG16 or DG531):

- New – Code 3 (if not Future in the prior year)

- Added – Code 4

- Future – Code 7 (only in the first year)

<!-- -->

- For these LEAs and schools, the system will automatically generate an NCES ID

States can retrieve the new NCES IDs by downloading the directory data from EDPass.

**Tech Tip!** If a state identifies an existing school or LEA that has not previously been reported, the state should report the school or LEA with an operational status of “Added” the first time the school or LEA is included in the directory. Schools or LEAs reported as “Added” will be assigned an NCES ID number. If the school or LEA is reported as “Open,” an error will occur that will prevent the file from processing.

#### Supervisory Union Identification Number (DG551)

Definition - The three-digit unique identifier assigned to the supervisory union.

| ***Important!*** If your state does not have supervisory unions or similar entities, leave this field blank. |
|--------------------------------------------------------------------------------------------------------------|

The supervisory union ID is used to link LEAs to each other in a hierarchical relationship. For example, a state has an administrative “all grades” LEA above a high school LEA and an elementary LEA. The supervisory union ID will link the administrative “all grades” LEA with the high school LEA and the elementary LEA.

The supervisory union ID is required for LEAs with the following LEA types (DG453):

- Regular public school district that is a component of a supervisory union (Code 2)

- Supervisory union (Code 3)

For all other LEAs, this field should be left blank.

The supervisory union ID is a three-digit state assigned number. It may be either:

- A state-assigned identifier

- A county code if the county superintendent acts as the administrative center

The supervisory union ID must exist in the administrative LEA (that is, the LEA with Code 3) prior to the supervisory union ID being used in the subordinate LEA with the Code 2. The IDs must match exactly, including how the data are justified in the field. For example, if the supervisory union ID is right justified for the administrative LEA, it must be right justified for the subordinate LEA.

**Tech Tip!** If a state is opening a new supervisory union, the state will have to submit one Directory file to establish the administrative LEAs and a second Directory file to establish and associate the subordinate LEAs.

### Contact Information

The contact information consists of the addresses and phone numbers. Addresses are used to identify duplicates and to obtain locale codes from the U.S. Census Bureau.

#### Address Mailing (DG8)

Definition - The set of elements that describes the mailing address of the education entity, including the mailing address, city, state, ZIP Code and ZIP Code + 4.

In the file, the mailing address is divided into the following fields:

| Field | Population | Guidance |
|---|---|---|
| Address Mailing 1 | Required | If a street address, Post Office box, or rural route is not available, use “No Street Address”<br>Include the correct street suffix (Ave, St, Rd)<br>Use only USPS recognized street suffix abbreviations when abbreviating street suffixes. See the [USPS web site](https://pe.usps.com/text/pub28/28apc_002.htm) for those recognized street suffix abbreviations.<br>Include any directional descriptor (North, South, East, West) |
| Address Mailing 2 | Optional |  |
| Address Mailing 3 | Optional |  |
| City Mailing | Required |  |
| State Abbreviation Mailing | Required | If state doesn’t match to the state code for the SEA, mark Out-Of-State Indicator as “YES.” |
| ZIP Code Mailing | Required |  |
| ZIP Code plus 4 Mailing | Optional |  |

#### Address Location (DG9)

Definition - The set of elements that describes the physical location of the education entity, including the street address, city, state, ZIP Code and ZIP Code + 4.

The location address is not required. It can be left blank when it is the same as the mailing address. When the mailing address is a post office box, the location must be provided.

In the file, the location address is divided into the following fields:

| Field | When provided | Guidance |
|---|---|---|
| Address Location 1 | Must be included | Include the correct street suffix (Ave, St, Rd)<br>Use only USPS recognized street suffix abbreviations when abbreviating street suffixes. See the [USPS web site](https://pe.usps.com/text/pub28/28apc_002.htm) for those recognized street suffix abbreviations.<br>Include any directional descriptor (North, South, East, West) |
| Address Location 2 | Optional |  |
| Address Location 3 | Optional |  |
| City Location | Must be included |  |
| State Abbreviation Location | Must be included | If state doesn’t match to the state code for the SEA, mark Out-Of-State Indicator as “YES.” |
| ZIP Code Location | Must be included |  |
| ZIP Code plus 4 Location | Optional |  |

Location Address Lines 1, 2, and 3 cannot be a Post Office Box. Any combination of “PO Box”, “P.O. Box” or “Post Office Box” is invalid. However, a rural route number, with or without a box number (e.g., RR 3, Box 25), will be accepted.

**Did you know?** ED uses the location address to obtain the locale codes, geographic location and congressional districts of LEAs and schools from the U.S. Census Bureau. Therefore, it is extremely important that the location addresses are accurate.

#### Telephone - Education Entity (DG10)

Definition - The 10-digit telephone number, including the area code, for the education entity.

Do not include hyphens, blanks, periods or parentheses.

**Tech Tip!** If an LEA is not operational, and as such does not have a valid telephone number, use the SEA’s telephone number. If a school is not operational, and as such does not have a valid telephone number, use the LEA’s telephone number.

#### Web Site Address (DG11)

Definition - The Uniform Resource Locator (URL) for the unique address of a Web page of an education entity.

Note: This field has a limit of 100 characters.

This field is optional. If a URL is not available or the entity does not have a URL, leave this field blank.

#### Out of State Indicator (DG669)

Definition - An indication that the mailing or location address of the LEA or school is outside of the state.

This is a simple flag (Yes/No) to indicate whether the school or LEA has an out–of–state address as compared to the state submitting the file.

Each state has a State Code (e.g., Texas’ is 48). If the mailing or location address Postal State Code (e.g., TX) of an LEA or School does not match the state code then set the Out of State indicator to Yes. This will avoid the validation error that would require the addresses to be within the state.

This field is optional and defaults to “No” if left blank.

### Descriptive Information

Descriptive information is submitted only for LEAs and schools. Descriptive information includes various statuses and types used to describe and classify LEAs and schools.

#### Operational Status - LEA (DG16) and Operational Status - School (DG531)

Definition DG16 - The classification of the operational condition of a local education agency (LEA).

Definition DG531 - The classification of the operational condition of a school.

Data for most File Specifications cannot be submitted for LEAs or schools with operational statuses of inactive, closed, and future schools. Closed, inactive or future LEAs may report GEPA data through the Federal Programs file – FS035.

**Tech Tip!** Appendix C “Assigning Operational Status” contains a chart that explains the relationship between the previous school year’s operational status and the current school year’s operational status. It also contains a chart that explains the relationship between an LEA’s operational status and the operational statuses of its schools.

Operational Status – Permitted Values

The operational status codes for LEAs are slightly different than for schools. Status 5 for LEAs is “changed boundary” while status 5 for schools is “changed LEA affiliation.” The definitions of the operational status codes are provided below:

**Table 2.5.1.1-1: Operational Status**

| **Code** | **Status** | **LEA Operational Status – This status applies when the LEA…** | **School Operational Status – This status applies when the school…** |
|---|---|---|---|
| 1 | Open | •<br>In previous SY<br>•<br>Was reported with a status that is operational<br>•<br>In current SY<br>•<br>Is in operation and had no significant changes in geographic boundaries | •<br>In previous SY<br>•<br>Was reported with a status that is operational<br>•<br>In current SY<br>•<br>Is in operation and is affiliated with the same LEA as the previous SY |
| 2 | Closed<br>(Use Inactive for temporarily closures.) | •<br>In previous SY<br>•<br>Was reported with a status that is operational<br>•<br>In current SY<br>•<br>Is NOT in operation and is not expected to be in operation in the future<br>Note: This status is also used to close out future LEAs that never opened. | •<br>In previous SY<br>•<br>Was reported with a status that is operational<br>•<br>In current SY<br>•<br>Is NOT in operation and is not expected to be in operation in the future<br>Note: This status is also used to close out future schools that never opened. |
| 3 | New<br>(Use Future if the LEA or school is not yet in operation.) | •<br>In prior SYs<br>•<br>Was NOT in operation in a prior SY<br>•<br>In current SY<br>•<br>Is in operation<br>Note: This status is used in the first SY that the LEA is operational regardless of whether the LEA was reported as Future in previous SY. | •<br>In prior SYs<br>•<br>Was NOT in operation in a prior SY<br>•<br>In current SY<br>•<br>Is in operation<br>Note: This status is used in the first SY that the school is operational regardless of whether the school was reported as Future in previous SY. |
| 4 | Added | •<br>In previous SY<br>•<br>Was not reported even though it was in operation<br>•<br>In current SY<br>•<br>Is in operation<br>Note: This status is for LEAs that were previously overlooked. | •<br>In previous SY<br>•<br>Was not reported even though it was in operation<br>•<br>In current SY<br>•<br>Is in operation<br>Note: This status is for schools that were previously overlooked. |
| 5 | Changed geographic boundary / Changed LEA affiliation | •<br>In previous SY<br>•<br>Was reported<br>•<br>In current SY<br>•<br>Is in operation but has undergone a significant change in geographic boundaries | •<br>In previous SY<br>•<br>Was reported<br>•<br>In current SY<br>•<br>Is in operation but was previously reported as affiliated with a different LEA |
| 6 | Inactive | •<br>In previous SY<br>•<br>Was reported<br>•<br>In current SY<br>•<br>Is temporarily closed but expected to reopen<br>Note: When an LEA that has been reported as inactive reopens, it is reported as Open (instead of reporting as Reopened) | •<br>In previous SY<br>•<br>Was reported<br>•<br>In current SY<br>•<br>Is temporarily closed but expected to reopen<br>Note: When a school that has been reported as inactive reopens, it is reported as Open (instead of reporting as Reopened) |
| 7 | Future | •<br>In prior SYs<br>•<br>Was not reported with an operational status<br>•<br>In current SY<br>•<br>Is NOT in operation at start of the SY<br>•<br>In future SY<br>•<br>Is scheduled to be in operation within 2 years | •<br>In prior SYs<br>•<br>Was not reported with an operational status<br>•<br>In current SY<br>•<br>Is NOT in operation at start of SY<br>•<br>In future SY<br>•<br>Is scheduled to be in operation within 2 years |
| 8 | Reopened | •<br>In prior SYs<br>•<br>Was reported as Closed within the previous 10 SYs<br>•<br>In current SY<br>•<br>Is in operation<br>Note: A reopened LEA must be reported with the NCES LEA ID it had prior to being reported as closed. | •<br>In prior SYs<br>•<br>Was reported as Closed within the previous 10 SYs<br>•<br>In current SY<br>•<br>Is in operation<br>Note: A reopened school must be reported with the NCES LEA and school IDs it had prior to being reported as closed. |

##### Operational Status – Special Situations

**What if a school/LEA has a very small student population and does not have any students for this year?**

If there are staff in the school/LEA, even if the FTE for staff is unknown:

- Report the school/LEA as 1 for “Open”

- Include the school/LEA in the Membership file (FS052), reporting the education unit total as zero.

If there are no staff assigned to the school/LEA:

- Report the school/LEA as “6” for inactive

- Do not include the school/LEA in the Membership file (FS052)

**What if a school/LEA reopens after it closed?**

LEAs and schools closed in EDFacts as closed in the prior year may be reopened for up to 10 school years. Beyond that 10-year period, the entity should be submitted as new.

The table below lists last SY that a closed LEA or school can be reopened.

> **Table 2.5.1.2-1**

| School Year Closed | Last School Year can be reopened |
|--------------------|----------------------------------|
| 2016-17            | 2026-27                          |
| 2017-18            | 2027-28                          |
| 2018-19            | 2028-29                          |
| 2019-20            | 2029-30                          |
| 2020-21            | 2030-31                          |
| 2021-22            | 2031-32                          |
| 2022-23            | 2032-33                          |
| 2023-24            | 2033-34                          |
| 2024-25            | 2034-35                          |
| 2025-26            | 2036-37                          |

To reopen a school or LEA closed prior to SY 2021-22, provide PSC with the following information.

> **Table 2.5.1.2-2**

| **To reopen LEAs** | **To reopen Schools** |
|---|---|
| •<br>LEA Name<br>•<br>Year closed<br>•<br>State LEA identifier<br>•<br>NCES LEA identifier | •<br>School Name<br>•<br>Year closed<br>•<br>State LEA identifier<br>•<br>NCES LEA identifier<br>•<br>State school identifier<br>•<br>NCES School Identifier |

**What if a school/LEA remains inactive for several years?**

If an LEA or school was reported to EDFacts as inactive in the prior year, it may change status (to open, closed, changed agency, or inactive) without a specific time limit. Schools or LEAs that are inactive require a Directory record each year.

If an LEA or school became inactive before the prior year, a rule failure will be issued. Provide a data note to explain when the school became inactive.

**Tech Tip!** Section 4.0 Provides information about changes to LEAs and schools.

##### Operational Status – Time Frames

The table below lists the limit for each operational status.

**Table 2.4.3.1.3-1: Limits for Operational Statuses**

| **Code** | **Status** | **Limit**                                                                                                                                  |
|----------|------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Open       | No limit                                                                                                                                   |
| 2        | Closed     | Can reopen any time if closed within previous 10 school years.                                                                             |
| 3        | New        | Used for one year then changed to open, closed, changed, or inactive                                                                       |
| 4        | Added      | Used for one year then changed to open, closed, changed, or inactive                                                                       |
| 5        | Changed    | No limit. However, generally used for one year than changed to open, closed, or inactive.                                                  |
| 6        | Inactive   | No set timeline but must be changed to open or closed eventually. ED will check on schools and LEAs that are Inactive for 5 years or more. |
| 7        | Future     | Two years then must be changed to new or closed                                                                                            |
| 8        | Reopened   | Used for one year then changed to open, closed, changed, or inactive                                                                       |

**Did you know?** The CCD closely reviews the list of new LEAs or schools and has the final word on NCES ID assignment. The CCD may change the status indicator of an LEA or school in the CCD files if the LEA or school does not meet the criteria for closing and reopening as “New”. If you are not sure whether a school or LEA meets the criteria for closing and reopening as “New”, please contact PSC for guidance.

#### Local Education Agency (LEA) Type (DG453)

Definition - The classification of an education unit reported in the local education agency (LEA) file.

The chart below explains the LEA types.

**Table 2.5.2-1: LEA Type**

| **Code** | **LEA Type**                                                                  | **Description**                                                                                                                                                                                                                                                                               | **Notes**                                                                                                                                                                       |
|----------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Regular public school district that is not a component of a supervisory union | A regular public school district is a local government administrative authority that governs the education system at a specified local level on behalf of the public and the state that is not a component of a supervisory union.                                                            |                                                                                                                                                                                 |
| 2        | Regular public school district that is a component of a supervisory union     | A regular public school district is a local government administrative authority that governs the education system at a specified local level on behalf of the public and the state that is component of a supervisory union.                                                                  | Each agency given this code must have an entry in the Supervisory Union ID data field.                                                                                          |
| 9        | Specialized public school district                                            | A specialized public school district is a school district that operates one or more schools that are designed for a specific educational need or purpose.                                                                                                                                     |                                                                                                                                                                                 |
| 3        | Supervisory union[^1]                                                         | A supervisory union is an administrative center or county superintendent’s office serving as the administrative center.                                                                                                                                                                       | Each agency given this code must have an entry in the Supervisory Union ID data field.                                                                                          |
| 4        | Service agency                                                                | A service agency is an agency that does not operate schools instead it provides specialized educational services (such as career and technical education) or related services (such as services in IEPs) to other education agencies that the agencies cannot readily provide for themselves. |                                                                                                                                                                                 |
| 5        | State operated agency                                                         | State operated agency is an organization overseen by a state agency that operates schools or programs that provide public elementary and/or secondary level instruction.                                                                                                                      |                                                                                                                                                                                 |
| 6        | Federal operated agency                                                       | Federal operated agency is a federal agency that provides elementary and/or secondary level instruction.                                                                                                                                                                                      |                                                                                                                                                                                 |
| 7        | Independent charter district                                                  | An independent charter district is an education unit created under the state charter legislation that is not under the administrative control of another local education agency and that operates one or more charter schools – and only charter schools.                                     | An individual charter school that acts also as a district and is reported as a district in the LEA Directory file should have an agency type of “Independent charter district”. |
| 8        | Other local education agency                                                  | The “Other education agency” permitted value is available for SEAs that have data to report at the LEA level for an education unit that the SEA has determined is not one of the other types.                                                                                                 | See section 2.5.2.1 below.                                                                                                                                                      |

##### Guidance for Other local education agency

Other education agencies could include:

- Intermediate levels of public agencies that provide education but are not school districts, such as juvenile correctional institutions, sheriff’s offices, or university lab schools;

- Public organizations that are responsible for providing education at sites such as hospitals, residential treatment centers; and

- Postsecondary schools or agencies reported in order to include a postsecondary “shared time” school, such as community colleges or technical institutes.

Do <u>not</u> report the following agencies on the current list as Type 8 - Other education agency:

- Nonpublic PK-12 school agencies (do not include these in the LEA Directory).

- Charter school agencies (these should be reported as Type 7 above).

#### School Type (DG21)

Definition - The classification of schools based on the curriculum concentration.

The chart below explains the school type codes. Charter schools are classified in the same manner as non-charter schools.

**Table 2.4.3.3-1: School Type**

| **Code** | **School Type** | **Description** |
|---|---|---|
| 1 | Regular school | A regular school is a public elementary/secondary school that does not focus primarily on career and technical, special, or alternative education, although it may provide these programs in addition to a regular curriculum. |
| 2 | Special education school | A special education school is a public elementary/secondary school that focuses primarily on serving the educational needs of students with disabilities (IDEA) and which adapts curriculum, materials, or instruction for these students. |
| 3 | Career and technical education school | A career and technical education school is a public elementary/secondary school that focuses primarily on providing secondary students with an occupationally relevant or career–related curriculum, including formal preparation for technical or professional occupations. |
| 4 | Alternative education school | An alternative school is a public elementary or secondary school that addresses the needs of students that typically cannot be met in a regular school program and is designed to meet the needs of students with academic difficulties, students with discipline problems, or both students with academic difficulties and discipline problems.<br>See additional guidance below. |
| 5 | Reportable program | The permitted value “reportable program” is available for SEAs that have data to report to EDFacts at the school level that the SEA has determined does not meet the definition of a public elementary/secondary school.<br>See additional guidance below. |

##### Alternative Education School (Type 4)

Alternative education schools serve students whose needs cannot be met in a traditional classroom setting. These may include students who:

- Are at risk of academic failure or dropping out of school

- Have been suspended or expelled or are at risk of being suspended or expelled

- Are pregnant or parenting

- In dropout recovery or credit recovery

- Are juvenile offenders or “delinquents”

- Engage in high-risk health behaviors

- Are disruptive or exhibit behavioral or discipline problems

- Are chronically truant or absent

- Have health problems that prevent attendance at a regular school

Alternative education schools may be sited in locations other than a traditional school building such as hospitals, mental health centers, jails, or juvenile detention centers. However, a school should NOT be classified as an alternative school solely because it is a residential institution. If it serves the general student population and not one of the student groups listed above, a school should be classified on the basis of the curriculum it offers as a regular, special education, or vocational school.

Schools that primarily serve children with disabilities should NOT be classified as alternative education schools; they should be classified as Special Education Schools.

Charter, magnet and virtual schools should NOT be classified as alternative schools solely because of their status as charter, magnet or virtual schools. Unless they serve a particular student population, they should be classified on the basis of the curriculum they offer as regular, special education, or vocational schools.

##### Reportable Program (Type 5)

To be reported as a reportable program in the Directory, that program or entity:

1.  Is <u>not</u> a public school under the CCD and EDFacts definition of a school; and

2.  Must report students to EDFacts or the CRDC <u>at the school level</u> to meet a specific federal requirement; and

3.  The students reported in the reportable program are eligible to receive free public education from the state.

Examples of Reportable Programs can include (but are not limited to):

- Juvenile detention/residential facilities/juvenile correctional facilities, including short-term detention facilities that are community-based or residential, where children with disabilities (IDEA) receive special education and related services (see also FS002),

- Private schools where children with disabilities (IDEA) receive special education and related services at public expense, homebound/hospital programs and residential facilities (public and private) where children with disabilities (IDEA) receive special education and related services (see also FS002),

- Early childhood programs, postsecondary programs, adult education centers

#### Reconstituted Status (DG743)

Definition – An indication that the school was restructured, transformed, or otherwise changed as a consequence of the state’s accountability system under ESEA or as a result of School Improvement Grants (SIG), but is not recognized as a new school for CCD purposes.

As a consequence of the state’s accountability system under ESEA or as a result of School Improvement Grants (SIG), a school may be restructured, transformed, or otherwise substantially changed in order to improve student achievement. In some instances, such changes may qualify the school as a new school as determined by the state. In these cases, the state will issue the school a new state ID, and the school will start a new accountability history. However, in many cases, such schools will not qualify as a new school for purposes of CCD and will continue to retain the same NCES ID. For example, if a restructured school that is recognized by the state as a new school with a new state ID continues to offer instruction in essentially the same grades or to the same population of students, it would not be considered a new school for purposes of CCD. In these instances, the event of restructuring, transformation, or other similar substantial change needs to be recorded in order to explain likely shifts in trend data. The event of restructuring, transformation, or similar change is recorded using the reconstituted status.

A reconstituted status determination of “Yes” or “No” is needed for all schools. A reconstituted status of “No” applies to any school that has not been restructured, transformed or otherwise substantially changed or one that qualifies as a new school for CCD purposes. The only schools that qualify for a reconstituted status of “yes” are reconstituted schools--*i.e.*, schools that do not qualify as a new school for purposes of CCD and are one of the following:

- In the first year of implementing a turnaround, transformation, or restart model under SIG;

- In the restructuring (implementation) year under ESEA accountability; or

- Experiencing a change under a state-defined accountability system similar to the ESEA restructuring (implementation) year.

To determine whether a school in the bulleted list above has a reconstituted status of “Yes,” first establish whether the school is a new school for purposes of CCD using the guidance in section 4.0 on changes to LEAs and Schools. If the school does not meet the criteria for a new school, then the school has a reconstituted status of “Yes.”

In summary:

- For reconstituted schools that do not meet the CCD criteria for a new school, use the permitted value “Yes.”

- Use the permitted value “No” for all other schools, including new schools as determined by CCD criteria.

**Tech Tip!** A school’s reconstituted status will never be “Yes” when its operational status is “New” (Code 3).

### Charters

This section explains how to report data on charter schools and districts.

#### States without charter schools

States that have no charter schools or no charter LEAs, report the data groups on charter as follows:

> In the LEA file

- Report Charter LEA Status (DG653) as “NA – Not Applicable” when either

  - the state does not have charter schools

  - the state does not permit charter LEAs

> In the school file

- Report Charter Status (DG27) as “Not Applicable”

- Leave the fields for charter authorizer identifier blank

#### Charter Status (DG27)

Definition - An indication that a public school provides free public elementary and/or secondary education to eligible students under a specific charter issued, pursuant to a state charter school law, by an authorized chartering agency/authority and that is designated by such authority to be public charter school.

Permitted Values:

- Yes

- No

- Not Applicable

A state should only use the Not Applicable value for Charter Status when there is no state charter school law.

In some states, a single charter can authorize schools or campuses in multiple locations. If the schools or campuses at each location independently meet the definition of a school, then those schools or campuses should be reported in the Directory individually as regular schools with a charter status of “Yes”.

**Did you know?** The CCD is used as a sampling frame. When multiple schools are reported as a single school, the sampling frame is in error and has to be redone. The rework costs time and money. Therefore, it is important to report each school individually in the Directory. See Section 1 “How directory data are used” in Attachment B of the EDFacts Information Collection (OMB Clearance package) for more information on how the EDFacts Directory is used.

#### Charter Authorizer Identifier (State) (DG804)

Definition - The unique identifier assigned to an authorized public chartering agency by the SEA.

This number is used to link the charter authorizers that will be in the Charter Authorizer Directory (FS 190) to specific charter schools reported in the Directory.

**Why are there two fields for charter authorizer identifier?**

In the situation where a charter may have multiple authorizers, two fields are available to input authorizer identifiers. The first field is for the primary authorizer and the second field is for a secondary authorizer, if there is one. The primary authorizer should be the authorizer that ultimately approves the charter petition, and all listed charter schools will have a primary authorizer. The secondary authorizer field would only be necessary for charter schools that complete a two-step authorization process. The SEA should determine whether a secondary authorizer is included based on the charter authorizing requirements in their state. If the charter school has only one authorizer, fill out the first field and leave the second field blank.

**What identifier should be used?**

These identifiers must match to a record in the Charter Authorizer Roster (FS190). The state is able to create any number they want for these identifiers, as long as it is unique within the state. If the authorizer is already an established LEA, the state may use the NCES or state identifier as the charter identifier.

| **Tech Tip!** – Make sure the charter authorizer identifier used in the Directory file for charter schools match exactly to the identifier used in Charter Authorizer Roster (FS190). |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### Charter LEA Status (DG653)

Definition - The status of a charter district as an LEA for purposes of federal programs.

If LEA type (DG 453) is not an Independent charter district (code 7), then use one of these options:

- **NA** - Not applicable – State does not have charters or state does not permit charter LEAs

- **NOTCHR** - Not a charter district– State has charter LEAs but this LEA is not a charter LEA.

If LEA type (DG 453) is Independent charter district (code 7), then use one of these options:

- **CHRTIDEAESEA** – LEA for federal programs - Charter district which is an LEA for programs authorized under *IDEA, ESEA* and *Perkins*

- **CHRTESEA** – LEA for ESEA and Perkins - Charter district which is an LEA for programs authorized under *ESEA* and *Perkins* but not under *IDEA*

- **CHRTIDEA** – LEA for IDEA - Charter district which is an LEA for programs authorized under *IDEA* but not under *ESEA* and *Perkins*

- **CHRTNOTLEA** – Not LEA for federal programs - Charter district which is not an LEA for federal programs

### Definitions

*Attachment B Directory EDFacts 2025-26 to 2027-28* includes an explanation of the directory and definitions.  Attachment B can be found on [reginfo.com](https://www.reginfo.gov/public/do/PRAViewIC?ref_nbr=202505-1850-001&icID=217323).

## File Naming Convention

The following file naming convention is to help identify files to provide technical assistance.

A maximum of 25 characters (including the file extension) is allowed for the file name.

The following is the naming convention for file submissions:

> sslev**filename**vvvvvvv.ext

**Table 3.0-1: File Naming Convention**

| **Where** | **Means** | **Limit in characters** |
|---|---|---|
| ss | USPS State Abbreviation | 2 |
| lev | Abbreviation for level:<br>•<br>SEA for a State Education Agency level<br>•<br>LEA for a Local Education Agency level<br>•<br>SCH for a school level | 3 |
| filename | DIRECTORY | 9 |
| vvvvvvv | Alphanumeric string designated by the SEA to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| .ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 3 |

## Changes to Leas and Schools

This section covers changes to a state’s LEAs and schools.

### New Schools or LEAs

ED needs to maintain the history and continuity of schools for longitudinal data studies, trend analysis, and research initiatives. Therefore, closing a school and reopening it as “New” is closely reviewed for the appropriate assignment of NCES IDs.

The lists below present possible reasons for creating a new school or LEA, how it relates to the assignment of a new NCES ID, and reasons that would not warrant assigning a new NCES ID.

A new school or LEA should be created (get a new NCES ID assigned) if:

1)  The grade span of the school or LEA changed by more than 3 grades, not including pre-kindergarten or kindergarten as grades;

2)  The school’s or LEA’s physical location changed and the attendance area changed significantly;

3)  Two schools or LEAs of about the same size, or with different grade spans, merge. The two original entities would be closed, and the merged education unit would be reported as a new school or agency.

A new school or LEA should NOT be created (should not get a new NCES ID) if:

- The grade span of the school or LEA changed by 3 grades or less, not including pre-kindergarten or kindergarten;

- The school or LEA’s physical location or address changed, but the attendance area did not change significantly;

- A smaller school or LEA merges with a larger entity that provides essentially the same grade span;

- A school changes charter status or magnet status without significantly changing the attendance area or changing the grade span;

- A school undergoes restructuring under provisions in ESEA;

- The name of a school or LEA changes;

- The state identifier for the school or LEA changes;

- A school changes LEAs or the boundary of an LEA changes without significantly changing the attendance area or changing the grade span.

- A temporary school is set up for reporting enrollments caused by a disruption in the education (e.g., COVID-19 or natural disaster).

When a non-charter public school becomes a charter school several changes can occur. If those changes fall under the reasons to create a new school, listed above, the old public school should close, a new public charter school should be opened and a new NCES ID will be assigned. However, if none of those reasons apply, the school should retain its existing NCES ID, it should get the appropriate operational status (i.e., Open or Changed Agency), and the charter status should be changed from “No” to “Yes”.

If an existing charter public school becomes a regular public school, the same rules apply.

### Merge of LEAs or Schools

When an LEA or school is merged into another LEA or school that provides essentially the same grades, the smaller entity should be closed while the larger entity is left open.

- Smaller entity – Operational status “Closed (2)”

- Larger entity – Operational status “Open (1)” and retains its NCES ID.

When two LEAs or schools of equal size or with different grade spans are merged or consolidated within an existing building or a new physical location, both entities should be closed and a new entity opened.

- Existing schools or LEAs – Operational status “Closed (2)”

- Consolidated new school or LEA – Operational status “New (3)” with a new NCES ID issued

### Split of LEAs or Schools

When an LEA or school splits into two or more entities, the one that retains the most characteristics of the original LEA or school retains the NCES ID number. The characteristics of the LEA or school are related to the student population for the LEA or school, the grades offered, and the attendance area from which the school or LEA draws students.

- LEA or school most like the original – Operational status “Open (1)” and retains its NCES ID

- Additional LEAs or schools created by the split – Operational status “New (3)” with new NCES IDs issued

### Operational School changes LEA

To change the LEA that a school is associated with, when the school is not in Future status, submit a school Directory file for the school. The table below has the relevant fields.

| **Data Element Name** | **Start Position** | **Length** | **Directions to change the LEA that a school is associated with** |
|---|---|---|---|
| **DG4** LEA Identifier (State) | 15 | 14 | Enter the new State identifier for the new LEA. |
| **DG1** LEA Identifier (NCES) | 29 | 7 | Enter the NCES ID for the new LEA |
| **DG5** School Identifier (State) | 36 | 20 | Enter the existing state identifier for the school. |
| **DG529** School Identifier (NCES) | 56 | 5 | Enter the existing NCES identifier for the school. |
| **DG531** Operational Status – School SY Start | 657 | 30 | If the change is at the start of the school year, enter “5” for changed agency.<br>If the change is during the school year, keep this the same as the original record. |
| **DG531N** Operational Status – School New | 687 | 30 | If the change is at the start of the school year, leave this blank.<br>If the change is at the during the school year, enter “5” for changed agency. |
| **DG571** Effective Date | 717 | 10 | If the change is at the start of the school year, leave this blank.<br>If the change is at the during the school year, enter the date of the change. The date must be before 9/30/2026. |
| **DG4P** Prior State LEA ID | 757 | 14 | Enter the state ID for the previous LEA here. |
| **DG5P** Prior State School ID | 771 | 20 | Leave this blank. |

Fill in all other applicable fields.

EDPass will check that the IDs in the following fields have been reported previously:

- DG5 School Identifier (State)

- DG4 LEA Identifier (State)

- DG4P Prior State LEA ID

If the IDs are not found, then an error will trigger.

The change takes effect once the upload of the file is complete.

**Tech Tip!** If the school is changing to a new LEA, then the state must first submit an LEA record for the new LEA before submitting the school record that changes the LEAs association.

### Future School changes LEA

When a future school changes LEA, the original school must be closed and a new school created.

If a school is in Future status and needs to move from one LEA to another:

- Original school in the old LEA – Operational Status “Close” (2)

- School in the new LEA – Operational Status “Future” (7)

## Changing State Identifiers

This section covers changing state identifiers. Moving a school to another LEA is covered in Section 4.0.

States can change State LEA Identifiers (DG4) and State school Identifiers (DG5). However, states **<u>cannot</u>** change NCES Identifiers for either LEAs (DG1) or schools (DG529).

When changing state identifiers, there is a previous state identifier referred to as DG4P or DG5P and there is a new state identifier referred to as DG4N and DG5N.

In the record for the LEA or school, the new state identifier (DG4N or DG5N) will be reported in the field for DG4 or DG5 since the new state identifier will become the state identifier. The previous state identifier (DG4P or DG5P) will be reported in the field for the previous state identifier.

### Changing the State LEA Identifier

To change or update a State LEA Identifier in an LEA Directory File, below are the relevant fields:

| **Data Element Name** | **Start Position** | **Length** | **Directions to change the state LEA Identifier in the LEA Directory** |
|---|---|---|---|
| **DG4** LEA Identifier (State) | 15 | 14 | Enter the new State LEA Identifier |
| **DG1** LEA Identifier (NCES) | 29 | 7 | Enter the existing NCES ID here. |
| **DG4P** Prior State LEA ID | 771 | 14 | Enter the previous (old) State LEA Identifier |

EDPass will check that the ID in the field “Prior State LEA ID” was indeed a previously reported state LEA ID. If the ID was not found, then an error will trigger.

If the ID reported in the “Prior State LEA ID” is found, then all schools associated with the previous State LEA Identifier will be updated to the new State LEA Identifier.

The change takes effect after the upload of the file is completed.

### Changing the State School Identifier

To change or update a State school identifier in a school Directory file, below are the relevant fields:

| **Data Element Name** | **Start Position** | **Length** | **Directions to change the school identifier in the school Directory** |
|---|---|---|---|
| **DG4** LEA Identifier (State) | 15 | 14 | Enter the existing LEA’s state identifier |
| **DG1** LEA Identifier (NCES) | 29 | 7 | Enter the existing LEA’s NCES identifier |
| **DG5** School Identifier (State) | 36 | 20 | Enter the new State school identifier in the field “DG5 School Identifier (State).” |
| **DG529** School Identifier (NCES) | 56 | 5 | Enter with the school’s existing NCES identifier |
| **DG4P** Prior State LEA ID | 757 | 14 | Enter the previous (old) State LEA identifier if also moving the existing school to a different LEA; otherwise leave blank |
| **DG5P** Prior State School ID | 771 | 20 | Enter the previous (old) State school identifier |

EDPass will check that the ID in the field “Prior State School ID” was indeed a previously reported state school identifier. If the ID is not found, then an error will trigger.

The State LEA Identifier in the field “LEA Identifier (State)” must be the same as the State LEA Identifier associated with the previous State school identifier. If the ID is not the same, an error will be triggered

If the ID reported in the “Prior State School ID” is found, then the state identifier for the school will be changed after the upload of the file is completed.

## Operational Status Changes during the School Year

If an SEA has a requirement to report a change to the operational status for LEAs and schools that occurred after the start of the school year, EDPass can accommodate reporting one update to the operational status. Each LEA and school can have only one operational status at the start of the school year and can have but not required one new or updated operational status for after the start of the school year.

When the new or updated operational status is known before the due date of the Directory, the SEA should include the new or updated operational status in the file. If the change is identified after the due date of the Directory, the SEA will need to request a correction opportunity to update the operational status.

**Operational to nonoperational during the school year**

When an LEA or school is identified as changing the status from operational (i.e., open, new, added, changed, or reopened) to nonoperational (i.e., closed, inactive, or future) after the beginning school year, SEAs can, but not required to, provide an updated status. SEAs can also wait until the next school year to report the school as nonoperational. For the data collected at the end of the school year (e.g., FS032 and FS040), if business rules trigger because of the omission of data records for the nonoperational LEA or school, instead of updating the operational status, SEAs can add a data note to the rule failure indicating that the entity became nonoperational during the school year and thus there is no data for the entity.

**Nonoperational to operational during the school year**

When an LEA or school is identified as changing the status from nonoperational to operational after the beginning of the school year, SEAs need to request a correction opportunity to update the status so other EDFacts data can be submitted for the LEA or school.

### LEA changes Operational Status after start of the school year

To report a new or updated operational status for an LEA after the start of the school year, below are the relevant fields:

| **Data Element Name** | **Start Position** | **Length** | **Directions to report a change in operational status for an LEA** |
|---|---|---|---|
| **DG16** Operational Status – LEA SY Start | 671 | 30 | Enter the operational status from the original directory record |
| **DG16N** Operational Status – LEA New | 701 | 30 | Enter the new or updated operational status |
| **DG571** Effective Date | 731 | 10 | Enter the date that the operational status changed. The date must be before 9/30/2026. |

#### LEA opens after the start of the school year

To report an LEA that opens after the start of the school year, below are the relevant fields:

| **Data Element Name** | **Start Position** | **Length** | **Directions to report LEA that opens after the start of the school year.** |
|---|---|---|---|
| **DG1** LEA Identifier (NCES) | 29 | 7 | Leave blank |
| **DG16** Operational Status – LEA SY Start | 671 | 30 | Enter “7” for “Future” |
| **DG16N** Operational Status – LEA New | 701 | 30 | Enter “3” for “New” |
| **DG571** Effective Date | 731 | 10 | Enter the date the LEA opened. The date must be before 9/30/2027. |

### School changes Operational Status after start of the school year

To report a new or updated operational status for a school after the start of the school year, below are the relevant fields:

| **Data Element Name** | **Start Position** | **Length** | **Directions to report a change in operational status for a school** |
|---|---|---|---|
| **DG531** Operational Status – School SY Start | 657 | 30 | Enter the operational status from the original directory record |
| **DG531N** Operational Status – School New | 687 | 30 | Enter the new or updated operational status |
| **DG571** Effective Date | 717 | 10 | Enter the date that the operational status changed. The date must be before 9/30/2027. |

#### School opens after the start of the school year

To report a school that opens after the start of the school year, below are the relevant fields:

| **Data Element Name** | **Start Position** | **Length** | **Directions to report school that opens after the start of the school year.** |
|---|---|---|---|
| **DG529** School Identifier (NCES) | 56 | 5 | Leave blank |
| **DG531** Operational Status – School SY Start | 657 | 30 | Enter “7” for “Future” |
| **DG531N** Operational Status – School New | 687 | 30 | Enter “3” for “New” |
| **DG571** Effective Date | 717 | 10 | Enter the date the school opened. The date must be before 9/30/2027. |

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

## Appendix C: Assigning Operational Status

This appendix includes charts for both individual LEA or school statuses and for statuses between LEAs and their schools.

**LEA or school statuses**

The chart below indicates what operational statuses are allowable based on the previously reported operational status for an LEA or school. For more information about operational status, see section 2.5.1.

**Table C-1: Verifying Reported CCD School/Agency Operational Status Against Previously Reported Status**

|                                   |                               | **Reported Operational Status** |              |           |             |               |                |              |                |                            |
|-----------------------------------|-------------------------------|---------------------------------|--------------|-----------|-------------|---------------|----------------|--------------|----------------|----------------------------|
|                                   |                               | **1-OPEN**                      | **2-CLOSED** | **3-NEW** | **4-ADDED** | **5-CHANGED** | **6-INACTIVE** | **7-FUTURE** | **8-REOPENED** | **Omit from CY Directory** |
| **Previously Operational Status** | **1-OPEN**                    | **Yes**                         | **Yes**      | **X**     | **X**       | **Yes**       | **Yes**        | **X**        | **X**          | **X**                      |
|                                   | **2-CLOSED**                  | **X**                           | **X**        | **X**     | **X**       | **X**         | **X**          | **X**        | **Yes**        | **Yes**                    |
|                                   | **3-NEW**                     | **Yes**                         | **Yes**      | **X**     | **X**       | **Yes**       | **Yes**        | **X**        | **X**          | **X**                      |
|                                   | **4-ADDED**                   | **Yes**                         | **Yes**      | **X**     | **X**       | **Yes**       | **Yes**        | **X**        | **X**          | **X**                      |
|                                   | **5-CHANGED**                 | **Yes**                         | **Yes**      | **X**     | **X**       | **Yes**       | **Yes**        | **X**        | **X**          | **X**                      |
|                                   | **6-INACTIVE**                | **Yes**                         | **Yes**      | **X**     | **X**       | **Yes**       | **Yes**        | **X**        | **X**          | **X**                      |
|                                   | **7-FUTURE**                  | **X**                           | **Yes**      | **Yes**   | **X**       | **X**         | **X**          | **Yes**      | **X**          | **X**                      |
|                                   | **8-REOPENED**                | **Yes**                         | **Yes**      | **X**     | **X**       | **Yes**       | **Yes**        | **X**        | **X**          | **X**                      |
|                                   | **Omitted from PY Directory** | **X**                           | **X**        | **Yes**   | **Yes**     | **X**         | **X**          | **Yes**      | **Yes**        |                            |

Verifying Reported CCD School/Agency Operational Status Against Previously Reported Status

> **Legend**
>
> Yes - Acceptable
>
> X – Not acceptable
>
> **Notes:**
>
> **Previously Reported Status 2-Closed**
>
> The only acceptable reported status when the previously reported status is “2-Closed” is “8-Reopened.”
>
> **Previously Reported Status 6-Inactive**
>
> Starting in SY 2009-10, an education unit can be inactive indefinitely. If the school or LEA became inactive before SY 2006-07, it cannot be reactivated.
>
> **Reported Status 3-New**
>
> An education unit does not have to be previously reported as “7-Future.”
>
> **Reported Status 8-Reopened**
>
> Starting in SY 2023-24, there is a 10 year limit for reopening.

**LEA and its schools’ statuses**

The chart below indicates what operational statuses are allowable based on the previously reported operational status. For more information about operational status, see section 2.5.1.

**Table C-2: Verifying LEA operational status to the operational statuses of assigned schools**

|                            |                | **School Operational Status** |              |           |             |               |                |              |                |
|----------------------------|----------------|-------------------------------|--------------|-----------|-------------|---------------|----------------|--------------|----------------|
|                            |                | **1-OPEN**                    | **2-CLOSED** | **3-NEW** | **4-ADDED** | **5-CHANGED** | **6-INACTIVE** | **7-FUTURE** | **8-REOPENED** |
| **LEA Operational Status** | **1-OPEN**     | **Yes**                       | **Yes**      | **Yes**   | **Yes**     | **Yes**       | **Yes**        | **Yes**      | **Yes**        |
|                            | **2-CLOSED**   | **X**                         | **Yes**      | **X**     | **X**       | **X**         | **X**          | **X**        | **X**          |
|                            | **3-NEW**      | **X**                         | **X**        | **Yes**   | **X**       | **Yes**       | **X**          | **Yes**      | **X**          |
|                            | **4-ADDED**    | **X**                         | **X**        | **Yes**   | **Yes**     | **Yes**       | **X**          | **Yes**      | **X**          |
|                            | **5-CHANGED**  | **Yes**                       | **Yes**      | **Yes**   | **Yes**     | **Yes**       | **Yes**        | **Yes**      | **Yes**        |
|                            | **6-INACTIVE** | **X**                         | **Yes**      | **X**     | **X**       | **X**         | **Yes**        | **Yes**      | **X**          |
|                            | **7-FUTURE**   | **X**                         | **X**        | **X**     | **X**       | **X**         | **Yes**        | **Yes**      | **X**          |
|                            | **8-REOPENED** | **X**                         | **X**        | **Yes**   | **Yes**     | **Yes**       | **X**          | **Yes**      | **Yes**        |

Verifying Reported CCD School/Agency Operational Status Against Previously Reported Status

## Appendix D: Fixed or Delimited Files

### D.1 SEA Directory File

This section describes the SEA Directory file. States are not required to submit an SEA Directory file each year. Instead, states submit an SEA Directory only when the information changes.

The "Pop" column in the header and data records is coded as follows:

M - Mandatory, this field must always be populated

O - Optional, data in this field are optional

#### D.1.1 Guidance for submitting the SEA Directory File

The SEA Directory file contains the following data groups:

> Unique Identifiers

- State Code (DG559)

- Education Entity Name (DG7)

- State Agency Number (DG570)

> Contact Information

- Address Mailing (DG8)

- Address Location (DG9)

- Telephone - Education Entity (DG10)

- Web Site Address (DG11)

#### D.1.2 SEA Header Record Definition

The header record is required and is the first record in every file uploaded to EDPass. The purpose of the header record is to provide information as to the file type, number of data records in the file, file name, file identifier, and file reporting period.

Table D.1.2–1: SEA Header Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SEA DIRECTORY INFO** |
| Total Records In File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. | 1 |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 753 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 880 | 1 |  | M |  |  |

Below is an example of a header record.

**Table D.1.2–2: SEA Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | SEA DIRECTORY INFO,1,EUSEADIRECTORYver0007.CSV,characters to identify file,2026-2027,¶                                    |

SEA Header Record Exampleformat, example

#### D.1.3 SEA Data Record Definition

Data Records are required and immediately follow the header record in every file uploaded to EDPass. For the Directory file at the SEA level, there is only one Data Record.

**Table D.1.3–1: SEA Data Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. | This will be only be “1” for the SEA directory |
| **DG559** State Code | 11 | 2 | String | M | See section 2.3.1<br>The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the Appendix A |
| **DG570** State Agency Number | 13 | 2 | String | M | See section 2.3.3<br>A number used to uniquely identify state agencies.<br>This ID cannot be updated through this file. | **01** – State Education Agency |
| Filler | 15 | 14 | String | M | Leave filler fields blank. |  |
| Filler | 29 | 7 | String | M | Leave filler fields blank. |  |
| Filler | 36 | 20 | String | M | Leave filler fields blank. |  |
| Filler | 56 | 12 | String | M | Leave filler fields blank. |  |
| **DG7** Education Entity Name - SEA | 68 | 60 | String | M | See section 2.3.2<br>The full registered name of the SEA reporting education data. |  |
| **DG11** Web Site Address - SEA | 128 | 100 | String | O | See section 2.4.4<br>The Uniform Resource Locator (URL) for the unique address of a Web page of an SEA. |  |
| **DG10** Telephone – SEA | 228 | 10 | String | M | See section 2.4.3<br>The 10-digit telephone number, including the area code, for the SEA.<br>Do not include hyphens, blanks, or parentheses. | Cannot be between 00000000000–2000000000 or 9900000000–9999999999. |
| **DG8** Address Mailing 1 - SEA | 238 | 60 | String | M | See section 2.4.1<br>The mailing street name and number or Post Office Box for the SEA |  |
| **DG8** Address Mailing 2 - SEA | 298 | 60 | String | O | See section 2.4.1<br>Additional mailing street address information for the SEA |  |
| **DG8** Address Mailing 3 - SEA | 358 | 60 | String | O | See section 2.4.1<br>Additional mailing street address information for the SEA |  |
| **DG8** City Mailing - SEA | 418 | 30 | String | M | See section 2.4.1<br>The mailing address city for the SEA |  |
| **DG8** State Abbreviation Mailing - SEA | 448 | 2 | String | M | See section 2.4.1<br>The state abbreviation for the mailing address for the SEA | For a list of valid USPS State Abbreviations, refer to Appendix A. |
| **DG8** ZIP Code Mailing – SEA | 450 | 5 | String | M | See section 2.4.1<br>The five–digit ZIP Code for the mailing address for the SEA | All 5 digits (cannot be 00000 or 99999 or less than 00600) |
| **DG8** ZIP Code Plus 4 Mailing - SEA | 455 | 4 | String | O | See section 2.4.1<br>The four–digit extension of the ZIP Code for the mailing address for the SEA | If included, all 4 digits (cannot be 0000) |
| **DG9** Address Location 1 - SEA | 459 | 60 | String | O | See section 2.4.2.The street address that describes the physical location of the SEA |  |
| **DG9** Address Location 2 - SEA | 519 | 60 | String | O | See section 2.4.2<br>Additional address information that describes the physical location of the SEA |  |
| **DG9** Address Location 3 - SEA | 579 | 60 | String | O | See section 2.4.2<br>Additional address information that describes the physical location of the SEA |  |
| **DG9** City Location - SEA | 639 | 30 | String | O | See section 2.4.2<br>The name of the city that describes the physical location of the SEA |  |
| **DG9** State Abbreviation Location – SEA | 669 | 2 | String | O | See section 2.4.2The state abbreviation for location address of the SEA | For a list of valid USPS State Abbreviations, refer to Appendix A |
| **DG9** ZIP Code Location - SEA | 671 | 5 | String | O | See section 2.4.2<br>The five–digit ZIP Code for the location address of the SEA | All 5 digits (cannot be 00000 or 99999 or less than 00600) |
| **DG9** ZIP Code Plus 4 Location - SEA | 676 | 4 | String | O | See section 2.4.2<br>The four–digit extension of the ZIP Code for the location address of the SEA | If included, all 4 digits (cannot be 0000) |
| Filler | 680 | 30 | String | M | Leave filler fields blank. |  |
| Filler | 710 | 30 | String | M | Leave filler fields blank. |  |
| Filler | 740 | 50 | String | M | Leave filler fields blank. |  |
| Filler | 790 | 10 | String | M | Leave filler fields blank. |  |
| Filler | 800 | 80 | String | M | Leave filler fields blank. |  |
| Explanation | 880 | 200 | String | O | Text field for state use. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 1080 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit.

**Table D.1.3–2: SEA Data Record Example**

| Format  | File Record Number,State Code,State Agency Number,Filler,Filler,Filler,Filler, Education Entity Name - SEA,Web Site Address - SEA,Telephone - SEA,Address Mailing 1 - SEA,Address Mailing 2 - SEA,Address Mailing 3 - SEA,City Mailing - SEA,State Abbreviation Mailing - SEA,ZIP Code Mailing – SEA,ZIP Code Plus 4 Mailing - SEA,Address Location 1 - SEA,Address Location 2 - SEA,Address Location 3 - SEA,City Location - SEA,State Abbreviation Location - SEA,ZIP Code Location - SEA,ZIP Code Plus 4 Location - SEA, Filler,Filler,Filler,Filler,Filler,Explanation,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Example | 1,80,01,,,,,Euphoria State Education Agency,www.doe.k12.eu.us,5552104958,PO Box 1650,Drawer 300,Bin 5,Commons Station,EU,12345,1234,123 Elm Street,STE900,Bin 5,Commons Station,EU,12345,1234,,,,,,explanation¶                                                                                                                                                                                                                                                                                                                                                                                               |

SEA data record exampleformat, example

### D.2 LEA Directory File

All LEA directory data are specific to a school year; therefore, states must submit a complete LEA directory each school year.

This section describes the fixed file and delimited file specifications used to transmit information pertaining to the LEA Directory File. The file type is specified in the header record.

The "Pop" column in the header and data records is coded as follows:

M - Mandatory, this field must always be populated

O - Optional, data in this field are optional

X – Population of the field is explained in the definition/comments column

#### D.2.1 Guidance for submitting the LEA Directory File

The LEA Directory file contains the following data groups:

> Unique Identifiers

- State Code (DG559)

- Education Entity Name (DG7)

- State Agency Number (DG570)

- LEA Identifier (State) (DG4)

- LEA Identifier (NCES) (DG1)

- If Local Education Agency (LEA) Type (DG453) is either supervisory union (Code 3) or component of a supervisory union (Code 2), then

  - Supervisory Union Identification Number (DG551)

> Contact information

- Address Mailing (DG8)

- Address Location (DG9)

- Telephone - Education Entity (DG10)

- Web Site Address (DG11)

- Out of State Indicator (DG669)

> Descriptive Information

- Operational Status – LEA (DG16)

- Local Education Agency (LEA) Type (DG453)

Charter Information

- Charter LEA Status (DG653)

#### D.2.2 LEA Header Record Definition

The header record is required and is the first record in every file submitted to EDPass. The purpose of the header record is to provide information as to the file type, number of Data Records in the file, file name, file identifier, and file reporting period.

**Table D.2.2–1: LEA Header Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **LEA DIRECTORY INFO** |
| Total Records in File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 678 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 805 | 1 |  | M |  |  |

Below is an example of a header record.

**Table D.2.2–2: LEA Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | LEA DIRECTORY INFO,10,EULEADIRECTORYver0007.CSV,characters to identify file,2026-2027,¶                                   |

LEA header record exampleformat, example

#### D.2.3 LEA Data Record Definition

Data Records are required and immediately follow the header record in every file uploaded to EDPass. Data Records provide the unique identifiers, contact information, and descriptive information about the LEAs in the state. Each LEA has a record.

**Table D.2.3–1: LEA Data Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the SEA that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | See section 2.3.1<br>The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to Appendix A. |
| **DG570** State Agency Number | 13 | 2 | String | M | See section 2..3.3<br>A number used to uniquely identify state agencies.<br>This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (State) | 15 | 14 | String | M | See section 2.3.4<br>The identifier assigned to an LEA by the SEA. Also known as State LEA Identification Number (ID). |  |
| **DG1** LEA Identifier (NCES) | 29 | 7 | String | X | **Population of this field** -<br>Blank only when operational status is New (when not previously future), Future (first year), or Added<br>See section 2.3.5<br>The seven-digit unique identifier assigned to the LEA by NCES consisting of the two-digit ANSI state code and a five-digit code unique within the state. | Two–digit state code followed by a five–digit local education agency (LEA) code. |
| Filler | 36 | 20 | String | M | Leave filler fields blank. |  |
| Filler | 56 | 12 | String | M | Leave filler fields blank. |  |
| **DG7** Education Entity Name - LEA | 68 | 60 | String | M | See section 2.3.2<br>The full registered name of the LEA reporting education data. |  |
| **DG669** Out of State Indicator | 128 | 3 | String | O | See section 2.4.5<br>An indication that the mailing or location address of the LEA is outside of the state.<br><br>Defaults to NO if blank. | **YES** – The LEA is out of state compared to the SEA.<br>**NO** – The LEA is not out of state compared to the SEA. |
| **DG453** Local Education Agency (LEA) Type | 131 | 1 | String | M | See section 2.5.2<br>The classification of an education unit reported in the local education agency (LEA) file. | **1** – Regular public school district that is not a component of a supervisory union<br>**2** – Regular public school district that is a component of a supervisory union<br>**9** – Specialized public school district<br>**3** – Supervisory union<br>**4** – Service agency<br>**5** – State operated agency<br>**6** – Federal operated agency<br>**7** – Independent charter district<br>**8** – Other local education agency |
| **DG11** Web Site Address - LEA | 132 | 100 | String | O | See section 2.4.4<br>The Uniform Resource Locator (URL) for the unique address of a Web page of an LEA. |  |
| **DG551** Supervisory Union Identification Number | 232 | 7 | String | O | See section 2.3.6<br>The three-digit unique identifier assigned to the supervisory union |  |
| **DG10** Telephone – LEA | 239 | 10 | String | M | See section 2.4.3<br>The 10-digit telephone number, including the area code, for the LEA.<br>Do not include hyphens, blanks, or parentheses. | Cannot be between 00000000000–2000000000 or 9900000000–9999999999. |
| **DG8** Address Mailing 1 - LEA | 249 | 60 | String | M | See section 2.4.1<br>The mailing street name and number or Post Office Box for the LEA. |  |
| **DG8** Address Mailing 2 - LEA | 309 | 60 | String | O | See section 2.4.1<br>Additional mailing street address information for the LEA |  |
| **DG8** Address Mailing 3 - LEA | 369 | 60 | String | O | See section 2.4.1<br>Additional mailing street address information for the LEA |  |
| **DG8** City Mailing - LEA | 429 | 30 | String | M | See section 2.4.1<br>The mailing address city for the LEA |  |
| **DG8** State Abbreviation Mailing - LEA | 459 | 2 | String | M | See section 2.4.1<br>The state abbreviation of the mailing address for the LEA | For a list of valid USPS State Abbreviations, refer to Appendix A |
| **DG8** ZIP Code Mailing - LEA | 461 | 5 | String | M | See section 2.4.1<br>The five–digit ZIP Code for the mailing address for the LEA | All 5 digits (cannot be 00000 or 99999 or less than 00600) |
| **DG8** ZIP Code Plus 4 Mailing - LEA | 466 | 4 | String | O | See section 2.4.1<br>The four–digit extension of the ZIP Code for the mailing address for the LEA | If included, all 4 digits (cannot be 0000) |
| **DG9** Address Location 1 - LEA | 470 | 60 | String | O | See section 2.4.2<br>The street address that describes the physical location of the LEA |  |
| **DG9** Address Location 2 - LEA | 530 | 60 | String | O | See section 2.4.2<br>Additional address information that describes the physical location of the LEA |  |
| **DG9** Address Location 3 - LEA | 590 | 60 | String | O | See section 2.4.2<br>Additional address information that describes the physical location of the LEA |  |
| **DG9** City Location - LEA | 650 | 30 | String | O | See section 2.4.2<br>The name of the city that describes the physical location of the LEA |  |
| **DG9** State Abbreviation Location - LEA | 680 | 2 | String | O | See section 2.4.2<br>The state abbreviation for location address of the LEA | For a list of valid USPS State Abbreviations, refer to Appendix A |
| **DG9** ZIP Code Location – LEA | 682 | 5 | String | O | See section 2.4.2<br>The five–digit ZIP Code for the location address of the LEA | All 5 digits (cannot be 00000 or 99999 or less than 00600)<br>OR<br>blank |
| **DG9** ZIP Code Plus 4 Location - LEA | 687 | 4 | String | O | See section 2.4.2<br>The four–digit extension of the ZIP Code for the location address of the LEA | If included, all 4 digits (cannot be 0000) |
| **DG16** Operational Status – LEA<br>SY Start | 691 | 30 | String | M | See section 2.5.1<br>The classification of the operational condition of a local education agency (LEA)., at the start of the school year | **1** – Open<br>**2** – Closed<br>**3** – New<br>**4** – Added<br>**5** – Changed geographic boundary<br>**6** – Inactive<br>**7** – Future<br>**8** – Reopened |
| **DG16N** Operational Status – LEA New<br>(Previously referred to as “Updated”) | 721 | 30 | String | X | **Population of this field** -<br>Use only if updating the LEA operational status from the start of the SY<br>See section 6.0<br>The new (updated) classification of the operational condition of a local education agency (LEA), if changed during the school year. | **1** – Open<br>**2** – Closed<br>**3** – New<br>**4** – Added<br>**5** – Changed geographic boundary<br>**6** – Inactive<br>**7** – Future<br>**8** – Reopened |
| **DG571** Effective Date | 751 | 10 | String | X | **Population of this field** - Use only if updating the LEA operational status from the start of the SY.<br>See section 6.0<br>The date the operational status changed. | **YYYY-MM-DD**<br>Maximum value is 2026-09-30 |
| **DG653** Charter LEA Status | 761 | 30 | String | M | See section 2.6.4.<br>The status of a charter district as an LEA for purposes of federal programs. | **For LEAs that are not charter:**<br>**NA –** Not applicable<br>**NOTCHR –** Not a charter district<br>**For LEAs that are charter**<br>**CHRTNOTLEA** - Not LEA for federal programs (Charter district which is not an LEA for federal programs)<br>**CHRTIDEA** - LEA for IDEA (Charter district which is an LEA for programs authorized under *IDEA* but not under *ESEA* and *Perkins)*<br>**CHRTESEA** – LEA for ESEA and Perkins (Charter district which is an LEA for programs authorized under *ESEA* and *Perkins* but not under *IDEA)*<br>**CHRTIDEAESEA** – LEA for federal programs (Charter district which is an LEA for programs authorized under *IDEA*, *ESEA* and *Perkins)* |
| **DG4P** Prior State LEA ID | 791 | 14 | String | X | **Population of this field** -<br>Used when the State LEA ID needs to be changed.<br>See Section 5.0 |  |
| Explanation | 805 | 200 | String | O | Text field for state use. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 1005 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit.

**Table D.2.3–2: LEA Data Record Example**

This example is when the LEA is not updating operational status or state identifiers.

| Format  | File Record Number,State Code,State Agency Number,LEA Identifier (State),LEA Identifier (NCES), Filler,Filler, Education Entity Name - LEA,Out of State Indicator,Local Education Agency (LEA) Type,Web Site Address - LEA,Supervisory Union Identification Number,Telephone – LEA,Address Mailing 1 - LEA,Address Mailing 2 - LEA,Address Mailing 3 - LEA,City Mailing - LEA,State Abbreviation Mailing - LEA,ZIP Code Mailing - LEA,ZIP Code Plus 4 Mailing - LEA,Address Location 1 - LEA,Address Location 2 - LEA,Address Location 3 - LEA,City Location - LEA,State Abbreviation Location - LEA,ZIP Code Location - LEA,ZIP Code Plus 4 Location - LEA,Operational Status – LEA SY Start,{blank field unless updating operational status then used for Operational Status – LEA New},{blank field unless updating operational status then used for Effective Date},Charter LEA Status,{blank field unless changing state identifer then used for Prior State LEA ID},Explanation,Carriage Return / Line Feed (CRLF) |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Example | 1,80,01,3400024,8000142,,,Whitcomb USD,N,1,www.whitcombschools.com,,5555559999,204 Main St,,,Whit City,EU,99999,,,,,,,,,1,,,NA,,¶                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

LEA data record exampleformat, example

### D.3 School Directory File

All school directory data are specific to a school year; therefore, states must submit complete a school directory each school year.

This section describes the fixed file and delimited file specifications used to transmit information pertaining to the School Directory File type. The file type is specified in the header record.

The "Pop" column in the header and data records is coded as follows:

M - Mandatory, this field must always be populated

O - Optional, data in this field are optional

X – Population of the field is explained in the definition/comments column

#### D.3.1 Guidance for submitting the School Directory File

The School Directory file contains the following data groups:

> Unique Identifiers

- State Code (DG559)

- Education Entity Name (DG7)

- State Agency Number (DG570)

- LEA Identifier (State) (DG4)

- LEA Identifier (NCES) (DG1)

- School Identifier (State) (DG5)

- School Identifier (NCES) (DG529)

> Contact information

- Address Mailing (DG8)

- Address Location (DG9)

- Telephone - Education Entity (DG10)

- Web Site Address (DG11)

- Out of State Indicator (DG669)

> Descriptive Information

- Operational Status – School (DG531)

- School Type (DG21)

- Reconstituted Status (DG743)

> Charter Information

- Charter Status (DG27)

  - If charter status is “yes,” then

  - Charter Authorizer Identifier (State) – Primary (and if needed, Secondary) Authorizer (DG804)

#### D.3.2 School Header Record Definition

The header record is required and is the first record in every file submitted to the ESS. The purpose of the header record is to provide information as to the file type, number of Data Records in the file, file name, file identifier, and file reporting period.

**Table D.3.2–1: School Header Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SCHOOL DIRECTORY INFO** |
| Total Records in File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 684 | String | M | Leave filler field blank. |  |
| Carriage Return / Line<br>Feed (CRLF) or Line Feed (LF) | 811 | 1 |  | M |  |  |

Below is an example of a header record.

**Table D.3.2–2: School Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | SCHOOL DIRECTORY INFO,105,EUSCHDIRECTORYver0007.CSV,characters to identify file, 2026-2027,¶                              |

#### D.3.3 School Data Record Definition

Data Records are required and immediately follow the header record in every file submitted to EDPass. Data Records provide the unique identifiers, contact information, and descriptive information for the schools in the state. Each school has a record.

**Table D.3.3–1: School Data Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the SEA that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | See section 2.3.1<br>The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to Appendix A |
| **DG570** State Agency Number | 13 | 2 | String | M | See section 2.3.3<br>A number used to uniquely identify state agencies.<br>This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (State) | 15 | 14 | String | M | See section 2.3.4<br>The identifier assigned to an LEA by the SEA. Also known as State LEA Identification Number (ID). |  |
| **DG1** LEA Identifier (NCES) | 29 | 7 | String | O | See section 2.3.5<br>The seven-digit unique identifier assigned to the LEA by NCES consisting of the two-digit ANSI state code and a five-digit code unique within the state. | Two–digit state code followed by a five–digit local education agency (LEA) code. |
| **DG5** School Identifier (State) | 36 | 20 | String | M | See section 2.3.4<br>The identifier assigned to a school by the SEA. Also known as State School Identification Number (ID). |  |
| **DG529** School Identifier (NCES) | 56 | 5 | String | X | **Population of this field** -<br>Blank only when operational status is New (when not previously future), Future (first year), or Added<br>See section 2.3.5.<br>The unique five-digit code for the LEA and the unique five-digit code for the school. | 5 Digits |
| **DG7** Education Entity Name - School | 61 | 60 | String | M | See section 2.3.2<br>The full registered name of the school, LEA, SEA, or other entity reporting education data. |  |
| **DG21** School Type | 121 | 1 | String | M | See section 2.5.3<br>The classification of schools based on the curriculum concentration. | **1** – Regular school<br>**2** – Special education school<br>**3** – Career and technical education school<br>**4** – Alternative education school<br>**5** – Reportable program |
| **DG669** Out of State Indicator | 122 | 3 | String | O | See section 2.4.5<br>An indication that the mailing or location address of the school is outside of the state.<br>Leaving this field blank will use the default value of NO. | **YES** – The school is out of state compared to the SEA.<br>**NO** – The school is not out of state compared to the SEA. |
| **DG11** Web Site Address - School | 125 | 100 | String | O | See section 2.4.4<br>The Uniform Resource Locator (URL) for the unique address of a Web page of a school. |  |
| **DG10** Telephone – School | 225 | 10 | String | M | See section 2.4.3<br>The 10-digit telephone number, including the area code, for the school.<br>Do not include hyphens, blanks, or parentheses. | Cannot be between 00000000000–2000000000 or 9900000000–9999999999. |
| **DG8** Address Mailing 1 - School | 235 | 60 | String | M | See section 2.4.1<br>The mailing street name and number or Post Office Box for the school. |  |
| **DG8** Address Mailing 2 - School | 295 | 60 | String | O | See section 2.4.1<br>Additional mailing street address information for the school |  |
| **DG8** Address Mailing 3 - School | 355 | 60 | String | O | See section 2.4.1<br>Additional mailing street address information for the school |  |
| **DG8** City Mailing - School | 415 | 30 | String | M | See section 2.4.1<br>The mailing address city for the school |  |
| **DG8** State Abbreviation Mailing - School | 445 | 2 | String | M | See section 2.4.1<br>The state abbreviation of the mailing address for the school | For a list of valid USPS State Abbreviations, refer to Appendix A. |
| **DG8** ZIP Code Mailing - School | 447 | 5 | String | M | See section 2.4.1<br>The five–digit ZIP Code for the mailing address for the school | All 5 digits (cannot be 00000 or 99999 or less than 00600) |
| **DG8** ZIP Code Plus 4 Mailing - School | 452 | 4 | String | O | See section 2.4.1<br>The four–digit extension of the ZIP Code for the mailing address for the school | If included, all 4 digits (cannot be 0000) |
| **DG9** Address Location 1 - School | 456 | 60 | String | O | See section 2.4.2<br>The street address that describes the physical location of the school |  |
| **DG9** Address Location 2 - School | 516 | 60 | String | O | See section 2.4.2<br>Additional address information that describes the physical location of the school |  |
| **DG9** Address Location 3 - School | 576 | 60 | String | O | See section 2.4.2<br>Additional address information that describes the physical location of the school |  |
| **DG9** City Location - School | 636 | 30 | String | O | See section 2.4.2<br>The name of the city that describes the physical location of the school |  |
| **DG9** State Abbreviation Location - School | 666 | 2 | String | O | See section 2.4.2<br>The state abbreviation for location address of the school | For a list of valid USPS State Abbreviations, refer to Appendix A |
| **DG9** ZIP Code Location - School | 668 | 5 | String | O | See section 2.4.2<br>The five–digit ZIP Code for the location address of the school | All 5 digits (cannot be 00000 or 99999 or less than 00600) |
| **DG9** ZIP Code Plus 4 Location - School | 673 | 4 | String | O | See section 2.4.2<br>The four–digit extension of the ZIP Code for the location address of the school | If included, all 4 digits (cannot be 0000) |
| **DG531** Operational Status – School SY Start | 677 | 30 | String | M | See section 2.5.1<br>The classification of the operational condition of a school, at the start of the school year. | **1** – Open<br>**2** – Closed<br>**3** – New<br>**4** – Added<br>**5** – Changed LEA affiliation<br>**6** – Inactive<br>**7** – Future<br>**8** – Reopened |
| **DG531N** Operational Status – School New (previously referred to as “Updated”) | 707 | 30 | String | X | **Population of this field** - Use only if updating the school operational status from the start of the SY<br>See Section 6.0<br>The new (updated) classification of the operational condition of a school, if changed during the school year. | **1** – Open<br>**2** – Closed<br>**3** – New<br>**4** – Added<br>**5** – Changed LEA affiliation<br>**6** – Inactive<br>**7** – Future<br>**8** – Reopened |
| **DG571** Effective Date | 737 | 10 | String | X | **Population of this field** - Use only if updating the school operational status from the start of the SY<br>See section 6.0<br>The date the operational status changed | **YYYY-MM-DD**<br>Maximum value is 2026-09-30 |
| **DG27** Charter Status | 747 | 30 | String | M | See section 2.6.2<br>An indication that a public school provides free public elementary and/or secondary education to eligible students under a specific charter issued, pursuant to a state charter school law, by an authorized chartering agency/authority and that is designated by such authority to be public charter school. | **YES** – Charter school<br>**NO** – Not a charter school<br>**NA** – Not Applicable |
| **DG4P** Prior State LEA ID | 777 | 14 | String | S | **Population of this field** - This field is to be used when the State LEA ID needs to be changed.<br>See section 5.0 |  |
| **DG5P** Prior State School ID | 791 | 20 | String | S | **Population of this field** - This field is to be used when the State School ID needs to be changed<br>See section 5.0 |  |
| **DG743** Reconstituted Status | 811 | 15 | String | M | See section 2.5.4<br>An indication that the school was restructured, transformed, or otherwise changed as a consequence of the state’s accountability system under ESEA or as a result of School Improvement Grants (SIG), but is not recognized as a new school for CCD purposes. | **YES** – Reconstituted school<br>**NO** – Not a reconstituted school |
| Filler | 826 | 15 | String | M | Leave filler fields blank. |  |
| **DG804** Charter Authorizer Identifier (State) - Primary Authorizer | 841 | 20 | String | X | **Population of this field** – When DG27 Charter Status is “YES.”<br>See section 2.6.3<br>The unique identifier assigned to an authorized public chartering agency by the SEA. |  |
| **DG804** Charter Authorizer Identifier (State) - Secondary Authorizer | 861 | 20 | String | X | **Population of this field** – When DG27 Charter Status is “YES” and school has a secondary authorizer.<br>See section 2.6.3<br>The unique identifier assigned to an authorized public chartering agency by the SEA. | If there is no secondary authorizer, leave this field blank. |
| Explanation | 881 | 200 | String | O | Text field for state use. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 1081 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit.

**Table D.3.3–2: School Data Record Example**

This example is when the school is not updating operational status or state identifiers.

| Format  | File Record Number,State Code,State Agency Number,LEA Identifier (State),LEA Identifier (NCES),School Identifier (State),School Identifier (NCES),Education Entity Name - School,School Type,Out of State Indicator,Web Site Address - School,Telephone - School,Address Mailing 1 - School,Address Mailing 2 - School,Address Mailing 3 - School,City Mailing - School,State Abbreviation Mailing - School,ZIP Code Mailing - School,ZIP Code Plus 4 Mailing - School,Address Location 1 - School,Address Location 2 - School,Address Location 3 - School,City Location - School,State Abbreviation Location - School,ZIP Code Location - School,ZIP Code Plus 4 Location - School,Operational Status – School SY Start,{blank field unless updating operational status then used for Operational Status – School New },{blank field unless updating operational status then used for Effective Date},Charter Status,{blank field unless changing LEA state identifier then used for Prior State LEA ID},{blank field unless changing school state identifier then used for Prior State School ID},Reconsituted Status,Filler,Charter Authorizer Identifier (State) – Primary Authorizer,Charter Authorizer Identifier (State) - Secondary Authorizer,Explanation,Carriage Return / Line Feed (CRLF) |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Example | 1,80,01,3400024,8000142,278A,32405,Whitcomb Elementary,1,NO,www.whitcombschools.com,5555559999,204 Main St,,,Whit City,EU,99999,,,,,,,,,,1,,,NO,,,NO,,,,¶                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

School Data Record Exampleformat, example

## Document History

| **Version Number** | **Date**    | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |             | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | August 2026 | Updated for SY 2026-27:                                                                 |
