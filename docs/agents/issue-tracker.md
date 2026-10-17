# Issue tracker: `.planning/` phase plans

The public remote (github.com/roshd87/EDUEDfactsExploration) has no issues enabled. Work is
tracked in the repo's `.planning/` system (GSD-style layout; no tool config file is kept).

## Layout

What exists today (post-split, 2026-10-12):

- `.planning/PROJECT.md`, `.planning/REQUIREMENTS.md`: project scope and requirement IDs (e.g. `GAP-01`)
- `.planning/ROADMAP.md`: phases and their goals; `.planning/STATE.md`: current position
- Repo-level decisions live in `EDFactsOutputPlan.md` §5 (E1–E5) and `HANDOFF.md`.

Per-phase directories are created only when a phase is planned in that tool; none exist since the
split (phases 04–06 live as `ROADMAP.md` rows and `STATE.md` lines). When they do, the shape is:

- `.planning/phases/<NN>-<slug>/`: one directory per phase
  - `<NN>-CONTEXT.md`, `<NN>-RESEARCH.md`, `<NN>-PATTERNS.md`: phase-level spec and decisions
  - `<NN>-<MM>-PLAN.md`: one plan (the "issue"/spec) per unit of work
  - `<NN>-<MM>-SUMMARY.md`: what the plan actually delivered
  - `<NN>-VERIFICATION.md`, `<NN>-VALIDATION.md`: acceptance results
- `.planning/todos/`, `.planning/quick/`: small ad-hoc items (create on first use)

## When a skill says "fetch the relevant ticket / spec"

Commit messages carry the plan ID in their scope, e.g. `feat(03-04): ...` or `docs(phase-03): ...`.
Map `NN-MM` → `.planning/phases/NN-*/NN-MM-PLAN.md` (plus its `SUMMARY.md`), and `phase-NN` →
that phase's `NN-CONTEXT.md` and `ROADMAP.md` entry. Requirement IDs resolve in `REQUIREMENTS.md`.

## When a skill says "publish to the issue tracker"

Add a file under `.planning/todos/` (ad-hoc) or a new `<NN>-<MM>-PLAN.md` in the current phase
directory. Record triage state as a `Status:` line near the top, one of `needs-triage`, `needs-info`,
`ready-for-agent`, `ready-for-human` or `wontfix`.
Append discussion under a `## Comments` heading.
