# Current Stage Driver

## Active Driver

The current active stage is:

- `H64_post_p53_p54_p55_f38_archive_first_freeze_packet`

The current published clean-descendant promotion-prep wave is:

- `P60_post_p59_published_clean_descendant_promotion_prep`

The current release hygiene rebaseline wave is:

- `P61_post_p60_release_hygiene_rebaseline`

The current merge-prep control sync wave is:

- `P62_post_p61_merge_prep_control_sync`

The current published clean descendant branch is:

- `wip/p60-post-p59-published-clean-descendant-prep`

The current docs router is:

- `docs/README.md`

The current branch/worktree registry is:

- `docs/branch_worktree_registry.md`

The preserved local integration branch is:

- `wip/p56-main-scratch`

The landed `H64` follow-through foundation is:

- `P56_post_h64_clean_merge_candidate_packet`
- `P57_post_h64_paper_submission_package_sync`
- `P58_post_h64_archive_release_closeout_sync`
- `P59_post_h64_control_and_handoff_sync`

The preserved prior active packet is:

- `H63_post_p50_p51_p52_f38_archive_first_closeout_packet`

The current dormant future dossier is:

- `F38_post_h62_r63_dormant_eligibility_profile_dossier`

The default downstream lane is:

- `archive_or_hygiene_stop`

## Current Machine-State Meaning

- `P56/P57/P58/P59` remain the landed follow-through foundation under `H64`.
- `P60` locks a dedicated published clean descendant on
  `wip/p60-post-p59-published-clean-descendant-prep` while preserving
  `wip/p56-main-scratch` as the absorbed local integration base only.
- the current local hygiene-first successor branch is
  `wip/p63-post-p62-tight-core-hygiene`; it is a successor execution lane, not
  a new published milestone by itself.
- `P61` reanchors release hygiene on the published descendant and expects
  `clean_worktree_ready_if_other_gates_green` before any outward release sync.
- `P62` keeps the driver, indexes, active-wave file, and next handoff in sync
  with the published clean-descendant stack.
- `docs/README.md` and `docs/branch_worktree_registry.md` now separate live
  routing from preserved history and local cleanup posture.
- merge posture remains `clean_descendant_only_never_dirty_root_main`.
- dirty root `main` remains quarantine-only.
- `F38` records the only surviving future family as a dormant no-go dossier and
  leaves the key cost-profile fields unresolved.
- `H64` is now the current active docs-only packet and selects
  `archive_first_freeze_becomes_current_active_route_and_r63_remains_dormant`.
- archive-first freeze remains the active route.
