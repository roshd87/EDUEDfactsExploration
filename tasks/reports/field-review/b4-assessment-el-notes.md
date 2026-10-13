# b4-assessment-el field extraction notes

Source: federal-table-cells.csv for table identity and locators; DOCX via `pandoc -t json` for cell line breaks (permitted values). Script: scratchpad/b4-assessment-el/{ext,gen}.py. 389 rows, no duplicate keys, all start_position/length integers, and each spec's fields are contiguous (start+length = next start).

## Coverage (all v23.0; header rows / data rows)
- FS045 7/17, FS050 7/14, FS116 7/16, FS126 7/14, FS137 7/13, FS138 7/14, FS139 7/12, FS141 7/14
- FS175 7/23, FS178 7/23, FS179 7/23, FS185 7/24, FS188 7/24, FS189 7/24, FS210 7/11, FS211 7/11

## Structure
- Every spec has exactly one header layout table and one data layout table (plus a Format/Example table each, skipped). No per-org-level or per-record variants. organization_level = `all` throughout; SEA/LEA/School differences are carried only by the File Type permitted values (and by School Identifier being absent in LEA-ceiling specs).
- Layout tables are not always in the first position of a section; located by first-cell text `Data Element Name` (FS141 header cell has an embedded line break, `Data Element\nName`).
- Data element names that print `DGnnn` then a line break are stored as `DGnnn Name`; DG id also in technical_name_or_xml_tag. Only DG559, DG570, DG4, DG5 carry DG prefixes; no other field has a technical tag.
- source_locator is `header-record-definition#t<n>r<k>` / `data-record-definition#t<n>r<k>` (section slug shortened to the stable prefix; t<n> = table ordinal in the DOCX, r<k> = 1-based body row).

## permitted_values_summary conventions
- Codes joined by `;`. Non-code prose is kept verbatim inside `[...]`, e.g. `[SEA level – Blank]`, `[See Section 2.4 for web site with list of language codes.]`, `[For Grade Level (HS)]` as sub-list headers, and `OR` as a token for File Reporting Period.
- Category fields list their codes in the layout cell itself, so no `category:` resolution from the categories section was needed. Exception: Language (Native), FS045 seq 13 and FS141 seq 8, points to an external language-code list (Section 2.4); FS045 table 8 lists only a handful of extra ISO 639-3 codes and was not folded in.
- File Type permitted values are the full SEA/LEA/(School) strings in brackets; FS045, 116, 126, 210, 211 list SEA and LEA only (LEA-ceiling specs, no School Identifier in the data record); the other 11 add SCHOOL.

## Anomalies
- FS045 has four consecutive Filler fields (seq 7-10, 15 chars each) before the categories; FS116 has three (seq 10-12); FS050 has one 125-char Filler (seq 10).
- Military Connected Student Status has length 125 in FS175, FS178, FS179 (absorbs the trailing space to position 374) but 15 in FS185, FS188, FS189.
- Combined fields: Grade Level (Lower) or (HS), Assessment Administered ... (lower grades) or (HS), Participation Status M/RLA/S (lower) or (HS) are single fields with two code lists under `For ...` headers (FS175, 178, 179, 185, 188, 189). The FS179/FS189 science variants use Grade Level (Lower SCI)/(HS SCI) with grade 09 in the lower list.
- Total Indicator permitted values are `N` only in FS050, 126, 137, 138, 139 (no Y total) and `N;Y` in the other 11 specs.
- FS116 serves two data groups (DG648, DG849) with one layout; Table Name lists both table names (TTLIIILEPSTDSRV;TTLIIILIEPSTDSRV). FS175/178/179/185/188/189 likewise list HS and LG table names.
- English Learner Accountability (FS050 seq 8, FS139 seq 7) is a category; a naive `count` regex mis-tagged it and it was fixed to `category`.

## Same-named fields that differ across the batch
- Position of every field after Table Name varies by spec because category columns differ (Total Indicator starts at 84/99/114/129/159/174/239/279/374 depending on spec; Explanation, Student Count, CRLF shift with it). Same-named category fields shift too: Disability Status (Only) at 69 (FS126), 99 (FS050, FS138), 114 (others).
- Header Filler length / CRLF start differ per spec: 458/585 (FS175-179), 363/490 (FS185, FS188), 333/460 (FS045, 050, 116, 139, 189), 213/340 (FS126, 141, 210, 211), 183/310 (FS137, 138). Header Total Records in File prints `Records In File` in FS126, 141, 210, 211 and `in File` in the other 12.
- Definition wording differences: DG559 State Code in FS045 says Federal Information Processing Standards (FIPS); the other 15 say ANSI (FS141 prints an en-dash `two–digit`). Total Indicator definition varies between `– see table`, `. See table`, and `see Table` (FS050/178/179 use `. See table`; FS116 `Table`). Filler FS116 lacks the final period. FS188 File Reporting Period definition has a stray quote artifact (`formats "CCYY–CCYY" “ or`). Table Name definition differs in FS175 and FS185.
- DG4 LEA Identifier definition has 3 wording variants across the batch; DG5 School Identifier appears only in the 11 specs that have school-level files.
