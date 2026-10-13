# EDFacts SY 2026-27 cross-file field review

Evidence for [[EDFacts-2026-27-Shared-Fields]] (`wiki/analysis/EDFacts-2026-27-Shared-Fields.md`) and
`wiki/analysis/edfacts-2026-27-shared-fields.csv`. Inputs: `tasks/reports/2026-27/federal-table-cells.csv`,
`federal-document-blocks.csv`, and the DOCX under `wiki/reference/edfacts/2026-27/file-specifications/`
(read-only). Built 2026-10-07.

## Batches

Five Sonnet workers, run at most three at a time, each writing only `<batch>-fields.csv` and `<batch>-notes.md`.

| Batch | Family | Spec-versions | Rows |
|---|---|---:|---:|
| `b1-idea` | IDEA Part B, Part C, dispute resolution: FS002 005 006 007 009 088 089 143 144 227 228 229 230 901–908 | 21 | 500 |
| `b2-directory-org` | Directory, org & accountability: FS029 (v23.0 + v23.1) 039 129 130 131 132 170 190 193 196 197 198 199 200 201 202 205 206 207 212 223 | 22 | 590 |
| `b3-student-staff` | Student counts & staff: FS032 033 040 052 086 118 150 151 160 163 194 195 222 226 059 067 070 099 203 | 19 | 419 |
| `b4-assessment-el` | Assessment & EL: FS045 050 116 126 137 138 139 141 175 178 179 185 188 189 210 211 | 16 | 389 |
| `b5-program` | Program participation (Title I, N or D, migrant): FS037 054 113 119 121 125 127 134 145 165 218 219 220 221 224 225 | 16 | 347 |

Total: 94 spec-versions (93 FS ids), 2,245 layout rows (672 header + 1,573 data).

## Worker shard schema

One row per printed layout-table field:
`file_spec_id, file_spec_version, record_kind (header|data), organization_level (SEA|LEA|School|all), sequence,
field_name (as printed), technical_name_or_xml_tag (DG number when printed), start_position, length,
data_type_or_format, requiredness (Pop cell verbatim), definition_text (verbatim, whitespace collapsed),
permitted_values_summary (codes joined by ';', optional `category:<name>=` prefix), category_role
(identifier|filler|category|total|count|explanation|control|other), source_locator (<section>#t<table>r<row>)`.

`organization_level` is `all` except FS029 v23.0 (separate SEA/LEA/School layouts) and FS059 (`SEA/LEA` and
`School` layouts, printed as two tables; kept as `SEA/LEA` rather than split).

## Validation performed (`validate_shards.py`)

- Coverage: all 94 catalog spec-versions present, both FS029 versions; every spec-version has header rows
  (7 each, 96 header layouts) and ≥8 data rows. No re-dispatch was needed.
- Keys: no duplicate `(spec, version, record_kind, organization_level, sequence)`.
- Row counts per spec-version equal the source layout-table tbody row counts in `federal-table-cells.csv` (94/94).
- Every row's `start_position` and `length` equal the source cells at its `source_locator` (2,245/2,245).
- Code completeness: every `CODE – description` token in the source permitted-values cell is checked against the
  summary. Manager fixes applied after this check (the shards were edited in place):
  - `b3`: File Reporting Period summary truncated to `2026` in 19 rows → `2026-2027;OR;2026 2027`.
  - `b2`: FS029 Out of State Indicator (LEA, School) `YES` → `YES;NO`; FS029 School Charter Status `YES` →
    `YES;NO;NA`; FS200 Indicator Type (AAM) was missing `AAM04`.
  - Remaining flags were regex artifacts of glued DOCX text (e.g. `3TO5NOTK`), confirmed against source.

## Consolidation (`consolidate_shared_fields.py`)

Field names are normalized (DG prefix including `N`/`P` suffix letters stripped, dash/space/case folded,
printed typos `(Sate)`, `Identifier(State)`, missing `)`, `Racial /Ethnic`, `Teachers FTE` folded, CRLF
variants unified, FS029 ` - SEA/LEA/School/LA` suffixes removed). Filler and CRLF are split by record kind.
Definitions: `identical` = byte-identical after whitespace collapse; `equivalent` = one contains the other or
≥0.85 similarity after case/punctuation folding; `differs` otherwise. Hand-reviewed overrides (marked `manual:`
in `variants`) cover State Code, LEA/School Identifier (State), Filler, Table Name, Total Indicator, Teacher/Staff
FTE. Permitted values are compared as code sets, with reference notes (`SEA level – Blank`, `For a list of valid
State Codes…`) dropped. The rebuild is deterministic (identical MD5 over two runs).
