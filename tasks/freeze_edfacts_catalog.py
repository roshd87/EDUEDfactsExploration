"""Freeze a downloaded EDFacts reference year into the 2025-26 collection shape.

Input: wiki/reference/edfacts/<year>/_inbox/<page-slug>/{page.html, *.docx|*.pdf|*.xlsx}
       as written by C:\\Temp\\cc-cdp\\cdp.ps1 (one folder per ed.gov page).
Output: file-specifications/ (renamed FS###-v##.#--<orig>.docx + CATALOG-INVENTORY.tsv + index.html),
        business-rules/, workbook/, metadata/, general/ (each with index.html), MANIFEST.csv, README.md.
The inbox is removed once every file has been moved. Run: python3 tasks/freeze_edfacts_catalog.py 2026-27
"""
import csv
import hashlib
import html
import re
import shutil
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = {  # inbox folder slug -> (target folder, source_role, artifact prefix)
    "edfacts-file-specifications-sy-{yr}": ("file-specifications", "EDPass file specification", "fs"),
    "edfacts-business-rules": ("business-rules", "EDFacts business rules", "brsi"),
    "edfacts-workbook": ("workbook", "EDFacts workbook", "workbook"),
    "edpass-metadata-documentation": ("metadata", "EDPass metadata user guide", "metadata"),
    "edpass-general-documentation": ("general", "EDPass general documentation", "general"),
    "edfacts-resources": (".", "EDFacts resources index", "resources"),
}
MEDIA = {".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
         ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
         ".pdf": "application/pdf", ".html": "text/html"}
LINK = re.compile(r'<(h[1-6])[^>]*>(.*?)</\1>|<a[^>]+href="([^"]*)"[^>]*>(.*?)</a>', re.S | re.I)
DOC = re.compile(r"\.(docx|xlsx|xls|pdf|zip)(\?|$)|/media/document/", re.I)
FS = re.compile(r"\b(FS\d{3})\b.*?\bv(\d+\.\d+)\b", re.S)


def sha256(p):
    with p.open("rb") as fh:
        return hashlib.file_digest(fh, "sha256").hexdigest()


def strip(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


def links_with_section(page_html):
    """Yield (section_heading, link_text, href) for document links, in page order."""
    section = ""
    for h, htext, href, atext in LINK.findall(page_html):
        if h:
            section = strip(htext)
        elif href and DOC.search(href):
            yield section, strip(atext), href


def status_from(section):
    s = section.lower()
    if "optional" in s:
        return "Optional"
    if "inactive" in s:
        return "Inactive"
    if "active" in s:
        return "Active"
    return "Unknown"


def main(year):
    base = ROOT / "wiki/reference/edfacts" / year
    inbox = base / "_inbox"
    frozen = date.today().isoformat()
    manifest = []
    inventory = []
    for slug_t, (target, role, prefix) in PAGES.items():
        slug = slug_t.format(yr=year)
        src = inbox / slug
        if not src.exists():
            print("skip (not downloaded):", slug)
            continue
        dst = base / target
        dst.mkdir(parents=True, exist_ok=True)
        page_html = (src / "page.html").read_text(encoding="utf-8")
        page_url = f"https://www.ed.gov/data/edfacts-initiative/edfacts-resources/" + (
            f"edfacts-file-specifications/{slug}" if prefix == "fs" else ("" if prefix == "resources" else slug))
        shutil.move(str(src / "page.html"), str(dst / "index.html"))
        manifest.append(dict(artifact_id=f"{prefix}-index", source_role=f"{role} index", source_url=page_url,
                             version_or_release=f"SY {year}", local_path=str((dst / "index.html").relative_to(base)).replace("\\", "/"),
                             media_type="text/html", sha256=sha256(dst / "index.html"), notes="Page as rendered in Chrome on the freeze date."))
        seen = set()
        for section, text, href in links_with_section(page_html):
            if href in seen:
                continue
            seen.add(href)
            if href.startswith("/"):
                href = "https://www.ed.gov" + href
            orig = re.sub(r"[^A-Za-z0-9._-]", "_", Path(href.split("?")[0]).name)
            f = src / orig
            if not f.exists():
                print("MISSING download:", slug, orig)
                continue
            if prefix == "fs":
                m = FS.search(text)
                assert m, text
                fsid, ver = m.group(1), f"v{m.group(2)}"
                new = f"{fsid}-{ver}--{orig}"
                inventory.append(dict(status=status_from(section), file_spec_id=fsid, version=ver, title=text, source_url=href, filename=new))
                aid, version = f"fs-{fsid.lower()}-{ver}", ver
            else:
                new, aid, version = orig, f"{prefix}-{Path(orig).stem.lower()[:60]}", text[:80]
            shutil.move(str(f), str(dst / new))
            manifest.append(dict(artifact_id=aid, source_role=role, source_url=href, version_or_release=version,
                                 local_path=str((dst / new).relative_to(base)).replace("\\", "/"),
                                 media_type=MEDIA.get(Path(new).suffix.lower(), "application/octet-stream"),
                                 sha256=sha256(dst / new), notes=text if prefix != "fs" else f"Catalog section: {section}"))
        leftovers = [p.name for p in src.iterdir()]
        assert not leftovers, (slug, leftovers)
        src.rmdir()
    # inventory
    inv_path = base / "file-specifications/CATALOG-INVENTORY.tsv"
    with inv_path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["status", "file_spec_id", "version", "title", "source_url", "filename"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(sorted(inventory, key=lambda r: (r["file_spec_id"], r["version"])))
    with (base / "MANIFEST.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["artifact_id", "source_role", "source_url", "version_or_release", "reporting_year", "frozen_at", "local_path", "media_type", "sha256", "status", "notes"], lineterminator="\n")
        w.writeheader()
        for m in manifest:
            w.writerow({**m, "reporting_year": year, "frozen_at": frozen, "status": "authoritative cached"})
    (inbox / "download-log.tsv").unlink(missing_ok=True)
    rest = [p.name for p in inbox.iterdir()] if inbox.exists() else []
    if inbox.exists() and not rest:
        inbox.rmdir()
    print(f"specs={len(inventory)} {dict(Counter(r['status'] for r in inventory))} manifest_rows={len(manifest)} inbox_left={rest}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "2026-27")
