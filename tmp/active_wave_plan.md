# Active Wave Plan

## Current Wave

Current scientific/control stack:

- current active docs-only decision packet:
  `H54_post_r58_r59_compiled_boundary_decision_packet`;
- preserved prior docs-only closeout:
  `H52_post_r55_r56_r57_origin_mechanism_decision_packet`;
- preserved prior compiled-boundary reentry packet:
  `H53_post_h52_compiled_boundary_reentry_packet`;
- preserved prior paper-grade endpoint:
  `H43_post_r44_useful_case_refreeze`;
- preserved active routing/refreeze packet:
  `H36_post_r40_bounded_scalar_family_refreeze`;
- current planning bundle:
  `F29_post_h52_restricted_compiled_boundary_bundle`;
- current low-priority operational/docs wave:
  `P38_post_h52_compiled_boundary_hygiene_sync`;
- completed lowering gate under the current compiled-boundary lane:
  `R58_origin_restricted_stack_bytecode_lowering_contract_gate`;
- completed execution gate under the current compiled-boundary lane:
  `R59_origin_compiled_trace_vm_execution_gate`;
- current downstream scientific lane:
  `no_active_downstream_runtime_lane`;
- blocked future storage:
  `F27_post_h50_bounded_trainable_or_transformed_executor_entry_bundle`,
  `R53_origin_transformed_executor_entry_gate`, and
  `R54_origin_trainable_executor_comparator_gate`.

Immediate active wave:

`F29_post_h52_restricted_compiled_boundary_bundle` remains the preserved
planning bundle that fixed `H53 -> R58 -> R59 -> H54` as the only admissible
order.

`H53_post_h52_compiled_boundary_reentry_packet` remains the preserved prior
compiled-boundary reentry packet. It selected
`authorize_compiled_boundary_reentry_through_r58_first` and kept `H52`
visible rather than overturning it.

`P38_post_h52_compiled_boundary_hygiene_sync` remains the current low-priority
operational/docs wave. It keeps the clean control worktree, descendant
execution worktrees, raw row dumps and artifacts above roughly `10 MiB`
out-of-git by default, and explicit no-merge posture for this wave. No merge
back to `main` occurs during this wave.

`R58_origin_restricted_stack_bytecode_lowering_contract_gate` is completed
with `restricted_stack_bytecode_lowering_supported_narrowly` on `5/5` fixed
compiled-boundary rows and exact source/spec/lowered parity.

`R59_origin_compiled_trace_vm_execution_gate` is completed with
`compiled_trace_vm_execution_supported_exactly` on `5/5` exact `R58` rows
across both linear and accelerated internal routes.

`H54_post_r58_r59_compiled_boundary_decision_packet` is now the current active
packet and selects
`freeze_restricted_compiled_boundary_supported_narrowly_without_fastpath_value`.

## Immediate Objectives

1. Preserve `H52` as a landed prior mechanism fast-path-value closeout.
2. Preserve `H43` as the paper-grade endpoint.
3. Preserve `H36` as the routing/refreeze packet underneath the current stack.
4. Preserve `H53` as the explicit reentry authorization history.
5. Preserve `R58` as completed exact compiled-boundary lowering evidence only.
6. Preserve `R59` as completed exact compiled-boundary execution evidence only.
7. Keep `H54` as the current docs-only closeout packet.
8. Keep the downstream scientific lane at `no_active_downstream_runtime_lane`.
9. Keep `F27`, `R53`, and `R54` blocked.
10. Keep dirty root `main` out of scope for scientific execution.
11. Keep raw row dumps and artifacts above roughly `10 MiB` out of git by
    default.

## Current Order

Completed forward order:

`F29_post_h52_restricted_compiled_boundary_bundle` ->
`H53_post_h52_compiled_boundary_reentry_packet` ->
`R58_origin_restricted_stack_bytecode_lowering_contract_gate` ->
`R59_origin_compiled_trace_vm_execution_gate` ->
`H54_post_r58_r59_compiled_boundary_decision_packet`

Low-priority sidecar:

`P38_post_h52_compiled_boundary_hygiene_sync`

## Current Rule

- `H54` is the current active docs-only packet.
- `H52` is preserved prior closeout and remains scientifically binding.
- `H53` is preserved prior compiled-boundary reentry history.
- `F29` is the preserved planning bundle.
- `P38` is the current low-priority operational/docs wave.
- `R58` is the completed exact compiled-boundary lowering gate.
- `R59` is the completed exact compiled-boundary execution gate.
- `no_active_downstream_runtime_lane` is the current downstream lane state.
- `F27`, `R53`, and `R54` remain blocked.
- no merge back to `main` occurs during this wave.

## Execution Posture

- This wave is already closed at `H54`.
- No remaining runtime gate or docs-only packet is pending on this branch.
- If later work is authorized, it must start from a new planning packet rather
  than by extending this closed compiled-boundary lane.

## Control References

- `docs/publication_record/current_stage_driver.md`
- `docs/plans/2026-03-25-post-h52-restricted-compiled-boundary-reentry-master-plan.md`
- `docs/milestones/F29_post_h52_restricted_compiled_boundary_bundle/`
- `docs/milestones/H53_post_h52_compiled_boundary_reentry_packet/`
- `docs/milestones/H54_post_r58_r59_compiled_boundary_decision_packet/`
- `docs/milestones/P38_post_h52_compiled_boundary_hygiene_sync/`
- `docs/milestones/R58_origin_restricted_stack_bytecode_lowering_contract_gate/`
- `docs/milestones/R59_origin_compiled_trace_vm_execution_gate/`
- `results/F29_post_h52_restricted_compiled_boundary_bundle/summary.json`
- `results/H52_post_r55_r56_r57_origin_mechanism_decision_packet/summary.json`
- `results/H53_post_h52_compiled_boundary_reentry_packet/summary.json`
- `results/H54_post_r58_r59_compiled_boundary_decision_packet/summary.json`
- `results/P38_post_h52_compiled_boundary_hygiene_sync/summary.json`
- `results/R58_origin_restricted_stack_bytecode_lowering_contract_gate/summary.json`
- `results/R59_origin_compiled_trace_vm_execution_gate/summary.json`
