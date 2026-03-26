# Active Wave Plan

## Current Wave

Current scientific/control stack:

- current active docs-only packet:
  `H62_post_p47_p48_p49_f37_hygiene_first_scope_decision_packet`;
- preserved prior active docs-only packet:
  `H61_post_h60_archive_first_position_packet`;
- preserved prior active-before-that packet:
  `H60_post_f34_next_lane_decision_packet`;
- preserved prior reproduction-gap packet:
  `H59_post_h58_reproduction_gap_decision_packet`;
- preserved prior docs-only closeout:
  `H58_post_r62_origin_value_boundary_closeout_packet`;
- preserved prior closeout certification:
  `F32_post_h58_closeout_certification_bundle`;
- preserved prior paper-grade endpoint:
  `H43_post_r44_useful_case_refreeze`;
- preserved active routing/refreeze packet:
  `H36_post_r40_bounded_scalar_family_refreeze`;
- current reauthorization bundle:
  `F37_post_h61_compiled_online_coprocessor_reauthorization_bundle`;
- current Origin advisory sync wave:
  `P49_post_h61_origin_advisory_sync`;
- current root-quarantine sidecar:
  `P47_post_h61_root_quarantine_and_main_merge_planning`;
- current clean-descendant promotion-prep sidecar:
  `P48_post_h61_clean_descendant_promotion_prep`;
- current publication/docs wave:
  `P46_post_h60_archive_first_publication_sync`;
- current far-future horizon log:
  `F35_post_h59_far_future_model_and_weights_horizon_log`;
- preserved prior qualification bundle:
  `F36_post_h60_conditional_compiled_online_reopen_qualification_bundle`;
- preserved prior reopen screen:
  `F34_post_h59_compiled_online_retrieval_reopen_screen`;
- preserved prior publication/docs wave:
  `P44_post_h59_publication_surface_and_claim_lock`;
- preserved prior repo-hygiene sidecar:
  `P43_post_h59_repo_graph_hygiene_and_merge_map`;
- preserved prior advisory/docs wave:
  `P42_post_h59_gptpro_reinterview_packet`;
- preserved prior publication/archive sidecar:
  `P41_post_h58_publication_and_archive_sync`;
- completed native value discriminator gate:
  `R62_origin_native_useful_kernel_value_discriminator_gate`;
- default downstream lane:
  `archive_or_hygiene_stop`;
- only conditional later gate:
  `r63_post_h62_coprocessor_eligibility_profile_gate`;
- blocked future storage:
  `F27_post_h50_bounded_trainable_or_transformed_executor_entry_bundle`,
  `R53_origin_transformed_executor_entry_gate`, and
  `R54_origin_trainable_executor_comparator_gate`.

Immediate active wave:

`H62_post_p47_p48_p49_f37_hygiene_first_scope_decision_packet` is the current
active packet and selects
`hygiene_first_scope_decision_keeps_archive_default_and_limits_any_reopen_to_r63_profile_gate`.

`F37_post_h61_compiled_online_coprocessor_reauthorization_bundle` keeps only
one future family alive on paper, narrows it to
`compiled_exact_hardmax_attention_coprocessor_on_lifted_useful_kernel_decode`,
and keeps runtime closed.

`P47_post_h61_root_quarantine_and_main_merge_planning` records the parked root
checkout as quarantine-only and keeps merge-main planning-only.

`P48_post_h61_clean_descendant_promotion_prep` makes promotion range and
oversized-artifact posture explicit before any later clean-descendant
promotion.

`P49_post_h61_origin_advisory_sync` keeps the Origin/GPTPro advisory material
available in the clean line while preserving advisory-only status.

## Immediate Objectives

1. Preserve `H43` as the current paper-grade endpoint.
2. Preserve `H58` as a real closeout rather than a staging point.
3. Preserve `H59`, `H60`, and `H61` as binding prior packets.
4. Keep the default downstream lane at `archive_or_hygiene_stop`.
5. Keep any future continuation limited to a later non-runtime `R63` profile
   gate.
6. Keep `F27`, `R53`, and `R54` blocked by default.
7. Keep dirty root `main` out of scientific execution and merge routing.
8. Keep raw row dumps and artifacts above roughly `10 MiB` out of git by
   default.

## Current Order

Completed forward order:

`F31_post_h56_final_discriminating_value_boundary_bundle` ->
`H57_post_h56_last_discriminator_authorization_packet` ->
`R62_origin_native_useful_kernel_value_discriminator_gate` ->
`H58_post_r62_origin_value_boundary_closeout_packet` ->
`F32_post_h58_closeout_certification_bundle` ->
`H59_post_h58_reproduction_gap_decision_packet` ->
`F34_post_h59_compiled_online_retrieval_reopen_screen` ->
`H60_post_f34_next_lane_decision_packet` ->
`F36_post_h60_conditional_compiled_online_reopen_qualification_bundle` ->
`H61_post_h60_archive_first_position_packet` ->
`F37_post_h61_compiled_online_coprocessor_reauthorization_bundle` ->
`H62_post_p47_p48_p49_f37_hygiene_first_scope_decision_packet`

Current sidecars and planning:

- `P41_post_h58_publication_and_archive_sync`
- `P42_post_h59_gptpro_reinterview_packet`
- `P43_post_h59_repo_graph_hygiene_and_merge_map`
- `P44_post_h59_publication_surface_and_claim_lock`
- `P45_post_h60_clean_descendant_integration_readiness`
- `P46_post_h60_archive_first_publication_sync`
- `P47_post_h61_root_quarantine_and_main_merge_planning`
- `P48_post_h61_clean_descendant_promotion_prep`
- `P49_post_h61_origin_advisory_sync`
- `F35_post_h59_far_future_model_and_weights_horizon_log`

## Current Rule

- `H62` is the current active docs-only packet.
- `H61`, `H60`, and `H59` remain preserved prior decision packets and remain
  scientifically binding.
- `H58` remains preserved prior closeout and remains scientifically binding.
- `F32` is the preserved closeout certification bundle.
- `P47` and `P48` are the active repo-hygiene sidecars.
- `P49` is the active advisory sync wave.
- `P46` remains the active publication/docs sync wave.
- `F37` is the current planning-only reauthorization bundle.
- `F35` is the current far-future horizon log.
- `R62` remains the completed native useful-kernel value discriminator gate.
- `archive_or_hygiene_stop` is the default downstream lane.
- `R63` remains conditional and non-runtime only.
- `F27`, `R53`, and `R54` remain blocked.
- no merge back to dirty root `main` occurs during this wave.

## Execution Posture

- No runtime gate is open.
- This branch is in hygiene-first archive-preserving consolidation.
- Any later scientific work must begin from a new explicit authorization
  packet, not from another same-lane executor-value probe.
- Even a later `R63` gate would remain non-runtime unless a later packet says
  otherwise.

## Control References

- `docs/publication_record/current_stage_driver.md`
- `docs/plans/2026-03-26-post-h61-hygiene-first-reauth-prep-design.md`
- `docs/plans/2026-03-25-post-h59-gptpro-reinterview-dossier.md`
- `docs/milestones/H62_post_p47_p48_p49_f37_hygiene_first_scope_decision_packet/`
- `docs/milestones/F37_post_h61_compiled_online_coprocessor_reauthorization_bundle/`
- `docs/milestones/P49_post_h61_origin_advisory_sync/`
- `docs/milestones/P48_post_h61_clean_descendant_promotion_prep/`
- `docs/milestones/P47_post_h61_root_quarantine_and_main_merge_planning/`
- `docs/milestones/P46_post_h60_archive_first_publication_sync/`
- `docs/milestones/H61_post_h60_archive_first_position_packet/`
- `results/H62_post_p47_p48_p49_f37_hygiene_first_scope_decision_packet/summary.json`
- `results/F37_post_h61_compiled_online_coprocessor_reauthorization_bundle/summary.json`
- `results/P49_post_h61_origin_advisory_sync/summary.json`
- `results/P48_post_h61_clean_descendant_promotion_prep/summary.json`
- `results/P47_post_h61_root_quarantine_and_main_merge_planning/summary.json`
- `results/P46_post_h60_archive_first_publication_sync/summary.json`
- `results/H61_post_h60_archive_first_position_packet/summary.json`
- `results/F36_post_h60_conditional_compiled_online_reopen_qualification_bundle/summary.json`
- `results/F35_post_h59_far_future_model_and_weights_horizon_log/summary.json`
- `results/H60_post_f34_next_lane_decision_packet/summary.json`
- `results/H59_post_h58_reproduction_gap_decision_packet/summary.json`
- `results/H58_post_r62_origin_value_boundary_closeout_packet/summary.json`
- `results/R62_origin_native_useful_kernel_value_discriminator_gate/summary.json`
