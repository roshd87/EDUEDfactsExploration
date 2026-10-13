# b5-program field extraction notes

Output: `b5-program-fields.csv`, 347 rows (112 header + 235 data), all v23.0, no duplicate keys, all start/length integers, positions contiguous in every table (start = prior start + length).

Method: layout tables read from CSV cells; permitted-value line breaks recovered from `pandoc -t json` (cells matched to CSV by table order and cell text). Every spec has exactly one header layout table and one data layout table (+ one small Format/Example table each, skipped), so organization_level = `all` everywhere. No merged cells, no missing tables.

## Counts (header / data)
FS037 7/20, FS054 7/15, FS113 7/22, FS119 7/18, FS121 7/19, FS125 7/22, FS127 7/17, FS134 7/12, FS145 7/13, FS165 7/9, FS218 7/11, FS219 7/11, FS220 7/11, FS221 7/11, FS224 7/12, FS225 7/12 (header total 112, data total 235).

## Anomalies
- `all` hides agency scope: FS037 and FS134 are one table for SEA and LEA (File Type lists both "SEA ..." and "LEA ..."; DG4 LEA Identifier says "SEA level – Blank"). FS113/119/121/145/054/218/220/224 are SEA files; FS125/127/219/221/225 are LEA files; FS165 is a School file (has DG5 School Identifier). The layouts themselves have a single table each.
- FS165 is structurally different: no Table Name, no Total Indicator, no category fillers; fields are DG110 count (Integer, pos 49 len 10), DG514 category (YES;NO;MISSING), Explanation. Data record ends at 274.
- Numbered DG prefix is printed in the name cell with a line break (`DG559` / `State Code`); FS119 prints `DG 559` and `DG 570` with a space (field_name kept as printed, technical tag normalised to DG559/DG570). FS127 prints `DG4 LEA identifier (State)` lowercase i; FS125/134/165 use `LEA Identifier (State)`; FS037/219/221/225 break the line before `(State)`.
- FS119 and FS127 Table Name lists two values (FS119 `DELPARTSTATE;NEGPARTSTATE`; FS127 `ATRISKLEA;DELPARTLEA`); the file covers two tables.
- FS037 and FS134 File Type likewise lists two values.
- Name variants: FS119 header `Total Records In File` (capital I) vs `in` elsewhere; FS145 CRLF field printed `(CRLF)or Line Feed` (missing space); header CRLF Type cell blank in all specs.
- Typo in definition: FS121 State Code "For a list of valid code State Codes".
- Header Filler lengths differ per spec (e.g. FS037 303, FS054 228, FS113 378, FS165 270); file width differs (FS037 430, FS054 355, FS113 505, FS119 385/400, FS165 397/274).

## Same-name fields that differ across the batch
- Total Indicator: position varies by layout (FS037 219, FS054 144, FS113 294, FS119 189, FS121 204, FS127 174, FS134 99, FS145 114, FS218-221 84, FS224/225 99). Permitted values: N only in FS054, FS113, FS125, FS145, FS218-221, FS224, FS225; N and Y (subtotal/total) in FS037, FS119, FS121, FS127, FS134.
- Explanation: always length 200 but start varies (FS165 74).
- Student Count: pos 495 FS113/125, 420 FS037, 405 FS121, 390 FS119, 375 FS127, 345 FS054, 315 FS145, 300 FS134/224/225, 285 FS218-221; length 10 in all.
- Racial Ethnic: pos 84 in FS037/119/127, pos 99 in FS121. Code order differs: FS037 `...HI7;PI7;WH7;MU7` vs FS119/121/127 `...HI7;PI7;MU7;WH7`.
- Age/Grade (w/o 13): pos 69 in FS054/FS121, 99 in FS145. Age/Grade (w/o 13 and BT2): pos 84 FS054, 114 FS121. FS134 uses a third variant `Age/Grade (w/o Out of School)` (no OOS code).
- Requiredness (Pop) for same-named fields: Progress Level is A in FS113 but M in FS125; MEP Services and Age/Grade (w/o 13) are M in FS145 but A in FS054/FS121; Academic Subject (Assessment - no science) is M in FS113/FS125 (filler-surrounded single category) but A in FS224/FS225; DG4/DG5 identifiers M everywhere.
- Delinquent Programs: pos 174 in FS119, pos 69 in FS127 (same code list). Disability Status (Only): pos 114 FS037, 129 FS119/127, 144 FS121.
- Academic / Career and Technical Outcomes: FS218/219 non-exit list vs FS220/221 `(Exit)` list, which adds ENROLLSCH first; same pos 69, len 15.
- FS113 vs FS125 (SEA vs LEA pair) are identical except Table Name, DG4 at pos 15 (FS125 only populated), File Type, and the Progress Level Pop value above.
- Table Name length 20 and pos 49 in every spec with that field.

## Permitted-values handling
Cells list codes inline as `CODE – Description`, so no lookup into the categories section was needed; summary keeps codes only, prefixed `category:<field name>=` for category fields. Verbatim notes kept for State Code ("For a list of valid State Codes...") and "SEA level – Blank". Reporting Period kept as `2026-2027 OR 2026 2027`.
