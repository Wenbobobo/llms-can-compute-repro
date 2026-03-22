# Release Preflight Checklist

This checklist defines the minimum outward-facing sync required after the
current freeze candidate is assembled.

## Wording and scope

- [ ] `README.md` stays a restrained landing page and keeps the current narrow
  non-goals explicit.
- [ ] `STATUS.md` reflects the current active `H25` decision packet while
  preserving `H23` as the current frozen same-endpoint scientific state and
  keeps any later `R29` / `F3` execution blocked.
- [ ] `release_summary_draft.md` remains the source for short public-surface
  wording downstream of landed `H25` while preserving the narrower `H23`
  scientific limits.

## Paper-facing ledgers

- [ ] `manuscript_bundle_draft.md` still matches the fixed section and artifact
  ownership on current scope.
- [ ] `paper_bundle_status.md`, `layout_decision_log.md`,
  `freeze_candidate_criteria.md`, `main_text_order.md`, and
  `appendix_companion_scope.md` remain synchronized.
- [ ] `blog_release_rules.md` still records the blocked-blog state explicitly.

## Machine-audited guards

- [ ] `results/P1_paper_readiness/summary.json` still reports `10/10` ready
  figure/table items on the frozen scope.
- [ ] `results/H25_refreeze_after_r30_r31_decision_packet/summary.json`
  reports zero blocked items on the current active decision packet.
- [ ] `results/H23_refreeze_after_r26_r27_r28/summary.json` reports zero
  blocked items on the current frozen scientific control surface.
- [ ] `results/R30_d0_boundary_reauthorization_packet/summary.json` remains
  available as the landed post-`H23` boundary decision packet.
- [ ] `results/R31_d0_same_endpoint_systems_recovery_reauthorization_packet/summary.json`
  remains available as the landed post-`H23` systems decision packet.
- [ ] `results/H22_post_h21_boundary_reopen_and_dual_track_lock/summary.json`
  remains available as the reopen-control packet for the current refrozen
  surface.
- [ ] `results/R26_d0_boundary_localization_execution_gate/summary.json`
  remains available as the first-wave boundary packet for the current refrozen
  surface.
- [ ] `results/R27_d0_boundary_localization_extension_gate/summary.json`
  remains available as the bounded second-wave extension packet.
- [ ] `results/R28_d0_trace_retrieval_contract_audit/summary.json` remains
  available as the mechanism-contract audit for the current refrozen surface.
- [ ] `results/H21_refreeze_after_r22_r23/summary.json` remains available as
  the preserved immediate pre-reopen control surface.
- [ ] `results/H19_refreeze_and_next_scope_decision/summary.json` remains
  available as the preserved pre-`R22/R23` control surface.
- [ ] `results/H17_refreeze_and_conditional_frontier_recheck/summary.json`
  still reports zero blocked items on the preserved prior same-scope refreeze
  surface.
- [ ] `results/H15_refreeze_and_decision_sync/summary.json` reports zero
  blocked items on the preserved prior refrozen control surface.
- [ ] `results/H14_core_first_reopen_guard/summary.json` reports zero blocked
  items on the preserved core-first reopen control surface.
- [ ] `results/H13_post_h12_governance_stage_health/summary.json` reports zero
  blocked items on the preserved governance/runtime handoff.
- [ ] `results/P5_public_surface_sync/summary.json` reports zero blocked items.
- [ ] `results/P5_callout_alignment/summary.json` reports zero blocked rows.
- [ ] `results/H2_bundle_lock_audit/summary.json` reports zero blocked items.
- [ ] `results/release_worktree_hygiene_snapshot/summary.json` classifies the
  current release-commit readiness and reports no diff-check content issues.
- [ ] `results/V1_full_suite_validation_runtime_timing_followup/summary.json`
  reports `healthy_but_slow` with zero timed-out files.

## Release hygiene

- [ ] Use `results/release_worktree_hygiene_snapshot/summary.json` to decide
  whether an outward sync commit is currently blocked by a dirty tree.
- [ ] No local-only source material under `docs/Origin/` or `docs/origin/`
  enters the public surface.
- [ ] Blog work remains blocked unless `blog_release_rules.md` is satisfied in
  full.
