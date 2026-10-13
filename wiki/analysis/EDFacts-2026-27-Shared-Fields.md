---
tags: [analysis, edfacts, fields]
baseline: "EDFacts SY 2026-27 catalog frozen 2026-10-07"
---

# EDFacts SY 2026-27 Shared Fields

> [!info] Seam: standard-agnostic
> Federal record layouts only. Nothing here depends on Generate, CEDS or Ed-Fi; it tells the spec-seed layer
> (`EDFactsOutputPlan.md` §3, "Spec seeds") which fields are defined once and which per file.

Every layout-table field in the 94 SY 2026-27 spec-versions (93 FS ids; FS029 v23.0 and v23.1) is extracted to
`tasks/reports/field-review/*-fields.csv` (2,245 rows: 672 header, 1,573 data) and compared by normalized name in
`wiki/analysis/edfacts-2026-27-shared-fields.csv`. Method and validation: `tasks/reports/field-review/README.md`.
Builds on [[EDFacts-2026-27-Delta]].

## Headline

| Measure | Count |
|---|---:|
| Distinct normalized fields | 216 |
| Single-spec fields | 128 |
| Shared fields (≥2 specs) | 88 |
| — universal (≥4 of 5 families, ≥20 specs) | 22 |
| — family-wide (≥4 specs) | 16 |
| — collection-specific (2–3 specs) | 50 |
| Definition byte-identical / equivalent / differs | 45 / 34 / 9 |
| Permitted values identical / equivalent / differs / none | 48 / 9 / 9 / 22 |
| Length consistent everywhere | 84 of 88 |
| Start position consistent everywhere | 37 of 88 (plus 2 Filler n/a) |
| Content-identical (definition, values, length) | 41 |
| Fully identical incl. position | 19 |

Content is highly reusable; position is not. 67 of 88 shared fields agree in definition, values and length,
but only 37 keep a fixed start position. A shared seed defines name, length, type and value set once, and each
`FS###` layout seed supplies its own start position.

## The fixed skeleton

**Header record: identical structure in all 96 header layouts.** File Type 1/50, Total Records in File 51/10,
File Name 61/25, File Identifier 86/32, File Reporting Period 118/9, Filler 127/(L−127), CRLF L/1. Only the
record length L varies (26 layouts at 460, 14 at 505, 10 at 430, range 270–880). L equals the data record length
in only 37 of 94 spec-versions, so the header Filler is per-spec. It is not padding to the data length.

**Data record prefix: positions 1–68 are fixed in 73 of 96 data layouts.** File Record Number 1/10,
State Code 11/2, State Agency Number (or Lead Agency Number) 13/2, LEA Identifier (State) 15/14 or Filler,
School Identifier (State) 29/20 or Filler, Table Name 49/20. Categories follow in 15-byte slots (312 of 320
category fields are length 15), usually from 69. Then come Total Indicator (1), Explanation (200), the count (10) and CRLF.

## Universal fields

| Field | Specs | Start | Len | Position fixed | Definition | Values |
|---|---:|---:|---:|---|---|---|
| File Type (H) | 93 | 1 | 50 | yes | equivalent | per-file literals |
| Total Records in File (H) | 93 | 51 | 10 | yes | equivalent | — (FS029 SEA: "1") |
| File Name (H) | 93 | 61 | 25 | yes | equivalent | see §3.0 |
| File Identifier (H) | 93 | 86 | 32 | yes | equivalent | — |
| File Reporting Period (H) | 93 | 118 | 9 | yes | equivalent | `2026-2027` / `2026 2027` |
| Filler (H) | 93 | 127 | varies | yes | equivalent | — |
| CRLF (H and D) | 93 | varies | 1 | no | identical | — |
| File Record Number | 93 | 1 | 10 | yes | equivalent | — |
| State Code | 93 | 11 | 2 | yes | equivalent | EDFacts Workbook list |
| State Agency Number | 85 | 13 | 2 | yes | equivalent | `01` |
| LEA Identifier (State) | 68 | 15 | 14 | yes | equivalent | blank at SEA level |
| School Identifier (State) | 41 | 29 | 20 | no (36 in FS029 School, FS039, FS197) | equivalent | blank at SEA/LEA |
| Table Name | 77 | 49 | 20 | no (FS099 44, FS193 29) | equivalent | per-file literals |
| Filler (D) | 77 | varies | 7–125 | n/a | equivalent | — |
| Total Indicator | 76 | varies | 1 | no | equivalent | **differs**: `N;Y` / `N` / `Y` |
| Explanation | 92 | varies | 200 | no | equivalent | — (absent only in FS190) |
| Student Count | 50 | varies | 10 | no | identical (empty) | — (FS151 length 8) |
| Racial Ethnic | 24 | varies | 15 | no | identical | AM7 AS7 BL7 HI7 PI7 WH7 MU7 MISSING |
| Sex (Membership) | 24 | varies | 15 | no | identical | F M MISSING |
| Disability Status (Only) | 23 | varies | 15 | no | identical | identical |
| English Learner Status (Only) | 21 | varies | 15 | no | identical | identical |

"Equivalent" definitions differ only editorially: dash glyphs, "State" against "SEA", a dropped period, a
section cross-reference, or FS045's "Federal Information Processing Standards" for ANSI (the same 2-digit codes).

## Family-wide fields

| Family | Fields (specs) |
|---|---|
| Student counts, assessment & EL | Economically Disadvantaged Status (16), Homeless Enrolled Status (11), Migratory Status (10), Major Racial and Ethnic Groups (9), Foster Care Status (8) |
| Assessment & EL | English Learner Status (Both) (9, plus IDEA), Military Connected Student Status (6), Proficiency Status (6), Assessment Administered (ELP) (4), Grade Level (Lower) or Grade Level (HS) (4) |
| IDEA Part B/C | Disability Category (IDEA) (7), Infants and Toddlers Count (4), Lead Agency Number (9, with FS029 v23.1) |
| Accountability (FS199–205) | State Defined Status Indicator (5), Major Racial and Ethnic Groups (Accountability) (4) |
| Program participation | Academic Subject (Assessment – No Science) (4) |

All of these have identical permitted values across their specs. Every one except Lead Agency Number, Grade Level and Major Racial
and Ethnic Groups (Accountability) moves position from file to file.

Collection-specific pairs mirror each other field for field: Part B and Part C dispute resolution (FS227/FS906,
FS228/FS907, FS229/FS908), the N or D pairs (FS218/219, FS220/221, FS119/127, FS113/125), and the FS029/FS190/FS196
address blocks. The address blocks have the same lengths but different start positions and Pop codes.

## Looks shared but differs

These would break a single shared seed:

1. **Total Indicator value set.** `N;Y` in 52 specs, `N` only in 20 (FS050 054 059 067 086 113 125 126 137 138
   139 144 145 194 218–221 224 225), `Y` only in FS193, FS205, FS222, FS226. Seventeen specs have no Total Indicator
   at all (directory, status and roster files). The accepted-values test is per spec.
2. **Header record length is not the data record length.** The two differ in 57 of 94 spec-versions, so header
   Filler length is a per-spec seed value, not `data_length − 127`.
3. **State Agency Number vs Lead Agency Number.** Both are DG570 at 13/2. The value is `01` in SEA files and `02` in
   FS029 v23.1 (LA Directory) and FS901–908. FS906–908 still define it as "state agencies".
4. **FS908 swaps two definitions relative to FS229.** Due Process Complaint Result and Resolution Meeting Outcome
   keep their codes (`RSLTNMTG`, `WRTNSTLAGRMNT`) and positions, but FS908 prints each field with the other's
   definition. Treat the codes as authoritative.
5. **Length drift on same-named fields.** Military Connected Student Status is 125 in FS175/178/179 and 15 in
   FS185/188/189. Student Count is 8 in FS151 and 10 elsewhere. Data Filler runs 7–125.
6. **Same identifier, shifted start.** School Identifier (State) starts at 36 where LEA Identifier (NCES) occupies 29–35 (FS029
   School, FS039, FS197). Table Name starts at 44 in FS099 and 29 in FS193. Staff/Teacher FTE start at 330, 345 (FS099) or 145 (FS203).
7. **Delinquent Programs.** FS119 permits `MISSING`; FS127 does not.
8. **Disability Category (IDEA).** FS006 and FS089 add IFSP to the definition; values are identical.

## Citations

- `tasks/reports/2026-27/federal-table-cells.csv` — sections `header-record-definition*`, `data-record-definition*`,
  `d.{1,2,3}.{2,3}-*` (FS029 v23.0); row-level locators in each shard's `source_locator`.
- `tasks/reports/field-review/b{1..5}-*-fields.csv` and `*-notes.md` — per-spec extraction and worker anomaly notes.
- Total Indicator: e.g. FS050 `data-record-definition#t13r11`, FS222 `data-record-definition#t8r7`.
- FS908 swap: FS229 and FS908 `data-record-definition#t14r10`–`r11`.
- Military Connected: FS175 `data-record-definition#t26r19` vs FS185 `#t25r16`.
- `wiki/analysis/edfacts-2026-27-shared-fields.csv` — one row per shared field with `variants` detail.
