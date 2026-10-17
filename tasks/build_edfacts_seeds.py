#!/usr/bin/env python3
"""Derive edu_ext_edfacts spec seeds from one year's Pandoc table cells.

Reads tasks/reports/<year>/federal-table-cells.csv and writes four seeds into
edu_ext_edfacts/seeds/: edfacts_files, edfacts_layouts, edfacts_category_sets,
edfacts_permitted_values. Specs are added to SPECS one wave at a time; every parse
asserts the spec's shape so a layout the parser does not understand fails loudly.

    python3 tasks/build_edfacts_seeds.py [--year 2026-27]
"""
import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEEDS = ROOT / "edu_ext_edfacts/seeds"
# ponytail: explicit allowlist; widen per Phase 4 wave once each spec's shape is checked.
SPECS = ["FS052"]
LEVELS = ("SEA", "LEA", "School")  # file types start SEA/LEA/SCHOOL, file names carry SEA/LEA/SCH


def norm(value):
    return re.sub(r"\s+", " ", value or "").strip()


def column_name(element):
    return re.sub(r"[^a-z0-9]+", "_", element.lower()).strip("_")


def tables_for(cells, fs):
    """{table_index: (section, header {col: text}, [body rows {col: text}])} for one spec."""
    raw = defaultdict(lambda: defaultdict(dict))
    sections = {}
    for cell in cells:
        if cell["file_spec_id"] != fs:
            continue
        t = int(cell["table_index"])
        raw[t][(cell["row_part"] != "thead", int(cell["row_index"]))][int(cell["cell_index"])] = norm(cell["value"])
        sections[t] = cell["section"]
    out = {}
    for t, rows in raw.items():
        header = next((r for (is_body, _), r in sorted(rows.items()) if not is_body), {})
        body = [r for (is_body, _), r in sorted(rows.items()) if is_body]
        out[t] = (sections[t], header, body)
    return out


def find(tables, predicate):
    return [(t, *tables[t]) for t in sorted(tables) if predicate(*tables[t])]


def parse_layout(rows, record_type):
    header_cols = None
    out = []
    for seq, row in enumerate(rows, 1):
        name = row.get(1, "")
        dg = ""
        m = re.match(r"(DG\d+)\s+(.*)", name)
        if m:
            dg, name = m.groups()
        if name.startswith("Carriage Return"):
            name = "CRLF"
        out.append({"record_type": record_type, "seq": seq, "element": name, "data_group": dg,
                    "column_name": column_name(name), "start_position": int(row[2]),
                    "length": int(row[3]), "data_type": row.get(4, ""), "pop": row.get(5, ""),
                    "permitted": row.get(7, "")})
    for prev, cur in zip(out, out[1:]):
        assert prev["start_position"] + prev["length"] == cur["start_position"], (record_type, prev, cur)
    assert out[-1]["element"] == "CRLF", out[-1]
    return out


def build_spec(cells, fs):
    tables = tables_for(cells, fs)
    version = next(c["file_spec_version"] for c in cells if c["file_spec_id"] == fs)

    (_, _, core_header, core_body), = find(tables, lambda s, h, b: s.startswith("core-requirements"))
    levels = [lvl for col, lvl in core_header.items() if lvl in LEVELS
              and any(r.get(col) for r in core_body)]
    assert levels, f"{fs}: no organization levels in core requirements"

    (_, _, h_header, h_body), = find(tables, lambda s, h, b: s.startswith("header-record") and h.get(1) == "Data Element Name")
    (_, _, d_header, d_body), = find(tables, lambda s, h, b: s.startswith("data-record") and h.get(1) == "Data Element Name")
    header = parse_layout(h_body, "header")
    data = parse_layout(d_body, "data")

    (_, _, m_header, m_body), = find(tables, lambda s, h, b: h.get(1) == "Aggregation" and "Total Indicator" in h.values())
    ti_col = next(c for c, v in m_header.items() if v == "Total Indicator")
    categories = [m_header[c] for c in sorted(m_header) if 1 < c < ti_col]
    data_by_name = {r["element"].lower(): r for r in data}
    for category in categories:
        assert category.lower() in data_by_name, f"{fs}: matrix category {category!r} not in data layout"

    sets = []
    for order, row in enumerate(m_body, 1):
        members = [m_header[c] for c in sorted(m_header) if 1 < c < ti_col and row.get(c) == "X"]
        for category in members or [""]:
            sets.append({"category_set": row[1], "set_order": order, "total_indicator": row[ti_col],
                         "category": category, "column_name": column_name(category) if category else ""})

    value_tables = find(tables, lambda s, h, b: h.get(1) == "Permitted Value Abbreviation")
    assert len(value_tables) == len(categories), f"{fs}: {len(value_tables)} value tables for {categories}"
    values = []
    for category, (_, _, _, body) in zip(categories, value_tables):
        permitted = data_by_name[category.lower()]["permitted"].replace(" ", "")
        for order, row in enumerate(body, 1):
            assert row[1].replace(" ", "") in permitted, f"{fs}: {row[1]} not listed for {category}"
            values.append({"category": category, "column_name": column_name(category),
                           "code": row[1], "label": row[2], "sort_order": order})

    (_, _, _, naming), = find(tables, lambda s, h, b: h.get(1) == "Where")
    token = next(r[2] for r in naming if r.get(1) == "filename")
    file_types = re.findall(r"(?:SEA|LEA|SCHOOL) .*?TABLE", next(r["permitted"] for r in header if r["element"] == "File Type"))
    table_name = next(r["permitted"] for r in data if r["element"] == "Table Name")
    period = next(r["permitted"] for r in header if r["element"] == "File Reporting Period").split("OR")[0]
    count_column = next(r for r in reversed(data) if r["data_type"] == "Integer")["column_name"]
    assert re.fullmatch(r"[A-Z0-9]+", table_name) and re.fullmatch(r"\d{4}-\d{4}", period), (table_name, period)

    files, layouts = [], []
    for level in levels:
        file_type, = [t for t in file_types if t.startswith(level.upper() + " ")]
        files.append({"file_spec_id": fs, "file_spec_version": version, "org_level": level,
                      "file_type": file_type, "table_name": table_name, "file_name_token": token,
                      "level_abbr": level.upper()[:3], "reporting_period": period,
                      "header_length": header[-1]["start_position"] - 1,
                      "data_length": data[-1]["start_position"] - 1, "count_column": count_column})
        for row in header + data:
            layouts.append({"file_spec_id": fs, "file_spec_version": version, "org_level": level,
                            **{k: v for k, v in row.items() if k != "permitted"}})
    stamp = {"file_spec_id": fs, "file_spec_version": version}
    category_sets = [{**stamp, "org_level": level, **s} for level in levels for s in sets]
    return files, layouts, category_sets, [{**stamp, **v} for v in values]


def write(name, rows):
    path = SEEDS / f"{name}.csv"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", default="2026-27")
    args = parser.parse_args()
    with (ROOT / f"tasks/reports/{args.year}/federal-table-cells.csv").open(encoding="utf-8", newline="") as handle:
        cells = list(csv.DictReader(handle))
    out = defaultdict(list)
    for fs in SPECS:
        for name, rows in zip(("edfacts_files", "edfacts_layouts", "edfacts_category_sets",
                               "edfacts_permitted_values"), build_spec(cells, fs)):
            out[name] += rows
    SEEDS.mkdir(parents=True, exist_ok=True)
    print(" ".join(f"{name}={write(name, rows)}" for name, rows in out.items()))


if __name__ == "__main__":
    main()
