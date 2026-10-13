# b2-directory-org field extraction notes

Output: `b2-directory-org-fields.csv`, 590 rows, 22 spec-versions, all with >=1 header and >=1 data row, no duplicate keys,
all start_position/length integers, no gaps or overlaps in position sequences (start+length = next start in every layout).
Method: layout tables located from `federal-table-cells.csv` (thead = Data Element Name); permitted-value and definition cells re-read
from the DOCX XML so multi-paragraph cells keep separators (the CSV concatenates paragraphs without spaces). Scripts are in scratchpad `b2-directory-org/`.

## Row counts (header / data)
- FS029 v23.0: SEA 7/31, LEA 7/34, School 7/38 (separate d.1/d.2/d.3 tables, organization_level SEA/LEA/School)
- FS029 v23.1: all 7/31 (single table; SEA record relabelled for Lead Agency, see below)
- FS039 7/10; FS129 7/12; FS130 7/12; FS131 7/17; FS132 7/18; FS170 7/9; FS190 7/23; FS193 7/11; FS196 7/24
- FS197 7/11; FS198 7/10; FS199 7/19; FS200 7/19; FS201 7/19; FS202 7/20; FS205 7/14; FS206 7/12; FS207 7/8; FS212 7/12; FS223 7/8
- Every non-FS029 spec has exactly one header layout and one data layout table (organization_level = all). No multi-table layouts in this batch.
  Each layout is followed by a Format/Example table (skipped).

## Structural anomalies
- FS029 v23.0 is the only spec here with per-level layouts; header Filler length differs (SEA 753, LEA 678, School 684) and
  CRLF position differs (880 / 805 / 811). Data CRLF: SEA 1080, LEA 1005, School 1081. Data records are 31/34/38 fields.
- FS029 v23.1 is a Lead Agency (LA) variant: header File Type still `SEA DIRECTORY INFO`, but field names read
  `DG570 Lead Agency Number` (permitted value 02, vs 01 in v23.0), `DG7 Education Entity Name - LA`, etc.; address/telephone/web cross-references
  point to sections 2.3.4-2.3.6 (v23.0 SEA points to 2.4.1-2.4.4). Positions, lengths, Pop are identical to the v23.0 SEA table
  (31 fields, 1:1 by sequence). v23.1 header is 7 fields with Filler 127/333 and CRLF at 460 (not the SEA 753/880).
  File Record Number definition says "Lead Agency"; permitted note says "only 1 for the LA directory".
- FS132 data: Filler at 79 (len 6) and 85 (len 6) instead of the usual 15; the second has blank Pop (the only blank-Pop non-CRLF field in the batch).
- Pop codes beyond M/O: A (29), X (9), SDS (5, State Defined Status Indicator), S (2), C (1); recorded verbatim.
- DG-prefix spacing is inconsistent in the printed names (`DG559State Code`, `DG 798Charter authorizer name`, `DG4LEA Identifier (State)`,
  `DG806Address Mailing 1`, `DG16NOperational Status`); kept as printed. technical_name_or_xml_tag normalises to `DG798`, `DG16N`, `DG4P`, `DG5P`, `DG531N`, `DG833N`.
- FS029 v23.0 LEA/School name variants: `DG16 Operational Status - LEA SY Start` (30 chars) and `DG16N ... New (previously referred to as "Updated")`; same for DG531/DG531N.
- Permitted values: all category fields list their codes inline in the layout cell, so no resolution from the categories section was needed
  (no `category:` prefixes used). Where a cell has codes plus prose/MISSING note, the summary is codes `;`-joined then ` || NOTE: ...`.
  Header File Type values (e.g. `LEA GRADES OFFERED | SCHOOL GRADES OFFERED`) are kept verbatim, not coded.
- category_role is heuristic: directory attribute fields (address, phone, URL, status, type, dates) = other; reported value fields in status/data
  files = count; Table Name = other; Total Indicator = total; Indicator Type / race / disability / EL / ED / Identification Subgroups = category.

## Same-name fields that differ across the batch
- Position: School Identifier (State) is at 36/20 in FS039 (Filler precedes it) but 29/20 in most others; Table Name 29/20 (FS193) vs 49/20 (FS199-202/205/212).
- Total Indicator start varies (79 FS193, 114 FS205, 189 FS199) as category columns shift; State Defined Status Indicator is 200 long but starts 330/405/420.
- Address Mailing 1 starts 129 (FS190, DG806), 350 (FS196, DG828), 238 (FS029 SEA/LA), 249 (FS029 LEA), 235 (FS029 School); all length 60.
  Effective Date 751 (LEA) vs 737 (School); Prior State LEA ID 791 (LEA) vs 777 (School), both in FS029 v23.0.
- Out of State Indicator is length 3 at 128 (FS029 LEA) vs 122 (FS029 School).
- Definitions: State Agency Number says "See section 2.3.3" or "2..3.3" (typo) in FS029 only; others plain. Explanation: "Text for state use" vs "Text field for state use" (one spec).
  State Defined Status Indicator definition differs per spec only in the named status field. LEA Identifier (State) in FS029/FS197 carries "See section 2.3.4".
- FS039 School Identifier permitted value `LEA level - Blank` (LEA-level rows have blank school ID, one table serves both levels).
- State Code permitted text: FS029 refers to "Appendix A", FS039-FS223 to "EDFacts Workbook".
