---
fs_id: FS089
title: "Children with Disabilities (IDEA) Early Childhood"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG613]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [ChildCount]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS089-v23.0--edfacts-fs089-23-0-dg613-children-disabilities-early-childhood-v230-114530.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs089-23-0-dg613-children-disabilities-early-childhood-v230-114530.docx"
sha256: 822faf42aba242813537d3a7c4ac5167103ff2c27d9bb17bad9675529ca284b5
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS089 — Children with Disabilities (IDEA) Early Childhood (v23.0)

> [!abstract] FS089 at a glance
> **Data groups:** DG613
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** SEA, LEA
> **Reporting Period:** Child Count Date - The date designated by the state that is between October 1 and December 1 for the IDEA child count
> **Type of count:** SEA: Once (unduplicated count); LEA: At only one LEA (unduplicated count across LEAs)
> **Zero counts:** SEA: Required for all valid combinations; see Zero Exceptions and Not applicable as explained below; LEA: Required for the total of the education unit. Not required for category sets or subtotals
> **Categories:** Educational Environment (IDEA) EC, Disability Category (IDEA), Age (Early Childhood), Racial Ethnic, Sex (Membership), English Learner Status (Both)
> **Data record:** 21 fields, 490 characters fixed-width
> **Generate domain:** [[ChildCount]]
> **Business rules:** [[FS089 Business Rules]] (BRSI SY 2025-26)
> **Metadata guides:** [[IDEA Part B Child Count Metadata User Guide]]
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS089-v23.0--edfacts-fs089-23-0-dg613-children-disabilities-early-childhood-v230-114530.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit EDFacts Data Group 613: Children with disabilities (IDEA) early childhood table. The definition for this data group is:

> The unduplicated number of children with disabilities (IDEA) who are ages 3 through 5 and not in kindergarten and receiving special education and related service according to an individualized education program (IEP), an individualized family service plan (IFSP), or a services plan in place on the state's child count date.

The data collected using this file specification are required by the Individuals with Disabilities Education Act (IDEA), Section 618. The data are also used for monitoring the programs and activities under IDEA. The LEA data are also used for the Non-Fiscal Survey of the Common Core of Data (CCD).

The ED data stewarding office/s for this file: OSERS/OSEP.

**Note:** We recognize there was a terminology change when the *Elementary and Secondary Education Act* (ESEA) was reauthorized as the *Every Student Succeeds Act*; where prior terminology referred to Limited English Proficient (LEP), new terminology refers to English Learners (EL). EDFacts still use the acronym “LEP” in the programming. Ideally, we would modify all the programming to match the new acronym but it is used extensively within the programming and the effort to change all the instances is outside the budget. When using the documentation files, be aware that all references to programming are a result of legacy practices and that any references to LEP have the meaning associated with EL.

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than any editorial changes listed in the document history on page ii, there have been no other changes to this file specification.

### Core Requirements for Submitting this File

The following table contains the reporting period, the education units included or excluded, the type of count, and zero count reporting.

**Table 2.2-1: Core Reporting Requirements**

|  | **SEA** | **LEA** | **School** |
|---|---|---|---|
| Reporting Period | Child Count Date - The date designated by the state that is between October 1 and December 1 for the IDEA child count | Child Count Date - The date designated by the state that is between October 1 and December 1 for the IDEA child count |  |
| Education units included | Include SEA | Include LEAs that reported students in FS052 and offered PK.<br>Students should be reported by the LEA that has responsibility for the students |  |
| Education units <u>not</u> reported |  | Closed, inactive, or future LEAs<br>LEAs that don’t offer PK |  |
| Type of count | Once (unduplicated count) | At only one LEA (unduplicated count across LEAs) |  |
| Zero counts | Required for all valid combinations; see Zero Exceptions and Not applicable as explained below | Required for the total of the education unit.<br>Not required for category sets or subtotals |  |
| Zero exceptions and Not applicable | Disability Category (IDEA) – If your state does not use a permitted value (*e.g.,* multiple disabilities), do not use that permitted value in the file (i.e., category sets A and B and subtotal 3). Your use of the permitted values must be consistent within the file and with other files that report data by Disability Category (IDEA). Your use of the permitted values must be consistent with responses to the IDEA Environments – Early Childhood and IDEA Child Count metadata collections.<br>Educational Environment (IDEA) EC – If a state does not use a permitted value (*e.g.,* Residential Facility), do not use that permitted value in the file (i.e., Category set B, C, D, and E and subtotals 6 and 7). Your use of the permitted values must be consistent within the file. Your use of the permitted values must be consistent with responses to the IDEA Environments – Early Childhood and IDEA Child Count metadata collections.<br>Disability Category (IDEA) by age – If the permitted value “development delay” is not applicable at certain ages, leave those combinations out of the file. Your use of the permitted values must be consistent within the file and with other files that report data by Disability Category (IDEA). Your use of the permitted values must be consistent with responses to the IDEA Environments – Early Childhood and IDEA Child Count metadata collections. | Disability Category (IDEA) – If your state does not use a permitted value (*e.g.,* multiple disabilities), do not use that permitted value in the file (i.e., category sets A and B and subtotal 3). Your use of the permitted values must be consistent within the file and with other files that report data by Disability Category (IDEA). Your use of the permitted values must be consistent with responses to the IDEA Environments – Early Childhood and IDEA Child Count metadata collections.<br>Educational Environment (IDEA) EC – If a state does not use a permitted value (*e.g.,* Residential Facility), do not use that permitted value in the file (i.e., Category set B, C, D, and E and subtotals 6 and 7). Your use of the permitted values must be consistent within the file. Your use of the permitted values must be consistent with responses to the IDEA Environments – Early Childhood and IDEA Child Count metadata collections.<br>Disability Category (IDEA) by age – If the permitted value “development delay” is not applicable at certain ages, leave those combinations out of the file. Your use of the permitted values must be consistent within the file and with other files that report data by Disability Category (IDEA). Your use of the permitted values must be consistent with responses to the IDEA Environments – Early Childhood and IDEA Child Count metadata collections. |  |
| Missing | Use “-1” to report missing counts.<br>Use “MISSING” when a category is not available. | Use “-1” to report missing counts.<br>Use “MISSING” when a category is not available. |  |
| Related metadata survey | FS5002 - IDEA Child Count<br>FS5004 - IDEA Environments – Early Childhood | FS5002 - IDEA Child Count<br>FS5004 - IDEA Environments – Early Childhood |  |

**Data Packages**

There are file specifications that contain a requirement that the data file and metadata or a related file must be submitted together. FS089 must be submitted together with FS5004 (IDEA Environments – Early Childhood).

### Required Categories and Totals

The table below lists the combinations of the categories and totals that are expected to be submitted for the state and each LEA or school that should be included in the file.

- An “X” in the column indicates that the category value must be submitted when reporting that aggregation.

- The total indicator must be either “Y” (Yes) or “N” (No).

  - If the record is for a category set, specify an “N” (No).

  - If the record is for a subtotal or education unit total, specify a “Y” (Yes).

The technical name of the data used in the file is: CHWDSBERLCHD

**Table 2.3–1: Required Categories and Totals**

| **Aggregation** | **Educational Environment (IDEA) EC** | **Disability Category (IDEA)** | **Age (Early Childhood)** | **Racial Ethnic** | **Sex (Membership)** | **English Learner Status (Both)** | **Total Indicator** | **Comments** |
|---|---|---|---|---|---|---|---|---|
| **Category Set A** | X | X | X |  |  |  | N | Student Count by Educational Environment (IDEA) EC by Disability Category (IDEA) by Age (Early Childhood) |
| **Category Set B** | X | X |  | X |  |  | N | Student Count by Educational Environment (IDEA) EC by Disability Category (IDEA) by Racial Ethnic |
| **Category Set C** | X |  |  |  | X |  | N | Student Count by Educational Environment (IDEA) EC by Sex (Membership) |
| **Category Set D** | X |  |  |  |  | X | N | Student Count by Educational Environment (IDEA) EC by English Learner Status (Both) |
| **Subtotal 1** |  |  |  |  | X |  | Y | Student Count by Sex (Membership) |
| **Subtotal 2** |  |  | X |  |  |  | Y | Student Count by Age (Early Childhood) |
| **Subtotal 3** |  | X |  |  |  |  | Y | Student Count by Disability Category (IDEA) |
| **Subtotal 4** |  |  |  | X |  |  | Y | Student Count by Racial Ethnic |
| **Subtotal 5** |  |  |  |  |  | X | Y | Student Count by English Learner Status (Both) |
| **Subtotal 6** | X |  |  |  |  |  | Y | Student Count by Educational Environment (IDEA) EC |
| **Education Unit Total** |  |  |  |  |  |  | Y | Education Unit Total of Student Count |

### Categories and Permitted Values

This section contains the categories and permitted values used for submitting this file.

**DG613 - Children with disabilities (IDEA) early childhood table:**

**Educational Environment (IDEA) EC**

The programs in which children ages 3 through 5 attend and the setting in which these children receive special education and related services.

| **Permitted Value Abbreviation** | **Permitted Value Description**                                     | **Comments**                                                                                                                                                                        |
|----------------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REC10YSVCS                       | Services in Regular Early Childhood Program (at least 10 hours)     | Attended a regular early childhood (EC) program at least 10 hours per week and received the majority of hours of special education and related services in the regular EC program.  |
| REC10YOTHLOC                     | Other Location Regular Early Childhood Program (at least 10 hours)  | Attended a regular early childhood program at least 10 hours per week and received the majority of hours of special education and related services in some other location.          |
| REC09YSVCS                       | Services in Regular Early Childhood Program (less than 10 hours)    | Attended a regular early childhood (EC) program less than 10 hours per week and received the majority of hours of special education and related services in the regular EC program. |
| REC09YOTHLOC                     | Other Location Regular Early Childhood Program (less than 10 hours) | Attended a regular early childhood program less than 10 hours per week and received the majority of hours of special education and related services in some other location.         |
| SC                               | Separate Class                                                      | Are not in regular early childhood programs                                                                                                                                         |
| SS                               | Separate School                                                     |                                                                                                                                                                                     |
| RF                               | Residential Facility                                                |                                                                                                                                                                                     |
| H                                | Home                                                                | Are not in regular early childhood programs                                                                                                                                         |
| SPL                              | Service Provider Location                                           | Are not in regular early childhood programs                                                                                                                                         |
| MISSING                          | Missing                                                             | Use when data are not available by this category.                                                                                                                                   |

**Disability Category (IDEA)**

The primary disability as identified in the Individualized Education Program (IEP), Individualized Family Service Plan (IFSP), or service plan.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                               |
|----------------------------------|---------------------------------|------------------------------------------------------------|
| AUT                              | Autism                          |                                                            |
| DB                               | Deaf-blindness                  |                                                            |
| DD                               | Developmental delay             | Valid only for children ages 3-9 when defined by the state |
| EMN                              | Emotional disturbance           |                                                            |
| HI                               | Hearing impairment              |                                                            |
| ID                               | Intellectual disability         |                                                            |
| MD                               | Multiple disabilities           |                                                            |
| OI                               | Orthopedic impairment           |                                                            |
| SLD                              | Specific learning disability    |                                                            |
| SLI                              | Speech or language impairment   |                                                            |
| TBI                              | Traumatic brain injury          |                                                            |
| VI                               | Visual impairment               |                                                            |
| OHI                              | Other health impairment         |                                                            |
| MISSING                          | Missing                         | Use when data are not available by this category.          |

**Age (Early Childhood)**

The discrete age of children (students) who are in early childhood on the state specified child count date.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                      |
|----------------------------------|---------------------------------|---------------------------------------------------|
| 3                                | Age 3                           |                                                   |
| 4                                | Age 4                           |                                                   |
| AGE05NOTK                        | Age 5 (Not Kindergarten)        |                                                   |
| MISSING                          | Missing                         | Use when data are not available by this category. |

**Racial Ethnic**

The general racial category that most clearly reflects individuals' recognition of their community or with which the individuals most identify.

| **Permitted Value Abbreviation** | **Permitted Value Description**           | **Comments**                                      |
|----------------------------------|-------------------------------------------|---------------------------------------------------|
| AM7                              | American Indian or Alaska Native          |                                                   |
| AS7                              | Asian                                     |                                                   |
| BL7                              | Black or African American                 |                                                   |
| HI7                              | Hispanic/Latino                           |                                                   |
| PI7                              | Native Hawaiian or Other Pacific Islander |                                                   |
| MU7                              | Two or more races                         |                                                   |
| WH7                              | White                                     |                                                   |
| MISSING                          | Missing                                   | Use when data are not available by this category. |

**Sex (Membership)**

An indication that students are either female or male.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                      |
|----------------------------------|---------------------------------|---------------------------------------------------|
| F                                | Female                          |                                                   |
| M                                | Male                            |                                                   |
| MISSING                          | Missing                         | Use when data are not available by this category. |

**English Learner Status (Both)**

An indication of whether students met the definition of an English learner.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                      |
|----------------------------------|---------------------------------|---------------------------------------------------|
| LEP                              | English learners                |                                                   |
| NLEP                             | Non-English learner             |                                                   |
| MISSING                          | Missing                         | Use when data are not available by this category. |

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

**Which children should be reported in this file?**

In alignment with 34 CFR 300.643 and 300.644, include report the unduplicated count of all children with disabilities (IDEA) who meet the following criteria:

- Are ages 3 through 5 not in kindergarten

- Receiving special education and related services according to an individualized education program, an individualized family service plan (IFSP), or a services plan[^1] in place on the count date. This includes children enrolled in private school by a parent, but who are still receiving special education services through the LEA under a services plan.

**How should children with disabilities (IDEA) who receive their education in a state-operated school (i.e., state school for the deaf) be reported?**

According to 34 CFR 300.2, children who receive their education exclusively at a state-operated facility should be reported in the SEA level count. If an LEA retains responsibility for the education of children who receive their education exclusively at a state-operated facility, the LEA may also report those students, depending on state procedures.

**How are counts of children reported by Age (Early Childhood)?** According to 34 CFR 300.641(b), children should be reported according to their discrete age, based on each child’s age as of the child count date.

**How are counts of children reported by Disability Category (IDEA)?**

Report students by one of the disability categories that are listed in the EDFacts Workbook. Disability categories noted in the EDFacts Workbook are in alignment with 34 CFR 300.8. According to 34 CFR 300.641(c), the SEA may not report a child under more than one disability category.

**How are children reported by developmental delay?**

According to 34 CFR 300.8(b), States must have defined and established eligibility criteria for developmental delay for children ages 3 through 5 in order to report children under that permitted value in this file. Only children ages 3 through 5 may be reported in the developmental delay disability category, and then only in states with diagnostic instruments and procedures to measure delays in physical, cognitive, communication, social, or emotional, or adaptive development. Although federal law does not require that states and LEAs categorize children according to developmental delay, if this category is required by state law, states are expected to report these children in the developmental delay category.

If the development delay is not authorized for use by the state, the permitted value development delay is not used in the file. The responses to the IDEA Environments – Early Childhood and Child Count metadata collections and the permitted values reported must align.

**How is a child with more than one primary disability reported**?

According to 34 CFR 300.641(d), if a child with a disability has more than one disability, the SEA must report that child in accordance with the following procedures:

- If a child has only two primary disabilities and those disabilities are deafness and blindness and the child is not reported as having a developmental delay, that child must be reported under the permitted value “deaf-blindness.”

- A child who has more than one primary disability and is not reported under the permitted value "deaf-blindness" (as explained in the bullet above) or as the permitted value of developmental delay must be reported under the permitted value “multiple disabilities.”

**How are counts of children reported by Educational Environment (IDEA) Early Childhood?**

The chart below explains the permitted values used for early childhood educational environment in alignment with 34 CFR 200.114.

**Table 2.5–1: Permitted Values for Early Childhood Educational Environment**

| **Type of Program**                                                                                                       | **Setting**                                                                                                                                                        | **Permitted Values**                                                 | **Code**     |
|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|--------------|
| Children Attending A Regular Early Childhood Program At Least 10 Hrs Per Week                                             | And Receiving The Majority Of Hours Of Special Education And Related Services In The Regular Early Childhood Program                                               | Services Regular Early Childhood Program (at least10 Hours)          | REC10YSVCS   |
| Children Attending A Regular Early Childhood Program At Least 10 Hrs Per Week                                             | And Receiving The Majority Of Hours Of Special Education And Related Services In Some Other Location                                                               | Other Location Regular Early Childhood Program (at least 10 Hours)   | REC10YOTHLOC |
| Children Attending A Regular Early Childhood Program Less Than 10 Hrs Per Week                                            | And Receiving The Majority Of Hours Of Special Education And Related Services In The Regular Early Childhood Program                                               | Services Regular Early Childhood Program (Less Than 10 Hours)        | REC09YSVCS   |
| Children Attending A Regular Early Childhood Program Less Than 10 Hrs Per Week                                            | And Receiving The Majority Of Hours Of Special Education And Related Services In Some Other Location                                                               | Other Location Regular Early Childhood Program (Less Than 10 Hours)  | REC09YOTHLOC |
| Children attending a special education program (NOT in any regular early childhood program)…                              | Specifically, a separate special education class                                                                                                                   | Separate Class                                                       | SC           |
| Children attending a special education program (NOT in any regular early childhood program)…                              | Specifically, a separate school                                                                                                                                    | Separate School                                                      | SS           |
| Children attending a special education program (NOT in any regular early childhood program)…                              | Specifically, a residential facility                                                                                                                               | Residential Facility                                                 | RF           |
| Children attending neither a regular early childhood program nor a special education program (Not included in rows above) | And receiving the majority of hours of special education and related services at home                                                                              | Home                                                                 | H            |
| Children attending neither a regular early childhood program nor a special education program (Not included in rows above) | And receiving the majority of hours of special education and related services at the service provider’s location or some other location not in any other category. | Service Provider Location                                            | SPL          |

**What are regular early childhood programs?**

A regular early childhood program[^2] is a program that includes a majority (at least 50 percent) of nondisabled children (i.e., children not on IEPs). This may include, but is not limited to the following:

- Head Start

- Preschool classes offered to an eligible pre-kindergarten population by the public school system

- Private preschools

- Group child development center or child care

**How should children receiving the majority of special education and related services in a location other than the child’s classroom but within the same building be reported**[^3]**?**

Special education and related services delivered to the child in the course of daily activities and routines in which all children in the classroom participate (e.g., “circle time”, “learning centers”) would be considered as being received in the Regular Early Childhood Program. However, services delivered in a location that removes the child from the opportunity to interact with nondisabled children would not be considered as being received in the Regular Early Childhood Program. These include, but are not limited to, services delivered in a 1:1 therapeutic setting, or in a small group comprised solely of children with disabilities whether or not they are provided in another location within the building where the regular early childhood program is located.

**What are special education programs?**

A special education program is a program that includes less than 50 percent nondisabled children (i.e., children not on IEPs)<sup>2</sup>. This may include, but is not limited to the following:

- Special education classes in

  - Regular school buildings

  - Trailers or portables outside regular school buildings

  - Child care facilities

  - Hospital facilities on an outpatient basis

  - Other community-based settings

- Separate schools

- Residential facilities

**Should child care and other programs that families have chosen for their child be considered when reporting these data?**

Yes, States should take into consideration child care and other programs that families have chosen for their child when determining the appropriate educational environment report category[^4].

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
| lev | Abbreviation for level:<br>•<br>SEA for a State Education Agency level<br>•<br>LEA for a Local Education Agency level | 3 |
| filename | **CHDSBERL** | 9 |
| vvvvvvv | Alphanumeric string designated by the SEA to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| .ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 4 |

## Fixed or Delimited Files

This section describes the fixed file and delimited file specifications. The fixed file and delimited files contain a header record followed by data records. The file type is specified in the header record.

The “Pop” column in the header and data records is coded as follows:

> M – Mandatory, this field must always be populated
>
> A – This field is populated in accordance with table 2.3-1 “Required Categories and Totals”
>
> O – Optional, data in this field are optional

### Header Record Definition

The header record is required and is the first record in every file submitted to EDPass. The purpose of the header record is to provide information as to the file type, number of data records in the file, file name, file identifier, and file reporting period.

**Table 4.1–1: Header Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviation** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SEA CHILDREN WITH DISABILITIES (IDEA) EC**<br>**LEA CHILDREN WITH DISABILITIES (IDEA) EC** |
| Total Records In File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 363 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 490 | 1 |  | M |  |  |

Below is an example of a header record.

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | LEA CHILDREN WITH DISABILITIES (IDEA) EC,15,euleaCHDSBERLv000001.csv,characters to identify file,2026-2027,¶              |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide counts for the specified category sets, subtotals and education unit totals.

**Table 4.2–1: Data Records**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviation** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (State) | 15 | 14 | String | M | The identifier assigned to a local education agency (LEA) by the state education agency (SEA). Also known as State LEA Identification Number (ID). This data element cannot be updated through this file. | SEA level – Blank |
| Filler | 29 | 20 | String | M | Leave filler field blank. |  |
| Table Name | 49 | 20 | String | M | See technical name in Section 2.3 Required Categories and Totals. | **CHWDSBERLCHD** |
| Racial Ethnic | 69 | 15 | String | A | The general racial category that most clearly reflects individuals' recognition of their community or with which the individuals most identify. | **AM7** – American Indian or Alaska Native<br>**AS7** – Asian<br>**BL7** – Black or African American<br>**HI7** – Hispanic/Latino<br>**PI7** – Native Hawaiian or Other Pacific Islander<br>**MU7** – Two or more races<br>**WH7** – White<br>**MISSING** |
| Sex (Membership) | 84 | 15 | String | A | An indication that students are either female or male. | **F** – Female<br>**M** – Male<br>**MISSING** |
| Age (Early Childhood) | 99 | 15 | String | A | The discrete age of children (students) who are in early childhood on the state specified child count date. | **3** – Age 3<br>**4** – Age 4<br>**AGE05NOTK** – Age 5 (Not Kindergarten)<br>**MISSING** |
| English Learner Status (Both) | 114 | 15 | String | A | An indication of whether students met the definition of an English learner. | **LEP** – English learners<br>**NLEP** – Non-English learner<br>**MISSING** |
| Disability Category (IDEA) | 129 | 15 | String | A | The primary disability as identified in the Individualized Education Program (IEP), Individualized Family Service Plan (IFSP), or service plan. | **AUT** – Autism<br>**DB** – Deaf-blindness<br>**DD** – Developmental delay<br>**EMN** – Emotional disturbance<br>**HI** – Hearing impairment<br>**ID** – Intellectual disability<br>**MD** – Multiple disabilities<br>**OI** – Orthopedic impairment<br>**SLD** – Specific learning disability<br>**SLI** – Speech or language impairment<br>**TBI** – Traumatic brain injury<br>**VI** – Visual impairment<br>**OHI** – Other health impairment<br>**MISSING** |
| Filler | 144 | 15 | String | M | Leave filler field blank. |  |
| Filler | 159 | 15 | String | M | Leave filler field blank. |  |
| Filler | 174 | 15 | String | M | Leave filler field blank. |  |
| Filler | 189 | 15 | String | M | Leave filler field blank. |  |
| Filler | 204 | 15 | String | M | Leave filler field blank. |  |
| Educational Environment (IDEA) EC | 219 | 60 | String | A | The programs in which children ages 3 through 5 attend and the setting in which these children receive special education and related services. | **REC10YSVCS** – Services in Regular Early Childhood Program (at least 10 hours)<br>**REC10YOTHLOC** – Other Location Regular Early Childhood Program (at least 10 hours)<br>**REC09YSVCS** – Services in Regular Early Childhood Program (less than 10 hours)<br>**REC09YOTHLOC** – Other Location Regular Early Childhood Program (less than 10 hours)<br>**SC** – Separate Class<br>**SS** – Separate School<br>**RF** – Residential Facility<br>**H** – Home<br>**SPL** – Service Provider Location<br>**MISSING** |
| Total Indicator | 279 | 1 | String | M | An indicator that defines the count level – see table 2.3-1 Required Categories and Totals | **N** – Specifies category set<br>**Y** – Specifies subtotal or total of the education unit |
| Explanation | 280 | 200 | String | O | Text field for state use. |  |
| Student Count | 480 | 10 | Integer | M |  |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 490 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit. See table 2.3-1.

**Table 4.2–2: Data Record Example – LEA level**

| **Aggregation**         | **Example**                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Format                  | File Record Number,State Code,State Agency Number,LEA Identifier (State),Filler,Table Name,Racial Ethnic,Sex (Membership),Age (Early Childhood),English Learner Status (Both),Disability Category (IDEA),Filler,Filler,Filler,Filler,Filler,Educational Environment (IDEA) EC,Total Indicator,Explanation,Student CountCarriage Return / Line Feed (CRLF) |
| Category Set A          | 1,80,01,00605EUPHORIA,,CHWDSBERLCHD,,,3,,AUT,,,,,,REC10YSVCS,N,,50¶                                                                                                                                                                                                                                                                                       |
| Category Set B          | 2,80,01,00605EUPHORIA,,CHWDSBERLCHD,AM7,,,,AUT,,,,,,RF,N,,50¶                                                                                                                                                                                                                                                                                             |
| Category Set C          | 3,80,01,00605EUPHORIA,,CHWDSBERLCHD,,M,,,,,,,,,RF,N,,50¶                                                                                                                                                                                                                                                                                                  |
| Category Set D          | 4,80,01,00605EUPHORIA,,CHWDSBERLCHD,,,,LEP,,,,,,,RF,N,,50¶                                                                                                                                                                                                                                                                                                |
| Subtotal 1              | 5,80,01,00605EUPHORIA,,CHWDSBERLCHD,,F,,,,,,,,,,Y,,50¶                                                                                                                                                                                                                                                                                                    |
| Subtotal 2              | 6,80,01,00605EUPHORIA,,CHWDSBERLCHD,,,3,,,,,,,,,Y,,50¶                                                                                                                                                                                                                                                                                                    |
| Subtotal 3              | 7,80,01,00605EUPHORIA,,CHWDSBERLCHD,,,,,AUT,,,,,,,Y,,50¶                                                                                                                                                                                                                                                                                                  |
| Subtotal 4              | 8,80,01,00605EUPHORIA,,CHWDSBERLCHD,AM7,,,,,,,,,,,Y,,50¶                                                                                                                                                                                                                                                                                                  |
| Subtotal 5              | 9,80,01,00605EUPHORIA,,CHWDSBERLCHD,,,,LEP,,,,,,,,Y,,50¶                                                                                                                                                                                                                                                                                                  |
| Subtotal 6              | 10,80,01,00605EUPHORIA,,CHWDSBERLCHD,,,,,,,,,,,SC,Y,,50¶                                                                                                                                                                                                                                                                                                  |
| Total of education unit | 11,80,01,00605EUPHORIA,,CHWDSBERLCHD,,,,,,,,,,,,Y,,500¶                                                                                                                                                                                                                                                                                                   |

## Document History

| **Version Number** | **Date**       | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |                | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | September 2026 | Updated for SY 2026-27:                                                                 |
