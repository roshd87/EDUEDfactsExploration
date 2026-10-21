---
fs_id: FS052
title: "Membership"
version: "v23.0"
school_year: "SY 2026-27"
data_groups: [DG39]
status_2025_26: Active
status_2026_27: Inactive
generate_domains: [Membership]
source_docx: "wiki/reference/edfacts/2026-27/file-specifications/FS052-v23.0--edfacts-fs052-23-0-dg39-membership-v230-114528.docx"
source_url: "https://www.ed.gov/media/document/edfacts-fs052-23-0-dg39-membership-v230-114528.docx"
sha256: 73ab788e0dd95cea13ba763942dd916490f2847720969d9f82f0e91a7089fa21
frozen: 2026-10-07
tags: [edfacts, spec, sy2026-27]
---

# FS052 — Membership (v23.0)

> [!abstract] FS052 at a glance
> **Data groups:** DG39
> **EDPass status:** Active in SY 2025-26; Inactive in SY 2026-27 at the 2026-10-07 freeze
> **Levels:** SEA, LEA, School
> **Reporting Period:** Oct 1 - October 1 or the closest school day
> **Type of count:** SEA: Once; headcount, not a full-time equivalency (FTE); LEA: At only one LEA; headcount, not a full-time equivalency (FTE); School: At only one school; headcount, not a full-time equivalency (FTE)
> **Zero counts:** Required, except as noted below
> **Categories:** Grade Level (Membership), Sex (Membership), Racial Ethnic
> **Data record:** 13 fields, 325 characters fixed-width
> **Generate domain:** [[Membership]]
> **Business rules:** [[FS052 Business Rules]] (BRSI SY 2025-26)
> **Metadata guides:** [[CCD Grades Offered Metadata User Guide]], [[CCD Staff FTE and Membership Metadata User Guide]]
> **See also:** [[analysis/EDFacts-2026-27-Delta|SY 2026-27 delta]], [[analysis/EDFacts-2026-27-Shared-Fields|shared fields]], [[EDFacts Workbook SY 2025-26|workbook]], [[EDFacts Specs|all specs]]

> [!info] Source
> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY 2026-27 DOCX (`wiki/reference/edfacts/2026-27/file-specifications/FS052-v23.0--edfacts-fs052-23-0-dg39-membership-v230-114528.docx`). Cover, document control, preface and table of contents are dropped; the document history is at the end. The DOCX remains the authority.

## Purpose

This document contains instructions for building files to submit EDFacts Data Group 39: Membership table. The definition for this data group is:

> The official unduplicated student enrollment, including students both present and absent, excluding duplicate counts of students within a specific school or local education agency or students whose membership is reported by another school or LEA.

The data collected using this file specification are collected under the authority of the Education Sciences Reform Act (ESRA).

The ED data stewarding office/s for this file: NCES

## Guidance for Submitting this File

This section contains changes from the previous school year, core requirements for submitting this file, required categories and totals, and general guidance.

### Changes from the SY 2025-26 File Specifications

Other than any editorial changes listed in the document history on page ii, there have been no other changes to this file specification.

### Core Requirements for Submitting this File

The following table contains the reporting period, the education units included or excluded, the type of count, and zero count reporting.

**Table 2.2-1: Core Reporting Requirements**

|  | **SEA** | **LEA** | **School** |
|---|---|---|---|
| Reporting Period | Oct 1 - October 1 or the closest school day | Oct 1 - October 1 or the closest school day | Oct 1 - October 1 or the closest school day |
| Education units included | Include SEA | LEAs that were operational on October 1 | Schools other than reportable programs that were operational on October 1 |
| Education units <u>NOT</u> reported |  | Closed, inactive, or future LEAs<br>OR<br>LEAs that opened after October 1<sup>st</sup><br>OR<br>Operational LEAs with FS039/DG18 = “NOGRADES” | Closed, inactive, or future schools<br>OR<br>Schools that opened after October 1<sup>st</sup><br>OR<br>Operational schools with school type “reportable programs”<br>OR<br>Operational schools with FS039/DG18 = “NOGRADES” |
| Type of count | Once;<br>headcount, not a full-time equivalency (FTE) | At only one LEA; headcount, not a full-time equivalency (FTE) | At only one school; headcount, not a full-time equivalency (FTE) |
| Zero counts | Required, except as noted below. | Required, except as noted below. | Required, except as noted below. |
| Zero exceptions or Not Applicable | Grade Level – If the state does not use Ungraded, Grade 13, and/or Adult Education, do not include records for the unused grade(s) in the file. | Grade Level – If the state does not use Ungraded, Grade 13, and/or Adult Education, do not include records for the unused grade(s) in the file.<br>Grade Level – Report only grade levels offered at the LEA (see Section 2.5 Data Reporting Guidelines for students outside of the grade span).<br>No Students in LEA - If there are no students in the LEA, report “total of education unit” as zero and do not include category set A or the subtotals for that LEA.<br>No Students in Grade Offered - If there are no students for a grade offered in the LEA, report the Subtotal by grade level (subtotal 4) as zero for that grade, then leave that grade level out of category set A and subtotals 1 and 2 for that LEA. | Grade Level – If the state does not use Ungraded, Grade 13, and/or Adult Education, do not include records for the unused grade(s) in the file.<br>Grade Level – Report only grade levels offered at the school (see Section 2.5 Data Reporting Guidelines for students outside of the grade span).<br>No Students in School - If there are no students in the school, report “total of education unit” as zero and do not include category set A or the subtotals for that school.<br>No Students in Grade Offered - If there are no students for a grade offered in the school, report the Subtotal by grade level (subtotal 4) as zero for that grade, then leave that grade level out of category set A and subtotals 1 and 2 for that school. |
| Missing | Use “-1” to report missing counts<br>Use “MISSING” when a category is not available | Use “-1” to report missing counts<br>Use “MISSING” when a category is not available | Use “-1” to report missing counts<br>Use “MISSING” when a category is not available |
| Related metadata survey | FS5017 - CCD Grades Offered Metadata<br>FS5024 - CCD Membership Metadata | FS5017 - CCD Grades Offered Metadata<br>FS5024 - CCD Membership Metadata | FS5017 - CCD Grades Offered Metadata<br>FS5024 - CCD Membership Metadata |

**Data Packages**

There are file specifications that contain a requirement that the data file and metadata or a related file must be submitted together. FS052 must be submitted together with FS5024 (CCD Membership metadata).

### Required Categories and Totals

The table below lists the combinations of the categories and totals that are expected to be submitted for the state and each LEA or school that should be included in the file.

- An “X” in the column indicates that the category value must be submitted when reporting that aggregation.

- The total indicator must be either “Y” (Yes) or “N” (No).

  - If the record is for a category set, specify an “N” (No).

  - If the record is for a subtotal or education unit total, specify a “Y” (Yes).

The technical name of the data used in the file is: MEMBER

**Table 2.3–1: Required Categories and Totals**

| **Aggregation** | **Grade Level (Membership)** | **Sex (Membership)** | **Racial Ethnic** | **Total Indicator** | **Comments** |
|---|---|---|---|---|---|
| **Category Set A** | X | X | X | N | Student Count by Grade Level (Membership) by Sex (Membership) by Racial Ethnic |
| **Subtotal 1** | X |  | X | Y | Student Count by Grade Level (Membership) by Racial Ethnic |
| **Subtotal 2** | X | X |  | Y | Student Count by Grade Level (Membership) by Sex (Membership) |
| **Subtotal 3** |  | X | X | Y | Student Count by Racial Ethnic by Sex (Membership) |
| **Subtotal 4** | X |  |  | Y | Student Count by Grade Level (Membership) |
| **Education Unit Total** |  |  |  | Y | Education Unit Total of Student Count |

### Categories and Permitted Values

This section contains the categories and permitted values used for submitting this file.

**DG39 - Membership table:**

**Grade Level (Membership)**

The grade level (primary instructional level) of students entering and receiving services in a school during a specific academic session.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                                                                                        |
|----------------------------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------|
| PK                               | Pre-Kindergarten                | A group or class that is part of a public school program and is taught in the year or years preceding kindergarten. |
| KG                               | Kindergarten                    |                                                                                                                     |
| 01                               | Grade 1                         |                                                                                                                     |
| 02                               | Grade 2                         |                                                                                                                     |
| 03                               | Grade 3                         |                                                                                                                     |
| 04                               | Grade 4                         |                                                                                                                     |
| 05                               | Grade 5                         |                                                                                                                     |
| 06                               | Grade 6                         |                                                                                                                     |
| 07                               | Grade 7                         |                                                                                                                     |
| 08                               | Grade 8                         |                                                                                                                     |
| 09                               | Grade 9                         |                                                                                                                     |
| 10                               | Grade 10                        |                                                                                                                     |
| 11                               | Grade 11                        |                                                                                                                     |
| 12                               | Grade 12                        |                                                                                                                     |
| 13                               | Grade 13                        |                                                                                                                     |
| UG                               | Ungraded                        | Students assigned to a class or program that does not have standard grade designations.                             |
| AE                               | Adult Education                 | Programs that are usually for students who have dropped out and returned to school for GED preparation.             |
| MISSING                          | Missing                         | Use when data are not available by this category.                                                                   |

**Sex (Membership)**

An indication that students are either female or male.

| **Permitted Value Abbreviation** | **Permitted Value Description** | **Comments**                                      |
|----------------------------------|---------------------------------|---------------------------------------------------|
| F                                | Female                          |                                                   |
| M                                | Male                            |                                                   |
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

### Data Reporting Guidelines

This section contains guidance for submitting this file in the format of questions and answers. The guidance is organized by the levels of the files submitted (school, LEA, and state). There is also a separate section on submitting the data by grade level.

**What if a state cannot report all students as either female or male**?

Leave those students out of category set A and the subtotals 2 and 3.  Include those students in subtotal 1 and 4 and the education unit total.

**Membership Reporting Scenarios**

The following table provides various scenarios to help identify where membership should be reported. See Section 2.6 Definitions for the definition of key terms.

**Table 2.5.–1: Reporting Membership**

| **Governance** | **LEA reports membership?** | **School reports membership?** | **Example** |
|---|---|---|---|
| 1. Student attends a school that is administered by the district that is responsible for him/her. | Home district | School in home district | This is the most common situation |
| 2. Student attends more than one school on a regular schedule | Home district | School of record in home district | A vocational school serves students from multiple districts; it is a “shared time” school that is not the school of record for any student. |
| 3. District initially responsible for the student sends him/her to attend public school in some other school district | Receiving district | Receiving school | District is too small to operate a high school; tuitions students out to neighboring district.<br>One or more districts may encounter a business rule edit that compares the sum of the school membership to the reported LEA membership. One or more may also encounter a business rule edit that compares students to teachers. If you should encounter such an edit due to this situation, please contact the Partner Support Center. |
| 4. District responsible for the student sends him/her to attend nonpublic school or program, in same or other school district.<sup>1</sup> | Sending district | Not reported | District tuitions special needs student to a private school that can meet these needs. |
| 5. Student attends a program within a school that may be self-contained, but does not have its own principal. EDFacts does not require reporting the program as a separate entity. | LEA responsible for school housing program | School that provides the principal/administrator for the program | District offers a within-school “dropout recapture” program with remedial instruction, substantial counseling, small pupil to teacher ratios for these high risk students. |
| 6. Student attends a program within a school that may be self-contained, but does not have its own principal. EDFacts requires reporting the program as a separate entity. | LEA responsible for school housing program | School that houses the Reportable program | The school includes a magnet program that must be reported separately to meet the requirements of the Civil Rights Data Collection. |
| 7. District contracts with some other education agency to provide services to students within the district’s schools. | District contracting for the services | School that the student attends | Regional Education Service Agency (RESA) hires teachers, and provides classes, within a district’s schools. The regular school principal is administratively responsible for these students. |
| 8. A specialized public school district (LEA TYPE=9) operates schools, i.e., has students, teachers, and an assigned administrator physically located in one or more LEAs. | Specialized public school district | School within the specialized public school district | The specialized public school district hires teachers, and provides classes, which may be housed in a district’s schools. The regular school principal is not administratively responsible for these students; there is a separate LEA-assigned administrator. |
| 9. State agency responsible for the student serves him/her in a school or program operated by that agency. | State agency | State agency’s school | State Department of Corrections operates elementary/secondary schools within corrections facilities. University operates a lab school. |
| 10. State agency responsible for the student sends him/her to a nonpublic school or program, in that or some other state. | State agency | Not reported | State Department of Health and Human Services tuitions special needs student to a private school in another state that specializes in meeting this student’s needs. |
| 11. Students given vouchers to attend private schools. | Not reported | Not reported |  |
| 12. Students placed by their parents in private schools whose tuition is paid for by their parents but who receive special education services from their home district. | Not reported | Not reported |  |
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Privately operated public schools should be reported in line with the public agency to which they are accountable. If the school is accountable to an LEA, report it as any other public school in the district. If the school is accountable to a state agency, follow the directions for example 9 or 10, as appropriate.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

Reporting MembershipGovernance, LEA reports membership?, School reports membership?, Example

**How are students outside of the grade span reported?**

A student may be enrolled in a grade that is not offered in the school or LEA (based on FS039 Grades Offered). Examples of this include:

- a gifted 8th grade student attending a grades 9-12 high school to take classes better matched to her abilities;

- a student in a remote area who cannot easily commute to a school that serves the student's assigned grade;

- a special needs student who is better served in a school that does not normally serve the student's assigned grade.

Report students in the grade in which they are enrolled in this school, even if the grade is outside the school’s grade span.

### Definitions

See the [EDFacts Workbook](https://www.ed.gov/data/edfacts-initiative/edfacts-resources/edfacts-workbook) for the standard definitions. The following definitions support this file:

**Home /Sending District**

The district responsible for providing the student with free public education. This is usually the district within which the student resides. A *home (sending) district* may send a student for which it is responsible to another *(receiving) district* for education.

**Receiving District**

A receiving district educates students from another district and is usually paid for that service by the student’s home (sending) district.

**School of Record**

The school of record is the school a student is assigned to and attends for their basic education. A student usually resides within the attendance area of the school of record. An exception to this is when a student is assigned to a school in a district other than his or her home district. In this case the student’s school of record would be the school to which they are assigned in the receiving district rather than the sending district. A student may attend another school(s) in addition to, or instead of, the school of record.

**Shared Time Schools**

The designation of “shared time” identifies a school that a student regularly attends but that is not the student’s school of record. Shared time schools are most commonly, but not exclusively, vocational/technical schools or postsecondary institutions. This does not include students enrolled in secondary school while also enrolled in a post-secondary school. (Schools are designated as “shared time” in the FS129 CCD School file.)

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
| filename | **MEMBERSHP** | 9 |
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

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Type | 1 | 50 | String | M | Identifies the type of file being submitted. | **SEA MEMBERSHIP TABLE**<br>**LEA MEMBERSHIP TABLE**<br>**SCHOOL MEMBERSHIP TABLE** |
| Total Records in File | 51 | 10 | Integer | M | The total number of data records contained in the file. The header record is NOT included in this count. |  |
| File Name | 61 | 25 | String | M | The file name including extension, the same as the external file name. | See section 3.0 |
| File Identifier | 86 | 32 | String | M | Any combination of standard characters to further identify the file as specified by the SEA (e.g., a date, person’s name, and version number). |  |
| File Reporting Period | 118 | 9 | String | M | The school year for which data are being reported. The required format is "CCYY–CCYY" or "CCYY CCYY", where either a hyphen or a space separates the beginning and ending years. | **2026-2027**<br>OR<br>**2026 2027** |
| Filler | 127 | 333 | String | M | Leave filler field blank. |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 460 | 1 |  | M |  |  |

Below is an example of a header record.

**Table 4.1–2: Header Record Example**

| Format  | File Type,Total Records in File,File Name,File Identifier,File Reporting Period,Filler,Carriage Return / Line Feed (CRLF) |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| Example | SCHOOL MEMBERSHIP TABLE,15,euschMEMBERSHPv000001.csv,characters to identify file,2026-2027,¶                              |

### Data Record Definition

Data records are required and immediately follow the header record in every file submitted to EDPass. Data records provide counts for the specified category sets, subtotals and education unit totals.

**Table 4.2–1: Data Records**

| **Data Element Name** | **Start Position** | **Length** | **Type** | **Pop** | **Definition / Comments** | **Permitted Values Abbreviations** |
|---|---|---|---|---|---|---|
| File Record Number | 1 | 10 | Integer | M | A sequential number assigned by the State that is unique to each row entry within the file. |  |
| **DG559** State Code | 11 | 2 | String | M | The two–digit American National Standards Institute (ANSI) code for the state, District of Columbia, and the outlying areas and freely associated areas of the United States. | For a list of valid State Codes, refer to the EDFacts Workbook. |
| **DG570** State Agency Number | 13 | 2 | String | M | A number used to uniquely identify state agencies. This ID cannot be updated through this file. | **01** – State Education Agency |
| **DG4** LEA Identifier (State) | 15 | 14 | String | M | The identifier assigned to a local education agency (LEA) by the state education agency (SEA). Also known as State LEA Identification Number (ID). This data element cannot be updated through this file. | SEA level – Blank |
| **DG5** School Identifier (State) | 29 | 20 | String | M | The identifier assigned to a school by the state education agency (SEA). Also known as the State School Identification Number (ID). This ID cannot be updated through this file. | SEA level – Blank<br>LEA level - Blank |
| Table Name | 49 | 20 | String | M | See technical name in Section 2.3 Required Categories and Totals. | **MEMBER** |
| Grade Level (membership) | 69 | 15 | String | A | The grade level (primary instructional level) of students entering and receiving services in a school during a specific academic session. | **PK** – Pre-Kindergarten<br>**KG** – Kindergarten<br>**01** – Grade 1<br>**02** – Grade 2<br>**03** – Grade 3<br>**04** – Grade 4<br>**05** – Grade 5<br>**06** – Grade 6<br>**07** – Grade 7<br>**08** – Grade 8<br>**09** – Grade 9<br>**10** – Grade 10<br>**11** – Grade 11<br>**12** – Grade 12<br>**13** – Grade 13<br>**UG** – Ungraded<br>**AE** – Adult Education<br>**MISSING** |
| Racial Ethnic | 84 | 15 | String | A | The general racial category that most clearly reflects individuals' recognition of their community or with which the individuals most identify. | **AM7** – American Indian or Alaska Native<br>**AS7** – Asian<br>**BL7** – Black or African American<br>**HI7** – Hispanic/Latino<br>**PI7** – Native Hawaiian or Other Pacific Islander<br>**MU7** – Two or more races<br>**WH7** – White<br>**MISSING** |
| Sex (Membership) | 99 | 15 | String | A | An indication that students are either female or male. | **F** – Female<br>**M** – Male<br>**MISSING** |
| Total Indicator | 114 | 1 | String | M | An indicator that defines the count level – see table 2.3-1 Required Categories and Totals | **N** – specifies detail level<br>**Y** – specifies a subtotal or total of the education unit level |
| Explanation | 115 | 200 | String | O | Text field for state use. |  |
| Student Count | 315 | 10 | Integer | M |  |  |
| Carriage Return / Line Feed (CRLF) or Line Feed (LF) | 325 | 1 |  | M |  |  |

Below is an example of a data record, this is the set of data that should be submitted for each education unit. See table 2.3-1.

**Table 4.2–2: Data Record Example – School level**

| **Aggregation**         | **Example**                                                                                                                                                                                                                                         |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Format                  | File Record Number,State Code,State Agency Number, LEA Identifier (State),School Identifier (State),Table Name,Grade Level (membership),Racial Ethnic,Sex (Membership),Total Indicator,Explanation,Student Count,Carriage Return / Line Feed (CRLF) |
| Category Set A          | 1,80,01,99981,0123,MEMBER,07,AM7,M,N,,5¶                                                                                                                                                                                                            |
| Subtotal 1              | 2,80,01,99981,0123,MEMBER,UG,AM7,,Y,,12¶                                                                                                                                                                                                            |
| Subtotal 2              | 3,80,01,99981,0123,MEMBER,12,,M,Y,,15¶                                                                                                                                                                                                              |
| Subtotal 3              | 4,80,01,99981,0123,MEMBER,,AM7,M,Y,,10¶                                                                                                                                                                                                             |
| Subtotal 4              | 5,80,01,99981,0123,MEMBER,KG,,,Y,,20¶                                                                                                                                                                                                               |
| Total of education unit | 6,80,01,99981,0123,MEMBER,,,,Y,,57¶                                                                                                                                                                                                                 |

## Document History

| **Version Number** | **Date**       | **Summary of Change**                                                                   |
|---|---|---|
| 1.0 – 22.0         |                | Versions 1.0 through 22.0 are used to build files for school years prior to SY 2026-27. |
| 23.0               | September 2026 | Updated for SY 2026-27:                                                                 |
