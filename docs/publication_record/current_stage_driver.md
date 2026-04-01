# Current Stage Driver

## Active Driver

The current active stage is:

- `H65_post_p66_p67_p68_archive_first_terminal_freeze_packet`

The current successor publication review wave is:

- `P66_post_p65_successor_publication_review`

The current published successor freeze wave is:

- `P67_post_p66_published_successor_freeze`

The current release hygiene and control rebaseline wave is:

- `P68_post_p67_release_hygiene_and_control_rebaseline`

The current published clean descendant branch is:

- `wip/p66-post-p65-published-successor-freeze`

The current docs router is:

- `docs/README.md`

The current branch/worktree registry is:

- `docs/branch_worktree_registry.md`

The preserved prior successor stack is:

- `P63_post_p62_published_successor_promotion_prep`
- `P64_post_p63_release_hygiene_rebaseline`
- `P65_post_p64_merge_prep_control_sync`

The preserved prior published clean-descendant branch is:

- `wip/p63-post-p62-tight-core-hygiene`

The preserved prior successor review branch is:

- `wip/p64-post-p63-successor-stack`

The preserved older published clean-descendant stack is:

- `P60_post_p59_published_clean_descendant_promotion_prep`
- `P61_post_p60_release_hygiene_rebaseline`
- `P62_post_p61_merge_prep_control_sync`

The preserved local integration branch is:

- `wip/p56-main-scratch`

The landed `H64` follow-through foundation is:

- `P56_post_h64_clean_merge_candidate_packet`
- `P57_post_h64_paper_submission_package_sync`
- `P58_post_h64_archive_release_closeout_sync`
- `P59_post_h64_control_and_handoff_sync`

The preserved prior active packet is:

- `H64_post_p53_p54_p55_f38_archive_first_freeze_packet`

The current dormant future dossier is:

- `F38_post_h62_r63_dormant_eligibility_profile_dossier`

The default downstream lane is:

- `explicit_archive_stop_or_hygiene_only`

## Current Machine-State Meaning

- `P56/P57/P58/P59` remain the landed follow-through foundation under the
  preserved `H64` packet.
- `P66` reviews the exact `p63..p64` successor delta and keeps the publication
  decision scoped to docs/export/control/release surfaces.
- `P67` promotes `wip/p66-post-p65-published-successor-freeze` into the live
  published clean descendant above the preserved `P63/P64/P65` stack.
- `P68` reanchors release hygiene, preflight, archive-ready posture, and
  current control on `wip/p66-post-p65-published-successor-freeze` while
  expecting `clean_worktree_ready_if_other_gates_green`.
- `wip/p63-post-p62-tight-core-hygiene` is preserved as the prior published
  clean descendant, not the live control branch.
- `wip/p64-post-p63-successor-stack` is preserved as the reviewed
  pre-publication successor lane, not the live control branch.
- `docs/README.md` and `docs/branch_worktree_registry.md` separate live routing
  from preserved history and quarantine posture.
- merge posture remains `clean_descendant_only_never_dirty_root_main`.
- dirty root `main` remains quarantine-only.
- `F38` records the only surviving future family as a dormant no-go dossier and
  leaves the key cost-profile fields unresolved.
- `H65` is the current active docs-only packet and selects
  `archive_first_terminal_freeze_becomes_current_active_route_and_defaults_to_explicit_stop`.
- explicit archive stop or hygiene-only follow-through remains the default live
  route.
