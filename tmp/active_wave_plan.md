# Active Wave Plan

## Current Wave

Current scientific/control stack:

- frozen scientific state:
  `H23_refreeze_after_r26_r27_r28`;
- active operational routing packet:
  `H25_refreeze_after_r30_r31_decision_packet`;
- primary justified next science lane:
  `R32_d0_family_local_boundary_sharp_zoom`;
- deferred systems-audit lane:
  `R33_d0_non_retrieval_overhead_localization_audit`;
- blocked future lanes:
  `R29_d0_same_endpoint_systems_recovery_execution_gate` and
  `F3_post_h23_scope_lift_decision_bundle`.

Immediate active wave:

`P16_h25_commit_hygiene_and_clean_worktree_promotion`

This wave is operational closeout only. It should finish the clean-worktree
split for the landed `H24/R30/R31/H25` packet and the narrower `P5` /
preflight closeout before any new runtime execution starts.

## Current Facts

- `R30`, `R31`, and `H25` are landed and re-exported.
- `P5_public_surface_sync` is synchronized to the `H25 active / H23 frozen`
  reading.
- `release_preflight_checklist_audit` is synchronized to the same reading and
  currently reports `docs_and_audits_green`.
- `release_worktree_hygiene_snapshot` still reports
  `dirty_worktree_release_commit_blocked`.
- clean scaffold worktree now exists at
  `D:/zWenbo/AI/LLMCompute-worktrees/h25-clean` on branch
  `wip/p16-h25-clean`.
- The remaining blocker before the next execution batch is repository hygiene,
  not scientific disagreement.

## Immediate Objectives

1. Keep `H23` as the current frozen scientific input.
2. Keep `H25` as the current active routing packet.
3. Finish clean-worktree closeout before opening `R32`.
4. Preserve the scientific order:
   `R32 -> deferred R33 -> blocked R29/F3`.
5. Avoid treating the current dirty tree as a reason to reopen claims.

## Suggested Worktree Map

- `main`: integration, root/publication driver sync, final verification,
  commit, push.
- `wt-h25-clean`: `P16` clean-worktree closeout only.
- `wt-r32`: `R32` plus planned `H26`.
- `wt-r33`: deferred `R33` plus planned `H27`, only if `H26` keeps `R33`
  justified next.

Current state:

- `wt-h25-clean` has been opened as the clean scaffold;
- the reviewable closeout subset still needs to be copied into it.

## Acceptance For This Wave

- one reviewable clean-worktree path is explicit before the next runtime batch;
- the `H24/R30/R31/H25` core packet and the narrower `P5` / preflight closeout
  are either one self-contained subset or two explicit subsets;
- state-dependent hygiene/preflight outputs are regenerated in the clean
  worktree;
- no new runtime execution starts from the current integrated dirty tree.

## Next Planned Order

Immediate operational order:

`P16_h25_commit_hygiene_and_clean_worktree_promotion` ->
clean-worktree `R32_d0_family_local_boundary_sharp_zoom` ->
planned `H26_refreeze_after_r32_boundary_sharp_zoom`

Conditional downstream order after `H26`:

deferred `R33_d0_non_retrieval_overhead_localization_audit` ->
planned `H27_refreeze_after_r32_r33_same_endpoint_decision` ->
still-blocked `R29_d0_same_endpoint_systems_recovery_execution_gate` only if a
later explicit packet changes its preconditions ->
still-blocked `F3_post_h23_scope_lift_decision_bundle`

## Validation Snapshot

- `uv run pytest tests/test_export_r30_d0_boundary_reauthorization_packet.py
  tests/test_export_r31_d0_same_endpoint_systems_recovery_reauthorization_packet.py
  tests/test_export_h25_refreeze_after_r30_r31_decision_packet.py
  tests/test_export_p5_public_surface_sync.py
  tests/test_export_release_preflight_checklist_audit.py` passed in the prior
  closeout batch (`14 passed`).
- `results/P5_public_surface_sync/summary.json` reports
  `current_paper_phase = h25_refreeze_after_r30_r31_decision_packet_active_h23_frozen`.
- `results/release_preflight_checklist_audit/summary.json` reports
  `preflight_state = docs_and_audits_green`.
- `results/release_worktree_hygiene_snapshot/summary.json` reports
  `dirty_worktree_release_commit_blocked`.

## Current References

- `docs/plans/2026-03-22-post-unattended-r32-mainline-design.md`
- `docs/plans/2026-03-22-post-h25-r32-r33-near-term-design.md`
- `docs/milestones/P16_h25_commit_hygiene_and_clean_worktree_promotion/`
- `docs/milestones/P16_h25_commit_hygiene_and_clean_worktree_promotion/commit_split_manifest.md`
- `docs/milestones/P16_h25_commit_hygiene_and_clean_worktree_promotion/worktree_runbook.md`
- `docs/milestones/R32_d0_family_local_boundary_sharp_zoom/execution_manifest.md`
- `docs/milestones/R33_d0_non_retrieval_overhead_localization_audit/component_localization_manifest.md`
- `docs/milestones/P15_internal_claim_and_handoff_sync_after_h25/commit_hygiene_handoff.md`
- `results/H25_refreeze_after_r30_r31_decision_packet/summary.json`
- `results/H23_refreeze_after_r26_r27_r28/summary.json`

## If Blocked

- do not start `R32` from the current integrated dirty tree;
- do not activate `R33` before `H26` or a later explicit packet;
- do not activate `R29` or `F3` by momentum;
- do not treat `P16` as a substitute science lane.
