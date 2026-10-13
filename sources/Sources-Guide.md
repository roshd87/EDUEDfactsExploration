---
tags:
  - guide
---

# Sources folder guide

Local grep-able caches of upstream code that the vault cites.

| Path | Contents |
|---|---|
| `generate/` | All 515 canonical `.sql` files of `generate.database/` at the frozen commit `37108eb`, in the upstream layout (`StoredProcedures/`, `Views/`, `Tables/`, `Functions/`, `Metadata/`, `Schemas/`). Vault citations of the form `generate.database/<path>@develop` resolve here. |
| `gen_tree_develop.txt` | (dropped 2026-10-13) Regenerate with the `gh api ... trees/master?recursive=1` command in `wiki/generate/README.md` if needed. |
