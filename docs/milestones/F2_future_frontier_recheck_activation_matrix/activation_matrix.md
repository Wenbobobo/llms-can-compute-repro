# Activation Matrix

`F2` is planning-only. It does not authorize any widened run by itself. The
matrix below exists so a later agent can decide whether frontier review is even
plan-worthy without rereading the full `H19 -> H25` packet.

## Trigger Matrix

| Condition | Current `H25` active / `H23` frozen state | Required for any future frontier-plan draft | Why it still matters |
| --- | --- | --- | --- |
| Same-endpoint evidence chain is coherent | satisfied | keep satisfied | `H19`, `H21`, `H23`, and `H25` now describe one bounded `D0` story rather than conflicting partial follow-ups |
| Mechanism story is claim-relevant on the current endpoint | satisfied | keep satisfied | `R20` and `R28` keep the retrieval/mechanism story claim-relevant without widening beyond the admitted same-endpoint evidence |
| True executor boundary is localized | not satisfied | `R32` or a later explicit same-endpoint follow-up would need to expose one reproducible family-local `first_fail` with neighboring exact rows, or a stronger principled contradiction than the current no-localization state | `H23` still ends at `bounded_grid_still_not_localized`, and `R30` authorizes one more family-local sharp zoom rather than frontier widening |
| Current-scope systems story is materially positive | not satisfied | `R33` or a later explicit same-endpoint systems packet would need to move the systems story materially positive on the same endpoint first, with `R29` staying blocked unless a later explicit packet reauthorizes it | `R23` still ends at `systems_still_mixed`, and `R31` routes the next justified systems work through a narrower non-retrieval audit while keeping `R29` blocked |
| Scope-lift thesis is explicitly re-authorized | not satisfied | a later refreeze would need to replace the standing no-widening state with an explicit new decision | `H25` keeps `F3` blocked and planning-only; planning notes are not authorization |
| The active downstream same-endpoint order is exhausted or explicitly superseded | not satisfied | the currently justified `R32 -> deferred R33 -> blocked R29/F3` order must either finish or be replaced by a later explicit packet | `F2` must not be used to skip over the still-open same-endpoint follow-up sequence |

## Non-goals

- Do not treat `R30` authorizing `R32` as implicit authorization for frontier
  review, scope lift, or endpoint widening.
- Do not treat `R31` or a future `R33` attribution audit as if the systems
  story is already materially positive.
- Do not restate a planning matrix as if it were a landed experimental result.
- Do not use `F2` to backdoor a broader “LLMs are computers” claim.

## Minimum Evidence Bundle

Any later frontier-plan draft should require, at minimum:

1. the preserved refreeze/decision chain
   `results/H17_refreeze_and_conditional_frontier_recheck/summary.json`,
   `results/H18_post_h17_mainline_reopen_guard/summary.json`,
   `results/H19_refreeze_and_next_scope_decision/summary.json`,
   `results/H21_refreeze_after_r22_r23/summary.json`,
   `results/H23_refreeze_after_r26_r27_r28/summary.json`, and
   `results/H25_refreeze_after_r30_r31_decision_packet/summary.json`;
2. the landed same-endpoint packet
   `results/R19_d0_pointer_like_surface_generalization_gate/summary.json`,
   `results/R20_d0_runtime_mechanism_ablation_matrix/summary.json`, and
   `results/R21_d0_exact_executor_boundary_break_map/summary.json`;
3. the landed post-`H19` and post-`H21` follow-up packets
   `results/H20_post_h19_mainline_reentry_and_hygiene_split/summary.json`,
   `results/H22_post_h21_boundary_reopen_and_dual_track_lock/summary.json`,
   `results/R22_d0_true_boundary_localization_gate/summary.json`,
   `results/R23_d0_same_endpoint_systems_overturn_gate/summary.json`, and
   `results/R26_d0_boundary_localization_execution_gate/summary.json`,
   `results/R27_d0_boundary_localization_extension_gate/summary.json`,
   `results/R28_d0_trace_retrieval_contract_audit/summary.json`,
   `results/R30_d0_boundary_reauthorization_packet/summary.json`, and
   `results/R31_d0_same_endpoint_systems_recovery_reauthorization_packet/summary.json`;
4. the current downstream planning manifests
   `docs/milestones/R32_d0_family_local_boundary_sharp_zoom/execution_manifest.md`,
   `docs/milestones/R33_d0_non_retrieval_overhead_localization_audit/component_localization_manifest.md`,
   and `docs/milestones/F3_post_h23_scope_lift_decision_bundle/decision_gate.md`;
5. the standing no-widening controls
   `results/M7_frontend_candidate_decision/decision_summary.json`;
6. the standing mixed systems gate
   `results/R2_systems_baseline_gate/summary.json` and
   `results/E1b_systems_patch/summary.json`.

## Smallest Acceptable Widened-Probe Shape

If a later explicit plan ever becomes justified, the first widened probe should
still be narrower than a new frontend:

- one explicitly named contradiction or gap tied back to the
  `H23/H25` unsupported or disconfirmed rows, not a broad exploratory sweep;
- one small comparator set tied back to the current blocked same-endpoint
  sequence rather than a new endpoint family;
- one fixed success/failure criterion decided before execution;
- one explicit stop condition that prevents an open-ended repair loop.
