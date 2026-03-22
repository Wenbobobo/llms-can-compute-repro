# Submission Candidate Criteria

This file defines the minimum conditions for upgrading the current
freeze-candidate checkpoint into a submission-candidate bundle on the same
frozen scope, currently anchored on active `H32` evidence and the current
docs-only `H34` control packet, while preserving `H33/R39` as the immediate
prior question-selection and completed same-substrate audit chain and
`H25/H23` as historical same-endpoint context.

## Must-pass criteria

1. Freeze-candidate conditions still hold.
   `freeze_candidate_criteria.md` remains the base gate; `P8` can add
   consistency and ledger lock requirements, but it cannot soften the existing
   scope boundaries.
2. Manuscript bundle and supporting ledgers are locked together.
   `manuscript_bundle_draft.md`, `caption_candidate_notes.md`,
   `figure_table_narrative_roles.md`, and `manuscript_section_map.md` must
   agree on the current claim-bearing main-text artifacts and section
   ownership.
3. Appendix minimum package is explicit and complete.
   Required companions under `appendix_companion_scope.md` and
   `appendix_boundary_map.md` must be present, and optional companions must stay
   clearly optional.
4. Claim, threat, and negative-result ledgers stay synchronized.
   `claim_ladder.md`, `claim_evidence_table.md`, `negative_results.md`, and
   `threats_to_validity.md` must describe the same frozen endpoint, the same
   blocked claims, and the same post-`H34` routing boundaries.
5. Release-facing summaries remain downstream.
   `release_summary_draft.md`, `README.md`, and `STATUS.md` may summarize the
   locked bundle, but they may not outrun it, imply a new evidence wave, or
   blur the distinction between active `H32` routing, current docs-only `H34`
   control, preserved `H33/R39` context, and historical `H25/H23`
   same-endpoint evidence.
6. Standing audits remain green.
   `P1`, `P5` public-surface sync, `P5` callout alignment, and the `H2`
   bundle-lock audit must all report zero blocked items on the current repo
   state.

## Required evidence anchors

- `results/P1_paper_readiness/summary.json`
- `results/H32_post_r38_compiled_boundary_refreeze/summary.json`
- `results/H34_post_r39_later_explicit_scope_decision_packet/summary.json`
- `results/H33_post_h32_conditional_next_question_packet/summary.json`
- `results/R39_origin_compiler_control_surface_dependency_audit/summary.json`
- `results/P5_public_surface_sync/summary.json`
- `results/P5_callout_alignment/summary.json`
- `results/H2_bundle_lock_audit/summary.json`
- `docs/publication_record/current_stage_driver.md`
- `docs/publication_record/main_text_order.md`
- `docs/publication_record/appendix_companion_scope.md`
- `docs/publication_record/conditional_reopen_protocol.md`

## Reopen only if

- a manuscript sentence no longer matches the frozen claim/evidence table;
- a required appendix companion is missing for a main-text claim;
- an audit reports a real bundle-lock failure;
- a later review deliberately authorizes one `E1` patch lane.
