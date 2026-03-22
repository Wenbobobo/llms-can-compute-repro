# Plans Index

This directory stores planning-only design documents, unattended master plans,
and packet-specific handoff notes. These files are routing aids, not
claim-bearing evidence. When a plan and a landed result differ, trust the
current stage driver, the milestone/result artifacts, and the machine-readable
`results/` summaries first.

## Current Start Points

- `2026-03-22-post-unattended-r32-mainline-design.md` — the current next-stage
  operational/science handoff: `P16` clean-worktree closeout first, `R32`
  second, `H26` third, then only conditional `R33/H27`.
- `2026-03-21-h18-unattended-mainline-master-plan.md` — broad unattended
  master plan for the mainline reproduction program.
- `2026-03-22-post-h23-reauthorization-design.md` — the design that landed the
  current `H24/R30/R31/H25` reauthorization/refreeze packet.
- `2026-03-22-post-h25-r32-r33-near-term-design.md` — the current near-term
  handoff for `R32` first, deferred `R33` second, with no new runtime execution
  from the current dirty integrated tree.

## Use With

- `../publication_record/current_stage_driver.md` — canonical current stage,
  routing order, and standing gates.
- `../../tmp/active_wave_plan.md` — short current-wave handoff and closeout
  notes.
- `../milestones/P16_h25_commit_hygiene_and_clean_worktree_promotion/` —
  immediate operational closeout lane before any new runtime batch.
- `../milestones/R32_d0_family_local_boundary_sharp_zoom/execution_manifest.md`
  — first-pass `R32` execution manifest.
- `../milestones/R33_d0_non_retrieval_overhead_localization_audit/component_localization_manifest.md`
  — first-pass `R33` audit manifest.

## Historical Plan Groups

- `2026-03-21-*` and `2026-03-22-*` — current post-`H19`, post-`H21`,
  post-`H23`, and post-`H25` design stack.
- `2026-03-20-*` — `H10` through `H17`, `R8` through `R18`, and release/control
  audit design set.
- `2026-03-19-*` — `H1` through `H9`, `R3` through `R7`, `P5` through `P10`,
  and early unattended governance/master-plan set.
- `2026-03-17-*` and `2026-03-18-*` — earliest bootstrap, exact hard-max,
  trainable latest-write, and first compiled-boundary planning set.

## Reading Rule

For current work, start with the newest plan in the relevant lane, then confirm
its status against:

1. `../publication_record/current_stage_driver.md`
2. `../../tmp/active_wave_plan.md`
3. the corresponding milestone `README.md` / `status.md`
4. the corresponding `results/<lane>/summary.json`

Do not treat an older plan as authorization to reopen a blocked lane.
