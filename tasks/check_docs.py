#!/usr/bin/env python3
"""Report repo paths named in the orientation docs that don't exist, plus missing local prerequisites.

Run by hand after editing CLAUDE.md, HANDOFF.md, orientation.md or docs/agents/. Exit 1 on findings.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ["CLAUDE.md", "HANDOFF.md", "orientation.md", "docs/agents/issue-tracker.md"]
# ponytail: a path is any backticked token containing "/" that isn't a URL, flag, glob or variable.
SKIP = re.compile(r"^(-|~|\$|https?:|[A-Za-z]:\\|\.\./)|[*?$]")
# Paths this repo documents but only the owner's machine or a future phase holds.
KNOWN_ABSENT = {".planning/phases/", ".planning/todos/", ".planning/quick/"}

bad = []
for doc in DOCS:
    for span in re.findall(r"`([^`\n]+)`", (ROOT / doc).read_text()):
        if (ROOT / span).exists():  # whole span is a path with spaces ("wiki/edfacts/EDFacts Specs.md")
            continue
        for tok in span.split():
            stem = re.split(r"[<>{}|]", tok)[0].rstrip(",;:)(")  # prefix before any <placeholder>
            if "/" not in stem or SKIP.search(stem) or stem in KNOWN_ABSENT:
                continue
            if not (ROOT / stem.split("/")[0]).exists():  # relative mention ("seeds/", "BRSI/"), not a repo path
                continue
            if not (ROOT / stem).exists():
                bad.append(f"{doc}: `{tok}` not on disk")

for p in ("wiki/reference/edfacts/2026-27/file-specifications", "sources/generate", "wiki/reference/ed-fi/6.1.0/Schemas"):
    if not (ROOT / p).exists():
        bad.append(f"frozen docs missing (git-ignored): {p} — re-run fetch + freeze")
for venv in ("edfacts-tools", "edfacts-dbt"):
    if not (Path.home() / ".venvs" / venv).exists():
        bad.append(f"~/.venvs/{venv} missing (see CLAUDE.md § Tooling / edu_ext_edfacts/README.md)")

print("\n".join(sorted(set(bad))) or "ok")
sys.exit(bool(bad))
