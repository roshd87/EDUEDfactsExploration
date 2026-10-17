#!/usr/bin/env python3
"""Build the BRSI rules review note for the vault: wiki/edfacts/BRSI/BRSI Rules Review for dbt Tests.md

Every SY 2025-26 BRSI rule that names one of the converted specs (or names a class of files) gets a
proposed handling and a pre-set decision, so a reviewer only flips the ones they disagree with.
The same content lives as a Claude Doc with dropdown decisions (REVIEW_DOC_URL); this note is the
vault copy and links to the spec and rules notes.

    ~/.venvs/edfacts-tools/bin/python tasks/build_brsi_review.py   # same venv as convert_companions_to_vault.py
"""
from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
from convert_companions_to_vault import BRSI_LABEL, BRSI_XLSX, OUT, brsi_rows, rule_fs_ids, spec_notes  # noqa: E402
from convert_specs_to_vault import FROZEN, REF, TARGET_YEAR, read_manifest  # noqa: E402

REVIEW_DOC_URL = "https://claude.ai/code/artifact/0d1fae66-f6a9-49f2-8c08-4875755c4d9a"
NOTE = OUT / "BRSI" / "BRSI Rules Review for dbt Tests.md"
DECISIONS = ["Test now", "Test later", "Not a dbt test", "Needs discussion"]
SECTIONS = [  # (heading, FS ids that claim a rule; a rule goes to the first section that claims it)
    ("Cross-file rules", None),
    ("FS052 Membership and FS039 Grades Offered", {"FS052", "FS039"}),
    ("FS002 and FS089 IDEA child count", {"FS002", "FS089"}),
    ("FS029 Directory", {"FS029"}),
    ("Remaining specs: FS033, FS059, FS129, charter files, N or D, IDEA Part C", "rest"),
]
PRIOR_YEAR = re.compile(r"prior year|previous year|prior school year|previous school year|year to year|prior sy|previous sy|from py|changed from py")

# Hand adjustments to the scripted triage, keyed by EDPass rule id: (handling, needs, decision).
# ponytail: a dict beats a second heuristic layer; extend it as the reviewer decides.
OVERRIDES = {
    "FERR-0002": ("Structural: only if a CSV output is ever added; the package emits fixed-width .txt", "", 2),
    "FERR-0003": ("Structural: only if a tab-delimited output is ever added; the package emits fixed-width .txt", "", 2),
    "FERR-0021": ("Structural: relationship test from every file's header to the FS029 SEA record", "FS029", 0),
    "FERR-0027": ("EDPass checks the uploading user's state; not reproducible in the warehouse", "", 2),
    "FERR-0030": ("EDPass permission check; not reproducible in the warehouse", "", 2),
    "FMTE-0010": ("Structural: accepted_values test against the permitted-values seed", "", 0),
    "FMTE-0011": ("Structural: relationship test against the category-set seed", "", 0),
    "FMTE-0020": ("Structural: unique test on the record grain", "", 0),
    "FMTE-0017": ("Structural: unique test on the FS039 record grain", "", 0),
    "All-0002 (A-LEA, B-SCH)": ("Generic structural check across every file; one shared test parameterised by spec", "FS029 operational status", 0),
    "DGO-0023": ("Warehouse test on the directory/roster marts (slice 3); branch A compares the name to the prior year", "Prior-year name for branch A", 3),
    "DGO-0030": ("Warehouse test on the directory/roster marts (slice 3); branch A compares the name to the prior year", "Prior-year name for branch A", 3),
    "CCD-0053": ("Directory check; only the new-school branch runs without the prior-year name", "Prior-year name for the renamed-school branch", 3),
    "DGO-0024": ("Directory check; only the new-school branch runs without the prior-year name", "Prior-year name for the renamed-school branch", 3),
    "DGO-0025": ("Directory check; only the new-school branch runs without the prior-year name", "Prior-year name for the renamed-school branch", 3),
    "DGO-0026": ("Directory check; only the new-school branch runs without the prior-year name", "Prior-year name for the renamed-school branch", 3),
    "DGO-0027": ("Directory check; only the new-school branch runs without the prior-year name", "Prior-year name for the renamed-school branch", 3),
    "DGO-0028": ("Directory check; only the new-LEA branch runs without the prior-year name", "Prior-year name for the renamed-LEA branch", 3),
    "DGO-0029": ("Directory check; only the new-LEA branch runs without the prior-year name", "Prior-year name for the renamed-LEA branch", 3),
    "DGO-0010": ("Runs outside EDPass pre-submission (PSC Notice); needs the CSP grantee list, not in the warehouse", "", 2),
    "FERR-0012": ("Structural: length check on the directory mart (minimum 3)", "", 0),
    "FERR-0013": ("Structural: format check on the directory and roster marts (5 digits, 00600 to 99998)", "", 0),
    "FERR-0014": ("Structural: format check on the directory and roster marts (4 digits, not 0000)", "", 0),
    "FERR-0015": ("Structural: format check on the directory mart", "", 0),
    "FERR-0025": ("Structural: format check on the directory mart", "", 0),
    "FERR-0026": ("Structural: format check on the directory mart", "", 0),
    "FERR-0029": ("Structural: length check on the directory and roster marts (minimum 3)", "", 0),
    "FERR-0017": ("Structural: decimal format check on FS059 FTE fields; the other listed specs follow when built", "", 0),
    "FMTE-0001": ("Structural: unique test on the education-unit grain of every single-record file (FS029, FS059, FS129, FS197, FS207 in scope); the other listed specs follow when built", "", 0),
    "FMTE-0002": ("Structural: unique test on the directory mart", "", 0),
    "FMTE-0003": ("Structural: consistency test on the directory mart", "", 0),
    "FMTE-0004": ("Structural: consistency test on the directory mart", "", 0),
    "FMTE-0005": ("Structural: not-null test on NCES ids for non-new units", "", 0),
    "FMTE-0006": ("Structural: relationship test from every school-level file to the FS029 school directory", "", 0),
    "FMTE-0009": ("Structural: relationship test from every LEA-level file to the FS029 LEA directory", "", 0),
    "FMTE-0012": ("Structural: unique test on NCES ids in the directory mart", "", 0),
    "FMTE-0013": ("Structural: consistency test on the directory mart", "", 0),
    "FMTE-0014": ("Structural: consistency test on the directory mart", "", 0),
    "FMTE-0015": ("Structural: consistency test on the directory mart", "", 0),
    "FMTE-0016": ("Structural: consistency test on the directory mart", "", 0),
    "FMTE-0018": ("Id-change consistency within the current-year directory mart", "", 0),
    "FMTE-0019": ("Id-change consistency within the current-year directory mart", "", 0),
    "FMTE-0029": ("Id consistency within the current-year directory mart", "", 0),
    "FMTE-0030": ("Id consistency within the current-year directory mart", "", 0),
    "FMTE-0031": ("Id consistency within the current-year directory mart", "", 0),
    "FMTE-0032": ("Id consistency within the current-year directory mart", "", 0),
    "FMTE-0033": ("Id consistency within the current-year directory mart", "", 0),
    "FMTE-0034": ("Id consistency between the LEA and school rows of the directory mart", "", 0),
    "FMTE-0037": ("Structural: consistency test on the directory mart", "", 0),
    "FMTE-0038": ("Id-change consistency within the current-year directory mart", "", 0),
    "FMTE-0042": ("Structural: range check on the directory mart", "", 0),
    "FMTE-0007": ("Structural: unique test on the charter authorizer roster", "", 0),
    "FMTE-0008": ("Structural: unique test on the management organization roster", "", 0),
    "IDEA-0259": ("Year-over-year comparison; needs last year's submitted file or a prior-year snapshot", "Prior-year submission, FS231", 1),
    "IDEA-0260": ("Year-over-year comparison; needs last year's submitted file or a prior-year snapshot", "Prior-year submission, FS231", 1),
}


def md(s: str) -> str:
    return re.sub(r"\s*\n+\s*", "<br>", s.replace("|", "\\|")).strip()


def levels(r):
    out = [lv for lv in ("SEA", "LEA", "SCH") if r.get(lv, "").upper().startswith("Y")]
    if r.get("Other") and r["Other"].upper() != "N":
        out.append("Other")
    return ", ".join(out) or "—"


def triage(r, in_scope: set[str]):
    """(proposed handling, needs, decision index, show logic)."""
    rid = r["EDPass Rule ID"]
    if rid in OVERRIDES:
        h, n, d = OVERRIDES[rid]
        return h, n, d, d in (0, 3)
    fs = set(rule_fs_ids(r))
    outside = sorted(fs - in_scope)
    txt = (r["Definition"] + " " + r["Rule Logic"]).lower()
    sysp = r["System of Publication"].upper()
    phase = r["Data Quality Phase"].lower()
    obj = r["Rule Objective"].lower()
    fail = r["Failure Classification"]
    if rid.startswith("Not Enabled") or sysp in ("DMS", "PSC NOTICE", "STATE EXECUTED") or phase.startswith(("post", "state")):
        return f"Runs outside EDPass pre-submission ({r['System of Publication'] or r['Data Quality Phase']}); not reproducible in the warehouse", "", 2, False
    if "longitudinal" in obj or PRIOR_YEAR.search(txt):
        return "Year-over-year comparison; needs last year's submitted file or a prior-year snapshot", "Prior-year submission", 1, False
    if outside:
        return f"Cross-file check with {', '.join(outside)}, not in scope", ", ".join(outside), 1, False
    if fail in ("Format Error", "File Error") or obj.startswith("format"):
        return "Structural: should hold by construction in the edfacts_file macro and seeds; add a macro unit test", "", 0, True
    if r["Metadata FS"]:
        mfs = "FS" + r["Metadata FS"].replace(", ", ", FS")
        return f"Warehouse test gated by the SEA metadata answer ({mfs} → edfacts_config)", f"edfacts_config: {mfs} DG {r['Metadata DG']}", 0, True
    if r["Threshold %"] or r["Threshold Base"]:
        t = []
        if r["Threshold %"]:
            t.append(f"threshold {r['Threshold %']} %")
        if r["Threshold Base"]:
            t.append(f"base {r['Threshold Base']}")
        return "Warehouse test at warn severity; " + ", ".join(t), "", 0, True
    if "directory" in obj:
        return "Warehouse test on the directory/roster marts (slice 3)", "", 0, True
    if not fs:
        return "Generic structural check across every file; one shared test parameterised by spec", "", 0, True
    return "Warehouse test: SQL over the counts produced by edfacts_counts", "", 0, True


def rule_label(r):
    rid = r["EDPass Rule ID"]
    if rid.startswith("Not Enabled"):
        return f"*DMS edit* ({r['Legacy Rule ID'][:40]})"
    return f"**{rid}**"


def files_cell(r, specs):
    if not rule_fs_ids(r):
        return md(r["FS"]) if r["FS"] else "*all*"
    return re.sub(r"\b(\d{3})\b", lambda m: f"[[{specs['FS' + m.group(1)]}\\|{m.group(1)}]]" if "FS" + m.group(1) in specs else m.group(1), re.sub(r"\s+", " ", r["FS"]))


def main():
    specs = spec_notes()  # 'FS052' -> 'FS052 Membership'
    in_scope = set(specs)
    rules = brsi_rows(openpyxl.load_workbook(REF / TARGET_YEAR / BRSI_XLSX, read_only=True), "SY 2025-26")
    sha = read_manifest(TARGET_YEAR).get(BRSI_XLSX, {}).get("sha256", "")

    groups = collections.OrderedDict((h, []) for h, _ in SECTIONS)
    seen = set()
    for r in sorted(rules, key=lambda r: r["EDPass Rule ID"]):
        ids = set(rule_fs_ids(r))
        if ids and not ids & in_scope:
            continue
        for heading, claim in SECTIONS:
            if (claim is None and not ids) or (claim == "rest" and ids) or (isinstance(claim, set) and ids & claim):
                if r["EDPass Rule ID"] not in seen or r["EDPass Rule ID"].startswith("Not Enabled"):
                    groups[heading].append(r)
                    seen.add(r["EDPass Rule ID"])
                break

    tallies = {}
    body = []
    for heading, rs in groups.items():
        counts = collections.Counter()
        lines = [f"## {heading}", "", "| Rule | Levels | Files | Definition | Logic | Proposed handling | Needs | Decision |", "|---|---|---|---|---|---|---|---|"]
        for r in rs:
            h, n, d, show = triage(r, in_scope)
            counts[d] += 1
            logic = md(r["Rule Logic"]) if show else "_see rules note_"
            lines.append(f"| {rule_label(r)} | {levels(r)} | {files_cell(r, specs)} | {md(r['Definition'])} | {logic} | {h} | {n} | {DECISIONS[d]} |")
        tallies[heading] = (len(rs), counts)
        body += lines + [""]

    total = sum(n for n, _ in tallies.values())
    tot = collections.Counter()
    for _, c in tallies.values():
        tot += c
    scope = ["| Section | Rules | Test now | Test later | Not a dbt test | Needs discussion |", "|---|---|---|---|---|---|"]
    for heading, (n, c) in tallies.items():
        scope.append(f"| {heading} | {n} | {c[0]} | {c[1]} | {c[2]} | {c[3]} |")
    scope.append(f"| **All** | **{total}** | **{tot[0]}** | **{tot[1]}** | **{tot[2]}** | **{tot[3]}** |")

    out = [
        "---",
        'title: "BRSI Rules Review for dbt Tests"',
        f'brsi: "{BRSI_LABEL}"',
        f"rules: {total}",
        f'review_doc: "{REVIEW_DOC_URL}"',
        f"source: {BRSI_XLSX}",
        f"sha256: {sha}",
        f"frozen: {FROZEN}",
        "tags: [edfacts, brsi, review, dbt-tests]",
        "---",
        "",
        "# BRSI Rules Review for dbt Tests",
        "",
        "> [!abstract] At a glance",
        f"> **Rules to decide:** {total} from [[BRSI SY 2025-26]] that name a converted spec or a class of files",
        f"> **Pre-set decisions:** {tot[0]} Test now, {tot[1]} Test later, {tot[2]} Not a dbt test, {tot[3]} Needs discussion",
        f"> **Live review copy with dropdowns:** [Claude Doc]({REVIEW_DOC_URL}). Decisions made there are the record; this note is the vault copy, regenerated by `tasks/build_brsi_review.py`.",
        "> **See also:** [[EDFacts Specs|all specs]], [[EDFacts Workbook SY 2025-26|workbook]]",
        "",
        "## Purpose and how to review",
        "",
        "Each EDPass business rule below needs one decision before it becomes a dbt test in `edu_ext_edfacts`: test it in the warehouse, defer it, or leave it to EDPass. The proposed handling column is a first pass from the rule text; the Decision column is pre-set to match it.",
        "",
        "1. Read the rule's definition and the proposed handling.",
        "2. Pick a Decision: **Test now** (Phase 3 slice), **Test later**, **Not a dbt test** (EDPass-side, needs prior-year submissions, or data the warehouse never holds), or **Needs discussion**.",
        "3. Add a note where the proposed handling is wrong or the needed data has a known source.",
        "",
        "After review, every **Test now** rule becomes a named dbt test (`brsi_<rule id>`) with the rule's error message as the test description, so EDPass failures and warehouse failures read the same.",
        "",
        "## Scope and counts",
        "",
        f"Every rule in the BRSI {BRSI_LABEL} (the newest published; no SY {TARGET_YEAR} edition existed at the {FROZEN} freeze) that names one of the 19 converted specs, plus the rules whose FS column names a class of files. Rules naming several specs appear once, in the first section that claims them. Discontinued rules are left out. Full rule text, error messages and legacy ids are in each spec's `<FSnnn> Business Rules` note.",
        "",
        *scope,
        "",
        "## Triage categories",
        "",
        "Assigned from the rule's phase, objective, threshold, metadata and FS columns in this order of precedence, then adjusted by hand for the cases named in each section (`OVERRIDES` in the script).",
        "",
        "| Proposed handling | When it applies | dbt mechanism | Pre-set decision |",
        "|---|---|---|---|",
        "| Runs outside EDPass pre-submission | System of publication is DMS, PSC Notice or State Executed, or the phase is post-submission | None; EDPass or the SEA runs it after submission | Not a dbt test |",
        "| Year-over-year comparison | Objective is Longitudinal, or the logic compares to the prior year | Needs a prior-year snapshot table of submitted counts; defer until one exists | Test later |",
        "| Cross-file check with an out-of-scope spec | The FS column names a spec that is not among the 19 converted | Defer until that spec is built | Test later |",
        "| Structural | Format Error, File Error, or a Format and Validation objective | Must hold by construction in `edfacts_file` and the seeds; one macro unit test per rule | Test now |",
        "| Gated by an SEA metadata answer | The rule reads a FS5xxx metadata collection | Singular test keyed on the matching `edfacts_config` column | Test now |",
        "| Threshold warning | The BRSI sets a threshold base or percent | dbt test with `severity: warn` and the threshold as a parameter | Test now |",
        "| Directory and roster check | Objective is Directory and rosters | SQL test over the directory marts (slice 3) | Test now |",
        "| Generic structural check | The FS column names a class of files rather than ids | One shared test macro, parameterised by spec | Test now |",
        "| Warehouse test | Everything else within the 19 specs | SQL test over the output of `edfacts_counts` | Test now |",
        "| Name heuristic with a prior-year branch | School or LEA name implies a type; only the new-unit branch runs without last year's name | Decide: new-unit branch only, or wait for the snapshot | Needs discussion |",
        "",
        *body,
        "## Open questions for the reviewer",
        "",
        "1. **Prior-year snapshot.** Should the package keep a snapshot table of each year's submitted counts so the year-over-year rules become tests next year, or stay out of scope for good?",
        "2. **School-name heuristics.** Run the new-unit branch of DGO-0023 to DGO-0030 and CCD-0053 only, or wait for the snapshot?",
        "3. **Threshold rules as warnings.** Proposed as `severity: warn`; confirm, or fail the build on any of them?",
        "4. **Structural rules.** Proposed as macro unit tests rather than data tests; is a passing unit test enough evidence, or add a data test on the emitted file as well?",
        "5. **Metadata-gated rules.** They cannot run until `edfacts_config` has the FS5xxx columns; acceptable sequencing, or stub the columns with Grand Bend defaults first?",
        "6. **Test naming.** `brsi_<rule id>` with the EDPass error message as the description.",
        "",
    ]
    NOTE.write_text("\n".join(out), encoding="utf-8")
    print(f"{total} rules -> {NOTE}; decisions {dict(tot)}")


if __name__ == "__main__":
    main()
