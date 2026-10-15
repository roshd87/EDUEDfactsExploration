---
fs_id: FS059
title: "Staff FTE"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG528, DG644]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [Staff]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS059-v23.0--edfacts-fs059-23-0-dg528-dg644-staff-fte-v230-114529.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs059-23-0-dg528-dg644-staff-fte-v230-114529.docx"
sha256: 706bb06899ea4fc0cabc94d0ca8961d10a7ac271d2d2f232ad61490a433ae097
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS059 — Staff FTE (v23.0)

> [!abstract] FS059 at a glance
> **Data groups:** DG528, DG644
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** SEA, LEA, School
> **Reporting Period:** Oct 1 - October 1 or the closest school day
> **Type of count:** Full time equivalent (FTE)
> **Zero counts:** Required
> **Categories:** Staff Category (CCD)
> **Data record:** 14 fields, 340 characters fixed-width
> **Generate domain:** [[Staff]]
> **Business rules:** [[FS059 Business Rules]] (BRSI SY 2025-26)
> **Metadata guides:** [[CCD Staff FTE and Membership Metadata User Guide]]
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS059-v23.0--edfacts-fs059-23-0-dg528-dg644-staff-fte-v230-114529.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit the following EDFacts Data Groups, which have different formats (see tables 4.2-1 and 4.2-3):

**Table 1.0-1: EDFacts Data Groups**

| **Data Group Name** | **DG** | **Definition**                                               | **Level**   |
|---------------------|--------|--------------------------------------------------------------|-------------|
| Staff FTE table     | 528    | The number of full-time equivalent (FTE) staff.              | SEA and LEA |
| Teachers (FTE)      | 644    | The number of full-time equivalent (FTE) classroom teachers. | School      |

EDFacts data groups

The data collected using this file specification are collected under the authority of the Education Sciences Reform Act (PL 107-279) and are used primarily for the Non-Fiscal Survey of the Common Core of Data (CCD).

The ED data stewarding office/s for this file: NCES

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 Specifications

Other than any editorial changes listed in the document history on page ii, there have been no changes to this file specification.

### Core Requirements for Submitting this File

The following table contains the reporting period, the education units included or excluded, the type of count, and zero count reporting.

**Table 2.2-1: Core Reporting Requirements**

|  | **SEA** | **LEA** | **School** |
|---|---|---|---|
| Reporting Period | Oct 1 - October 1 or the closest school day | Oct 1 - October 1 or the closest school day | Oct 1 - October 1 or the closest school day |
| Education units included | Include SEA | LEAs that were operational on October 1<sup>st</sup> | Schools other than reportable programs that were operational on October 1. |
| Education units <u>not</u> reported |  | Closed, inactive, or future LEAs or LEAs that opened after October 1<sup>st</sup> | Closed, inactive, or future Schools or Schools that opened after October 1<sup>st</sup><br>Schools with school type of "reportable program" |
| Type of count | Full time equivalent (FTE) | Full time equivalent (FTE) | Full time equivalent (FTE) |
| Zero counts | Required | Required | Required |
| Zero exceptions and Not applicable | Ungraded Teachers – If the state does not use ungraded teachers, then do not include records for that permitted value in the file.<br>School Counselors – In section 2.5 see question “What if a state cannot map to elementary school counselors and secondary school counselors.” | Ungraded Teachers – If the state does not use ungraded teachers, then do not include records for that permitted value in the file.<br>Staff Category (CCD) – See comments for each permitted value in section 2.4. |  |
| Missing | Use “-1” to report missing counts.<br>Use “MISSING” when a category is not available. | Use “-1” to report missing counts.<br>Use “MISSING” when a category is not available. | Use “-1” to report missing counts. |
| Related metadata survey | FS5018 - CCD Staffing metadata collection | FS5018 - CCD Staffing metadata collection |  |

**Data Packages**

There are file specifications that contain a requirement that the data file and metadata or a related file must be submitted together. FS059 must be submitted together with FS5018 (CCD Staffing metadata).

### Required Categories and Totals

As indicated in table 1.0-1, a different data group is collected at the school level than at the SEA and LEA levels. Therefore, the record layouts for the school level are different from the record layouts for the SEA and LEA levels.

The table below lists the combinations of the categories and totals that are expected to be submitted for the state and each LEA or school that should be included in the file.

- An “X” in the column indicates that the category value must be submitted when reporting that aggregation.

- The total indicator must be either “Y” (Yes) or “N” (No).

  - If the record is for a category set, specify an “N” (No).

  - If the record is for a subtotal or education unit total, specify a “Y” (Yes).

**Table 2.3–1: DG528 Required Categories and Totals for SEA and LEA Levels**

| **Category Set**            | **Staff Category (CCD)** | **Total Indicator** | **Comments**                |
|-----------------------------|--------------------------|---------------------|-----------------------------|
| Category Set A              | X                        | N                   | FTE by Staff Category (CCD) |
| Total of the education unit |                          | Y                   | Total of the Education Unit |

For the school level file, there are no required categories and totals. The total indicator is reported as “N” in all records.

**Table 2.3–2: DG644 Required Categories and Totals for School Level**

| **Category Set**            | **Total Indicator** | **Comments**                |
|-----------------------------|---------------------|-----------------------------|
| Total of the education unit | N                   | Total of the Education Unit |

**Table 2.3-3 Staff FTE Table Names Used in Files**

| **DG#** | **DG Name**     | **Table Name used in file** |
|---------|-----------------|-----------------------------|
| 528     | Staff FTE table | FTESTAFF                    |
| 644     | Teachers (FTE)  | CLASSTEACHFTE               |

### Categories and Permitted Values

This section contains the categories and permitted values used for submitting this file.

**DG528 – Staff FTE table:**

**Staff Category (CCD)**

Titles of employment, official status, or rank.

| **Permitted Value Abbreviation** | **Permitted Value Description**                         | **Comments**                                                                                                                                                                                                                                                                         |
|----------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PKTCH                            | Pre-Kindergarten Teachers                               | Report for LEAs that offer Pre-Kindergarten and have students in Pre-Kindergarten                                                                                                                                                                                                    |
| KGTCH                            | Kindergarten Teachers                                   | Report for LEAs that offer Kindergarten and have students in Kindergarten                                                                                                                                                                                                            |
| ELMTCH                           | Elementary Teachers                                     | Report for LEAs that offer elementary grades and have students in elementary grades                                                                                                                                                                                                  |
| SECTCH                           | Secondary Teachers                                      | Report for LEAs that offer secondary grades and have students in secondary grades                                                                                                                                                                                                    |
| UGTCH                            | Ungraded Teachers                                       | Report for LEAs in states that indicated in the Staff FTE metadata collection that they have teachers identified as teachers for ungraded classes.                                                                                                                                   |
| PARA                             | Paraprofessionals/Instructional Aides                   | Report for LEAs with students                                                                                                                                                                                                                                                        |
| ELMGUI                           | Elementary School Counselors                            | Report for LEAs with students that offer elementary grades                                                                                                                                                                                                                           |
| SECGUI                           | Secondary School Counselors                             | Report for LEAs with students that offer secondary grades                                                                                                                                                                                                                            |
| GUI                              | School Counselors                                       | Use when unable to distinguish between elementary and secondary counselors. Report for LEAs with students                                                                                                                                                                            |
| LIBSPE                           | Librarians/Media Specialists                            | Report for LEAs with students                                                                                                                                                                                                                                                        |
| LIBSUP                           | Library/Media Support Staff                             | Report for LEAs with students                                                                                                                                                                                                                                                        |
| LEAADM                           | LEA Administrators                                      | Report for all LEAs                                                                                                                                                                                                                                                                  |
| LEASUP                           | LEA Administrative Support Staff                        | Report for all LEAs                                                                                                                                                                                                                                                                  |
| CORSUP                           | Instructional Coordinators and Supervisors to the Staff | Report for LEAs with students                                                                                                                                                                                                                                                        |
| SCHADM                           | School Administrators                                   | Report for LEAs with operational schools                                                                                                                                                                                                                                             |
| SCHSUP                           | School Administrative Support Staff                     | Report for LEAs with operational schools                                                                                                                                                                                                                                             |
| STUSUPWOPSYCH                    | Student Support Services Staff (w/o Psychology)         | Report for LEAs with students. Does not include School Psychologists.                                                                                                                                                                                                                |
| SCHPSYCH                         | School Psychologists                                    | Report for LEAs with students. Professional staff member who provides direct and indirect support, including prevention and intervention, to evaluate and address students’ intellectual development, academic success, social-emotional learning, and mental and behavioral health. |
| OTHSUP                           | All Other Support Staff                                 | Report for all LEAs                                                                                                                                                                                                                                                                  |
| MISSING                          | Missing                                                 | Use when data are not available by this category.                                                                                                                                                                                                                                    |

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers.

**How should contracted staff be reported?**

Include contracted staff for work that is part of the regular operations.

1)  Include individuals who contract directly with a school district; this is not limited to cases in which the individual receives retirement and other benefits from the district or state.

    - Examples may include bus drivers, school nurses, psychologists, physical therapists.

2)  Include staff employed by another entity that is contracted to provide **work that is part of the district’s regular operations**. These staff work within the district but are employees of the entity with which the district contracts. The district does not pay retirement or other benefits.

    - Examples may include school security personnel provided by a private firm or charter school teachers who are employees of a charter school operator.

Do not include employees of contractors who provide a **non-regular** service; these are staff furnished by the contractor, on- or off-site, to provide the service.

- Examples may include carpenters, electricians, etc. working for a firm hired to refurbish a school building, or cooks and truck drivers who prepare and deliver meals once a week to schools under a contract with a food-service firm.

The distinction between staff reported and not reported is whether the service is part of the district’s regular operation or if it is a non-regular service.

- For example:

  - If a district contracts with a company for a school bus driving service (where the buses are used regularly), the drivers should be reported as staff.

  - If a district contracts with a company for lunchroom services onsite, the food servers who serve the students on daily basis should be reported as staff.

  - If a construction company is hired to build an addition to the school, the employees of a construction company working on the addition to the school should not be reported.

#### Reporting by Full-Time Equivalent (FTE)

**How are staff reported?**

Report staff in terms of FTE (full-time equivalent). FTE should be counted in hundredths. For example, if a teaching position is filled by four people, each working the same amount of time, each person would count as .25 FTE. The total FTE counts for instructional staff must be reported to the **nearest hundredth**, with an **EXPLICIT** decimal (e.g., 59.20).

**Can an individual staff member’s total FTE exceed 1.0?**

Yes. An individual staff member’s total FTE can exceed 1.0 if that individual regularly works overtime. For example, if FTE is defined as a 40 hour week, and a teacher teaches 40 hours at one school each week and an additional 4 hours teaching elementary/secondary classes at another school, that teacher’s total FTE would be 1.1 (44 hours / 40 hours) and the teacher would be counted as 1.0 FTE at the first school and 0.1 FTE at the second school.

**What if a staff member has more than one assignment?**

If a staff member has more than one assignment, count the staff member in terms of the assignments.  An assignment could be a school, a position, or a teacher category. For example:

- If a school staff member worked three-quarters of the time as a teacher, and one-quarter of the time as a librarian, he or she would be counted as a 0.75 teacher FTE and a 0.25 librarian FTE.

- If a full-time teacher’s time is split equally between two schools, that teacher would be counted as 0.5 FTE in each school.

- If a teacher teaches both prekindergarten and kindergarten, his/her total FTE should be proportionally divided between those two teacher categories (PKTCH and KGTCH) based on the time spent with each.

- If the staff records do not distinguish between prekindergarten teachers (PKTCH) and kindergarten teachers (KGTCH), the total FTE for these two should be divided proportionally between them.

#### Staff FTE (DG528)

**What if a state cannot map to elementary school counselors (ELMGUI) and secondary school counselors (SECGUI)?**

There are three permitted values for school counselors:

- Elementary school counselors (ELMGUI)

- Secondary school counselors (SECGUI)

- School counselors (GUI)

If a state cannot map to ELMGUI and SECGUI, the state should report the aggregate school counselors using the permitted value “School Counselors” (GUI). If using the aggregate category (GUI) for counselors, report zeros for elementary and secondary school counselors/directors (ELMGUI and SECGUI).

##### Staff FTE (DG528) – SEA Level

**Are records required for each permitted value in the staff category?**

All permitted values apply at the SEA level except UGTCH which is not applicable for all states. If counts are not available for one or more of the permitted values, use -1 (missing) for the count value.

##### Staff FTE (DG528) – LEA Level

**Are records required for each permitted value in the staff category?**

Records are required for each permitted value that applies to the LEA.

| Situation | Reporting |
|---|---|
| LEA has no staff | Report zero for education unit total<br>•<br>This reporting will trigger errors that will need to be explained. |
| LEA has no students | The following fields may not apply:<br>•<br>Teachers (PKTCH, KGTCH, ELMTCH, SECTCH, UGTCH)<br>•<br>Paraprofessionals/Instructional Aides (PARA)<br>•<br>Instructional Coordinators and Support to the Staff (CORSUP)<br>•<br>School Counselors (ELMGUI, SECGUI, GUI)<br>•<br>Library/Media Specialists (LIBSPE)<br>•<br>Library/Media Support Staff (LIBSUP)<br>•<br>Student Support Services Staff (STUSUPWOPSYCH)<br>•<br>Psychologists (SCHPSYCH)<br>•<br>Other Support Services Staff (OTHSUP) |
| LEA has no pre-kindergarten students | The following field may not apply:<br>•<br>Pre-Kindergarten Teachers (PKTCH) |
| LEA has no kindergarten students | The following field may not apply:<br>•<br>Kindergarten Teachers (KGTCH) |
| LEA has no students in elementary grades | The following fields may not apply:<br>•<br>Elementary Teachers (ELMTCH)<br>•<br>Elementary School Counselors (ELMGUI) |
| LEA has no students in grades 9 through 12 | The following fields may not apply:<br>•<br>Secondary Teachers (SECTCH)<br>•<br>Secondary School Counselors (SECGUI) |

**How are staff reported for an LEA (such as a charter LEA) when the same people are the administrators for the LEA and for the school?**

Report LEA administrators and administrative support staff as zero and attribute all of the administrative FTE to the school administrator and administrative support permitted values.

#### Teachers (FTE) (DG644) – School Level

This data group is reported at the school level.

**What if an operational school has no teachers?**

If the entity being reported has no teachers associated with it, reconsider whether the entity meets the definition of a school for reporting data to ED through EDFacts.

If there are teachers providing instruction at the school, but their primary assignment is another school, the FTE total for these teachers should be proportionally divided between both schools.

In the rare instance where a school is operational, has students in membership, but has no teachers, report teachers as zero. This reporting will trigger errors that will need a data note.

**How do Staff FTE (DG528) teacher counts in the SEA and LEA levels relate to the Teachers (FTE) (DG644) counts in the school level?**

The teachers reported for SEA and LEA levels using the following permitted values should also be reported at the school level for Teachers (FTE) DG644:

- Pre-Kindergarten teachers (PKTCH)

- Kindergarten teachers (KGTCH)

- Elementary teachers (ELMTCH)

- Secondary teachers (SECTCH)

- Teachers of Ungraded classes (UGTCH) if applicable to the state

### Definitions

This collection uses the Common Core of Data’s (CCD) definitions of staff categories, listed below.

#### Instructional Staff – Direct classroom instruction

Direct classroom instruction:

- Professional: teacher (PKTCH, KGTCH, ELMTCH, SECTCH, UGTCH)

- Ancillary: instructional aide (PARA)

**Pre-kindergarten Teachers (PKTCH)**

Teachers of a group or class that is part of a public school program that is taught during the year or years preceding kindergarten.

- **INCLUDE** teachers of Head Start students if Head Start is part of an authorized public education program of an LEA.

**Kindergarten Teachers (KGTCH)**

Teachers of a group or class that is part of a public school program and is taught during the year preceding first grade.

**Elementary Teachers (ELMTCH)**

Teachers of general level instruction classified by state and local practice as elementary and composed of any span of grades not above grade 8.

- **EXCLUDE** pre-kindergarten and kindergarten teachers from this count.

Secondary Teachers (SECTCH)

Teachers of a general level of instruction classified by state and local practice as secondary and composed of any span of grades beginning with the next grade following the elementary grades and ending with or below grade 12.

Ungraded Teachers (UGTCH)

Teachers of a group or class that is not organized on the basis of grade grouping and has no standard grade designation.

- **INCLUDE** the FTE of teachers instructing both regular classes that have no grade designations as well as special classes for exceptional students that have no grade designations. Such classes are likely to contain students of different ages who frequently are identified according to level of performance in one or more areas of instruction rather than according to grade level or age level.

Paraprofessionals/Instructional Aides (PARA)

Staff members assigned to assist a teacher with routine activities associated with teaching, i.e., activities requiring minor decisions regarding students, such as monitoring, conducting rote exercises, operating equipment and clerking.

- **INCLUDE**

  - tutors if the position does not require teaching credentials

only paid staff, whether direct hires or contracted staff (see above discussion on contracted staff under question **How should contracted staff be reported?**).

- **EXCLUDE** volunteer aides and vacant positions

#### Instructional Staff – Not direct classroom instruction

Not direct classroom instruction:

- Professional: librarian or media specialist (LIBSPE)

- Ancillary: library and media support staff (LIBSUP)

Librarians/Media Specialists (LIBSPE)

Professional staff member or supervisors assigned specific duties and school time for professional library services activities. Professional library service activities include selecting, acquiring, preparing, cataloging, and circulating books and other printed materials; planning the use of the library by students, teachers, and instructional staff; and guiding individuals in the use of library books and material maintained separately or as a part of an instructional materials center.

Library/Media Support Staff (LIBSUP)

Staff member who renders other professional library and media services. Duties of these staff members include selecting, preparing, caring for, and making available to instructional staff, equipment, films, filmstrips, transparencies, tapes, TV programs, and similar materials maintained separately or as part of an instructional materials center. Include activities in the audiovisual center, TV studio, related work-study areas, and services provided by audiovisual personnel.

- INCLUDE library aides and those involved in library/media support.

#### Administrative Staff - LEA

LEA administration

- Professional:

  - LEA administrator (LEAADM)

  - instructional coordinator/supervisor (CORSUP)

- Ancillary: LEA administrative support staff (LEASUP)

LEA Administrators (LEAADM) - Chief executive officers of education agencies

- **INCLUDE** superintendents, deputies, and assistant superintendents; other persons with district-wide responsibilities; e.g., accountants, auditors, business managers, facilities managers, technology or information system administrators, or supervisors of transportation, food services, or security.

- **EXCLUDE** supervisors of instructional coordinators, supervisors of s counselors, and supervisors of student support staff. (These staff are reported under “student support services staff.”)

Instructional Coordinators and Supervisors (CORSUP)

Staff supervising instructional programs at the school district or sub-district level.

- **INCLUDE** supervisors of educational television staff; coordinators and supervisors of audiovisual services; curriculum coordinators or supervisors and in-service training staff, including teacher mentors; Title I coordinators and home economics supervisors; and supervisory staff engaged in development of computer-assisted instruction

- **EXCLUDE** school-based department chairpersons (these individuals are reported under “school administrator.”)

LEA Administrative Support Staff (LEASUP)

Staff members providing direct support to LEA administrators, business office support, data processing, secretarial and other clerical staff; staff implementing software solutions and staff providing hardware and software maintenance and data user support.

#### Administrative Staff - School

School administration

- Professional: school administrator (SCHADM)

- Ancillary: school administrative support staff (SCHSUP)

School Administrators (SCHADM)

Staff members whose activities are concerned with directing and managing the operation of a particular school.

- **INCLUDE** Principals, assistant principals, and persons who supervise school operations, assign duties to staff members, supervise and maintain the records of the school, and coordinate school instructional activities with those of the education agency, including department chairpersons.

School Administrative Support Staff (SCHSUP)

Staff whose activities are concerned with support of the teaching and administrative duties of the office of the principal or department chairpersons.

- **INCLUDE** clerical staff and secretaries.

#### Support Staff

Professional

- school counselor/director (ELMGUI, SECGUI, GUI)

- student support services staff (STUSUPWOPSYCH)

- school psychologist (SCHPSYCH)

Ancillary

- other support staff (OTHSUP)

School Counselors/Directors (ELMGUI, SECGUI, GUI)

Professional staff assigned specific duties and school time for: counseling students and parents, addressing learning problems, evaluating students’ abilities and assisting students in career and personal development

- **INCLUDE** supervisors and directors of guidance programs.

Student Support Services Staff (STUSUPWOPSYCH)

Professional staff members whose activities are concerned with the direct support of students and who nurture, but do not instruct students.

- **INCLUDE** attendance officers; staff providing health, speech pathology, audiology, or social services; and supervisors of the preceding staff; coaches, athletic advisors, and athletic trainers if position does not require teaching credentials.

School Psychologists (SCHPSYCH)

Professional staff member who provides direct and indirect support, including prevention and intervention, to evaluate and address student’s intellectual development, academic success, social-emotional learning, and mental and behavioral health.

All Other Support Staff (OTHSUP)

Support staff not reported in instructional or student support.

- **INCLUDE** employees such as plant and equipment maintenance, bus drivers, security, and food service workers.

## File Naming Convention

The following file naming convention is to help identify files to provide technical assistance.

A maximum of 25 characters (including the file extension) is allowed for the file name.

The following is the naming convention for file submissions:

> sslev**filename**vvvvvvv.ext

**Table 3.0-1: File Naming Convention**

| **Where** | **Means** | **Limit in characters** |
|---|---|---|
| ss | USPS State Abbreviation | 2 |
| lev | Abbreviation for level:<br>•<br>SEA for an SEA level<br>•<br>LEA for an LEA level<br>•<br>SCH for a school level | 3 |
| filename | **FTESTFTBL** | 9 |
| vvvvvvv | Alphanumeric string designated by the SEA to uniquely identify the individual submission (*e.g.,* ver0001, v010803) | 7 |
| .ext | Extension identifying the file format:<br>.txt – fixed<br>.csv – comma delimited<br>.tab – tab delimited | 4 |

## Fixed or Delimited Files

This section describes the fixed file and delimited file specifications. The fixed file and delimited files contain a header record followed by data records. The file type is specified in the header record.

The “Pop” column in the header and data records is coded as follows:

> M - Mandatory, this field must always be populated
>
> A - This field is populated in accordance with table 2.3-1 “Required Categories and Totals” for the SEA and LEA levels (For the school level, fields are either M or O.)
>
> O - Optional, data in this field are optional

### Header Record Definition

The header record is required and is the first record in every file submitted to EDPass. The purpose of the header record is to provide information as to the file type, number of data records in the file, file name, file identifier, and file reporting period.

**Table 4.1–1: Header Record- SEA, LEA and SCH Levels**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SEA STAFF FTE**<br>**LEA STAFF FTE**<br>**SCHOOL STAFF FTE** |
| Total Records In File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 213 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 340 | 1 |  | M |  |  |

Below is an example of a header record.

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return/Line Feed (CRLF) |
|---------|-------------------------------------------------------------------------------------------------------------------------|
| Example | SEA STAFF FTE,15,EUSEAFTESTFTBLver0007.CSV,characters to identify file,2026-2027,¶                                      |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide counts for the specified category sets, subtotals and education unit totals.

The data record for the school level is different than the data records for the SEA and LEA levels:

- Table 4.2-1 contains the data records for the SEA and LEA level.

- Table 4.2-3 contains the data records for the school level.

**Table 4.2–1: Data Records - SEA and LEA level**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two–digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (state) | 15 | 14 | String | M | The identifier assigned to a local education agency (LEA) by the state education agency (SEA). Also known as State LEA Identification Number (ID). This data element cannot be updated through this file. | SEA level – Blank |
| Filler | 29 | 20 | String | M | Leave Filler Field Blank |  |
| **DG528** Table Name | 49 | 20 | String | M | See technical name in Section 2.3 Required Categories and Totals | **FTESTAFF** |
| Filler | 69 | 15 | String | M | Leave Filler Field Blank |  |
| Staff Category (CCD) | 84 | 15 | String | A | Titles of employment, official status, or rank. | **PKTCH** - Pre-Kindergarten Teachers<br>**KGTCH** - Kindergarten Teachers<br>**ELMTCH** - Elementary Teachers<br>**SECTCH** - Secondary Teachers<br>**UGTCH** - Ungraded Teachers<br>**PARA** - Paraprofessionals/Instructional Aides<br>**ELMGUI** - Elementary School Counselors<br>**SECGUI** - Secondary School Counselors<br>**GUI** - School Counselors<br>**LIBSPE** - Librarians/Media Specialists<br>**LIBSUP** - Library/Media Support Staff<br>**LEAADM** - LEA Administrators<br>**LEASUP** - LEA Administrative Support Staff<br>**CORSUP** - Instructional Coordinators and Supervisors to the Staff<br>**SCHADM** - School Administrators<br>**SCHSUP** - School Administrative Support Staff<br>**STUSUPWOPSYCH** - Student Support Services Staff (w/o Psychology)<br>**SCHPSYCH** - School Psychologists<br>**OTHSUP** - All Other Support Staff<br>**MISSING** |
| Filler | 99 | 15 | String | M | Leave filler field blank. |   |
| Filler | 114 | 15 | String | M | Leave filler field blank. |  |
| Total Indicator | 129 | 1 | String | M | An indicator that defines the count level – see Table 2.3–1: DG528 Required Categories and Totals for SEA and LEA Levels | **N** – Specifies category set<br>**Y** – Specifies subtotal or total of the education unit |
| Explanation | 130 | 200 | String | O | Text field for state use. |  |
| Staff FTE | 330 | 10 | Decimal Number | M | Decimal numbers down to one hundredth FTE are permitted. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 340 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit. See table 2.3-1.

**Table 4.2–2: Data Record Example – LEA level**

| **Aggregation**         | **Example**                                                                                                                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Format                  | File Record Number,State Code,State Agency Number,LEA Identifier (state),Filler,Table Name,Filler,Staff Category (CCD),Filler,Filler,Total Indicator,Explanation,Staff FTE,Carriage Return / Line Feed (CRLF) |
| Category Set A          | 1,80,01,00605EUPHORIA,,FTESTAFF,,PKTCH,,,N,,10.75¶                                                                                                                                                            |
| Total of education unit | 19,80,01,00605EUPHORIA,,FTESTAFF,,,,,Y,,170.75¶                                                                                                                                                               |

**Table 4.2–3: Data Records - School level**

| **Data Element Name** | **Start**<br>**Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two–digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (state) | 15 | 14 | String | M | The identifier assigned to a local education agency (LEA) by the state education agency (SEA). Also known as State LEA Identification Number (ID). This data element cannot be updated through this file. |  |
| **DG5** School Identifier (state) | 29 | 20 | String | M | The identifier assigned to a school by the state education agency (SEA). Also known as the State School Identification Number (ID). This ID cannot be updated through this file. |  |
| **DG644** Table Name | 49 | 20 | String | M | See technical name in Section 2.3 Required Categories and Totals | **CLASSTEACHFTE** |
| Filler | 69 | 15 | String | M | Leave filler field blank. |   |
| Filler | 84 | 15 | String | M | Leave filler field blank. |  |
| Filler | 99 | 15 | String | M | Leave filler field blank. |   |
| Filler | 114 | 15 | String | M | Leave filler field blank. |  |
| Total Indicator | 129 | 1 | String | M | An indicator that defines the count level – see Table 2.3–2: DG644 Required Categories and Totals for School Level | **N** – Specifies category set |
| Explanation | 130 | 200 | String | O | Text field for state use. |  |
| Teachers FTE | 330 | 10 | Decimal<br>Number | M | Decimal numbers down to one hundredth FTE are permitted. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 340 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit. See table 2.3-2.

**Table 4.2–4: Data Record Example – School level**

| **Aggregation**     | **Example**                                                                                                                                                                                                             |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Format              | File Record Number,State Code,State Agency Number,LEA Identifier (state),School Identifier (state),Table Name,Filler,Filler,Filler,Filler,Total Indicator,Explanation,Teachers (FTE),Carriage Return / Line Feed (CRLF) |
| School level record | 1,80,01,00605EUPHORIA,EUSCHOOL0001,CLASSTEACHFTE,,,,,N,,10.75¶                                                                                                                                                          |

## Document History

| **Version Number** | **Date**       | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |                | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | September 2026 | Updated for SY 2026-27:                                                                 |
