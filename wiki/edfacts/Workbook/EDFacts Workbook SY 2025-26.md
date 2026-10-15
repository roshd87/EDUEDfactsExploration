---
title: EDFacts Workbook SY 2025-26
school_year: SY 2025-26
source: workbook/edfacts-workbook-faqs-sy-2025-26-113626.pdf
sha256: ba6e9a3e495ddd47e26fb0c2c8fbf03342022f2bc4ef0723b4bb991cbf07c273
frozen: 2026-10-07
tags: [edfacts, workbook, edpass]
---

# EDFacts Workbook with FAQs — SY 2025-26

> [!abstract] At a glance
> The reference guide for the EDFacts information collection: EDPass roles, the directory upload order, each program area's files, metadata and data packages, notification templates, FAQs, standard data definitions, the -1 missing-data rule, race/ethnicity guidance, state codes and the glossary.
> **Newest published:** SY 2025-26 (no SY 2026-27 workbook at the 2026-10-07 freeze).
> **See also:** [[EDFacts Specs|all specs]], [[BRSI SY 2025-26|business rules]]

> [!info] Source
> Converted by `tasks/convert_companions_to_vault.py` from the frozen SY 2026-27 catalog copy of the EDFacts Workbook (`wiki/reference/edfacts/2026-27/workbook/edfacts-workbook-faqs-sy-2025-26-113626.pdf`). The original remains the authority.

> [!note] Screenshots and figures from the PDF are not carried over; headings, text and tables are.

## 1. Introduction

This document provides information on how to upload data files, enter metadata, resolve data quality errors, maintain the annual State Submission Plan (SSP), upload data notes, and submit data through the EDPass application for SY 2025-26. A glossary of EDFacts terminology appears in Appendix B.

### 1.1 Partner Support Center (PSC)

To assist states with data upload, metadata entry, data submission, and reporting, ED provides a dedicated Partner Support Center (PSC). PSC distributes email announcements about system shutdowns, reminders of due dates, and technical hints. PSC distributes a monthly Support Update that includes submission reminders, system upgrade announcements, and other helpful information. SEA staff members who use EDPass will automatically receive these announcements. PSC also serves as a liaison between the states and ED.

PSC also provides technical assistance through the EDFacts Community of Practice Site. The EDFacts Community of Practice site (known as EDFacts CoP) promotes collaboration, knowledge sharing, and interaction among EDFacts Coordinators and the larger EDFacts community.

Please contact PSC via email at EDFacts @ed.gov .

PSC is open from 9:00 a.m. to 5:00 p.m. ET, Monday through Friday, excluding federal holidays.

### 1.2 Technical Assistance

#### Resources available on EDFacts Community of Practice Site:

Accessing resources on the EDFacts CoP site does not require a login; however, logging into the EDFacts CoP site grants EDFacts Coordinators access to the Discussion Board to participate in valuable conversations with peers, browse key discussions from the past, access or upload relevant resources to an open-source library, and engage in a number of other features made available on the site.

Visiting the EDFacts CoP site is highly recommended. If you do not yet have a login and want to join the EDFacts CoP, please contact PSC.

- **Data Submission Organizer** : Lists the due date for each File Specification and metadata collections by school year, as well as the level at which each file is submitted.

- **PSC Support Updates:** Includes current and past issues in a newsletter to SEAs on how to effectively use EDFacts and understand related changes.

- **Upcoming Events Calendar:** Lists upcoming file and survey due dates.

- **EDFacts **Corner:** Contains resources related to the modernization efforts of the EDFacts data collection including past webinars, webinar recordings, and supporting documentation.

   - EDPass Bulletin Board: Provides helpful hints and technical support related to EDPass; maintained daily during data collection windows.

- **PSC Videos / Webinars:** Contains links to webinar recordings and presentation files from past PSC training sessions conducted for states.

- **EDFacts **Meeting Archive:** Includes meeting materials from the EDFacts Data Conferences annually held by ED.

- **File Format Checker (FFC):** This tool can be installed locally for states to check for non-XML format errors prior to attempting to upload data files to EDPass. The file format checker is available through the EDFacts Community or available upon request from PSC.

- **Featured Resources and Tools** : Technical assistance documents on EDFacts related topics, coordination, and systems. Folders include the EDFacts OMB Package Resources and Tools_ , for the most recent OMB Package documentation.

For additional information on accessing assistance resources, please contact PSC.

### 1.3 Clearance Package

The Office of Management and Budget (OMB) approved the “Annual Mandatory Collection of Elementary and Secondary Education Data for EDFacts ” for school years 2025-26, 2026-27 and 2027-28. This data collection activity is approved until September 30, 2028. The data approved for collection by EDFacts includes data submitted by SEAs through EDPass. The complete package information can be found at Reginfo.gov.

## 2. EDPass Application

The EDPass application is used to upload data files, collect metadata, resolve data quality issues, maintain the SSP, provide data notes, and submit data to ED.

EDPass can be accessed at the following link: EDPass – Login

### 2.1 User Roles

There are two types of roles assigned to users.

- **EDPass Manager –** This role gives the user access to:

   - All EDPass functions and data areas

   - Administrative access to manage user roles and accounts

   - Limit of 2 users assigned to this role per entity

- **Other Users –** Allows a user to have general access to EDPass with permissions aligned with the specific functions and data areas designated by the EDPass Manager.

**_Note!_** Users must first establish a secure Login.gov account to log into EDPass.

### 2.2 EDFacts File Specifications

The EDPass File Specifications can be downloaded from the EDFacts Initiative File Specifications. Links for EDPass File Specifications are also available in the Data Submission Organizer (DSO) in the EDFacts CoP site.

Upon accessing the EDFacts Initiative File Specifications, select the School Year link, then select the EDPass File Specifications link in the Link to File column.

File Specifications are listed on the website as either EDPass File Specifications – Active or EDPass File Specifications – Inactive. Inactive files are moved to the _EDPass File Specifications – Active_ section as files are unlocked in EDPass. In addition, some school years contain File Specifications that are retired or not required; these are listed in their respective sections on the web page.

File Specifications may require an update during the collection year due to updated or enhanced policy, mid-year changes, or to fix technical problems/defects. File Specifications are version controlled. To ensure the use of the correct version, reference the version number of the File Specification.

**_Note!_** Data has been collected in EDPass beginning with SY 2022-23 data.

### 2.3 Directory / Grades Offered Files

This section provides a basic outline of the Directory file in EDFacts and does not substitute reading the [[FS029 Directory|FS029]] – Directory File Specification when building and uploading Directory files. For detailed information regarding the Directory file, please

see the [[FS029 Directory|FS029]] – Directory File Specification on the EDFacts SY 2025-26 File Specifications page.

EDFacts maintains a four-tier directory of education units in each of the 50 states, the District of Columbia, Puerto Rico, Guam, American Samoa, Marshall Islands, Micronesia, Northern Marianas, Republic of Palau, Virgin Islands, Department of Defense, and the Bureau of Indian Education. The three tiers are, from highest to lowest:

- (1) State education agency (SEA)

- (2) Local education agency (LEA), referred to as “agency” in NCES Common Core of Data (CCD)

- (3) School (SCH)

- (4) Charter Collection

**_Note!_** Some states have schools that do not fit into the EDFacts four-tier system. Contact the PSC with any questions regarding this issue.

In EDPass the required order of the directory and charter data file upload is as follows:

1. SEA Directory is rolled over year to year – _no action required by the SEA_ .

2. LEA Directory ([[FS029 Directory|FS029]]) – With supervisory unions[1]

   - An LEA record must exist before schools belonging to that LEA can be uploaded.

   - An LEA record must exist before any other data can be uploaded for that LEA

   - If a state has supervisory unions, a file transmittal with the LEAs that are supervisory unions must be uploaded _before a file transmittal with the subordinate LEAs can be uploaded._

3. LEA Directory ([[FS029 Directory|FS029]]) – With subordinate LEAs

4. Charter Authorizer Roster ([[FS190 Charter Authorizer Directory|FS190]]) if applicable

   - Charter Authorizers are associated with charter schools in the school directory. The charter authorizers must already exist before uploading the school directory.

5. School Directory ([[FS029 Directory|FS029]])

   - A school record must exist before any other data can be uploaded for that school

6. Management Organization Roster ([[FS196 Management Organization for Charter Schools Roster|FS196]]) if applicable

   - Management Organization Roster must be submitted before Crosswalk of Charter Schools to Management Organizations ([[FS197 Crosswalk of Charter Schools to Management Organizations|FS197]]).

> [1] SEAs with no supervisory unions and subordinate LEAs can uploaded its LEAs in a single LEA file.

Since acceptance of all other files is dependent upon having complete directory data for every education unit, the SEA should confirm that all directory data are complete and accurate before uploading and submitting all other files.

All school and LEA directory data are specific to a single school year. This satisfies ED’s need for an **_annual_** survey for CCD. Business rules will be used to match one institution in a school year to the same institution in the prior school year. Business rules at the LEA and school levels check to verify that the status for each entity for the current year align with the status for that same entity in the prior year (in alignment with Appendix Table C-1 of the [[FS029 Directory|FS029]] – Directory File Specification). These are described in more detail in the guidance section of the Directory File Specification.

**_Note!_** In EDPass, the NCES IDs and the Directory and Grades Offered report are available via the _Download Data_ option from the Data submission List kebab menu (see the EDPass User Guide for instructions).

The table below lists the data groups in the Directory and Grades Offered File Specifications.

|**File Spec**|**Data Group Name**|**DG ID**|
|[[FS029 Directory\|029]]|Address location|9|
|[[FS029 Directory\|029]]|Address mailing|8|
|[[FS029 Directory\|029]]|Charter authorizer identifier (state)|804|
|[[FS029 Directory\|029]]|Charter LEA status|653|
|[[FS029 Directory\|029]]|Charter status|27|
|[[FS029 Directory\|029]]|Education entity name|7|
|[[FS029 Directory\|029]]|Effective date|571|
|[[FS029 Directory\|029]]|LEA identifier (NCES)|1|
|[[FS029 Directory\|029]]|LEA identifier (state)|4|
|[[FS029 Directory\|029]]|Local education agency (LEA) type|453|
|[[FS029 Directory\|029]]|Out of state indicator|669|
|[[FS029 Directory\|029]]|Reconstituted status|743|
|[[FS029 Directory\|029]]|School identifier (NCES)|529|
|[[FS029 Directory\|029]]|School identifier (state)|5|
|[[FS029 Directory\|029]]|School type|21|
|[[FS029 Directory\|029]]|State agency number|570|
|[[FS029 Directory\|029]]|State code|559|
|[[FS029 Directory\|029]]|Supervisory union identification number|551|
|[[FS029 Directory\|029]]|Telephone - education entity|10|
|[[FS029 Directory\|029]]|Operational status – LEA|16|
|[[FS029 Directory\|029]]|Operational status – school|531|

|[[FS029 Directory\|029]]|Web site address|11|
|[[FS039 Grades Offered\|039]]|Grades Offered|18|

### 2.4 Non-Directory Files

#### 2.4.1 Accountability and Reporting Provisions of ESEA, as amended by ESSA

The data groups in this section support the oversight and reporting of the accountability provisions of ESEA, as amended by ESSA.

**_School Support and Improvement_**

|**File Spec**|**Data Group Name**|**DG ID**|
|206|Comprehensive support and targeted support schools|842|
|212|Comprehensive Support and improvement identification|866|
|212|Target Support and improvement identification|867|
|212|Additional Targeted Support and Improvement identification<br>table|888|

#### 2.4.2 Other Accountability

|**File Spec**|**Data Group Name**|**DG ID**|
|132|School Improvement Funds 1003(a)|794|
|160|HS graduates postsecondary enrollment table|739|
|195|Chronic absenteeism table - SEA/LEA|887|
|195|Chronic absenteeism table - School|814|
|199|Graduation rate indicator status table|834|
|200|Academic achievement indicator status table|835|
|201|Other academic indicator status table|836|
|202|School quality or student success indicator status table|838|
|203|Teachers table|839|
|205|Progress achieving English language proficiency indicator<br>status table|837|
|226|Economically disadvantaged students|56|

#### 2.4.3 Adjusted Cohort Graduation Rate

##### Required

|**File Spec**|**Data Group Name**|**DG ID**|
|150|Regulatory four-year adjusted cohort graduation rate table|695|
|151|Cohorts for regulatory four-year adjusted cohort graduation<br>rate table|696|

##### Required

If an SEA has adopted one or more extended-year Adjusted Cohort Graduation Rate (ACGR) as part of the SEA’s approved ESEA consolidated State plan for the reporting year, the SEA reports each extended-year ACGR included in the State plan. Do not report extended-year ACGRs not included in the State’s approved ESEA consolidated State plan for the reporting year. If an SEA submits extended year data, the SEA must submit both the rate data in FS150 and the cohort data in FS151. The 5011 - ACGR metadata collection is pre-populated with the expected extended-year ACGRs per State plan.

|**File Spec**|**Data Group Name**|**DG ID**|
|150|Regulatory five-year adjusted cohort graduation rate table|697|
|150|Regulatory six-year adjusted cohort graduation rate table|755|
|150|Regulatory seven-year adjusted cohort graduation rate table|850|
|150|Regulatory eight-year adjusted cohort graduation rate table|852|
|150|Regulatory nine-year adjusted cohort graduation rate table|854|
|150|Regulatory ten-year adjusted cohort graduation rate table|856|
|151|Cohorts for regulatory five-year adjusted cohort graduation<br>rate table|698|
|151|Cohorts for regulatory six-year adjusted cohort graduation<br>rate table|756|
|151|Cohorts for regulatory seven-year adjusted cohort graduation<br>rate table|851|
|151|Cohorts for regulatory eight-year adjusted cohort graduation<br>rate table|853|
|151|Cohorts for regulatory nine-year adjusted cohort graduation<br>rate table|855|
|151|Cohorts for regulatory ten-year adjusted cohort graduation<br>rate table|857|

#### 2.4.4 State Assessments

##### Required

|**File Spec**|**Data Group Name**|**DG ID**|
|175|Academic achievement in mathematics grades 3-8 table|874|
|175|Academic achievement in mathematics HS table|875|

|**File Spec**|**Data Group Name**|**DG ID**|
|178|Academic achievement in reading/language arts grades 3-8<br>table|876|
|178|Academic achievement in reading/language arts HS table|877|
|179|Academic achievement in science grades 3-9 table|878|
|179|Academic achievement in science HS table|879|
|185|Assessment participation in mathematics grades 3-8 table|880|
|185|Assessment participation in mathematics HS table|881|
|188|Assessment participation in reading/language arts grades 3-8<br>table|882|
|188|Assessment participation in reading/language arts HS table|883|
|189|Assessment participation in science grades 3-9 table|884|
|189|Assessment participation in science HS table|885|

#### 2.4.5 Funding Flexibility – REAP

The data group in this section supports the provisions of ESEA, as amended by ESSA, to provide LEAs or SEAs flexibility in how they use federal education funding.

|**File Spec**|**Data Group Name**|**DG ID**|
|131|REAP Alternative Fund Use Authority (AFUA) status|614|

#### 2.4.6 Individuals with Disabilities Education Act (IDEA) Part B

The data groups in this section support oversight and reporting of the Individuals with Disabilities Education Act (IDEA) (IDEA Section 300.8(c)(1-13)). Data in this section are used for the Office of Special Education Program’s (OSEP’s) Annual Report to Congress and for IDEA state accountability purposes.

|**File Spec**|**Data Group Name**|**DG ID**|
|[[FS002 Children with Disabilities (IDEA) School Age\|002]]|Children with disabilities (IDEA) school age table|74|
|005|Children with disabilities (IDEA) removal to interim alternative<br>educational setting table|512|
|006|Children with disabilities (IDEA) suspensions/expulsions table|475|
|007|Children with disabilities (IDEA) reasons for unilateral removal table|476|
|009|Children with disabilities (IDEA) exiting special education table|85|
|070|Special education teachers (FTE) table|486|
|088|Children with disabilities (IDEA) disciplinary removals table|598|
|[[FS089 Children with Disabilities (IDEA) Early Childhood\|089]]|Children with disabilities (IDEA) early childhood table|613|
|099|Special education related services personnel (FTE) table|609|
|112|Special education paraprofessionals (FTE) table|647|

|**File Spec**|**Data Group Name**|**DG ID**|
|143|Children with disabilities (IDEA) total disciplinary removals table|682|
|144|Educational services during expulsion table|683|
|227|IDEA Part B Dispute Resolution Written, Signed Complaints|894|
|228|IDEA Part B Dispute Resolution Mediation Requests|895|
|229|IDEA Part B Dispute Resolution Due Process Complaints|896|
|230|IDEA Part B Dispute Resolution Expedited Due Process Complaints|897|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|231]]|IDEA Part B Allocations|898|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|231]]|IDEA Part B Allocations|899|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|231]]|IDEA Part B Allocations|900|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|232]]|MOE Status|901|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|232]]|MOE Status|902|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|232]]|MOE Status|903|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|232]]|MOE Status|904|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|233]]|MOE Funds|905|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|233]]|MOE Funds|906|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|234]]|CEIS and CCEIS Provisions|907|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|234]]|CEIS and CCEIS Provisions|908|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|235]]|Significant Disproportionality Reason|909|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|236]]|CEIS and CCEIS Reservations|910|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|236]]|CEIS and CCEIS Reservations|911|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|237]]|Children Receiving CEIS|912|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|237]]|Children Receiving CEIS|913|
|[[IDEA Part B MOE CEIS CCEIS Metadata User Guide\|238]]|Children Receiving CCEIS|914|

If an LEA reported students in [[FS002 Children with Disabilities (IDEA) School Age|FS002]] and [[FS089 Children with Disabilities (IDEA) Early Childhood|FS089]], the LEA is expected to report data in the personnel files (FS070, FS099, and FS112).

**_Tip!_** Permitted values reported in [[FS002 Children with Disabilities (IDEA) School Age|FS002]], [[FS089 Children with Disabilities (IDEA) Early Childhood|FS089]], and FS099 must align with the responses to the metadata collected via EDPass for SY 2025-26, listed in Section 2.5.

#### 2.4.7 English Learners and Title III of ESEA, as Amended by ESSA

The data groups in this section support oversight and reporting of programs for the education of English Learners as contained in Title I and Title III of ESEA, as amended by ESSA. Title III also provides programs for students who are immigrants.

|**File Spec**|**Data Group Name**|**DG ID**|
|045|Immigrant table|519|
|050|Title III English language proficiency results table|151|
|067|Title III teachers table|422|
|116|Title III ELs served table|648|
|116|Title III students served in English language instruction program<br>table|849|
|126|Title III former EL students table|668|
|137|English language proficiency test table|674|
|138|Title III English language proficiency test table|675|
|139|English language proficiency results table|676|
|141|EL enrolled table|678|
|210|Title III English learners five years table (previously DG 840)|864|
|211|Title III English learners exited table (previously DG 841)|865|

#### 2.4.8 McKinney-Vento Homeless Program

The data groups in this section support oversight and reporting of the McKinney-Vento Education for Homeless Children and Youth Program, a formula grant program that aids in the education of homeless children and youths and collects comprehensive information regarding the impediments they must overcome to regularly attend school.

|**File Spec**|**Data Group Name**|**DG ID**|
|118|Homeless students enrolled table|655|
|170|McKinney-Vento subgrant recipient flag|754|
|194|Young homeless children served (McKinney-Vento) table|818|

#### 2.4.9 Migrant Education Program

The data groups in this section support oversight and reporting of the Migrant Education Program (MEP).

|**File Spec**|**Data Group Name**|**DG ID**|
|054|MEP children served 12-month table|102|
|121|Migratory children eligible 12-month table|634|
|145|MEP services table|684|
|165|Migratory children eligible regular school year table|110|
|165|Consolidated MEP funds status|514|

#### 2.4.10 Neglected or Delinquent Program

The data groups in this section support oversight and reporting of the Prevention and Intervention Programs for the Education of Children and Youth Who Are Neglected, Delinquent or At-Risk Program (N or D) (under ESEA _,_ as amended by ESSA, Title I, Part D, Subparts 1 and 2), a formula grant program to provide supplementary educational services to children and youth in state-run institutions to ensure a successful transition to school or the workforce. This section does not include programs funded solely through Title I, Part A.

|**File Spec**|**Data Group Name**|**DG ID**|
|113|N or D academic achievement table - State Agency|628|
|119|Neglected programs participation table - State Agency|869|
|119|Delinquent programs participation table - State Agency|870|
|125|N or D academic achievement table – LEA|629|
|127|Delinquent programs participation table - LEA|872|
|127|At-Risk programs participation table - LEA|873|
|218|Title I Neglected or Delinquent outcomes in programs table –<br>state agency|889|
|219|Title I Delinquent and At-Risk outcomes in programs table –<br>LEA|890|
|220|Title I Neglected or Delinquent program at exit table – state<br>agency|891|
|221|Title I Delinquent and At-Risk program at exit table – LEA|892|
|222|Title I Part A foster care enrolled|893|
|[[FS224 N or D Assessment Proficiency – State Agency\|224]]|N or D assessment proficiency table – State Agency (optional)|868|
|[[FS225 N or D Assessment Proficiency – LEA\|225]]|N or D assessment proficiency table – LEA (optional)|871|

#### 2.4.11 Non-Fiscal Common Core of Data (CCD)

The data groups in this section comprise most of the Non-Fiscal CCD data. CCD is a program that annually collects fiscal and non-fiscal data about all public schools, public school districts, and SEAs in the United States. The data are supplied by SEA officials and include information that describes schools and school districts, including name, address, and phone number; descriptive information about students and staff, including demographics; and fiscal data, including revenues and current expenditures. EDFacts collects only non-fiscal data for CCD.

|**File Spec**|**Data Group Name**|**DG ID**|
|032|Dropouts table|326|
|[[FS033 Free and Reduced Price Lunch\|033]]|Free and reduced-price lunch table|565|
|[[FS033 Free and Reduced Price Lunch\|033]]|Direct certification|813|
|040|Graduates/completers table|306|

|**File Spec**|**Data Group Name**|**DG ID**|
|[[FS052 Membership\|052]]|Membership table|39|
|[[FS059 Staff FTE\|059]]|Staff FTE table|528|
|[[FS059 Staff FTE\|059]]|Teachers (FTE)|644|
|[[FS129 CCD School\|129]]|Virtual school status|803|
|[[FS129 CCD School\|129]]|NSLP status|791|
|[[FS129 CCD School\|129]]|Shared time status|573|

#### 2.4.12 Gun-Free Schools Act

The data groups in this section relate to the Gun-Free Schools Act (GFSA).

|**File Spec**|**Data Group Name**|**DG ID**|
|086|Students involved with firearms table|596|
|130|Persistently dangerous status|36|
|163|GFSA reporting status|603|

#### 2.4.13 Title I Program (Non-Accountability Provisions)

The data groups in this section support oversight and reporting of the Title I Program excluding the accountability and reporting which are in separate sections in this workbook.

|**File Spec**|**Data Group Name**|**DG ID**|
|037|Title I SWP/TAS participation table|548|
|134|Title I participation table|670|
|193|Title I, Part A Allocations|797|
|193|Parental involvement reservation|788|
|193|LEA Reservation to serve homeless children and youth|886|
|223|Title I school status|22|

#### 2.4.14 Charter Schools and Districts

The data groups in this section support oversight and reporting of charter schools. Only states with charter legislation report these data groups.

##### Charter Appropriation

|**File Spec**|**Data Group Name**|**DG ID**|
|[[FS207 State Appropriations for Charter Schools\|207]]|State appropriation for charter schools|845|

##### Charter Authorizers

Charter schools are linked to charter authorizers through the directory.

|**File Spec**|**Data Group Name**|**DG ID**|
|[[FS190 Charter Authorizer Directory\|190]]|Charter authorizer name|798|
|[[FS190 Charter Authorizer Directory\|190]]|Charter authorizer address location|805|
|[[FS190 Charter Authorizer Directory\|190]]|Charter authorizer address mailing|806|
|[[FS190 Charter Authorizer Directory\|190]]|Charter authorizer type|807|
|[[FS190 Charter Authorizer Directory\|190]]|Charter authorizer identifier (state)|808|

##### Management Organizations

Charter schools are linked to management organizations through the [[FS197 Crosswalk of Charter Schools to Management Organizations|FS197]] Crosswalk of Charter Schools to Management Organizations.

##### Definition

A management organization is a separate legal entity that 1) contracts with one or more charter schools to manage, operate, and oversee the charter schools; or 2) holds a charter, or charters, to operate a network of charter schools.

|**File Spec**|**Data Group Name**|**DG ID**|
|[[FS196 Management Organization for Charter Schools Roster\|196]]|Management Organization Name|825|
|[[FS196 Management Organization for Charter Schools Roster\|196]]|Employer identification number (EIN)|826|
|[[FS196 Management Organization for Charter Schools Roster\|196]]|Organization address location|827|
|[[FS196 Management Organization for Charter Schools Roster\|196]]|Organization address mailing|828|
|[[FS196 Management Organization for Charter Schools Roster\|196]]|Management organization type|829|
|[[FS197 Crosswalk of Charter Schools to Management Organizations\|197]]|Crosswalk of Charter Schools to Management Organizations|833|

##### Charter Contracts

|**File Spec**|**Data Group Name**|**DG ID**|
|[[FS198 Charter Contracts\|198]]|Charter Contract ID Number|830|
|[[FS198 Charter Contracts\|198]]|Charter Contract Approval Date|831|
|[[FS198 Charter Contracts\|198]]|Charter Contract Renewal Date|832|

### 2.5 Individuals with Disabilities Education Act (IDEA) Part C

The data in this section are collected under the authority of the Individuals with Disabilities Education Act (IDEA), 20 U.S.C. 1418(a)(1)(C) and (a)(3).Data in this section are used for the Annual Mandatory Report on Infants and Toddlers Exiting Part C (OMB 1820-0557, expires 2/28/2027).

|**File Spec**||**DG ID**|
|901|Infants and Toddlers with Disabilities (IDEA Part C) Exiting|5022|
|[[FS902 Infants and Toddlers with Disabilities (IDEA Part C) Early Intervention\|902]]|Infants and Toddlers with Disabilities (IDEA Part C) Early<br>Intervention|5023|
|[[FS903 Children with Disabilities (IDEA Part C) Continuing Early Intervention\|903]]|Children with Disabilities (IDEA Part C) Continuing Early<br>Intervention|5024|
|[[FS904 At Risk Infants and Toddlers with Disabilities (IDEA Part C)\|904]]|At Risk Infants and Toddlers with Disabilities (IDEA Part C)|5025|
|[[FS905 Infants and Toddlers with Disabilities (IDEA Part C) Cumulative Count\|905]]|Infants and Toddlers with Disabilities (IDEA Part C) Early<br>Intervention Services|5026|
|[[IDEA Part C Dispute Resolution Metadata User Guide\|906]]|IDEA Part C Dispute Resolution Written, Signed Complaints|5029|
|[[IDEA Part C Dispute Resolution Metadata User Guide\|907]]|IDEA Part C Dispute Resolution Mediation Requests|5030|
|[[IDEA Part C Dispute Resolution Metadata User Guide\|908]]|IDEA Part C Dispute Resolution Due Process Complaints|5031|

### 2.6 EDPass Metadata

EDPass collects EDFacts metadata via EDPass metadata collections. The metadata is used to define state-specific parameters for reporting data collected in EDFacts data files. The user guides for the metadata collections can be downloaded from the EDFacts CoP page.

User guides may require an update during the collection year due to updated or enhanced policy or changes that take place mid-year. User guides, like File Specifications, are version controlled. To ensure the use of the correct version, reference the Document History section of the user guide.

|**FS**|**EDPass** **Metadata Collection**|
|---|---|
|5002|IDEA Child Count|
|5003|IDEA Environments – School Age|
|5004|IDEA Environments – Early Childhood|
|5005|Assessment metadata - General|
|5006|Assessment metadata - Math|
|5007|Assessment metadata - RLA|
|5008|Assessment metadata – Science|
|5009|Statewide English Language Proficiency Assessments metadata|
|5010|Gun Free Schools Act (GFSA)|
|5011|Extended-year ACGR metadata|
|5012|IDEA Discipline metadata|
|5013|IDEA Staffing metadata|
|5014|IDEA Exiting metadata|
|5015|CCD Dropouts metadata|

|5016|CCD Graduates/Completers metadata|
|---|---|
|5017|CCD Grades Offered|
|5018|CCD Staffing metadata|
|5024|CCD Membership metadata|
|5026|IDEA Part C Exiting|
|5027|IDEA Part C Child Count|
|5028|IDEA Part C Dispute Resolution Metadata|
|5029|Determination Data Year Metadata|

### 2.7 EDPass Data Packages

The following data must be submitted as a package for SEAs and LAs (Part C). All required levels of both the file specification and metadata must be in the _Ready to Submit_ status in order to proceed with submission.

- **Charter Management Organizations:** [[FS196 Management Organization for Charter Schools Roster|FS196]] (Multiple DGs) — Management Organization for Charter Schools Roster and [[FS197 Crosswalk of Charter Schools to Management Organizations|FS197]] (DG833) — Crosswalk of Charter Schools to Management Organizations

- **Assessment Data Packages:**

   - Mathematics Data Package

      - FS175 (DG874, DG875) — Academic Achievement in Mathematics

      - FS185 (DG880, DG881) — Assessment Participation in Mathematics

      - [[Academic Assessment Metadata User Guide|FS5006]] - Assessment metadata — Mathematics

   - Reading/Language Arts Data Package

      - FS178 (DG876, DG877) — Academic Achievement in Reading/Language Arts

      - FS188 (DG882, DG883) — Assessment Participation in Reading/Language Arts

      - [[Academic Assessment Metadata User Guide|FS5007]] - Assessment metadata - Reading/Language Arts

   - Science Data Package

      - FS179 (DG878, DG879) — Academic Achievement in Science

      - FS189 (DG884, DG885) — Assessment Participation in Science

      - ▪ [[Academic Assessment Metadata User Guide|FS5008]] - Assessment metadata – Science

- **Extended- year ACGR:** FS5011 – Extended-year ACGR metadata (read only page), FS150 — Adjusted Cohort Graduation Rate and FS151 — Cohorts for Adjusted Cohort Graduation Rate

- **IDEA Environments – School Age:** [[IDEA Part B Child Count Metadata User Guide|FS5003]] – IDEA Environments – School Age and [[FS002 Children with Disabilities (IDEA) School Age|FS002]] – Children with Disabilities (IDEA) School Age

- **IDEA Environments – Early Childhood:** [[IDEA Part B Child Count Metadata User Guide|FS5004]] – IDEA Environments – Early Childhood and [[FS089 Children with Disabilities (IDEA) Early Childhood|FS089]] – Children with Disabilities (IDEA) Early Childhood

- **IDEA Discipline:** [[IDEA Discipline Exiting Staffing Metadata User Guide|FS5012]] – IDEA Discipline metadata and FS144 (DG683) — Educational Services During Expulsion data file

- **IDEA Staffing:** [[IDEA Discipline Exiting Staffing Metadata User Guide|FS5013]] – IDEA Staffing metadata and FS099 (DG609) — Special Education Related Services Personnel data file

- **IDEA Exiting:** [[IDEA Discipline Exiting Staffing Metadata User Guide|FS5014]] – IDEA Exiting and FS009 – Children with Disabilities (IDEA) Exiting Special Education data file

- **CCD Staffing:** [[CCD Staff FTE and Membership Metadata User Guide|FS5018]] – CCD Staffing metadata and [[FS059 Staff FTE|FS059]] – Staff FTE

- **CCD Dropouts:** [[CCD Dropouts Graduates Completers Metadata User Guide|FS5015]] – CCD Dropouts metadata and FS032 (DG326) — Dropouts data file

- **CCD Graduates/Completers:** [[CCD Dropouts Graduates Completers Metadata User Guide|FS5016]] – Graduates/Completers metadata and FS040 (DG306) — Graduates/Completers data file

- **CCD Membership:** [[CCD Staff FTE and Membership Metadata User Guide|FS5024]] – CCD Membership metadata and [[FS052 Membership|FS052]] – Membership

- **Accountability:**

   - FS199 (DG 834) – Graduation Rate Indicator Status and [[Accountability Metadata User Guide|FS5019]] – Graduation Rate Indicator Status metadata

   - FS200 (DG835) – Academic Achievement Indicator Status and [[Accountability Metadata User Guide|FS5020]] – Academic Achievement Indicator Status metadata

   - FS201(DG836) – Other Academic Indicator Status and [[Accountability Metadata User Guide|FS5021]] – Other Academic Indicator Status metadata

   - FS202 (DG838) – School Quality or Student Success Indicator Status and [[Accountability Metadata User Guide|FS5022]] – School Quality or Student Success Indicator Status metadata

   - FS205 (DG837) – Progress Achieving English Language Proficiency Indicator Status and [[Accountability Metadata User Guide|FS5023]] – Progress Achieving English Language Proficiency Indicator Status metadata

- **IDEA Part B Dispute Resolution:**

   - FS227 (DG894) – IDEA Part B Dispute Resolution Written, Signed and Complaints

   - FS228 (DG895) – IDEA Part B Dispute Resolution Mediation Requests

   - FS229 (DG896) – IDEA Part B Dispute Resolution Due Process Complaints

   - FS230 (DG897) – IDEA Part B Dispute Resolution Expedited Due Process Complaints

- **IDEA Part B MOE and CEIS:**

   - [[IDEA Part B MOE CEIS CCEIS Metadata User Guide|FS231]] (DG898, 899, 900) – IDEA Part B Allocations

   - [[IDEA Part B MOE CEIS CCEIS Metadata User Guide|FS232]] (DG901, 902, 903, 904) – MOE Reduction

   - [[IDEA Part B MOE CEIS CCEIS Metadata User Guide|FS233]] (DG905, 906) – MOE Reduction Funds

`o` [[IDEA Part B MOE CEIS CCEIS Metadata User Guide|FS234]] (DG907, 908) – CEIS Provision

   - [[IDEA Part B MOE CEIS CCEIS Metadata User Guide|FS235]] (DG909) – Significant Disproportionality Identification

   - [[IDEA Part B MOE CEIS CCEIS Metadata User Guide|FS236]] (DG910, 911) – CEIS Reservation

   - [[IDEA Part B MOE CEIS CCEIS Metadata User Guide|FS237]] (DG912, 913) – Children Receiving CEIS

   - [[IDEA Part B MOE CEIS CCEIS Metadata User Guide|FS238]] (DG914) – Children Receiving CCEIS

   - [[IDEA Part B MOE CEIS CCEIS Metadata User Guide|FS5029]] (DG2093) – Determination Data Year Metadata

- **IDEA Part C Exiting:**

   - FS901 (DG5022) – Infants and Toddlers with Disabilities (IDEA Part C) Exiting

   - [[IDEA Part C Exiting Metadata User Guide|FS5026]] Infants and Toddlers with Disabilities (IDEA Part C) Exiting Metadata

- **IDEA Part C Child Count:**

   - [[FS902 Infants and Toddlers with Disabilities (IDEA Part C) Early Intervention|FS902]] (DG5023) – Infants and Toddlers with Disabilities (IDEA Part C) Early Intervention

   - [[FS903 Children with Disabilities (IDEA Part C) Continuing Early Intervention|FS903]] (DG504) – Children with Disabilities (IDEA Part C) Continuing Early Intervention

   - [[FS904 At Risk Infants and Toddlers with Disabilities (IDEA Part C)|FS904]] (DG5025) – At Risk Infants and Toddlers with Disabilities (IDEA Part C)

   - [[FS905 Infants and Toddlers with Disabilities (IDEA Part C) Cumulative Count|FS905]] (DG5026) – Infants and Toddlers with Disabilities (IDEA Part C) Early Intervention Services

   - [[IDEA Part C Child Count Metadata User Guide|FS5027]] Infants and Toddlers with Disabilities (IDEA Part C) Count Metadata

- **IDEA Part C Dispute:**

   - [[IDEA Part C Dispute Resolution Metadata User Guide|FS906]] (DG5029) – IDEA Part C Dispute Resolution Written, Signed Complaints

   - [[IDEA Part C Dispute Resolution Metadata User Guide|FS907]] (DG5030) – IDEA Part C Dispute Resolution Mediation Requests

   - `o` [[IDEA Part C Dispute Resolution Metadata User Guide|FS908]] (DG5031) – IDEA Part C Dispute Resolution Due Process Complaints

   - FS5028 Infants and Toddlers with Disabilities (IDEA Part C) Dispute Resolution Metadata

## 3. Common Processes Overview

This section discusses common EDFacts processes and contains templates to assist with process notifications.

### 4.1 Standard Notification Templates

PSC requests standard information for general requests submitted by states to the Department. The following templates provide the information needed when requests or notifications are escalated to the Department. When contacting PSC for these requests, please provide the information in the template.

#### 4.1.1 Request Correction Opportunity for NCES IDs for Future Schools

When an SEA needs to submit a [[FS029 Directory|FS029]] – Directory file to obtain NCES IDs for future schools, the request for a correction opportunity must include the following template with detailed responses:

- File: [[FS029 Directory|FS029]]

- File Level: (LEA or SCH or both)

- Can your state adjust the timelines, so you have all info in and final prior to ED's [[FS029 Directory|FS029]] due date?

- Scope: Short description of the LEAs and SCHs being added

#### 4.1.2 Request Correction Opportunity after Due Date

When an SEA discovers corrections need to be made to data or data notes after the due date, the SEA must request a correction opportunity. A correction opportunity request must be submitted to PSC once the updated data is available for resubmission to be considered by the program office. The request for a correction opportunity must include the following template with detailed responses:

- File(s):

- Level(s):

- School Year(s):

- Has the SEA requested a correction opportunity for this FS previously? `o` If yes, provide PSC ticket number:

   - If yes, what is the SEA doing to mitigate corrections to this data going forward?

- Detailed justification for the correction request on why the data/files and/or data note need corrections):

- Detailed explanation on the impact on the data – How much does this correction change the data (include detailed scope of data change)?:

- How will the SEA assure that these data will be correct for the next school year and beyond?

**_Note!_** If a correction request is approved, enter a detailed comment in the SSP regarding what data were corrected and why.

**_New!_** In an effort to support states in addressing data quality results, ensuring that files are resubmitted in a timely manner, and submitted statuses are not reverted, we are updating the process for requesting and completing correction opportunities.

Moving forward, once a state has been notified that its COR files have been unlocked in EDPass, the state should prioritize resubmission and **must notify PSC as soon as the relevant files have been resubmitted** . After receiving this notification, PSC will relock the files in EDPass to help avoid file statuses reverting from _Submitted_ due to cross-file validations.

PSC strongly advises states to refrain from uploading additional files after a COR file has been resubmitted and until PSC has officially relocked the files. Please note that leading up to EDPass close days, there may be a delay before PSC is able to relock files. States may continue to upload and submit additional files if necessary to avoid missing a deadline; however, states should actively monitor any unlocked COR files that were resubmitted and ensure that any status reversions are addressed.

#### 4.1.3 Late File Submission Notifications

If a file will not be submitted by the file due date, update the SSP in EDPass for that file and school year to indicate the expected late submission date. A note explaining the reason for delay will be required in the _Timely “Notes”_ field.

#### 4.1.4 New EDFacts Coordinator

Please provide PSC timely notifications of new EDFacts Coordinators. The notification of a new Coordinator _must_ come from the previous Coordinator. PSC will need the following information for these requests:

- Full Name

- Phone Number

- SEA Email address (Confirmation that a login.gov account has been created)

- State or Entity

- Individual being replaced as Coordinator?

- Does that person still require access to any EDFacts applications, including EDPass?

- Is the new Coordinator also being named as an SEA EDPass Manager?

#### 4.1.5 New CCD Non-Fiscal Coordinator

Please provide PSC timely notifications of new CCD Non-Fiscal Coordinators to ensure accounts are set up correctly. The notification of a new Coordinator _must_ come from the previous Coordinator. PSC will need the following information for these requests:

- Full Name

- Phone Number

- SEA Email address

- State or Entity

- Individual being replaced as Coordinator?

- Does the new Coordinator still require access to any EDFacts applications, including DMS?

#### 4.1.6 New IDEA Data Manager

Please provide PSC timely notifications of new IDEA Part B or Part C Data Managers. The notification of a new Data Manager _must_ come from the previous Data Manager. PSC will need the following information for these requests:

- Full Name

- Phone Number

- SEA Email address (Confirmation that a Login.gov account has been created)

- State or Entity

- Specify IDEA Part B or Part C Data Manager

- Who is being replaced as Data Manager?

- Does that person still require access to EDPass?

- For Part C only - Is the new Coordinator also being named as a LA EDPass Manager?

#### 4.1.7 New SPP/APR Coordinator – Part B and Part C

The EDFacts Partner Support Center also assists SEAs with the SPP/APR data collection for Part B and Part C.

Please provide PSC timely notifications of a new Part B State Director or Part C State Coordinator to ensure APR Tool accounts are set up correctly. PSC will need the following information for these requests:

- Full Name

- Phone Number

- SEA Email address (Confirmation that a Login.gov account has been created)

- State

- Specify Part B State Director or Part C State Coordinator:

- Who is being replaced as Part B State Director or Part C State Coordinator? Does that person still require access to the APR Tool?

- Level of permission? (View User, Data Entry User, Submission User, Super User)

## 4. Frequently Asked Questions (FAQs)

### How do I request a new account?

The SEA EDPass Managers are responsible for the maintenance of SEA user accounts within EDPass and the LA EDPass Managers are responsible for the maintenance of LA user accounts within EDPass.

### Are NCES IDs mandatory for all schools and LEAs?

When submitting directory data, NCES identifiers are mandatory for all schools and LEAs unless the school or LEA has one of the following School Year Start Operational statuses:

- New (if not **_Future_** in the prior year)

- Added

- Future (only in the first year)

### What should I do if I have uploaded data in EDPass that is incorrect, prior to submission?

When uploading data files to EDPass, choose from two options: (1) Merge, merges data with existing data); or (2) Replace, replaces existing files. The EDPass User Guide, located on the EDFacts Initiative Site has instructions on the upload process. If assistance is needed, contact PSC.

### What should I do if I have submitted data in EDPass that needs to be updated, and the due date has passed ?

After a due date has passed, data are no longer accepted by EDPass. A detailed request must be sent to PSC requesting a “Correction Opportunity” (COR) for the data to be unlocked in EDPass for the system to allow updated files to be uploaded/submitted. PSC will process the request through the necessary channels to ensure that the impacted program offices are aware and approve of the request. It is the state’s responsibility to notify PSC as soon as the COR files have been resubmitted so that the files can be locked and prevent the Submitted status from reverting due to cross file validations.

**_Important!_** In the event of a COR being granted, ED will inform the SEA of the correction period dates. Additionally, if an SEA is correcting published data (i.e., Graduation or Assessment data), there is no guarantee the data will be republished after correction.

### Other than for technical assistance, when do I contact PSC?

To suggest a change or enhancement that will make EDFacts and EDPass work more efficiently for the states, please inform PSC. Suggestions are periodically reviewed to determine if resources and priorities allow for implementation. When approved enhancements are activated, PSC will notify states in the PSC Support Update.

**_Tip!_** If there are individuals in your state who want to receive the PSC Support Update, send an email to PSC including the individual’s email address. PSC will add the user to the Support Update distribution list.

## Appendix A: Standard Data Definitions

As part of the drive to streamline data collections across the Department, EDFacts has standardized several definitions used throughout the EDFacts data groups. The standardization of data definitions reduces recordkeeping and reporting burden on the states, ultimately increasing the level of data quality.

### Children with Disabilities (IDEA)

Children having intellectual disability; hearing impairment, including deafness; speech or language impairment; visual impairment, including blindness; serious emotional disturbance (hereafter referred to as emotional disturbance); orthopedic impairment; autism; traumatic brain injury; developmental delay; other health impairment; specific learning disability; deaf-blindness; or multiple disabilities and who, by reason thereof, receive special education and related services under the Individuals with Disabilities Education Act (IDEA _)_ according to an Individualized Education Program (IEP), Individualized Family Service Plan (IFSP), or a services plan.<sup>1</sup>

Definition adapted from PL 108-446, Section 602(3), 34 C.F.R. Part 300.8(a)(1).

### Disability Categories Under IDEA

Some files collect data by disability categories under IDEA (IDEA Section 300.8(c)(113)). Not all states use all disability categories allowed by IDEA (e.g., other health impairment; developmental delay for a subset of the allowable ages). Below are the definitions of the disability categories.

**Autism —** This refers to a developmental disability significantly affecting verbal and nonverbal communication and social interaction, generally evident before age 3, that adversely affects educational performance. Other characteristics often associated with autism are engagement in repetitive activities and stereotyped movements, resistance to environmental change or change in daily routines, and unusual responses to sensory experiences. Autism does not apply if a child's educational performance is adversely affected primarily because the child has an emotional disturbance.

**Deaf-blindness —** This refers to concomitant hearing and visual impairments, the combination of which causes such severe communication and other developmental and educational problems that they cannot be accommodated in special education programs solely for children with blindness or for children with deafness.

**Deafness —** This refers to a hearing impairment that is so severe that the child is impaired in processing linguistic information through hearing, with or without amplification, that adversely affects a child’s educational performance.

**Developmental delay —** A child with a developmental delay, as defined by the Individuals with Disabilities Education Act, is a child who is experiencing developmental delays, as defined by your state, and as measured by appropriate diagnostic instruments and procedures in one or more of the following cognitive areas: physical development, cognitive development, communication development, social or emotional development, or adaptive development.

**_Note!_** A state may only use this disability category for children with disabilities (IDEA) ages 3 through 9.

**Emotional disturbance —** This refers to a condition exhibiting one or more of the following characteristics over a long period of time and to a marked degree, which adversely affects a child’s educational performance: (1) an inability to learn, which cannot be explained by intellectual, sensory or health factors; (2) an inability to build or maintain satisfactory interpersonal relationships with peers and teachers; (3) inappropriate behavior or feelings under normal circumstances; (4) a general pervasive mood of unhappiness or depression; or (5) a tendency to develop physical symptoms or fears associated with personal or school problems. This term includes schizophrenia. The term does not apply to children who are socially maladjusted, unless it is determined they have an emotional disturbance.

**Hearing impairment —** This refers to an impairment in hearing, whether permanent or fluctuating, that adversely affects a child’s educational performance but that is not included under the definition of deafness.

**Intellectual disability —** This refers to significantly sub average general intellectual functioning, existing concurrently with deficits in adaptive behavior and manifested during the developmental period, that adversely affects a child's educational performance.

**Multiple disabilities —** This refers to concomitant impairments (e.g., intellectual disability-blindness, intellectual disability -orthopedic impairments) the combination of which causes such severe educational problems that they cannot be accommodated in special education programs solely for one of the impairments. The term does not include deaf-blindness.

**Orthopedic impairment —** This refers to a severe orthopedic impairment that adversely affects a child's educational performance. The term includes impairments caused by congenital anomaly (e.g., clubfoot, absence of some member), impairments caused by disease (e.g., poliomyelitis, bone tuberculosis) and impairments from other causes (e.g., cerebral palsy, amputations and fractures or burns that cause contractures).

**Specific learning disability —** This refers to a disorder in one or more of the basic psychological processes involved in understanding or using language, spoken or written, which may manifest itself in an imperfect ability to listen, think, speak, read, write, spell or do mathematical calculations, including such conditions as perceptual disabilities, brain injury, minimal brain dysfunction, dyslexia and developmental aphasia. The term does not include learning problems that primarily result from visual, hearing or motor

disabilities, of intellectual disability, of emotional disturbance or of environmental, cultural, or economic disadvantage.

**Speech or language impairment —** This refers to a communication disorder, such as stuttering, impaired articulation, a language impairment, or a voice impairment that adversely affects a child’s educational performance.

**Traumatic brain injury —** This refers to an acquired injury to the brain caused by an external physical force, resulting in total or partial functional disability or psychosocial impairment or both, that adversely affects a child's educational performance. The term applies to open or closed head injuries resulting in impairments in one or more areas, such as cognition; language; memory; attention; reasoning; abstract thinking; judgment; problem-solving; sensory, perceptual, and motor abilities; psychosocial behavior; physical functions; information processing; and speech. The term does not apply to brain injuries that are congenital or degenerative or to brain injuries induced by birth trauma.

**Visual impairment —** This term, including blindness, means an impairment in vision that, even with correction, adversely affects a child's educational performance. The term includes both partial sight and blindness.

**Other health impairment —** This refers to having limited strength, vitality or alertness, including a heightened alertness to environmental stimuli, that results in limited alertness with respect to the educational environment, that (i) is due to chronic or acute health problems such as asthma, attention deficit disorder or attention deficit hyperactivity disorder, diabetes, epilepsy, a heart condition, hemophilia, lead poisoning, leukemia, nephritis, rheumatic fever, sickle cell anemia, and Tourette syndrome; and (ii) adversely affects a child’s educational performance.

### English Learner Students

In coordination with the state’s definition based on Section 8101(20) of the ESEA, as amended by the ESSA, the term ‘English learner’, when used with respect to an individual, means an individual –

(A) who is aged 3 through 21;

(B) who is enrolled or preparing to enroll in an elementary school or a secondary school;

(C ) _(who is i, ii, or iii)_

(i) who was not born in the United States or whose native languages are languages other than English;

_(ii) (who is I and II)_

(I) who is a Native American or Alaska Native, or a native resident of the outlying areas; and

(II) who comes from an environment where a language other than English has had a significant impact on the individual’s level of English language proficiency; or

(iii) who is migratory, whose native language is a language other than English, and who come from an environment where a language other than English is dominant; and

(D) whose difficulties in speaking, reading, writing, or understanding the English language may be sufficient to deny the individual _(who is denied i or ii or iii)_<sup>_2_</sup>

- (i) the ability to meet the challenging State academic standards;

- (ii) the ability to successfully achieve in classrooms where the language of instruction is English; or

(iii) the opportunity to participate fully in society.

**_Note!_** To be classified as an English learner:

- An individual must be A, B, C, and D.

- For C, an individual can be i, ii, or iii.

- If C-ii, the individual must be I and II.

- For D, an individual must be denied i or ii or iii.3

### Migratory Children

According to sections 1115(c)(1)(A) (incorporated into the MEP program by virtue of sections 1304(c)(2), 1115(b), and 1309(2) of the statute and 200.103(a) of the regulations, a child is a "migratory child" and is eligible for MEP services if all of the following conditions are met:

   1. The child is not older than 21 years of age; _and_

   2. The child is entitled to a free public education (through grade 12) under State law, or the child is not yet at a grade level at which the LEA provides a free public education; _and_

   3. The child made a qualifying move in the preceding 36 months as a migratory agricultural worker or a migratory fisher, or did so with, or to join a parent/guardian or spouse who is a migratory agricultural worker or a migratory fisher; and

   4. With regard to the qualifying move identified in paragraph 3 above, the child moved due to economic necessity from one residence to another residence, and:

      - a. From one school district to another; or

      - b. In a State that is comprised of a single school district, has moved from one administrative area to another within such district; or

      - c. Resides in a school district of more than 15,000 square miles and migrates a distance of 20 miles or more to a temporary residence.

- **Homeless students**

Children/youth who lack a fixed, regular, and adequate nighttime residence, and includes:

- (1) students who are sharing the housing of other persons due to loss of housing, economic hardship, or a similar reason; are living in motels, hotels, trailer parks,

> 2 Must be determined by a valid assessment

> 3 Statutory reference – Section 8101(20) of _ESEA_

or camping grounds due to the lack of alternative adequate accommodations; are living in emergency or transitional shelters; are abandoned in hospitals;

(2) students who have a primary night-time residence that is a public or private place not designed for or ordinarily used as a regular sleeping accommodation for human beings (within the meaning of section 103(a)(2)(C));

- (3) students who are living in cars, parks, public spaces, abandoned buildings, substandard housing, bus or train stations, or similar settings; and

- (4) migratory students who qualify as homeless for the purposes of this subtitle because they are living in circumstances described in (1) through (3) above.<sup>4</sup>

### Covered State for McKinney-Vento

To be considered a covered state, the state must have statutory law that defines or describes the phrase, “awaiting foster care placement” for purposes of a program under the McKinney-Vento Act. [P.L. 114-95, Section 9501(c)]

### Children in foster care

‘‘Foster care’’ means 24-hour substitute care for children placed away from their parents and for whom the agency under title IV–E of the Social Security Act has placement and care responsibility. This includes, but is not limited to, placements in foster family homes, foster homes of relatives, group homes, emergency shelters, residential facilities, childcare institutions, and proadaptive homes. A child is in foster care in accordance with this definition regardless of whether the foster care facility is licensed and payments are made by the State, tribal, or local agency for the care of the child, whether adoption subsidy payments are being made prior to the finalization of an adoption, or whether there is federal matching of any payments that are made.

### Students who are military connected

Students who are military connected. Status as a student with a parent who is a member of the armed forces, where ‘‘armed forces.’’ Note that the National Defense Authorization Act for Fiscal Year 2020 removed the requirement for a parent to be on “active duty.” Rather, they must only be a “member of the Armed Forces.” Under 10 U.S.C. 101(a)(4), “Armed Forces” is defined to include the Army, Navy, Air Force, Marine Corps, Space Force, and Coast Guard, which would also incorporate their reserve components (i.e., Army National Guard and Air National Guard, and Army, Navy, Air Force, Marine Corps, and Coast Guard Reserves).  With this change, and in the absence of any limitation with respect to an individual’s duty status or a definition of a “member” of the Armed Forces, a State educational agency (SEA) has some flexibility in defining the subgroup. Given removal of the “active duty” limitation, however, at a minimum the subgroup must include students with parents on “active service.”  Under 10 U.S.C. 101(d)(3), this would include individuals on active duty or full-time National Guard duty, but not those on inactive status or in the Retired Reserves. Beyond this, an SEA may establish a more expansive definition.

4 As defined by MV Homeless Education Assistance Act of 2002, Subtitle B of Title VII, Section 725

## Appendix B: Reporting Missing Data with -1

When reporting data and counts are missing, SEAs should report the count as “-1” in the data file for the education unit total (EUT) regardless of whether the data will ever be available. For some File Specifications, the -1 count will fail the business rules checking completeness. The SEA will need to resolve the rule failure by providing a data note that explains why the data for the entity is missing.

## Appendix C: Race Ethnicity Guidance

Final guidance issued in the Federal Register on October 19, 2007 (72 Fed. Reg. 59267) on the collection and reporting of racial and ethnic data by educational institutions and other grantees now allows individuals to self-identify their ethnicity and race and select more than one race and/or ethnicity. This change permits individuals to more accurately reflect their racial and ethnic backgrounds by expanding reporting options from five to seven permitted values and permitting individuals to select more than one category. The final guidance requires, beginning with data for SY 2010-11 and future school years, that all SEAs must submit racial and ethnic data (except for assessment and accountability data required under Title I of the ESEA) by the seven permitted values. The seven permitted values are listed below:

- American Indian or Alaskan Native

- Asian

- Black or African American

- Hispanic/Latino

- Native Hawaiian or Other Pacific Islander

- White

- Two or more races

## Appendix D: State Abbreviations and State Codes

|**State Name**|**State Code**|**State Abbreviation**|
|ALABAMA|01|AL|
|ALASKA|02|AK|
|ARIZONA|04|AZ|
|ARKANSAS|05|AR|
|CALIFORNIA|06|CA|
|COLORADO|08|CO|
|CONNECTICUT|09|CT|
|DELAWARE|10|DE|
|DISTRICT OF COLUMBIA|11|DC|
|FLORIDA|12|FL|
|GEORGIA|13|GA|
|HAWAII|15|HI|
|IDAHO|16|ID|
|ILLINOIS|17|IL|
|INDIANA|18|IN|
|IOWA|19|IA|
|KANSAS|20|KS|
|KENTUCKY|21|KY|
|LOUISIANA|22|LA|
|MAINE|23|ME|
|MARYLAND|24|MD|
|MASSACHUSETTS|25|MA|
|MICHIGAN|26|MI|
|MINNESOTA|27|MN|

|**State Name**|**State Code**|**State Abbreviation**|
|MISSISSIPPI|28|MS|
|MISSOURI|29|MO|
|MONTANA|30|MT|
|NEBRASKA|31|NE|
|NEVADA|32|NV|
|NEW HAMPSHIRE|33|NH|
|NEW JERSEY|34|NJ|
|NEW MEXICO|35|NM|
|NEW YORK|36|NY|
|NORTH CAROLINA|37|NC|
|NORTH DAKOTA|38|ND|
|OHIO|39|OH|
|OKLAHOMA|40|OK|
|OREGON|41|OR|
|PENNSYLVANIA|42|PA|
|RHODE ISLAND|44|RI|
|SOUTH CAROLINA|45|SC|
|SOUTH DAKOTA|46|SD|
|TENNESSEE|47|TN|
|TEXAS|48|TX|
|UTAH|49|UT|
|VERMONT|50|VT|
|VIRGINIA|51|VA|
|WASHINGTON|53|WA|
|WEST VIRGINIA|54|WV|

|**State Name**|**State Code**|**State Abbreviation**|
|WISCONSIN|55|WI|
|WYOMING|56|WY|
|AMERICAN SAMOA|60|AS|
|BUREAU OF INDIAN AFFAIRS|59|BI<sup>5</sup>(6)|
|DEPARTMENT OF DEFENSE|63|DoD (10)|
|GUAM|66|GU|
|MARSHALL ISLANDS|68|MH|
|MICRONESIA|64|FM|
|NORTHERN MARIANAS|69|MP|
|PUERTO RICO|72|PR|
|REPUBLIC OF PALAU|70|PW|
|VIRGIN ISLANDS|78|VI|

5 Not official U.S. Postal State Abbreviations. The state abbreviations for the Department of Defense (overseas) schools are AA, AE, and AP to indicate schools located in Asia, Europe, and the Pacific respectively. For the Department of Defense (domestic) schools and Bureau of Indian Education schools, state abbreviations correspond to the state in which the school is located.

## Appendix E: EDFacts Glossary

|**Term**<br>Category|**Topic**<br>EDFacts|**Description**<br>A data category (category) characterizes a count, dollar<br>value, or percentage rate in an EDFactsdata group. A data<br>category is a grouping that an SEA uses to aggregate data<br>before the SEA sends the data to ED.|
|Category set|EDFacts|A data category set (category set) is a combination of data<br>categories (e.g., racial ethnic by grade level).|
|CCD|ED|Common Core of Data collected by the National Center for<br>Education Statistics (NCES)|
|CWD|ED|Children with disabilities (IDEA)|
|Data group|EDFacts|An EDFactsdata group is a specific aggregation (i.e., group)<br>of related data that is stored in EDFactsto satisfy the<br>specific information need of one or more ED program<br>offices. An EDFactsdata group does not represent a single<br>data entry but rather a set of related data entries. Each<br>EDFactsdata group is intended to be discrete, concise,<br>universally understood, and non-redundant.|
|Data record|EDFacts|Detailed information, in a specified order and format, for an<br>education unit.|
|EDFacts<br>Coordinator|EDFacts|Official SEA contact for EDFacts|
|EDPass|EDFacts|Data collection system where SEAs upload data files, resolve<br>data quality errors with data notes, maintain the SSP and<br>submit data to the Department|
|Education unit|EDFacts|An individual education entity such as SEA, LEA, or SCH.|
|Education unit<br>level|EDFacts|Tier in the education hierarchy—SCH, LEA, or SEA level.|
|E_MAPS_|EDFacts|EDFactsMetadata and Process System|
|English Learner<br>(EL)|ED|As defined in Appendix A (formerly referred to as “Limited<br>English Proficient”).|
|ESEA|ED|Elementary and Secondary Education Act of 1965, as<br>amended|
|ESSA|ED|Every Student Succeeds Act (ESSA) - reauthorizes<br>Elementary and Secondary Education Act (ESEA).|

|**Term**<br>File<br>Specification|**Topic**<br>EDFacts|**Description**<br>A document that outlines the files, record layout and data<br>elements in the record layouts.|
|IDEA|ED|Individuals with Disabilities Education Act|
|LA|ED|Lead agency|
|LEA|ED|Local education agency|
|MEP|ED|Migratory Education Program|
|NCES|ED|National Center for Education Statistics|
|OMB|Federal|U.S. Office of Management and Budget—the approval<br>authority for all data collections; administers and enforces<br>the_Paperwork Reduction Act_of 1995.|
|PSC|EDFacts|Partner Support Center|
|Reporting<br>period|EDFacts|The specific date or period of time for which data is<br>reported.|
|SCH|EDFacts|School|
|SEA|ED|State education agency|
|SEA<br>submitter(s)|EDFacts|Person(s) the SEA has approved to submit files and access<br>the secure part of EDPass. Each submitter receives a<br>personal USER ID and PASSWORD from ED.|
|SSP|EDFacts|State Submission Plan|
|Steward|ED|Office or person with primary responsibility for a data<br>group.|
|Submission|EDFacts|A set of related data belonging to only one education unit<br>(i.e., one school or one LEA), for one school year and for one<br>file. For example, Membership data for a single school for<br>the SY 2020-21, or current year status data for an LEA for<br>the SY 2020-21.|
|SWP|ED|School-wide program for Title I|
|SY|ED|School Year|
|TAS|ED|Targeted Assistance Schools for Title I|

The Department of Education’s mission is to promote student achievement and preparation for global competitiveness by fostering educational excellence and ensuring equal access.

## Document History

|**Version**<br>**Number**|**Date**|**Summary of Change**|
|2.0 – 3.0|May 2025|Tracked updates for SY 2023-24|
|4.0|March 2026|• Rolled over for SY 2025-26<br>• FS039 – Grades Offered and FS5017 - Grades<br>Offered Metadata are no longer a package<br>• Added MOE/CEIS/CCEIS files under 2.4 Non-<br>Directory Files<br>• Update to the Correction Opportunity Process in<br>Section 4.1.1|
