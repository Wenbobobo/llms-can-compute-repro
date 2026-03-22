# Milestones Index

This directory stores milestone-local staging areas, result digests, and
planning-only bundles. These folders are not equal in status: some are the
current active/frozen surfaces, some are deferred or blocked future lanes, and
many are preserved historical packets. Use this index to avoid treating an old
milestone as the current driver by accident.

## Reading Order

For current work, read milestones in this order:

1. `../publication_record/current_stage_driver.md`
2. `../../tmp/active_wave_plan.md`
3. the relevant milestone `README.md` / `status.md`
4. the matching `results/<lane>/summary.json`

If milestone prose conflicts with the current stage driver or result summary,
trust the current stage driver and the machine-readable result.

## Current Top Of Stack

- `H25_refreeze_after_r30_r31_decision_packet/` — current active operational
  decision packet.
- `H23_refreeze_after_r26_r27_r28/` — current frozen scientific state.

## Immediate Operational Closeout

- `P16_h25_commit_hygiene_and_clean_worktree_promotion/` — immediate
  clean-worktree closeout lane before `R32`.

## Current Downstream Next Lanes

- `R32_d0_family_local_boundary_sharp_zoom/` — primary justified next science
  lane.
- `R33_d0_non_retrieval_overhead_localization_audit/` — deferred systems-audit
  lane.

## Planned Downstream Refreeze Packets

- `H26_refreeze_after_r32_boundary_sharp_zoom/` — planned post-`R32`
  same-endpoint refreeze.
- `H27_refreeze_after_r32_r33_same_endpoint_decision/` — planned conditional
  post-`R33` same-endpoint refreeze.

## Current Blocked Or Planning-Only Lanes

- `R29_d0_same_endpoint_systems_recovery_execution_gate/` — blocked future
  same-endpoint systems lane.
- `F2_future_frontier_recheck_activation_matrix/` — planning-only frontier
  activation surface downstream of the full `H19 -> H25` chain.
- `F3_post_h23_scope_lift_decision_bundle/` — blocked scope-lift gate.
- `F4_post_h23_origin_claim_delta_matrix/` — internal origin-facing delta
  surface anchored to frozen `H23`.
- `P15_internal_claim_and_handoff_sync_after_h25/` — internal handoff and
  commit-hygiene guidance for the current stack.

## Immediate Preserved Controls

- `H24_post_h23_reauthorization_and_hygiene_split/`
- `R30_d0_boundary_reauthorization_packet/`
- `R31_d0_same_endpoint_systems_recovery_reauthorization_packet/`
- `H22_post_h21_boundary_reopen_and_dual_track_lock/`
- `R26_d0_boundary_localization_execution_gate/`
- `R27_d0_boundary_localization_extension_gate/`
- `R28_d0_trace_retrieval_contract_audit/`
- `H21_refreeze_after_r22_r23/`
- `R22_d0_true_boundary_localization_gate/`
- `R23_d0_same_endpoint_systems_overturn_gate/`
- `H20_post_h19_mainline_reentry_and_hygiene_split/`
- `H19_refreeze_and_next_scope_decision/`
- `H18_post_h17_mainline_reopen_and_scope_lock/`
- `H17_refreeze_and_conditional_frontier_recheck/`

## Historical Families

- `H*` — handoff, reopen, refreeze, or governance packet.
- `R*` — experiment or decision lane.
- `P*` — publication/public-surface/manuscript lane.
- `F*` — future-planning or blocked-lane surface.
- `E*` — conditional reopen protocol or patch lane.
- `M*` — older mechanism/model/bootstrap stack.
- `V*` — validation and runtime audit surfaces.

## Current Rule

Do not activate a blocked or deferred milestone from momentum. On the current
stack:

- `H25` is active operational routing.
- `H23` is frozen scientific evidence.
- `R32` comes before deferred `R33`.
- `R29`, `F3`, and any broader frontier move remain blocked without a later
  explicit packet.
