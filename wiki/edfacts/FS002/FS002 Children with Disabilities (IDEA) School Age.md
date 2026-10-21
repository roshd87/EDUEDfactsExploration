---
fs_id: FS002
title: "Children with Disabilities (IDEA) School Age"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG74]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [ChildCount]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS002-v23.0--edfacts-fs002-23-0-dg74-children-disabilities-school-age-v230-114523.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs002-23-0-dg74-children-disabilities-school-age-v230-114523.docx"
sha256: 302750f5df52317970e67de19539a545f37514f6fc3393ef526de11caa867883
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS002 — Children with Disabilities (IDEA) School Age (v23.0)

> [!abstract] FS002 at a glance
> **Data groups:** DG74
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** SEA, LEA, School
> **Reporting Period:** Child Count Date - The date designated by the state that is between October 1 and December 1 for the IDEA child count
> **Type of count:** SEA: Once (unduplicated count); LEA: At only one LEA (unduplicated count across LEAs); School: At only one school
> **Zero counts:** SEA: Required for all valid combinations; see Zero Exceptions or Not Applicable as explained below; LEA: Required for the total of the education unit. Not required for category sets or subtotal; School: Required for the total of the education unit. Not required for category sets or subtotals
> **Categories:** Educational Environment (IDEA) SA, Disability Category (IDEA), Sex (Membership), Age (School Age), Racial Ethnic, English Learner Status (Both)
> **Data record:** 25 fields, 505 characters fixed-width
> **Generate domain:** [[ChildCount]]
> **Business rules:** [[FS002 Business Rules]] (BRSI SY 2025-26)
> **Metadata guides:** [[IDEA Part B Child Count Metadata User Guide]]
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS002-v23.0--edfacts-fs002-23-0-dg74-children-disabilities-school-age-v230-114523.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit EDFacts Data Group 74: Children with disabilities (IDEA) school age table. The definition for this data group is:

> The unduplicated number of children with disabilities (IDEA) who are ages 5 (in kindergarten) through 21 and receiving special education and related service according to an individualized education program (IEP) or a services plan in place on the state's child count date.

The data collected using this file specification are required by the Individuals with Disabilities Education Act (IDEA), Section 618.  The data are also used in the Non-Fiscal Survey of the Common Core of Data (LEA level) and by the Office for Civil Rights (School level).

The ED data stewarding office/s for this file: OSERS/OSEP and OCR (school-level)

**Note:** We recognize there was a terminology change when the *Elementary and Secondary Education Act* (ESEA) was reauthorized as the *Every Student Succeeds Act*; where prior terminology referred to Limited English Proficient (LEP), new terminology refers to English Learners (EL). EDFacts still use the acronym “LEP” in the programming. Ideally, we would modify all the programming to match the new acronym but it is used extensively within the programming and the effort to change all the instances is outside the budget. When using the documentation files, be aware that all references to programming are a result of legacy practices and that any references to LEP have the meaning associated with EL.

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than any editorial changes listed in the document history on page ii, there have been no other changes to this file specification.

### Requirements for Submitting this Data Group at the SEA and LEA Level

This section contains two tables that summarize the reporting requirements at the SEA and LEA level. Requirements for submitting at the school level are in section 2.3. The first table contains the reporting period, the education units included or excluded, the type of count, and zero count reporting. The second table contains the required categories and applicable totals.

**Table 2.2-1: Core Reporting Requirements for SEA and LEA Levels**

|  | **SEA** | **LEA** |
|---|---|---|
| Reporting Period | Child Count Date – The date designated by the state that is between October 1 and December 1 for the IDEA child count | Child Count Date – The date designated by the state that is between October 1 and December 1 for the IDEA child count |
| Education Units Reported | Include SEA | Include LEAs that had responsibility for the education of children with disabilities (IDEA) at the time of the state’s child count. |
| Education Units Not Reported |  | Closed, inactive, or future LEAs |
| Type of Count | Once (unduplicated count) | At only one LEA (unduplicated count across LEAs) |
| Zero Counts | Required for all valid combinations; see Zero Exceptions or Not Applicable as explained below. | Required for the total of the education unit.<br>Not required for category sets or subtotal. |
| Zero Exceptions or Not Applicable | Disability Category (IDEA) – If your state does not use a permitted value (*e.g.,* multiple disabilities), do not use that permitted value in the file (i.e., category sets A and B and subtotal 3). Your use of the permitted values must be consistent within the file and with other files that report data by disability category (IDEA). Your use of the permitted values must be consistent with responses to the IDEA Environments – School Age and IDEA Child Count metadata collections.<br>Educational Environment (IDEA) SA - If a state does not use a permitted value (*e.g.,* Residential Facility), do not use that permitted value in the file (i.e., Category set B, C, D, and E and subtotals 6 and 7). Your use of the permitted values must be consistent within the file. Your use of the permitted values must be consistent with responses to the IDEA Environments – School Age and IDEA Child Count metadata collections.<br>Disability Category (IDEA) by age – If the permitted value “development delay” is not applicable at certain ages, leave those combinations out of the file. Your use of the permitted values must be consistent within the file and with other files that report data by disability category (IDEA). Your use of the permitted values must be consistent with responses to the IDEA Environments – School Age and IDEA Child Count metadata collections. | Disability Category (IDEA) – If your state does not use a permitted value (*e.g.,* multiple disabilities), do not use that permitted value in the file (i.e., category sets A and B and subtotal 3). Your use of the permitted values must be consistent within the file and with other files that report data by disability category (IDEA). Your use of the permitted values must be consistent with responses to the IDEA Environments – School Age and IDEA Child Count metadata collections.<br>Educational Environment (IDEA) SA - If a state does not use a permitted value (*e.g.,* Residential Facility), do not use that permitted value in the file (i.e., Category set B, C, D, and E and subtotals 6 and 7). Your use of the permitted values must be consistent within the file. Your use of the permitted values must be consistent with responses to the IDEA Environments – School Age and IDEA Child Count metadata collections.<br>Disability Category (IDEA) by age – If the permitted value “development delay” is not applicable at certain ages, leave those combinations out of the file. Your use of the permitted values must be consistent within the file and with other files that report data by disability category (IDEA). Your use of the permitted values must be consistent with responses to the IDEA Environments – School Age and IDEA Child Count metadata collections. |
| Missing | Use “-1” to report missing counts. Use “MISSING” when a category is not available. | Use “-1” to report missing counts. Use “MISSING” when a category is not available. |
| Related Metadata Survey | FS5002 - IDEA Child Count<br>FS5003 - IDEA Environments – School Age | FS5002 - IDEA Child Count<br>FS5003 - IDEA Environments – School Age |

**Data Packages**

There are file specifications that contain a requirement that the data file and metadata or a related file must be submitted together. FS002 must be submitted together with FS5003 (IDEA Environments – School Age metadata).

The table below lists the combinations of the categories and totals that are expected to be submitted for this file at the SEA and LEA levels:

- An “X” in the column indicates that the category value must be submitted when reporting that aggregation.

  - For example, in category set B, data must be disaggregated by Disability Category (IDEA), Age (School Age) and Educational Environment (IDEA) SA.

- A “Z” in the column indicates that the category value is not required to be submitted when reporting that aggregation but may be included if available.

  - For example, in category set A, data can be submitted disaggregated by Racial Ethnic and Disability Category (IDEA) with Sex (Membership) reported as missing.

  - If the data in the “Z” cells are not included, the category must be reported as “missing”.

- The total indicator must be either “Y” (Yes) or “N” (No).

  - If the record is for a category set, specify an “N” (No).

  - If the record is for a subtotal or education unit total, specify a “Y” (Yes).

The technical name of the data used in the file is: IDEADISAB

**Table 2.2–2: Required Categories and Totals for SEA and LEA level**

| **Aggregation** | **Racial Ethnic** | **Sex (Membership)** | **Disability Category (IDEA)** | **Age**<br>**(School Age)** | **Educational Environment**<br>**(IDEA) SA** | **English Learner Status (Both)** | **Total Indicator** | **Comments** |
|---|---|---|---|---|---|---|---|---|
| **Category Set A** | X | Z | X |  |  |  | N | Student Count by Racial Ethnic by Disability Category (IDEA) and if available by Sex (Membership) |
| **Category Set B** |  |  | X | X | X |  | N | Student Count by Disability Category (IDEA) by Age (School Age) by Educational Environment (IDEA) SA |
| **Category Set C** | X |  |  |  | X |  | N | Student Count by Racial Ethnic by Educational Environment (IDEA) SA |
| **Category Set D** |  | X | Z |  | X |  | N | Student Count by Sex (Membership) by Educational Environment (IDEA) SA and if available by Disability Category (IDEA) |
| **Category Set E** |  | Z | Z |  | X | X | N | Student Count by Educational Environment (IDEA) SA by English Learner Status (Both) and if available by Sex (Membership) and by Disability Category (IDEA) |
| **Subtotal 1** |  | X |  |  |  |  | Y | Student Count by Sex (Membership) |
| **Subtotal 2** |  |  |  | X |  |  | Y | Student Count by Age (School Age) |
| **Subtotal 3** |  |  | X |  |  |  | Y | Student Count by Disability Category (IDEA) |
| **Subtotal 4** | X |  |  |  |  |  | Y | Student Count by Racial Ethnic |
| **Subtotal 5** |  |  |  |  |  | X | Y | Student Count by English Learner Status (Both) |
| **Subtotal 6** |  |  |  |  | X |  | Y | Student Count by Educational Environment (IDEA) SA |
| **Subtotal 7** |  |  |  | X | X |  | Y | Student Count by Age (School Age) by Educational Environment (IDEA) SA |
| **Total of the Education Unit** |  |  |  |  |  |  | Y | Total of the Education Unit |

### Requirements for Submitting this Data Group at the School Level

This section contains two tables that summarize the reporting requirements for the school level. The first table contains the reporting period, the education units included or excluded, the type of count, and zero count reporting. The second table contains the required categories and applicable totals (school level).

**Table 2.3-1 Core Reporting Requirements for School Level**

|  | **School** |
|---|---|
| Reporting Period | Child Count Date - The date designated by the state that is between October 1 and December 1 for the IDEA child count. |
| Education Units Reported | Include public schools where children with disabilities (IDEA) attended at the time of the state’s child count<br>*Note* – Public schools include state-operated agencies that provide education to students with disabilities (IDEA), including agencies that serve students with specific disabilities (IDEA) (such as hearing impaired or vision impaired) and agencies that provide education to adjudicated youth |
| Education Units Not Reported | Closed, inactive, or future schools. |
| Type of Count | At only one school |
| Zero Counts | Required for the total of the education unit.<br>Not required for category sets or subtotals. |
| Zero Exceptions and Not Applicable | Disability Category (IDEA) – If your state does not use a permitted value (*e.g.,* multiple disabilities), do not use that permitted value in the file (i.e., category sets A and B and subtotal 3). Your use of the permitted values must be consistent within the file and with other files that report data by disability category (IDEA). Your use of the permitted values must be consistent with responses to the IDEA Environments – School Age and Child Count metadata collections.<br>Educational Environment (IDEA) SA - If a state does not use a permitted value (*e.g.,* Residential Facility), do not use that permitted value in the file (i.e., Category set B, C, D, and E and subtotals 6 and7). Your use of the permitted values must be consistent within the file. Your use of the permitted values must be consistent with responses to the IDEA Environments – School Age and Child Count metadata collections.<br>Disability Category (IDEA) by age – If the permitted value “development delay” is not applicable at certain ages, leave those combinations out of the file. Your use of the permitted values must be consistent within the file and with other files that report data by disability category (IDEA). Your use of the permitted values must be consistent with responses to the IDEA Environments – School Age and Child Count metadata collections. |
| Missing | Use “-1” to report missing counts.<br>Use “MISSING” when a category is not available. |
| Related Metadata Survey | The responses to the IDEA Environments – School Age and Child Count metadata collections and the permitted values reported must align. See information related to IDEA Environments – School Age and Child Count metadata collections in Zero Exceptions and Not Applicable above. |

The table below lists the combinations of the categories and totals that are expected to be submitted for this file at the school level:

- An “X” in the column indicates that the category value must be submitted when reporting that aggregation.

  - For example, category set A must be disaggregated by Racial Ethnic, Sex (Membership) and Disability Category (IDEA).

- A “Z” in the column indicates that the category value is not required to be submitted when reporting that aggregation but may be included if available.

  - For example, in category set E data are not required to be disaggregated by Educational Environment (IDEA) SA.

  - If the data in the “Z” cells are not included, the category must be reported as “missing”.

- The total indicator must be either “Y” (Yes) or “N” (No).

  - If the record is for a category set, specify an “N” (No).

  - If the record is for a subtotal or education unit total, specify a “Y” (Yes).

The technical name of the data used in the file is: IDEADISAB

Some of the category sets and totals are not required at the school level. The final column indicates which category sets and totals are required.

If an optional category set or subtotal will not be submitted, the state must still submit one record of that category set, using MISSING for any categories in that record. Since students in a missing category set (or subtotal) cannot be counted, a count of -1 should be submitted. An example of the one record that must be submitted for category set B when that category set will not be used follows.

| Submit this record if Category Set B will not be submitted | 1,80,01,StateLEAID,StateSchoolID,IDEADISAB,,,,,,,,,,MISSING,,,MISSING,MISSING,,N,,-1 |
|------------------------------------------------------------|--------------------------------------------------------------------------------------|

**Table 2.3–2: Required Categories and Totals for School level**

| **Category Set** | **Racial**<br>**Ethnic** | **Sex (Membership)** | **Disability Category (IDEA)** | **Age**<br>**(School Age)** | **Educational Environment**<br>**(IDEA) SA** | **English Learner Status (Both)** | **Total**<br>**Indicator** | **Is the category set or subtotal required at the school level** |
|---|---|---|---|---|---|---|---|---|
| **Category Set A** | X | X | X |  |  |  | N | Yes |
| **Category Set B** |  |  | Z | Z | Z |  | N | No |
| **Category Set C** | Z |  |  |  | Z |  | N | No |
| **Category Set D** |  | X | X |  | X |  | N | Yes |
| **Category Set E** |  | X | X |  | Z | X | N | Yes |
| **Subtotal 1** |  | X |  |  |  |  | Y | Yes |
| **Subtotal 2** |  |  |  | Z |  |  | Y | No |
| **Subtotal 3** |  |  | X |  |  |  | Y | Yes |
| **Subtotal 4** | X |  |  |  |  |  | Y | Yes |
| **Subtotal 5** |  |  |  |  |  | X | Y | Yes |
| **Subtotal 6** |  |  |  |  | X |  | Y | Yes |
| **Subtotal 7** |  |  |  | Z | Z |  | Y | No |
| **Total of the Education Unit** |  |  |  |  |  |  | Y | Yes |

### Categories and Permitted Values

This section contains the categories and permitted values used for submitting this file.

**DG74 - Children with disabilities (IDEA) school age table:**

**Educational Environment (IDEA) SA**

The settings in which school-aged children ages 5 who are in kindergarten through 21 receive special education and related services.

| **Permitted Value Abbreviation** | **Permitted Value Description**                 | **Comments**                                              |
|----------------------------------|-------------------------------------------------|-----------------------------------------------------------|
| RC80                             | Inside regular class 80% or more of the day     |                                                           |
| RC79TO40                         | Inside regular class 40% through 79% of the day |                                                           |
| RC39                             | Inside regular class less than 40% of the day   |                                                           |
| SS                               | Separate School                                 |                                                           |
| RF                               | Residential Facility                            |                                                           |
| HH                               | Homebound/Hospital                              | Do not use this permitted value in the school level file. |
| CF                               | Correctional Facilities                         |                                                           |
| PPPS                             | Parentally placed in private schools            | Do not use this permitted value in the school level file. |
| MISSING                          | Missing                                         | Use when data are not available by this category.         |

**Disability Category (IDEA)**

The primary disability as identified in the Individualized Education Program (IEP or service plan.

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

**Sex (Membership)**

An indication that students are either female or male.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                      |
|----------------------------------|---------------------------------|---------------------------------------------------|
| F                                | Female                          |                                                   |
| M                                | Male                            |                                                   |
| MISSING                          | Missing                         | Use when data are not available by this category. |

**Age (School Age)**

The discrete age of children (students) who are school age on the state specified child count date.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                      |
|----------------------------------|---------------------------------|---------------------------------------------------|
| AGE05K                           | Age 5 (Kindergarten)            |                                                   |
| 6                                | Age 6                           |                                                   |
| 7                                | Age 7                           |                                                   |
| 8                                | Age 8                           |                                                   |
| 9                                | Age 9                           |                                                   |
| 10                               | Age 10                          |                                                   |
| 11                               | Age 11                          |                                                   |
| 12                               | Age 12                          |                                                   |
| 13                               | Age 13                          |                                                   |
| 14                               | Age 14                          |                                                   |
| 15                               | Age 15                          |                                                   |
| 16                               | Age 16                          |                                                   |
| 17                               | Age 17                          |                                                   |
| 18                               | Age 18                          |                                                   |
| 19                               | Age 19                          |                                                   |
| 20                               | Age 20                          |                                                   |
| 21                               | Age 21                          |                                                   |
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

**English Learner Status (Both)**

An indication of whether students met the definition of an English learner.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                      |
|----------------------------------|---------------------------------|---------------------------------------------------|
| LEP                              | English learners                |                                                   |
| NLEP                             | Non-English learner             |                                                   |
| MISSING                          | Missing                         | Use when data are not available by this category. |

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

**Which students should be reported in this file?**

In alignment with 34 CFR 300.643 and 300,644, report the unduplicated count of the children (students) with disabilities (IDEA) who meet the following criteria:

- Are ages 5 in kindergarten through 21

- Receiving special education and related services according to an individualized education program (IEP) or services plan[^1] in place on the state’s child count date. This includes children enrolled in private school by a parent, but who are still receiving special education services through the LEA under a services plan.

**How are student counts reported by Age (School Age)?**

According to 34 CFR 300.641(b), children should be reported according to their discrete age, based on each child’s age as of the state’s child count date.

**How are student counts reported by Disability Category (IDEA)?**

Report students by one of the disability categories that are listed in the EDFacts Workbook. Disability categories noted in the EDFacts Workbook are in alignment with 34 CFR 300.8. According to 34 CFR 300.641(c), the SEA may not report a child under more than one disability category.

**How are students reported by developmental delay?**

According to 34 CFR 300.8(b), States must have defined and established eligibility criteria for developmental delay for children ages 6 through 9 in order to report children under that permitted value in this file. Only children ages 3 through 9 may be reported in the developmental delay disability category, and then only in states with diagnostic instruments and procedures to measure delays in physical, cognitive, communication, social, or emotional, or adaptive development. Although federal law does not require that states and LEAs categorize children according to developmental delay, if this category is required by state law, states are expected to report these children in the developmental delay category.

If developmental delay is not authorized for use by the state, the permitted value developmental delay is not used in the file. The responses to the IDEA Environments – School Age and Child Count metadata collections and the permitted values reported must align.

**How are students with more than one primary disability reported?**

According to 34 CFR 300.641(d), if a child with a disability has more than one disability, the SEA must report that child in accordance with the following procedures:

- If a child has only two primary disabilities and those disabilities are deafness and blindness and the child is not reported as having a developmental delay, that child must be reported under the permitted value “deaf-blindness.”

- A child who has more than one primary disability and is not reported under the permitted value "deaf-blindness" (as explained in the bullet above) or as the permitted value of developmental delay must be reported under the permitted value “multiple disabilities.”

**How is percentage of time calculated?**[^2]

To calculate the percentage of time **inside** the regular classroom, divide the number of hours the child spends inside the regular classroom by the *total number of hours in the school day* (including lunch, recess and study periods). The result is multiplied by 100.

Time spent outside the regular classroom receiving services unrelated to the child’s disability (e.g., time receiving English learner services) should be considered time inside the regular classroom.

Educational time spent in age-appropriate community-based settings that include individuals with and without disabilities, such as college campuses or vocational sites, should be counted as time spent inside the regular classroom.

#### SEA level

**Which students should be reported in this file at the SEA level?**

In alignment with 34 CFR 300.643 and 300.644, include all students with disabilities (IDEA) who are ages 5 in kindergarten through 21, receiving special education and related services according to an IEP or services plan in place on the state’s child count date, including children who are:

- Parentally-placed in private schools who receive services under a services plan

- In correctional facilities

- In state-operated educational facilities

- In public schools

**How are student counts reported by Educational Environment (IDEA) School Age?<sup>2</sup>**

Report the students with disabilities (IDEA) by the setting in which the students have been placed for educational services. Below are the definitions of the permitted values:

- Inside regular class 80% or more of day (RC80). These are children who received special education and related services outside the regular classroom for less than 21% of the school day. This may include children placed in:

  - Regular class with special education/related services provided within regular classes

  - Regular class with special education/related services outside regular classes

  - Regular class with special education services provided in resource rooms

- Inside regular class no more than 79% of day and no less than 40% of the day (RC79TO40). These are children who received special education and related services outside the regular classroom for at least 21% but no more than 60% of the school day. Do not include children who are reported as receiving education programs in public or private separate school or residential facilities. This may include children placed in:

  - resource rooms with special education/related services provided within the resource room

  - resource rooms with part-time instruction in a regular class

- Inside regular class less than 40% of the day (RC39). These are children who received special education and related services outside the regular classroom for more than 60% of the school day. Do not include children who are reported as receiving education programs in public or private separate school or residential facilities. This may include children placed in:

  - self-contained special classrooms with part-time instruction in a regular class

  - self-contained special classrooms with full-time special education instruction on a regular school campus

- Separate School (SS) – These are children who received education programs in public or private separate day school facilities. This includes children with disabilities receiving special education and related services, at public expense, for greater than 50% of the school day in public or private separate schools. This may include children placed in:

  - public and private day schools for students with disabilities

  - public and private day schools for students with disabilities for a portion of the school day (greater than 50%) and in regular school buildings for the remainder of the school day

  - public and private residential facilities if the student does not live at the facility

- Residential Facility (RF) – These are children who received education programs and lived in public or private residential facilities during the school week. This includes children with disabilities receiving special education and related services, at public expense, for greater than 50% of the school day in public or private residential facilities. This may include children placed in:

  - public and private residential schools for students with disabilities

  - public and private residential schools for students with disabilities for a portion of the school day (greater than 50%) and in separate day schools or regular school buildings for the remainder of the school day

Do <u>not</u> include students who received education programs at the facility, but do not live there.

- Homebound/Hospital (HH) – These are children who received programs in homebound/hospital environments. This includes children receiving special education and related services in hospital programs or homebound programs. Do <u>not</u> include children whose parents have opted to home–school them and who receive special education at the public expense.

<!-- -->

- Correctional Facilities (CF) – These are children who received special education in correctional facilities. These data are intended to be an unduplicated count of all children receiving special education in short-term detention facilities (community-based or residential) or correctional facilities.

- Parentally-placed in Private Schools (PPPS) – These are children who are enrolled by their parents or guardians in regular parochial or other private schools and whose basic education is paid through private resources and who received special education and related services at public expense from a local educational agency or intermediate educational unit under a services plan[^3].

  - Include children whose parents chose to home-school them, but who receive special education and related services at the public expense.

  - Do not include children who are placed in private schools by the LEA.

#### LEA Level

The information in this section has been developed as technical assistance to data submitters based on questions from the field regarding this data collection as well as common data reporting issues that were identified during data quality reviews of this data collection.

**Which students should be reported in this file at the LEA level?**

Include all students with disabilities (IDEA) who are ages 5 in kindergarten through 21 receiving special education and related services according to an IEP or services plan in place on the state’s child count date, for which the LEA is responsible for the child’s IEP or service plan.

**How should students with disabilities (IDEA) who receive their education in a state-operated school (i.e., state school for the deaf) be reported?**

Students who receive their education exclusively at a state-operated facility should be reported in the SEA level count. If an LEA retains responsibility for the education of students who receive their education exclusively at a state-operated facility, the LEA may also report those students, depending on state procedures.

#### School Level

The information in this section has been developed as technical assistance to data submitters based on questions from the field regarding this data collection as well as common data reporting issues that were identified during data quality reviews of this data collection.

**Which students should be reported in this file at the school level?**

Include students who meet the data group definition and are in public schools. Public schools include state-operated agencies that provide education to students with disabilities (IDEA), including agencies that serve students with specific disabilities (IDEA) (such as hearing impaired or vision impaired) and agencies that provide education to adjudicated youth.

**Which children should not be reported in this file?**

Do <u>not</u> include children with disabilities (IDEA) who are:

- Ages 3 through 5 not in kindergarten

- Ages 22 and over

- Homebound

- Hospitalized

- In private schools for 50% or more of the school day (whether parentally-placed or publicly-placed)

**How are students reported if they attend one school for their general education, but receive special education and related services in a different school or educational unit?**

In the school-level file, report students in the school or educational unit where they spend 50% or more of the school day.

If a student attends two schools, each for exactly 50% of the school day, then count the student at the school in which the students receives general education, rather than at the school where the student receives special education and related services.

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
| lev | Abbreviation for level:<br>•<br>SEA for a State Education Agency level<br>•<br>LEA for a Local Education Agency level<br>•<br>SCH for a school level | 3 |
| filename | **CWDBLIDEA** | 9 |
| vvvvvvv | Alphanumeric string designated by the SEA to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| .ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 4 |

## Fixed or Delimited Files

This section describes the fixed file and delimited file specifications. The fixed file and delimited files contain a header record followed by data records. The file type is specified in the header record.

The “Pop” column in the header and data records is coded as follows:

> M - Mandatory, this field must always be populated
>
> A - This field is populated for the SEA and LEA level in accordance with table 2.2-2 “Required Categories and Totals” and for the school level in accordance with table 2.3-2

O - Optional, data in this field are optional

### Header Record Definition

The header record is required and is the first record in every file submitted to EDPass. The purpose of the header record is to provide information as to the file type, number of data records in the file, file name, file identifier, and file reporting period.

**Table 4.1–1: Header Record**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviation** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SEA CHILDREN WITH DISABILITIES**<br>**LEA CHILDREN WITH DISABILITIES**<br>**SCHOOL CHILDREN WITH DISABILITIES** |
| Total Records in File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 378 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 505 | 1 |  | M |  |  |

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | LEA CHILDREN WITH DISABILITIES,13,EULEACWDBLIDEAver0007.csv,characters to identify file,2026-2027,¶                       |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide counts for the specified category sets, subtotals and education unit totals.

**Table 4.2–1: Data Records**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values**<br>**Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two-digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (State) | 15 | 14 | String | M | The identifier assigned to a local education agency (LEA) by the state education agency (SEA). Also known as State LEA Identification Number (ID). This data element cannot be updated through this file. | SEA level – Blank |
| **DG5** School Identifier (State) | 29 | 20 | String | M | The identifier assigned to a school by the state education agency (SEA). Also known as the State School Identification Number (ID). This ID cannot be updated through this file. | SEA level – Blank<br>LEA level - Blank |
| Table Name | 49 | 20 | String | M | See technical name in sections 2.2 and 2.3. | **IDEADISAB** |
| Filler | 69 | 15 | String | M | Leave filler field blank. |  |
| Racial Ethnic | 84 | 15 | String | A | The general racial category that most clearly reflects individuals' recognition of their community or with which the individuals most identify. | **AM7** – American Indian or Alaska Native<br>**AS7** – Asian<br>**BL7** – Black or African American<br>**HI7** – Hispanic/Latino<br>**PI7** – Native Hawaiian or Other Pacific Islander<br>**WH7** – White<br>**MU7** – Two or more races<br>**MISSING** |
| Sex (Membership) | 99 | 15 | String | A | An indication that students are either female or male. | **F –** Female<br>**M –** Male<br>**MISSING** |
| Filler | 114 | 15 | String | M | Leave filler field blank. |  |
| Filler | 129 | 15 | String | M | Leave filler field blank. |  |
| Filler | 144 | 15 | String | M | Leave filler field blank. |  |
| Filler | 159 | 15 | String | M | Leave filler field blank. |  |
| Filler | 174 | 15 | String | M | Leave filler field blank. |  |
| Filler | 189 | 15 | String | M | Leave filler field blank. |  |
| Disability Category (IDEA) | 204 | 15 | String | A | The primary disability as identified in the Individualized Education Program (IEP) or service plan. | **AUT** – Autism<br>**DB** – Deaf–blindness<br>**DD** – Developmental delay<br>**EMN** – Emotional disturbance<br>**HI** – Hearing impairment<br>**ID** – Intellectual disability<br>**MD** – Multiple disabilities<br>**OI** – Orthopedic impairment<br>**SLD** – Specific learning disability<br>**SLI** – Speech or language impairment<br>**TBI** – Traumatic brain injury<br>**VI** – Visual impairment<br>**OHI** – Other health impairment<br>**MISSING** |
| Filler | 219 | 15 | String | M | Leave filler field blank. |  |
| Filler | 234 | 15 | String | M | Leave filler field blank. |  |
| Age (School Age) | 249 | 15 | String | A | The discrete age of children (students) who are school age on the state specified child count date. | **AGE05K** – Age 5 (Kindergarten)<br>**6** – Age 6<br>**7** – Age 7<br>**8** – Age 8<br>**9** – Age 9<br>**10** – Age 10<br>**11** – Age 11<br>**12** – Age 12<br>**13** – Age 13<br>**14** – Age 14<br>**15** – Age 15<br>**16** – Age 16<br>**17** – Age 17<br>**18** – Age 18<br>**19** – Age 19<br>**20** – Age 20<br>**21** – Age 21<br>**MISSING** |
| Educational Environment (IDEA) SA | 264 | 15 | String | A | The settings in which school-aged children ages 5 who are in kindergarten through 21 receive special education and related services. | **RC80** – Inside regular class 80% or more of the day<br>**RC79TO40** – Inside regular class 40% through 79% of the day<br>**RC39** – Inside regular class less than 40% of the day<br>**SS** – Separate School<br>**RF** – Residential Facility<br>**HH** – Homebound/Hospital<br>**CF** – Correctional Facilities<br>**PPPS** – Parentally placed in private schools<br>**MISSING** |
| English Learner Status (Both) | 279 | 15 | String | A | An indication of whether students met the definition of an English learner. | **LEP** – English learners<br>**NLEP** – Non–English learner<br>**MISSING** |
| Total Indicator | 294 | 1 | String | M | An indicator that defines the count level – see tables 2.2-2 and 2.3-2 Required Categories and Totals | **N** – specifies detail level<br>**Y** – specifies a subtotal or total of the education unit level. |
| Explanation | 295 | 200 | String | O | Text field for state use. |  |
| Student Count | 495 | 10 | Integer | M |  |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 505 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit. See tables 2.2-2 and 2.3-2.

**Table 4.2–2: Data Record Example – School level**

| **Aggregation**               | **Example**                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Format                        | File Record Number,State Code,State Agency Number,LEA Identifier (State),School Identifier (State),Table Name,Filler,Racial Ethnic,Sex (Membership),Filler,Filler,Filler,Filler,Filler,Filler,Disability Category (IDEA),Filler,Filler,Age (School Age),Educational Environment (IDEA) SA,English Learner Status (Both),Total Indicator,Explanation,Student Count,Carriage Return / Line Feed (CRLF) |
| Category Set A                | 1,80,01,00605EUPHORIA,00100,IDEADISAB,,AM7,F,,,,,,,AUT,,,,,,N,,5¶                                                                                                                                                                                                                                                                                                                                    |
| Category Set B                | 2,80,01,00605EUPHORIA,00100,IDEADISAB,,,,,,,,,,DB,,,6,SS,,N,,5¶                                                                                                                                                                                                                                                                                                                                      |
| Category Set C                | 3,80,01,00605EUPHORIA,00100,IDEADISAB,,AS7,,,,,,,,,,,,RC80,,N,,5¶                                                                                                                                                                                                                                                                                                                                    |
| Category Set D                | 4,80,01,00605EUPHORIA,00100,IDEADISAB,,,M,,,,,,,DD,,,,RC79TO40,,N,,5¶                                                                                                                                                                                                                                                                                                                                |
| Category Set E                | 5,80,01,00605EUPHORIA,00100,IDEADISAB,,,F,,,,,,,EMN,,,,RC39,LEP,N,,5¶                                                                                                                                                                                                                                                                                                                                |
| Subtotal1                     | 6,80,01,00605EUPHORIA,00100,IDEADISAB,,,F,,,,,,,,,,,,,Y,,10¶                                                                                                                                                                                                                                                                                                                                         |
| Subtotal 2                    | 7,80,01,00605EUPHORIA,00100,IDEADISAB,,,,,,,,,,,,,6,,,Y,,5¶                                                                                                                                                                                                                                                                                                                                          |
| Subtotal 3                    | 8,80,01,00605EUPHORIA,00100,IDEADISAB,,,,,,,,,,AUT,,,,,,Y,,5¶                                                                                                                                                                                                                                                                                                                                        |
| Subtotal 4                    | 9,80,01,00605EUPHORIA,00100,IDEADISAB,, AM7,,,,,,,,,,,,,,Y,,25¶                                                                                                                                                                                                                                                                                                                                      |
| Subtotal 5                    | 10,80,01,00605EUPHORIA,00100,IDEADISAB,,,,,,,,,,,,,,,LEP,Y,,25¶                                                                                                                                                                                                                                                                                                                                      |
| Subtotal 6                    | 11,80,01,00605EUPHORIA,00100,IDEADISAB,,,,,,,,,,,,,,SS,,Y,,25¶                                                                                                                                                                                                                                                                                                                                       |
| Subtotal 7                    | 12,80,01,00605EUPHORIA,00100,IDEADISAB,,,,,,,,,,,,,6,SS,,Y,,25¶                                                                                                                                                                                                                                                                                                                                      |
| Total of the Educational Unit | 13,80,01,00605EUPHORIA,00100,IDEADISAB,,,,,,,,,,,,,,,,Y,,25¶                                                                                                                                                                                                                                                                                                                                         |

Title: Data Record Example – School level Aggregation, Example

## Document History

| **Version Number** | **Date**       | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |                | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | September 2026 | Updated for SY 2026-27:                                                                 |
