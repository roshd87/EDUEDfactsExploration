#!/usr/bin/env python3
"""Losslessly export cached EDFacts DOCX table cells using Pandoc's JSON AST."""
import argparse
import csv
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Defaults reproduce the frozen SY2025-26 run (driver = the hand-curated bindings list).
# `--year 2026-27 --all --out-dir tasks/reports/2026-27` extracts every catalog spec of another year.
ARGS = argparse.ArgumentParser(description=__doc__)
ARGS.add_argument("--year", default="2025-26")
ARGS.add_argument("--all", action="store_true", help="drive from the catalog inventory, not the bindings list")
ARGS.add_argument("--out-dir", default="tasks/reports")
OPTS = ARGS.parse_args()
INPUT = ROOT / "tasks/reports/canonical-shards/federal-grain/federal-grain-bindings.csv"  # ponytail: P0 bindings file was deleted in the 2026-10-12 split; only --all mode works
SPECS_DIR = ROOT / f"wiki/reference/edfacts/{OPTS.year}/file-specifications"
CATALOG = SPECS_DIR / "CATALOG-INVENTORY.tsv"
TABLE_OUT = ROOT / OPTS.out_dir / "federal-table-cells.csv"
BLOCK_OUT = ROOT / OPTS.out_dir / "federal-document-blocks.csv"
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


def source_specs():
    if OPTS.all:
        return sorted(catalog_paths())
    with INPUT.open(encoding="utf-8", newline="") as handle:
        return [(row["file_spec_id"], row["file_spec_version"]) for row in csv.DictReader(handle)]


def main():
    paths = catalog_paths()
    specs = source_specs()
    duplicates = [pair for pair, count in
                  ((pair, specs.count(pair)) for pair in set(specs)) if count > 1]
    if duplicates:
        raise AssertionError(f"duplicate (spec, version) pairs in driver list: {sorted(duplicates)}")
    unresolved = [pair for pair in specs if pair not in paths]
    if unresolved:
        raise AssertionError(f"driver list pairs with no cached DOCX in CATALOG-INVENTORY.tsv: {sorted(unresolved)}")

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
