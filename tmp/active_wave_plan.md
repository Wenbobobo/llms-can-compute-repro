# Active Wave Plan

## Current Wave

Current scientific/control stack:

- current active docs-only decision packet:
  `H37_post_h36_runtime_relevance_decision_packet`;
- preserved prior active routing/refreeze packet:
  `H36_post_r40_bounded_scalar_family_refreeze`;
- completed operational promotion-prep lane:
  `P25_post_h36_clean_promotion_prep`;
- current canonical origin-facing derivative bundle:
  `F15_post_h36_origin_goal_reanchor_bundle`;
- preserved prior docs-only control packet:
  `H35_post_p23_bounded_scalar_family_runtime_decision_packet`;
- preserved prior docs-only sync packet:
  `P24_post_h36_bounded_scalar_runtime_sync`;
- preserved earlier no-runtime interpretation packet:
  `H34_post_r39_later_explicit_scope_decision_packet`;
- preserved earlier compiled-boundary refreeze packet:
  `H32_post_r38_compiled_boundary_refreeze`;
- preserved later explicit packet:
  `H31_post_h30_later_explicit_boundary_decision_packet`;
- preserved prior compiled-boundary refreeze packet:
  `H30_post_r36_r37_scope_decision_packet`;
- preserved Origin-core refreeze packet:
  `H29_refreeze_after_r34_r35_origin_core_gate`;
- preserved same-endpoint closeout packet:
  `H27_refreeze_after_r32_r33_same_endpoint_decision`;
- preserved upstream primitive gate:
  `R34_origin_retrieval_primitive_contract_gate`;
- preserved upstream execution gate:
  `R35_origin_append_only_stack_vm_execution_gate`;
- preserved narrow precision lane:
  `R36_origin_long_horizon_precision_scaling_gate`;
- preserved tiny compiled-boundary lane:
  `R37_origin_compiler_boundary_gate`;
- preserved richer control-surface extension lane:
  `R38_origin_compiler_control_surface_extension_gate`;
- preserved same-substrate dependency audit lane:
  `R39_origin_compiler_control_surface_dependency_audit`;
- completed bounded-scalar runtime lane:
  `R40_origin_bounded_scalar_locals_and_flags_gate`;
- deferred future runtime blueprint:
  `R41_origin_runtime_relevance_threat_stress_audit`;
- blocked future lanes:
  `R29_d0_same_endpoint_systems_recovery_execution_gate` and
  `F3_post_h23_scope_lift_decision_bundle`.

Immediate active wave:

`H37` keeps the `H36` bounded-scalar freeze, `P25` records clean promotion
prep, `F15` becomes the current canonical derivative bundle, and there is no
active downstream runtime lane.

## Current Facts

- `wip/h35-r40-p24-exec` remains the scientific source of truth for the landed
  `H35 -> R40 -> H36 -> P24` wave.
- `wip/p25-f15-h37-exec` is the clean promotion-prep branch created from that
  source state.
- dirty `main` remains untouched by design in this wave.
- `H34` preserves
  `freeze_compiled_boundary_as_complete_for_now` as the earlier same-substrate
  no-reopen interpretation.
- `H35` authorizes exactly one bounded-scalar same-substrate runtime gate.
- `R40` validates explicit bounded frame locals plus typed `FLAG` slots on one
  admitted row and one same-family boundary row while rejecting the declared
  negatives.
- `H36` freezes that result narrowly and restores
  `no_active_downstream_runtime_lane`.
- `F14` preserves only two surviving same-substrate cautions, and no candidate
  is yet uniquely isolated strongly enough to justify a reopen packet.
- `F15` records the bounded-scalar family as `supported_here` narrowly and
  ranks the two `F14` runtime-relevance cautions as the top unresolved
  same-substrate gaps.
- `H37` selects `keep_h36_freeze` and keeps `R41` deferred.

## Immediate Objectives

1. Preserve `H37` as the current active docs-only decision packet.
2. Preserve `H36` as the prior active routing/refreeze packet.
3. Preserve `P25` as `prepare_only`, not merge authorization.
4. Preserve `F15` as the current canonical derivative bundle.
5. Preserve `R40` as narrow same-substrate evidence for explicit bounded frame
   locals plus typed `FLAG` slots only.
6. Keep `R41` deferred until a later explicit post-`H37` packet authorizes it.
7. Avoid reopening `R29`, `F3`, broader compiler/demo scope, or frontier
   widening by momentum.

## Last Completed Order

Immediate completed order:

`P16_h25_commit_hygiene_and_clean_worktree_promotion` ->
clean-worktree `R32_d0_family_local_boundary_sharp_zoom` ->
`H26_refreeze_after_r32_boundary_sharp_zoom` ->
clean-worktree `R33_d0_non_retrieval_overhead_localization_audit` ->
`H27_refreeze_after_r32_r33_same_endpoint_decision` ->
`H28_post_h27_origin_core_reanchor_packet` ->
`R34_origin_retrieval_primitive_contract_gate` ->
`R35_origin_append_only_stack_vm_execution_gate` ->
`H29_refreeze_after_r34_r35_origin_core_gate` ->
`R36_origin_long_horizon_precision_scaling_gate` ->
`R37_origin_compiler_boundary_gate` ->
`H30_post_r36_r37_scope_decision_packet` ->
`H31_post_h30_later_explicit_boundary_decision_packet` ->
`R38_origin_compiler_control_surface_extension_gate` ->
`H32_post_r38_compiled_boundary_refreeze` ->
`H33_post_h32_conditional_next_question_packet` ->
`R39_origin_compiler_control_surface_dependency_audit` ->
`H34_post_r39_later_explicit_scope_decision_packet` ->
`H35_post_p23_bounded_scalar_family_runtime_decision_packet` ->
`R40_origin_bounded_scalar_locals_and_flags_gate` ->
`H36_post_r40_bounded_scalar_family_refreeze` ->
`P25_post_h36_clean_promotion_prep` ->
`F15_post_h36_origin_goal_reanchor_bundle` ->
`H37_post_h36_runtime_relevance_decision_packet`

## Next Conditional Order

no active downstream runtime lane

If reauthorized later:

later explicit post-`H37` packet ->
conditional `R41_origin_runtime_relevance_threat_stress_audit` ->
later refreeze packet

## Current References

- `docs/plans/2026-03-23-post-h36-p25-f15-h37-control-design.md`
- `docs/plans/2026-03-23-post-h36-r41-runtime-relevance-threat-design.md`
- `docs/milestones/P25_post_h36_clean_promotion_prep/`
- `docs/milestones/F15_post_h36_origin_goal_reanchor_bundle/`
- `docs/milestones/H37_post_h36_runtime_relevance_decision_packet/`
- `docs/milestones/H36_post_r40_bounded_scalar_family_refreeze/`
- `docs/milestones/H35_post_p23_bounded_scalar_family_runtime_decision_packet/`
- `docs/milestones/R40_origin_bounded_scalar_locals_and_flags_gate/`
- `docs/milestones/R41_origin_runtime_relevance_threat_stress_audit/`
- `results/P25_post_h36_clean_promotion_prep/summary.json`
- `results/H37_post_h36_runtime_relevance_decision_packet/summary.json`
- `results/H36_post_r40_bounded_scalar_family_refreeze/summary.json`
- `results/R40_origin_bounded_scalar_locals_and_flags_gate/summary.json`
- `docs/publication_record/current_stage_driver.md`
- `tmp/active_wave_plan.md`

## If Blocked

- do not merge back into dirty `main` by momentum;
- do not treat `P25` as merge authorization;
- do not treat `H37` as authorization to execute `R41`;
- do not reopen `R29` or `F3` by wording alone;
- do not treat `F15`, `F14`, or the saved `R41` design surface as automatic
  runtime authorization;
- require a later explicit packet before any future same-substrate reopen or
  routing/scope change.
