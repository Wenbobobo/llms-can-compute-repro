# Integration Log

## 2026-03-19 — `P5` closure and `P6` scaffold

### Scope

- completed the sentence-level polish and callout-alignment pass on the current
  manuscript bundle without reopening scope;
- refreshed `README.md`, `STATUS.md`, and
  `docs/publication_record/release_summary_draft.md` to reflect the completed
  `P5` state and the next layout/readiness lane;
- refreshed the narrow `P5` public-surface and callout-alignment audits so they
  now report post-`P5` status;
- created `docs/plans/2026-03-19-p6-layout-tightening-and-release-readiness-design.md`
  and the `docs/milestones/P6_layout_tightening_and_release_readiness/`
  scaffold for the next unattended paper-facing wave.

### Validation

- `D:\zWenbo\AI\LLMCompute\.venv\Scripts\python.exe scripts/export_p5_public_surface_sync.py`
  passed;
- `D:\zWenbo\AI\LLMCompute\.venv\Scripts\python.exe scripts/export_p5_callout_alignment.py`
  passed;
- `D:\zWenbo\AI\LLMCompute\.venv\Scripts\python.exe -m pytest -q tests/test_export_p5_public_surface_sync.py tests/test_export_p5_callout_alignment.py`
  passed with `7 passed`;
- `D:\zWenbo\AI\LLMCompute\.venv\Scripts\python.exe -m pytest -q`
  passed with `136 passed, 1 warning`;
- `git diff --check` passed with only line-ending normalization warnings on
  regenerated `results/P5_*` artifacts.

### Outcome

- `P5` is now recorded as closed rather than merely in-progress;
- the repo surface and machine-readable `P5` audits agree that the next work is
  a separate layout-tightening / release-readiness wave;
- `P6` now contains the minimum durable context needed for the next full
  plan-mode replanning pass.

## 2026-03-19 — public-surface sync to `main`

### Scope

- synced the `P5` manuscript-assembly batch from `wip/p3-paper-freeze` back to
  `main` by fast-forward;
- carried over the new publication-record assets:
  - `manuscript_bundle_draft.md`
  - `appendix_stub_notes.md`
  - `caption_candidate_notes.md`
  - `layout_decision_log.md`
  - `figure_table_narrative_roles.md`
  - `section_caption_notes.md`
  - `manuscript_stub_notes.md`
- carried over the public-surface wording refresh for `README.md` and
  `STATUS.md`;
- carried over the refreshed `P1` readiness exports with the `D0`
  exact-trace/final-state table normalized to current-scope `ready`.

### Validation

- `git diff --check` passed on `main`;
- `uv run pytest -q` passed on `main` with `129 passed, 1 warning`.

### Outcome

- `main` is no longer behind the active paper scope;
- the repository front page, status page, `P1` readiness exports, and
  publication ledgers now tell the same current-scope story;
- the next paper-lane work can move back to drafting strategy instead of
  emergency public-surface catch-up.
