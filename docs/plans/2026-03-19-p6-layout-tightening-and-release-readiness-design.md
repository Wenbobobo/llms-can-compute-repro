# P6 Layout Tightening and Release Readiness Design

## Context

`P5` closes the manuscript-assembly lane on the frozen current scope: the
bundle now reads as a sentence-polished paper draft, the public surface is
machine-audited against that draft, and main-text artifact pairings are also
machine-audited. The next paper-facing risk is no longer missing structure or
unstated scope boundaries. It is layout drift: figures, tables, captions,
appendix companions, and release-facing summaries can fall out of sync even
when the underlying claim set stays fixed.

This next phase therefore stays deliberately narrow. It does not reopen
experiments, revisit `R1` or `R2`, or widen beyond tiny typed bytecode `D0`.
Instead, it turns the current sentence-polished bundle into a layout-disciplined
and release-ready paper package.

## Recommended approach

Take the smallest approach that improves paper readiness without reopening
science:

1. keep the current claim/evidence bundle fixed;
2. tighten figure/table placement, ordering, and caption integration;
3. keep README/STATUS/release-summary wording downstream of the manuscript;
4. record any layout-only decisions in one place so later unattended passes do
   not improvise.

This is preferable to either reopening systems work too early or starting a
full paper toolchain migration before the current markdown bundle is stable.

## Parallel slices

### Slice A — Manuscript layout discipline

- tighten local transitions where figure/table callouts land;
- decide whether any section needs a compact placement note for its paired
  artifact set;
- keep the `R2` gate inline unless a later pass explicitly promotes the compact
  gate table already allowed in `layout_decision_log.md`;
- keep starter-suite `D0` evidence separate from stress/reference and
  memory-surface companions.

Primary files:
- `docs/publication_record/manuscript_bundle_draft.md`
- `docs/publication_record/caption_candidate_notes.md`
- `docs/publication_record/figure_table_narrative_roles.md`
- `docs/publication_record/manuscript_section_map.md`
- `docs/publication_record/layout_decision_log.md`

### Slice B — Release-readiness packaging

- tighten `paper_bundle_status.md` so it reflects the post-`P5` state rather
  than the earlier assembly phase;
- keep `release_summary_draft.md`, `README.md`, and `STATUS.md` downstream and
  restrained;
- record any new release-safe bundle rules in milestone ledgers and the
  experiment manifest;
- prepare a stable handoff point for the later full plan-mode replanning pass.

Primary files:
- `docs/publication_record/paper_bundle_status.md`
- `docs/publication_record/release_summary_draft.md`
- `README.md`
- `STATUS.md`
- `docs/publication_record/experiment_manifest.md`
- `docs/milestones/P6_layout_tightening_and_release_readiness/`

### Slice C — Audit-preserving maintenance

- rerun the narrow `P5` public-surface and callout-alignment exports after each
  wording batch that touches the manuscript or public surface;
- keep the audit summaries readable enough that unattended follow-up agents can
  detect whether the repo is still in a post-`P5` state;
- avoid adding new export surfaces unless layout work creates a real blind
  spot.

Primary files:
- `scripts/export_p5_public_surface_sync.py`
- `scripts/export_p5_callout_alignment.py`
- `tests/test_export_p5_public_surface_sync.py`
- `tests/test_export_p5_callout_alignment.py`
- `results/P5_public_surface_sync/`
- `results/P5_callout_alignment/`

## Acceptance

- `P5` remains closed and explicitly recorded as closed;
- the next paper-facing todo list is about layout/readiness, not scientific
  scope;
- figure/table placement, caption source, and appendix-companion boundaries are
  documented well enough for another unattended wave to continue safely;
- README/STATUS/release-summary wording stays downstream of the manuscript and
  passes the narrow `P5` audits.
