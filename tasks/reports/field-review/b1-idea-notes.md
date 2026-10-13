# b1-idea extraction notes (21 specs, all v23.0, SY2026-27)

Source: tasks/reports/2026-27/federal-table-cells.csv (cell text) plus DOCX XML (paragraph breaks, for permitted-value codes).
Output: b1-idea-fields.csv, 500 rows. Every spec has 7 header rows and 1 data table.

## Counts (header / data)
FS002 7/25, FS005 7/22, FS006 7/22, FS007 7/22, FS009 7/26, FS088 7/15, FS089 7/21, FS143 7/15, FS144 7/13,
FS227 7/15, FS228 7/14, FS229 7/15, FS230 7/15, FS901 7/13, FS902 7/15, FS903 7/15, FS904 7/13, FS905 7/13,
FS906 7/15, FS907 7/14, FS908 7/15.

## Method and checks
- organization_level is `all` throughout: no spec in this batch has per-level layout tables. FS002 carries one data layout
  that includes School Identifier (SEA/LEA/School share it; permitted values say "SEA level - Blank", "LEA level - Blank").
- Each header/data layout table is followed by a Format/Example table (skipped). FS904/FS905 also have an extra
  15-cell example table (Category Set A.. / Subtotal) after the data layout; FS902/903 the same. Not fields.
- Positions are contiguous and integers in every table; no duplicate keys; no merged layout cells.
- Permitted values are the codes in the layout table's own cell (every category field resolved there, so no
  `category:` prefix was needed). Verbatim notes kept for "SEA level - Blank", "See section 3.0", the State Code pointer.
- Hand fixes: FS229 Due Process Complaint Status (DPCPND printed as "DPCPND- Due process complaints pending") and
  FS230 Expedited Due Process Complaint Result (EXPRSLTNMTG printed "EXPRSLTNMTG - Expedited resolution meetings").
- category_role: File Record Number and CRLF in data rows are tagged `control`; Table Name `other`; Event Count (FS007, FS143) `count`.

## Anomalies
- Header record length differs from data record length (header pads to a longer CRLF position) in 12 specs:
  FS088 header ends 460 / data 355; FS143 460/355; FS227, FS229, FS230, FS902, FS903, FS906, FS908 505/355;
  FS228, FS907 505/340; FS901 520/325; FS904, FS905 505/325. Header = data only in FS005/006/007 (460), FS009 (520),
  FS089 (490), FS144 (325), FS002 (505). Filler lengths (e.g. FS002 header filler 378) account for the gap.
- FS088 Removal Length (IDEA) lists LTOREQ1;2TO10;GREATER10 with no MISSING (other category fields list MISSING).
- Race code order differs: FS005/006/007/089/143 list MU7 before WH7; FS002/088/902-905 list WH7 before MU7 (same set).
- FS144 Total Indicator permits only `N` (all others `N;Y`). Its element names are "DG 559 State Code", "DG 570 State Agency Number"
  (space after DG); other specs use "DG559".
- FS901/902/903/904/905 use "Lead Agency Number" (value 02); FS906/907/908 (Part C) definition text still says
  "uniquely identify state agencies" while the others say lead agencies.
- FS227-FS230, FS906-FS908 have Filler in the LEA/School positions (state-level files); FS901-FS905 likewise.
- FS902 Age (EI) is AGEB;AGE1;AGE2, FS903 Age (EI Con) AGE3;AGE4;AGE5; FS904 Age (EI) is the same as FS902.
- FS230 example header misspells "Expedited Heartings ..." and "Expedicated ... Count"; the layout table spells them correctly.
- FS901 "Racial/Ethnic" and "Sex" vs "Racial Ethnic"/"Sex (Membership)" elsewhere; FS009 "Racial /Ethnic". FS009 "Basis of Exit"
  includes code D.

## Same name, different layout/definition across the batch
- Start positions differ because column order differs per spec: Racial Ethnic 84 (FS002/005/006/007/088/143/905), 69 (FS089),
  129 (FS902/903), 99 (FS904). Sex (Membership) 99/69/84. English Learner Status (Both) at 279/99/219/234/129/114.
  Disability Category (IDEA) at 204/114/129. Length is 15 everywhere for category fields.
- Count fields vary in name and position: Student Count (FS002 495, FS005/006 450, FS009 510, FS088 345, FS089 480, FS144 315),
  Event Count (FS007 450, FS143 345), Infants and Toddlers Count (FS901/904/905 315, FS902 345), Child Count (FS903),
  WSC Count, Mediation Requests Count, Due Process Complaints Count, Expedited Due Process Complaints Count (FS230).
- Definition wording differs for the same field: WSC Status/Findings/Timelines/Pending Type (FS227 "An indication..." vs FS906
  "Indication..."); Due Process Complaint Result and Resolution Meeting Outcome definitions in FS229 and FS908 are swapped
  relative to each other; Disability Category (IDEA) text in FS006/FS089 differs from other specs; State Code definition in FS006.
- Header File Reporting Period: "school year" (FS009, FS144) vs "year" (FS902-905); Total Records in File wording in FS144 only
  ("Data Records"). Table Name definition: FS002 "sections 2.2 and 2.3", FS227-230 "Section 2.3 Required Categories".
