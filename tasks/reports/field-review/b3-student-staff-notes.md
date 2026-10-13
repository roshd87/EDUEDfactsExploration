# b3-student-staff field extraction notes

Output: b3-student-staff-fields.csv, 419 rows, 19 specs, all v23.0. Layout tables taken from the DOCX via `pandoc -t json` (cell paragraphs and line breaks preserved); table_index values match federal-table-cells.csv.

## Counts (header / data)
- FS032 7/18; FS033 7/11; FS040 7/21; FS052 7/13; FS086 7/14; FS118 7/17
- FS150 7/16; FS151 7/17; FS160 7/16; FS163 7/9; FS194 7/12; FS195 7/18
- FS222 7/10; FS226 7/10; FS067 7/14; FS070 7/14; FS099 7/13; FS203 7/15
- FS059 7 header / 14 data SEA/LEA + 14 data School (28 data rows)
- No duplicate keys; every start_position and length is an integer; per-table positions are contiguous (no gaps/overlaps).

## Multi-table layouts and conventions
- FS059 has two data layouts, per org level: t13 (Table 4.2-1, "SEA and LEA level", DG528 FTESTAFF) and t15 (Table 4.2-3, School, DG644 CLASSTEACHFTE). The SEA and LEA share one table, so organization_level is the literal "SEA/LEA" (not split into SEA and LEA rows) and "School". t13 has Staff Category (CCD) at pos 84; t15 has Filler there and a School Identifier (State) at 29 where t13 has Filler.
- FS195 has one data layout (t20) serving SEA/LEA/School, so organization_level = all. Its examples (t21 SEA/LEA, t22 School) are not fields and are skipped.
- All other specs: one header + one data layout, level all. Format/Example tables skipped.
- FS163 (GFSA) has no Table Name or Total Indicator field: data = File Record Number, State Code, State Agency Number, LEA ID, School ID, Filler, GFSA Reporting Status, Explanation, CRLF.
- Two printed names embed the DG number with no space or with a space: "DG528Table Name" (FS059 printed without space after the DG), "DG 559 State Code" (FS150, FS151). technical_name_or_xml_tag normalised to DG559 etc. FS059 field_name has whitespace collapsed ("DG528 Table Name").
- Fields with the same DG prefix appear only on state/LEA/school identifiers (DG559, DG570, DG4, DG5) and FS059 Table Names (DG528, DG644). FS150/FS151 carry DG559 only on State Code.
- permitted_values_summary: codes parsed from "CODE - description" lines in the layout cell; for category fields the code list was re-resolved from the matching Categories and Permitted Values table (matched by definition text) and prefixed `category:<field name>=`. Layout cell and section table code sets agree for every category field (including MISSING, which the section tables list and the layout cell also lists). FS150 Major Racial and Ethnic Groups has no definition-matching table; resolved to t10 ("Note: The Major Racial and Ethnic Groups...") by hand.
- Non-category fields keep their note text, e.g. "SEA level - Blank", "For a list of valid State Codes, refer to the EDFacts Workbook." Table Name codes joined with ';' (FS150/FS151 list GRADRT4YRADJ..GRADRT10YRADJ, GRADCOHORT4YR..GRADCOHORT10YR; FS033 LUNCHFREERED;DIRECTCERT; FS195 CHRONABSENT;CHRONABSENTSL). FS195 category cells (Sex, Racial Ethnic, disability, EL) also carry "When reporting for DG887, leave blank", which is dropped from the summary.
- category_role heuristics: FS163 GFSA Reporting Status and all Table Name fields are role `other`; Student/Teacher/Staff Count, FTE and Student Rate are `count`.

## Anomalies and cross-spec differences
- Same field, different position (records differ per spec; positions are not comparable across specs): Racial Ethnic 84 (FS032/040/052/195) vs 159 (FS118); Sex (Membership) 99 (FS032/040/052/160) vs 69 (FS195); English Learner Status (Only) 129/114/99; Economically Disadvantaged 159/114/144; Homeless Enrolled 174/129/144. Major Racial and Ethnic Groups 69 (FS150/151) vs 84 (FS160).
- FS099 Table Name starts at 44 length 20, preceded by a 15-char Filler at 29; every other spec has Table Name at 49 (LEA ID 15/14, then 20-char School ID/filler 29/20). FS099 Staff Category (Special Education Related Services) is length 50, unlike the 15-char category fields elsewhere. FS099 has Filler at 29/15 in place of a School Identifier field.
- Student Count length 10 everywhere except FS151 (length 8, pos 375). FS150 Student Rate is the rate field (not a count).
- FTE type: "Decimal Number" (FS059, FS070) vs "Decimal" (FS099, FS203); FS059 t15 prints "DecimalNumber". Definitions differ: FS059 Staff FTE "Decimal numbers down to one hundredth FTE are permitted." vs FS099/FS070/FS203 "Report decimal numbers down to one-hundredth FTE". FS070/FS203 Teacher FTE start 330 vs 145.
- Header record: File Type 1/50, Total Records in File 51/10 (printed "In" capitalised in FS033, FS151, FS059), File Name 61/25, File Identifier 86/32, File Reporting Period 118/9 identical in all 19. Header Filler length and CRLF position vary per spec. Header CRLF position differs from data CRLF position in FS052 (460/325), FS118 (370/385), FS150 (351/366), FS151 (351/383), FS222 and FS226 (430/280), FS070 (460/340), FS203 (460/355); equal in the rest.
- Total Indicator / Explanation positions vary by spec (Total Indicator: FS032 189, FS033 84, FS222/226 69, FS194/195 249); Explanation always length 200 except where printed otherwise.
- Wording drift only: File Record Number definition says "SEA" in FS163 and "State" elsewhere; State Code uses en-dash "two-digit" in FS033/052/059/099/FS040 and hyphen elsewhere; typo "ASNI" in FS151 State Code definition; Total Indicator definition varies (FS032 "See table 2.3-1", FS222/226 omit the table reference, FS059 cites DG528/DG644 tables). FS160 header-example text prints "(CLRF)" in the Format table (typo, not a field).
- Disability Status (IDEA) in FS032/FS040 lists WODIS;WDIS; Disability Status (Only) in FS118/150/151/160/195 lists WDIS only. FS086 has two discipline-method fields with different code sets (non-IDEA: EXPNOTMODNOALT.. 7 codes; IDEA: EXPNOTMOD, EXPMOD, OTHERDISACTION, REMOVEOTHER, NOACTION).
- FS033 Lunch Program Status layout cell and section table both list FL, RPL, MISSING.
