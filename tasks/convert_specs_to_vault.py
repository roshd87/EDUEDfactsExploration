#!/usr/bin/env python3
"""Convert the EDFacts file-specification DOCX files into Obsidian notes.

Filter: every spec that was Active or Optional in the SY 2025-26 EDPass catalog, taken from the
SY 2026-27 frozen catalog (``wiki/reference/edfacts/2026-27/``). Output: one note per spec under
``wiki/edfacts/<FSnnn>/`` plus an index note.

    python3 tasks/convert_specs_to_vault.py            # writes wiki/edfacts/
    python3 tasks/convert_specs_to_vault.py --out DIR  # elsewhere (review)

Needs pandoc on PATH. Re-running is idempotent: the output is a pure function of the frozen
DOCX files, the two catalog inventories and the manifest.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / "wiki" / "reference" / "edfacts"
FILTER_YEAR, TARGET_YEAR = "2025-26", "2026-27"
FROZEN = "2026-10-07"
GENERATE_DOMAINS = ROOT / "wiki" / "generate" / "domains"
DELTA_NOTE = "analysis/EDFacts-2026-27-Delta"
SHARED_NOTE = "analysis/EDFacts-2026-27-Shared-Fields"

# ponytail: section order is the same in all 20 specs, so heading matching is by text, not by number.
H1_TITLE_CASE_KEEP = {"LEA", "SEA", "LA", "IDEA", "FTE", "CCD", "EDPass", "SY", "N", "D", "FS", "DG", "ID", "NCES", "EIN", "ESEA"}


# ----------------------------------------------------------------------------- catalog


def read_inventory(year: str) -> list[dict]:
    path = REF / year / "file-specifications" / "CATALOG-INVENTORY.tsv"
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def spec_key(row: dict) -> tuple[str, bool]:
    return row["file_spec_id"], " LA " in f" {row['title']} " or "LA Directory" in row["title"]


def read_manifest(year: str) -> dict[str, dict]:
    path = REF / year / "MANIFEST.csv"
    with path.open(newline="", encoding="utf-8") as fh:
        return {r["local_path"]: r for r in csv.DictReader(fh)}


def generate_domain_map() -> dict[str, list[str]]:
    out: dict[str, list[str]] = defaultdict(list)
    for note in sorted(GENERATE_DOMAINS.glob("*.md")):
        text = note.read_text(encoding="utf-8")
        for fs in set(re.findall(r"\bFS\d{3}\b", text)):
            out[fs].append(note.stem)
    return out


def parse_title(title: str) -> tuple[str, list[str], str]:
    """'FS052 (DG39) – Membership v23.0' -> ('Membership', ['DG39'], 'v23.0')."""
    m = re.match(r"FS\d{3}\s*\((?P<dgs>[^)]*)\)\s*[–—-]\s*(?P<name>.*?)\s*(?P<ver>v\d+\.\d+)\s*$", title)
    if not m:
        raise ValueError(f"unparseable title: {title!r}")
    dgs = re.findall(r"DG\d+", m.group("dgs"))
    return m.group("name").strip(), dgs, m.group("ver")


# ----------------------------------------------------------------------------- html tables


class TableParser(HTMLParser):
    """Flatten one pandoc HTML <table> into rows of markdown cell strings."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rows: list[list[str]] = []
        self.row: list[str] | None = None
        self.cell: list[str] | None = None
        self.skip = 0  # inside <caption>
        self.href: str | None = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "caption":
            self.skip += 1
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self.cell = []
            self.colspan = int(a.get("colspan", 1) or 1)
        elif self.cell is not None:
            if tag == "br":
                self.cell.append("<br>")
            elif tag == "p":
                if self.cell and self.cell[-1] not in ("<br>", ""):
                    self.cell.append("<br>")
            elif tag in ("strong", "b"):
                self.cell.append("**")
            elif tag in ("em", "i"):
                self.cell.append("*")
            elif tag in ("u", "sub", "sup"):
                self.cell.append(f"<{tag}>")
            elif tag == "a":
                self.href = a.get("href")
                self.cell.append("[")
            elif tag == "li":
                if self.cell and self.cell[-1] not in ("<br>",):
                    self.cell.append("<br>")
                self.cell.append("• ")

    def handle_endtag(self, tag):
        if tag == "caption":
            self.skip -= 1
        elif tag == "tr" and self.row is not None:
            self.rows.append(self.row)
            self.row = None
        elif tag in ("td", "th") and self.cell is not None:
            text = clean_cell("".join(self.cell))
            self.row.append(text)
            self.row.extend([""] * (self.colspan - 1))
            self.cell = None
        elif self.cell is not None:
            if tag in ("strong", "b"):
                self.cell.append("**")
            elif tag in ("em", "i"):
                self.cell.append("*")
            elif tag in ("u", "sub", "sup"):
                self.cell.append(f"</{tag}>")
            elif tag == "a":
                self.cell.append(f"]({self.href})" if self.href else "]")
                self.href = None

    def handle_data(self, data):
        if self.skip or self.cell is None:
            return
        self.cell.append(data.replace("\n", " "))


def clean_cell(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s*<br>\s*", "<br>", text).strip()
    text = re.sub(r"(<br>)+$", "", text)
    text = re.sub(r"^(<br>)+", "", text)
    text = fix_bold(text)
    text = re.sub(r"\*\*(DG ?\d+\w*)\*\*(?:<br>|(?=\S))", r"**\1** ", text)  # '**DG559<br>**State Code'
    text = text.replace("|", "\\|")
    return edfacts_word(text)


def fix_bold(text: str) -> str:
    """Word bold runs straddle spaces and line breaks ('**F –** Female**<br>M –**'); markdown's can't.

    Re-emit each bold run as one `**..**` per <br>-separated piece, whitespace outside the markers.
    """
    parts = text.split("**")
    if len(parts) % 2 == 0:  # unbalanced: give up on bold in this cell
        return text.replace("**", "")
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 0:
            out.append(p)
            continue
        pieces = []
        for seg in p.split("<br>"):
            s = seg.strip()
            lead, trail = seg[: len(seg) - len(seg.lstrip())], seg[len(seg.rstrip()):]
            pieces.append(f"{lead}**{s}**{trail}" if s else seg)
        out.append("<br>".join(pieces))
    return "".join(out).replace("****", "")


def html_table_to_pipe(block: str) -> str:
    p = TableParser()
    p.feed(block)
    rows = [r for r in p.rows if any(c.strip() for c in r)]
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    header, body = rows[0], rows[1:]
    if not any(h.strip() for h in header):
        header = [""] * width
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * width]
    out += ["| " + " | ".join(r) + " |" for r in body]
    return "\n".join(out)


# ----------------------------------------------------------------------------- markdown cleanup

HTML_TABLE = re.compile(r"<table[^>]*>.*?</table>", re.S)
IMG = re.compile(r'<img src="([^"]+)"[^>]*/>')
ANCHOR_SPAN = re.compile(r'<span id="[^"]*" class="anchor"></span>')
BACK_COVER = re.compile(r"\n+The Department of Education'?s mission is to promote.*\Z", re.S)


def edfacts_word(text: str) -> str:
    return re.sub(r"ED\*Fact\*?s\*?", "EDFacts", text)


def title_case_heading(text: str) -> str:
    if text != text.upper():
        return text
    words = []
    for w in text.split():
        words.append(w if w in H1_TITLE_CASE_KEEP or re.match(r"^[A-Z]:$", w) else w.capitalize())
    s = " ".join(words)
    return re.sub(r"\b(Or|And|For|Of|The|To|In|This|From|During|At)\b", lambda m: m.group(1).lower(), s)


def pandoc_md(docx: Path, media_dir: Path) -> str:
    return subprocess.run(
        ["pandoc", str(docx), "-t", "gfm", "--wrap=none", f"--extract-media={media_dir}"],
        check=True, capture_output=True, text=True,
    ).stdout


def split_front_matter(md: str) -> tuple[str, str]:
    """Return (front, body) split at the first '# PURPOSE' heading."""
    m = re.search(r"^#\s+PURPOSE\s*$", md, re.M)
    if not m:
        raise ValueError("no PURPOSE heading")
    return md[: m.start()], md[m.start():]


def document_history(front: str) -> str:
    m = re.search(r"DOCUMENT HISTORY\s*\n\n((?:\|.*\n)+)", front)
    if not m:
        return ""
    table = m.group(1).rstrip("\n").splitlines()
    # pandoc emits a blank header row; promote the first body row to the header.
    if table and not table[0].replace("|", "").strip():
        table = table[2:]
        table.insert(1, "|" + "---|" * (table[0].count("|") - 1))
    return "\n".join(table)


def anchor_map(body: str) -> dict[str, str]:
    """pandoc auto-id -> heading text, for rewriting [text](#id) into [[#Heading]]."""
    out = {}
    for m in re.finditer(r"^#+\s+(.+?)\s*$", body, re.M):
        text = m.group(1).strip()
        ident = re.sub(r"[^\w\s-]", "", text.lower()).strip().replace(" ", "-")
        ident = re.sub(r"-+", "-", ident)
        out.setdefault(ident, text)
    return out


def is_caption_residue(line: str) -> bool:
    """pandoc puts a Word table's alt text after the table as a paragraph: 'TitleCol1, Col2, Col3'."""
    if not line or line.startswith(("#", "|", "**", "-", ">", "<", "!", "[", "*")):
        return False
    if line.endswith((".", ":", ";", ")")):
        return False
    return bool(re.search(r"[a-z][A-Z]", line)) or line.count(",") >= 2 and not re.search(r"\b(and|or)\b", line)


def clean_body(body: str, out_media: Path, boilerplate_media: set[str]) -> tuple[str, list[str]]:
    dropped: list[str] = []
    body = HTML_TABLE.sub(lambda m: html_table_to_pipe(m.group(0)), body)
    body = ANCHOR_SPAN.sub("", body)
    body = BACK_COVER.sub("\n", body)
    body = edfacts_word(body)

    def img(m):
        src = Path(m.group(1))
        if md5(src) in boilerplate_media:
            return ""
        out_media.mkdir(parents=True, exist_ok=True)
        dest = out_media / src.name
        shutil.copyfile(src, dest)
        return f"![[{dest.name}]]"

    body = IMG.sub(img, body)
    anchors = anchor_map(body)

    def link(m):
        text, ident = m.group(1), m.group(2)
        heading = anchors.get(ident)
        return f"[[#{heading}|{text}]]" if heading else text

    body = re.sub(r"\[([^\]]+)\]\(#([^)]+)\)", link, body)

    lines = []
    prev_table = False
    for raw in body.split("\n"):
        line = raw.rstrip()
        if re.match(r"^#+\s*$", line) or line.strip() == "**":  # empty heading = page break; stray bold
            continue
        m = re.match(r"^(#+)\s+(.*?)\s*$", line)
        if m:
            level, text = m.groups()
            text = text.strip("* ").strip()
            if len(level) == 1:
                text = title_case_heading(text)
            line = "#" * (len(level) + 1) + " " + text
        if prev_table and line.strip() and not line.startswith("|") and is_caption_residue(line.strip()):
            dropped.append(line.strip())
            prev_table = False
            continue
        if line.strip():
            prev_table = line.startswith("|")
        lines.append(line)
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text, dropped


def md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


# ----------------------------------------------------------------------------- at a glance


def first_table_after(body: str, heading_re: str) -> list[list[str]]:
    m = re.search(rf"^##+\s+{heading_re}.*?$", body, re.M)
    if not m:
        return []
    rest = body[m.end():]
    nxt = re.search(r"^##\s", rest, re.M)
    if nxt:
        rest = rest[: nxt.start()]
    t = re.search(r"((?:^\|.*\n)+)", rest, re.M)
    if not t:
        return []
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in t.group(1).splitlines()]
    return [r for r in rows if not all(set(c) <= {"-"} for c in r)]


def core_requirements(body: str) -> tuple[list[str], dict[str, dict[str, str]]]:
    """Levels with at least one filled cell, merged across every 'Requirements for Submitting' table
    (FS002 keeps its school level in a second table); rows keyed by lower-cased label."""
    heading = r"(Core )?Requirements for Submitting"
    levels: list[str] = []
    data: dict[str, dict[str, str]] = {}
    for m in re.finditer(rf"^##+\s+{heading}.*?$", body, re.M):
        rows = first_table_after(body[m.start():], heading)
        if not rows or len(rows[0]) < 2:
            continue
        body_rows = [r for r in rows[1:] if r[0].strip()]
        for i, lv in enumerate(h.strip("* ") for h in rows[0][1:]):
            cells = {r[0].strip("* ").lower(): (r[i + 1] if i + 1 < len(r) else "") for r in body_rows}
            if not any(v.strip() for v in cells.values()):
                continue  # the spec's table has the column, but the file has no such level
            if lv not in levels:
                levels.append(lv)
            for label, v in cells.items():
                data.setdefault(label, {})[lv] = v
    return levels, data


def record_layout(body: str, heading_re: str = r"(?:[\w.]+\s+)?(?:\w+\s+)?Data Record Definition") -> tuple[int, int]:
    rows = first_table_after(body, heading_re)
    n, end = 0, 0
    for r in rows[1:]:
        if len(r) < 3:
            continue
        try:
            start, length = int(r[1]), int(r[2])
        except ValueError:
            continue
        n += 1
        end = max(end, start + length - 1)
    return n, end


def section(body: str, heading_re: str) -> str:
    """Text of the first heading matching heading_re, up to the next heading of the same or higher level."""
    m = re.search(rf"^(#+)\s+{heading_re}.*?$", body, re.M)
    if not m:
        return ""
    level = len(m.group(1))
    rest = body[m.end():]
    nxt = re.search(rf"^#{{1,{level}}}\s", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def category_names(body: str) -> list[str]:
    rest = section(body, r"Categories and Permitted Values")
    names = []
    for mm in re.finditer(r"^(?:\*\*(.+?)\*\*|###\s+(.+?))\s*$", rest, re.M):
        name = (mm.group(1) or mm.group(2)).strip().rstrip(":")
        if name.startswith("DG") or name.lower().startswith("table") or name.lower().startswith("permitted value"):
            continue
        if name not in names:
            names.append(name)
    return names


def at_a_glance(body: str, meta: dict) -> str:
    levels, core = core_requirements(body)
    lines = [f"> [!abstract] {meta['fs_id']} at a glance"]
    lines.append(f"> **Data groups:** {', '.join(meta['data_groups']) or 'multiple'}")
    lines.append(f"> **EDPass status:** {meta['status_2025_26']} in SY 2025-26; {meta['status_2026_27']} in SY 2026-27 at the {FROZEN} freeze")
    if levels:
        lines.append(f"> **Levels:** {', '.join(levels)}")
        # ponytail: only the rows that change how a file is built; the full table sits two screens down.
        for label in ("Reporting Period", "Type of count", "Zero counts", "Zero count reporting"):
            # ponytail: en-dash and trailing-period drift between a spec's SEA/LEA and school tables is not a difference
            vals = [re.sub(r"(<br>)+", " ", core.get(label.lower(), {}).get(lv, "")).replace("–", "-").strip().rstrip(".") for lv in levels]
            uniq = [v for i, v in enumerate(vals) if v and v not in vals[:i]]
            if not uniq:
                continue
            if len(uniq) == 1:
                lines.append(f"> **{label}:** {uniq[0]}")
            else:
                lines.append(f"> **{label}:** " + "; ".join(f"{lv}: {v or '—'}" for lv, v in zip(levels, vals)))
    cats = category_names(body)
    if cats:
        lines.append(f"> **Categories:** {', '.join(cats)}")
    n, end = record_layout(body)
    if n:
        lines.append(f"> **Data record:** {n} fields, {end} characters fixed-width")
    links = [f"[[{d}]]" for d in meta["generate_domains"]]
    if links:
        lines.append(f"> **Generate domain:** {', '.join(links)}")
    if meta.get("rules_note"):
        lines.append(f"> **Business rules:** [[{meta['rules_note']}]] (BRSI SY 2025-26)")
    if meta.get("metadata_notes"):
        lines.append("> **Metadata guides:** " + ", ".join(f"[[{n}]]" for n in meta["metadata_notes"]))
    see = [f"[[{DELTA_NOTE}|SY 2026-27 delta]]", f"[[{SHARED_NOTE}|shared fields]]"]
    if meta.get("workbook_note"):
        see.append(f"[[{meta['workbook_note']}|workbook]]")
    see.append("[[EDFacts Specs|all specs]]")
    lines.append("> **See also:** " + ", ".join(see))
    return "\n".join(lines)


def companions(out: Path) -> dict:
    """What convert_companions_to_vault.py produced, if it has run: metadata guides per spec, workbook, rules notes."""
    guides = []
    for note in sorted((out / "Metadata").glob("*.md")) if (out / "Metadata").exists() else []:
        fm = {}
        for ln in note.read_text(encoding="utf-8").split("---")[1].splitlines():
            if ":" in ln:
                k, v = ln.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
        lst = lambda s: [x.strip() for x in s.strip("[]").split(",") if x.strip()]  # noqa: E731
        guides.append({"note": note.stem, "collection": fm.get("collection", note.stem), "version": fm.get("version", ""),
                       "school_year": fm.get("school_year", ""), "metadata_specs": lst(fm.get("metadata_specs", "")),
                       "related_specs": lst(fm.get("related_specs", ""))})
    workbook = sorted(p.stem for p in (out / "Workbook").glob("*.md")) if (out / "Workbook").exists() else []
    brsi = sorted(p.stem for p in (out / "BRSI").glob("BRSI SY *.md")) if (out / "BRSI").exists() else []  # not the review note
    review = (out / "BRSI" / "BRSI Rules Review for dbt Tests.md")
    return {"guides": guides, "workbook": workbook[0] if workbook else "", "brsi": brsi[0] if brsi else "",
            "review": review.stem if review.exists() else ""}


# ----------------------------------------------------------------------------- notes


def q(s) -> str:
    return '"' + str(s).replace('"', '\\"') + '"'


def frontmatter(meta: dict) -> str:
    lines = ["---"]
    lines.append(f"fs_id: {meta['fs_id']}")
    lines.append(f"title: {q(meta['title'])}")
    lines.append(f"version: {q(meta['version'])}")
    lines.append(f"school_year: {q('SY ' + TARGET_YEAR)}")
    lines.append("data_groups: [" + ", ".join(meta["data_groups"]) + "]")
    lines.append(f"status_2025_26: {meta['status_2025_26']}")
    lines.append(f"status_2026_27: {meta['status_2026_27']}")
    lines.append(f"generate_domains: [" + ", ".join(meta["generate_domains"]) + "]")
    lines.append(f"source_docx: {q(meta['source_docx'])}")
    lines.append(f"source_url: {q(meta['source_url'])}")
    lines.append(f"sha256: {meta['sha256']}")
    lines.append(f"frozen: {FROZEN}")
    lines.append("tags: [edfacts, spec, sy2026-27]")
    lines.append("---")
    return "\n".join(lines)


def build_note(meta: dict, body: str, history: str) -> str:
    parts = [frontmatter(meta), "", f"# {meta['fs_id']} — {meta['title']} ({meta['version']})", ""]
    parts.append(at_a_glance(body, meta))
    parts.append("")
    parts.append(
        f"> [!info] Source\n> Converted by `tasks/convert_specs_to_vault.py` from the frozen SY {TARGET_YEAR} DOCX "
        f"(`{meta['source_docx']}`). Cover, document control, preface and table of contents are dropped; "
        "the document history is at the end. The DOCX remains the authority."
    )
    parts.append("")
    parts.append(body.rstrip())
    if history:
        parts += ["", "## Document History", "", history]
    return "\n".join(parts) + "\n"


def index_note(specs: list[dict], comp: dict) -> str:
    lines = [
        "---",
        "tags: [edfacts, spec, moc]",
        f"source_year: {q(TARGET_YEAR)}",
        f"filter_year: {q(FILTER_YEAR)}",
        "---",
        "",
        f"# EDFacts File Specifications — SY {TARGET_YEAR}",
        "",
        f"The file specifications that were **Active or Optional in the SY {FILTER_YEAR} EDPass catalog**, "
        f"converted from the SY {TARGET_YEAR} frozen DOCX files (`wiki/reference/edfacts/{TARGET_YEAR}/`). "
        f"At the {FROZEN} freeze every SY {TARGET_YEAR} spec was still Inactive (\"no active files at this time\"), "
        f"so the SY {FILTER_YEAR} status is the working filter. Regenerate with "
        "`python3 tasks/convert_specs_to_vault.py`.",
        "",
        "Related: [[" + DELTA_NOTE + "|SY 2026-27 delta]] · [[" + SHARED_NOTE + "|shared fields]] · "
        "[[generate/Home|CEDS Generate wiki]] · [[Domains-Guide|Generate domains]]",
        "",
        "| Spec | Title | Data groups | SY 2025-26 | Generate domain | Business rules | Metadata guides |",
        "|---|---|---|---|---|---|---|",
    ]
    for s in specs:
        dom = ", ".join(f"[[{d}]]" for d in s["generate_domains"]) or "—"
        rules = f"[[{s['rules_note']}\\|rules]]" if s.get("rules_note") else "—"
        guides = ", ".join(f"[[{n}\\|{n.replace(' Metadata User Guide', '')}]]" for n in s.get("metadata_notes", [])) or "—"
        lines.append(
            f"| [[{s['note']}\\|{s['fs_id']}{' LA' if s['la'] else ''}]] | {s['title']} | "
            f"{', '.join(s['data_groups']) or 'multiple'} | {s['status_2025_26']} | {dom} | {rules} | {guides} |"
        )
    if comp["workbook"] or comp["brsi"] or comp["guides"]:
        lines += ["", "## Companion documents", "",
                  "Converted by `tasks/convert_companions_to_vault.py`. The BRSI and Workbook are the SY 2025-26 editions, "
                  "the newest published at the freeze; each metadata guide is the newest version the EDPass metadata page links.", ""]
        if comp["workbook"]:
            lines.append(f"- [[{comp['workbook']}]] — EDPass roles, directory upload order, program-area file lists, FAQs, standard definitions, glossary")
        if comp["brsi"]:
            lines.append(f"- [[{comp['brsi']}]] — Business Rules Single Inventory: scope, cross-file rules, version history; per-spec rules in the table above")
        if comp.get("review"):
            lines.append(f"- [[{comp['review']}]] — proposed dbt-test handling and decision per BRSI rule (`tasks/build_brsi_review.py`)")
        if comp["guides"]:
            lines += ["", "| Metadata collection | Version | Year | Metadata specs | Applies to |", "|---|---|---|---|---|"]
            by_id = {s["fs_id"]: s["note"] for s in specs if not s["la"]}
            for g in comp["guides"]:
                applies = ", ".join(f"[[{by_id[f]}\\|{f}]]" if f in by_id else f for f in g["related_specs"]) or "none of the converted specs"
                lines.append(f"| [[{g['note']}\\|{g['collection']}]] | {g['version']} | {g['school_year']} | {', '.join(g['metadata_specs'])} | {applies} |")
    return "\n".join(lines) + "\n"


# ----------------------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=ROOT / "wiki" / "edfacts")
    args = ap.parse_args()

    old = [r for r in read_inventory(FILTER_YEAR) if r["status"] in ("Active", "Optional")]
    new = {spec_key(r): r for r in read_inventory(TARGET_YEAR)}
    manifest = read_manifest(TARGET_YEAR)
    domains = generate_domain_map()

    work = []
    for r in old:
        key = spec_key(r)
        n = new.get(key)
        if not n:
            print(f"!! {key} not in {TARGET_YEAR} catalog", file=sys.stderr)
            continue
        work.append((r, n, key))

    with tempfile.TemporaryDirectory(prefix="specs-") as tmpdir:
        tmp = Path(tmpdir)
        converted = []
        for r, n, key in work:
            docx = REF / TARGET_YEAR / "file-specifications" / n["filename"]
            media = tmp / f"media-{key[0]}{'-LA' if key[1] else ''}"
            converted.append((r, n, key, pandoc_md(docx, media), media))

        # Images that appear in most specs are letterhead; drop them.
        counts: Counter[str] = Counter()
        for *_, media in converted:
            counts.update({md5(p) for p in media.rglob("*") if p.is_file()})
        boilerplate = {h for h, c in counts.items() if c >= max(3, len(converted) // 2)}

        specs = []
        all_dropped = []
        comp = companions(args.out)
        for r, n, key, md, media in converted:
            name, dgs, ver = parse_title(n["title"])
            fs_id, la = key
            folder = args.out / fs_id
            folder.mkdir(parents=True, exist_ok=True)
            note_name = f"{fs_id} {name}"
            rel_docx = f"wiki/reference/edfacts/{TARGET_YEAR}/file-specifications/{n['filename']}"
            rules_note = f"{fs_id} Business Rules"
            meta = {
                "fs_id": fs_id, "la": la, "title": name, "version": ver, "data_groups": dgs,
                "status_2025_26": r["status"], "status_2026_27": n["status"],
                "generate_domains": domains.get(fs_id, []),
                "source_docx": rel_docx, "source_url": n["source_url"],
                "sha256": manifest.get(f"file-specifications/{n['filename']}", {}).get("sha256", ""),
                "note": note_name,  # basenames are unique in the vault, so links need no folder
                "rules_note": rules_note if (folder / f"{rules_note}.md").exists() else "",
                "metadata_notes": [g["note"] for g in comp["guides"] if fs_id in g["related_specs"]],
                "workbook_note": comp["workbook"],
            }
            front, body = split_front_matter(md)
            body, dropped = clean_body(body, folder / "media", boilerplate)
            all_dropped += [(fs_id, d) for d in dropped]
            (folder / f"{note_name}.md").write_text(build_note(meta, body, document_history(front)), encoding="utf-8")
            specs.append(meta)
            print(f"{fs_id}{' LA' if la else '':3} {ver} {name}")

    (args.out / "EDFacts Specs.md").write_text(index_note(specs, comp), encoding="utf-8")
    if all_dropped:
        print("\nDropped caption residue:")
        for fs, d in all_dropped:
            print(f"  {fs}: {d}")
    print(f"\n{len(specs)} notes -> {args.out}")


if __name__ == "__main__":
    main()
