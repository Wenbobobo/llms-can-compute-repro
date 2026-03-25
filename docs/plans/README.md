# Plans Index

This directory stores planning-only design documents, unattended master plans,
and packet-specific handoff notes. Plans are routing aids, not claim-bearing
evidence. When a plan conflicts with landed artifacts, trust the current stage
driver and machine-readable `results/` summaries first.

## Current Start Points

- `2026-03-25-post-h54-useful-kernel-closeout-analysis.md`
  closeout analysis comparing `R60/R61` against prior value-negative lanes
- `2026-03-25-post-h54-useful-kernel-stopgo-design.md`
  preserved successor design for the now-closed post-`H54` stop/go packet
- `2026-03-25-post-h52-restricted-compiled-boundary-reentry-master-plan.md`
  preserved master plan for the now-closed compiled-boundary wave
- `../milestones/H56_post_r60_r61_useful_kernel_decision_packet/`
  current active docs-only closeout packet
- `../milestones/F30_post_h54_useful_kernel_bridge_bundle/`
  preserved planning-only bundle that fixed `H55 -> R60 -> R61 -> H56`
- `../milestones/P39_post_h54_successor_worktree_hygiene_sync/`
  aligned low-priority hygiene sidecar for the closed wave

## Current Route

- mainline:
  `F30 -> H55 -> R60 -> R61 -> H56`
- sidecar:
  `P39`

Blocked by default:

- `F27`
- `R53`
- `R54`

## Preserved Historical Plans

- `2026-03-25-post-h50-origin-mechanism-reentry-master-plan.md`
  preserved design for the completed `F28 -> H51 -> R55 -> R56 -> R57 -> H52`
  wave
- `2026-03-24-post-h49-origin-core-next-wave-design.md`
  preserved design for the completed `F26 -> R51 -> R52 -> H50` wave
- `2026-03-24-post-h47-p35-f23-mainline-extension-master-plan.md`
  preserved useful-case extension plan from the earlier `H47` stage
- `2026-03-24-post-h43-mainline-reentry-master-plan.md`
  preserved post-`H43` exact-first reentry plan
- `2026-03-21-h18-unattended-mainline-master-plan.md`
  broad unattended historical master plan from the earlier mainline program

## Use With

- `../publication_record/current_stage_driver.md`
- `../../tmp/active_wave_plan.md`
- `2026-03-25-post-h54-useful-kernel-closeout-analysis.md`
- `../milestones/F30_post_h54_useful_kernel_bridge_bundle/`
- `../milestones/H56_post_r60_r61_useful_kernel_decision_packet/`
- `../milestones/P39_post_h54_successor_worktree_hygiene_sync/`
- `../../results/F30_post_h54_useful_kernel_bridge_bundle/summary.json`
- `../../results/H56_post_r60_r61_useful_kernel_decision_packet/summary.json`
- `../../results/P39_post_h54_successor_worktree_hygiene_sync/summary.json`
- `../milestones/F29_post_h52_restricted_compiled_boundary_bundle/`
- `../milestones/H54_post_r58_r59_compiled_boundary_decision_packet/`
- `../milestones/P38_post_h52_compiled_boundary_hygiene_sync/`
- `../../results/F29_post_h52_restricted_compiled_boundary_bundle/summary.json`
- `../../results/H54_post_r58_r59_compiled_boundary_decision_packet/summary.json`
- `../../results/P38_post_h52_compiled_boundary_hygiene_sync/summary.json`

Historical design files remain useful for lineage reconstruction, but they are
not the live control surface for the current wave.
