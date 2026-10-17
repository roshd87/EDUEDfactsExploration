# CLAUDE.md

## What this is

Produce EDPass-submittable EDFacts files from an **Ed-Fi + EDU/Stadium** warehouse (`edu_wh` dbt
marts) as a dbt extension package, `edu_ext_edfacts/`: spec-derived seeds (category sets, layouts,
permitted values), a GROUPING SETS count macro, and a fixed-width record macro. Plan:
`EDFactsOutputPlan.md`. Status and next steps: `HANDOFF.md`. Tracker: `.planning/` (see
`docs/agents/issue-tracker.md`). Split out of `GenerateExplorer` on 2026-10-12 (that repo was deleted 2026-10-13). The
read-only wiki of how CEDS Generate works lives here at `wiki/generate/` (moved 2026-10-13; reading
guide in `wiki/generate/README.md`) — use
it for business rules the specs leave unstated; its SQL citations point at
`sources/generate/`.

Start here: `orientation.md` (map of the repo: what is generated, hand-written, or frozen/git-ignored),
then `HANDOFF.md` (status). Touching a top-level area, a `tasks/` script or the `.planning/` layout
means editing `orientation.md` in the same change; `python3 tasks/check_docs.py` reports paths these
docs name that no longer exist.

## Sources of truth

- **EDFacts file specifications** (SY 2026-27, plus Workbook, BRSI, EDPass metadata guides) are the
  authority on file content. Frozen under `wiki/reference/edfacts/<year>/` (checksummed — never
  hand-edit) with full-text extractions in `tasks/reports/<year>/`. SY 2025-26 is kept as lineage.
- **Ed-Fi:** `wiki/reference/ed-fi/6.1.0/` (pinned schemas + descriptors), `sources/edfi/` (DS 5.2.0
  swagger cited by `wiki/analysis/EDFacts-EdFi-Gap-Analysis.md`).
- The EDU/Stadium model map lives in `/mnt/c/Repos/EDUAPIExplorer/wiki/`.

## Refreshing the spec catalog

`www.ed.gov` returns 403 to every non-browser client (curl, PowerShell, headless Chrome, WebFetch).
Refresh only with `tasks/fetch_edgov_via_chrome.ps1` (drives a visible Windows Chrome over the
DevTools protocol from WSL), then `tasks/freeze_edfacts_catalog.py <year>`.

## Build

```sh
python3 tasks/build_edfacts_seeds.py --year 2026-27   # byte-identical rebuild of edu_ext_edfacts/seeds
python3 tasks/convert_specs_to_vault.py                 # wiki/edfacts/: Obsidian notes for the 20 SY 2025-26 Active/Optional specs
~/.venvs/edfacts-tools/bin/python tasks/convert_companions_to_vault.py   # + BRSI, Workbook, metadata guides (needs openpyxl, pymupdf4llm)
python3 tasks/convert_specs_to_vault.py                 # again, so spec notes pick up the companion back-links
~/.venvs/edfacts-tools/bin/python tasks/build_brsi_review.py            # BRSI rules review sheet (proposed dbt-test handling per rule)
```

Then `dbt build` per `edu_ext_edfacts/README.md`. Full rebuild list in `HANDOFF.md`.

The Obsidian vault is `wiki/`. Legible per-spec notes (frontmatter, at-a-glance callout, pipe
tables, links to the Generate domain notes) live under `wiki/edfacts/<FSnnn>/`, indexed by
`wiki/edfacts/EDFacts Specs.md`, with `<FSnnn> Business Rules` (BRSI) beside each spec and the Workbook and
EDPass metadata guides under `wiki/edfacts/{Workbook,BRSI,Metadata}/`; all generated, so edit the converters, not the notes.

## Tooling (findings)

- **System Python is externally managed** (PEP 668; `pip install` refuses). Anything beyond the
  stdlib goes in `~/.venvs/edfacts-tools` (`python3 -m venv ~/.venvs/edfacts-tools &&
  ~/.venvs/edfacts-tools/bin/pip install openpyxl pymupdf4llm`). Not installed anywhere: pandas,
  python-docx, pdfplumber, poppler (`pdftotext`), ghostscript, qpdf, LibreOffice.
- **DOCX → markdown: pandoc** (`-t gfm --wrap=none`). It emits an HTML `<table>` for any table with
  multi-paragraph cells, col/row spans or lists in cells (every record-layout table), so
  `convert_specs_to_vault.py` flattens those with `html.parser` into pipe tables (`<br>` for
  paragraph breaks, bold re-emitted per line because Word bold runs straddle whitespace). pandoc
  also leaves a Word table's alt text as a paragraph after the table ("Data RecordsData Element
  Name, Start Position, …"); the converter drops those by pattern and prints what it dropped.
- **PDF → markdown: pymupdf4llm** (`to_markdown(path, page_chunks=True)`). Heading levels come from
  font size and are unreliable, so the companion converter re-levels from the section numbering
  (`1.0` = chapter, `2.4.1` = depth 3). Running headers/footers are removed as lines that repeat
  on ≥30 % of pages; lone page numbers and stray single letters (figure placeholders) are
  dropped; `ED` + `_Facts_` styling fragments are rejoined to `EDFacts`.
- **XLSX: openpyxl** (`read_only=True`). The BRSI's `FS` column is free text ("029, 039, 052" or
  "All files collecting category sets"), so rules are matched to specs by 3-digit id; the
  non-numeric ones become the cross-file section of the BRSI note.
- **Obsidian specifics:** vault root is `wiki/`; note basenames are unique, so links use the
  basename (`[[FS052 Membership|FS052]]`), never a folder path; inside a table cell the alias pipe
  must be `\|`; callouts (`> [!abstract]`) carry the at-a-glance block; `<u>`, `<sup>`, `<br>`
  render as HTML.
- **Frozen docs are git-ignored** (see `.gitignore`); the converters read them from disk, so a
  fresh clone must re-run the fetch and freeze before it can rebuild `wiki/edfacts/`.

## Agent skills

- Issue tracker: `.planning/` phase plans, local-only repo. See `docs/agents/issue-tracker.md`.
- Triage labels: `docs/agents/triage-labels.md`. Domain docs: `docs/agents/domain.md`.
