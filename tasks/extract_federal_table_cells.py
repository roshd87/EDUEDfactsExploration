#!/usr/bin/env python3
"""Losslessly export cached EDFacts DOCX table cells using Pandoc's JSON AST.

Every spec in the year's CATALOG-INVENTORY.tsv -> tasks/reports/<year>/federal-{table-cells,document-blocks}.csv.

    python3 tasks/extract_federal_table_cells.py [--year 2026-27]
"""
import argparse
import csv
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARGS = argparse.ArgumentParser(description=__doc__)
ARGS.add_argument("--year", default="2026-27")
OPTS = ARGS.parse_args()
SPECS_DIR = ROOT / f"wiki/reference/edfacts/{OPTS.year}/file-specifications"
CATALOG = SPECS_DIR / "CATALOG-INVENTORY.tsv"
OUT_DIR = ROOT / "tasks/reports" / OPTS.year
TABLE_OUT = OUT_DIR / "federal-table-cells.csv"
BLOCK_OUT = OUT_DIR / "federal-document-blocks.csv"
TABLE_RE = re.compile(r"\bTable\s+2\.\d", re.I)


def flatten(node):
    if node is None:
        return ""
    if isinstance(node, str):
        return node
    if isinstance(node, list):
        return "".join(flatten(item) for item in node)
    if not isinstance(node, dict):
        return ""
    tag = node.get("t")
    content = node.get("c")
    if tag in {"Str", "Code", "Math", "RawInline", "RawBlock"}:
        return content[-1] if isinstance(content, list) else str(content or "")
    if tag in {"Space", "SoftBreak", "LineBreak"}:
        return " "
    if tag == "Quoted":
        return flatten(content[1])
    return flatten(content)


def clean(value):
    return re.sub(r"\s+", " ", value).strip()


def rows(part, label):
    """Yield (section, row-index, cells) from Pandoc TableHead/Body/Foot."""
    if not part:
        return
    if label in ("thead", "tfoot"):
        for index, row in enumerate(part[1], 1):
            yield label, index, row[1]
    else:
        for body_index, body in enumerate(part, 1):
            for index, row in enumerate(body[3], 1):
                yield f"tbody{body_index}", index, row[1]


def catalog_paths():
    result = {}
    with CATALOG.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            result[(row["file_spec_id"], row["version"])] = SPECS_DIR / row["filename"]
    return result


def main():
    paths = catalog_paths()
    specs = sorted(paths)

    cells, blocks = [], []
    for fs_id, version in specs:
        docx = paths[(fs_id, version)]
        data = json.loads(subprocess.run(
            ["/usr/bin/pandoc", str(docx), "-t", "json"],
            check=True, text=True, capture_output=True,
        ).stdout)
        section, preceding_table_text, preceding_text, table_index = "document start", "", "", 0
        for block_index, block in enumerate(data["blocks"], 1):
            tag, content = block.get("t"), block.get("c")
            text = clean(flatten(content))
            if tag == "Header":
                section = text or section
            if tag in {"Para", "Plain", "BlockQuote"}:
                blocks.append({
                    "file_spec_id": fs_id, "file_spec_version": version, "document_path": str(docx.relative_to(ROOT)),
                    "section": section, "block_index": block_index, "value": text,
                })
                if TABLE_RE.search(text):
                    preceding_table_text = text
                if text:
                    preceding_text = text
            if tag != "Table":
                continue
            table_index += 1
            _, caption, _, thead, tbodies, tfoot = content
            caption_text = clean(flatten(caption)) or preceding_table_text
            for part, label in ((thead, "thead"), (tbodies, "tbody"), (tfoot, "tfoot")):
                for row_part, row_index, row_cells in rows(part, label) or ():
                    for cell_index, cell in enumerate(row_cells, 1):
                        _, alignment, rowspan, colspan, cell_blocks = cell
                        cells.append({
                            "file_spec_id": fs_id, "file_spec_version": version,
                            "document_path": str(docx.relative_to(ROOT)), "section": section,
                            "table_index": table_index, "table_caption_or_preceding_text": caption_text,
                            "nearest_preceding_text": preceding_text,
                            "row_part": row_part, "row_index": row_index, "cell_index": cell_index,
                            "alignment": alignment.get("t", alignment) if isinstance(alignment, dict) else alignment,
                            "rowspan": rowspan, "colspan": colspan, "value": clean(flatten(cell_blocks)),
                        })

    TABLE_OUT.parent.mkdir(parents=True, exist_ok=True)
    table_fields = ["file_spec_id", "file_spec_version", "document_path", "section", "table_index",
                    "table_caption_or_preceding_text", "nearest_preceding_text", "row_part", "row_index", "cell_index", "alignment",
                    "rowspan", "colspan", "value"]
    block_fields = ["file_spec_id", "file_spec_version", "document_path", "section", "block_index", "value"]
    for path, fields, data in ((TABLE_OUT, table_fields, cells), (BLOCK_OUT, block_fields, blocks)):
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader(); writer.writerows(data)

    fs002_cells = " ".join(row["value"] for row in cells if row["file_spec_id"] == "FS002")
    fs002_blocks = " ".join(row["value"] for row in blocks if row["file_spec_id"] == "FS002")
    for token, haystack in (("unduplicated number of children with disabilities", fs002_blocks.lower()),
                          ("sea", fs002_cells.lower()), ("lea", fs002_cells.lower()),
                          ("school", fs002_cells.lower()), ("category set a", fs002_cells.lower()),
                          ("aut", fs002_cells.lower())):
        if token not in haystack:
            raise AssertionError(f"FS002 extraction missing {token!r}")
    print(f"documents={len(specs)} table_cells={len(cells)} document_blocks={len(blocks)}")


if __name__ == "__main__":
    main()
