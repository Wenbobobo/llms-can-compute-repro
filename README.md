# llms-can-compute-repro

Careful reproduction of a narrow execution-substrate reading of Percepta's
_Can LLMs Be Computers?_ field note.

The repository does not target a general "LLMs are computers" claim. The
current closed question is narrower: one restricted typed stack-bytecode
lowering surface and its lowered trace-VM execution remain exact on a fixed
five-row compiled-boundary suite, but that result still does not justify a
fast-path or broader systems-value claim.

## Current Stage

As of `2026-03-25`, the current active packet is
`H54_post_r58_r59_compiled_boundary_decision_packet`.

Current anchors:

- active docs-only packet:
  `H54_post_r58_r59_compiled_boundary_decision_packet`
- preserved prior docs-only closeout:
  `H52_post_r55_r56_r57_origin_mechanism_decision_packet`
- preserved prior compiled-boundary reentry packet:
  `H53_post_h52_compiled_boundary_reentry_packet`
- current planning bundle:
  `F29_post_h52_restricted_compiled_boundary_bundle`
- current low-priority operational/docs wave:
  `P38_post_h52_compiled_boundary_hygiene_sync`
- completed lowering gate under the current compiled-boundary lane:
  `R58_origin_restricted_stack_bytecode_lowering_contract_gate`
- completed execution gate under the current compiled-boundary lane:
  `R59_origin_compiled_trace_vm_execution_gate`
- current downstream scientific lane:
  `no_active_downstream_runtime_lane`
- preserved paper-grade endpoint:
  `H43_post_r44_useful_case_refreeze`
- preserved routing/refreeze packet:
  `H36_post_r40_bounded_scalar_family_refreeze`

The current planning bundle is
`F29_post_h52_restricted_compiled_boundary_bundle`. `H54` closes the current
compiled-boundary lane as
`freeze_restricted_compiled_boundary_supported_narrowly_without_fastpath_value`:
landed `R58` keeps exact source/spec/lowered parity on `5/5` fixed typed
stack-bytecode rows, and landed `R59` keeps exact lowered execution on those
same `5/5` rows across both linear and accelerated internal routes. The repo
therefore returns to no active downstream runtime lane without authorizing
arbitrary `C`, broad Wasm, or a general compiler-systems claim.

## Current Order

- completed mainline:
  `F29 -> H53 -> R58 -> R59 -> H54`
- sidecar:
  `P38`

## Execution Posture

There are no remaining runtime or docs-only execution tasks on this closed
wave. This branch is now a preserved closeout surface. The next meaningful
step is a new explicit planning packet in a successor worktree, not more
compiled-boundary execution on this branch.

## Current Scope

The closed wave is limited to:

1. landed planning-only `F29` routing for one restricted compiled-boundary
   lane;
2. landed docs-only `H53` authorization through `R58` only;
3. landed exact `R58` typed stack-bytecode lowering evidence;
4. landed exact `R59` lowered trace-VM execution evidence; and
5. landed docs-only `H54` compiled-boundary closeout.

Still blocked:

- `F27_post_h50_bounded_trainable_or_transformed_executor_entry_bundle`
- `R53_origin_transformed_executor_entry_gate`
- `R54_origin_trainable_executor_comparator_gate`
- arbitrary `C`
- broad Wasm claims
- merge back to dirty root `main`

Raw row dumps and artifacts above roughly `10 MiB` stay out of git by default
on the active wave.

## Read First

- `docs/publication_record/current_stage_driver.md`
- `tmp/active_wave_plan.md`
- `docs/plans/2026-03-25-post-h52-restricted-compiled-boundary-reentry-master-plan.md`
- `results/F29_post_h52_restricted_compiled_boundary_bundle/summary.json`
- `results/H52_post_r55_r56_r57_origin_mechanism_decision_packet/summary.json`
- `results/H53_post_h52_compiled_boundary_reentry_packet/summary.json`
- `results/R58_origin_restricted_stack_bytecode_lowering_contract_gate/summary.json`
- `results/R59_origin_compiled_trace_vm_execution_gate/summary.json`
- `results/H54_post_r58_r59_compiled_boundary_decision_packet/summary.json`
- `results/P38_post_h52_compiled_boundary_hygiene_sync/summary.json`

Older milestone and plan inventories remain in the repository as historical
records. When historical prose conflicts with current routing, trust the files
above.
