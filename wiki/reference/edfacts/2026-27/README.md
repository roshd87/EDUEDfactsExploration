# EDFacts Reference Artifacts — SY 2026-27

Frozen 2026-10-07 from the U.S. Department of Education EDFacts pages, fetched through a real
Chrome window driven over the DevTools protocol (`tasks/fetch_edgov_via_chrome.ps1`) because
`www.ed.gov` returns 403 to every non-browser client. Files were then renamed, checksummed and
inventoried by `tasks/freeze_edfacts_catalog.py 2026-27`. Provenance and SHA-256 for every file
are in [MANIFEST.csv](MANIFEST.csv).

- `file-specifications/` — all **94** DOCX specifications linked from the SY 2026-27 page, every
  one **v23.0** and, on the freeze date, every one **Inactive** ("There are no active files at
  this time"). `CATALOG-INVENTORY.tsv` carries status, id, version, title, source URL and local
  filename; `index.html` is the page as rendered.
- `business-rules/` — the EDFacts Business Rules page and the BRSI workbooks it linked
  (SY 2025-26 **v1.04**, SY 2024-25, SY 2023-24 v1.13, and the SY 2022-23 user guide). No
  SY 2026-27 BRSI was published yet.
- `workbook/` — the EDFacts Workbook page and the SY 2025-26, 2024-25 and 2023-24 workbooks.
- `metadata/` — the EDPass Metadata Documentation page and all 28 linked metadata user guides
  (current and prior versions as linked).
- `general/` — the EDPass General Documentation page and the 2026 EDPass user and
  account-management guides.
- `index.html` — the EDFacts Resources page as rendered.

Differences from SY 2025-26 (`../2025-26/`): FS112 (Special Education Paraprofessionals) is no
longer in the catalog, no FS id was added, every spec is re-versioned to 23.x, and the prior-year
companion documents are kept because the pages still link them. Content delta per spec:
`wiki/analysis/EDFacts-2026-27-Delta.md`.

Do not add, rename or edit files here; refresh only by re-running the fetch and freeze scripts.
