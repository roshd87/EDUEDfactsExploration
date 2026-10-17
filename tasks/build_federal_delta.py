"""Diff two reporting years' Pandoc extractions (table cells + text blocks) spec by spec.

Usage: python3 tasks/build_federal_delta.py 2025-26 2026-27
Reads tasks/reports/<year>/federal-table-cells.csv and federal-document-blocks.csv (from
extract_federal_table_cells.py --year <year>) and writes
tasks/reports/<new>/federal-delta-<old>-to-<new>.csv: one row per (FS, section) with the number of
normalized cell/block values added and removed, plus up to three examples each. Year strings,
version numbers and whitespace are normalized away so only substantive text differences count.
"""
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_SECTIONS = re.compile(r"document.?control|contents|changes.from|preface|document start", re.I)


def norm(v, old, new):
    v = v.replace(old, "YEAR").replace(new, "YEAR")
    for y in (old, new):
        a, b = y.split("-")
        v = v.replace(f"20{b}", "YR").replace(a, "YR")
    v = re.sub(r"\bv?\d{1,2}\.\d\b", "VER", v)          # 22.0 / v23.1
    v = re.sub(r"[–—‐-]", "-", v)
    v = re.sub(r"\s+", " ", v).strip().lower()
    return v


def load(year, old, new):
    """[table cells, text blocks]: {(fs, section): {normalized values}} for one year's extraction."""
    out = []
    for name in ("federal-table-cells.csv", "federal-document-blocks.csv"):
        values = defaultdict(set)
        with (ROOT / "tasks/reports" / year / name).open(encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                if not SKIP_SECTIONS.search(r["section"]) and r["value"].strip():
                    values[(r["file_spec_id"], r["section"])].add(norm(r["value"], old, new))
        out.append(values)
    return out


def main(old, new):
    oc, ob = load(old, old, new)
    nc, nb = load(new, old, new)
    out = []
    for kind, o, n in (("table", oc, nc), ("text", ob, nb)):
        for key in sorted(set(o) | set(n)):
            added = sorted(n.get(key, set()) - o.get(key, set()))
            removed = sorted(o.get(key, set()) - n.get(key, set()))
            if not added and not removed:
                continue
            out.append({
                "file_spec_id": key[0], "section": key[1], "kind": kind,
                "added": len(added), "removed": len(removed),
                "added_examples": " || ".join(a[:160] for a in added[:3]),
                "removed_examples": " || ".join(r[:160] for r in removed[:3]),
            })
    dest = ROOT / "tasks/reports" / new / f"federal-delta-{old}-to-{new}.csv"
    with dest.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    specs = sorted({r["file_spec_id"] for r in out})
    print(f"delta_rows={len(out)} specs_with_changes={len(specs)} -> {dest.relative_to(ROOT)}")
    print(" ".join(specs))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
