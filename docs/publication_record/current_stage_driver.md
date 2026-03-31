# Current Stage Driver

## Active Driver

The current active stage is:

- `H64_post_p53_p54_p55_f38_archive_first_freeze_packet`

The current clean merge-candidate packet is:

- `P56_post_h64_clean_merge_candidate_packet`

The current paper/submission package sync wave is:

- `P57_post_h64_paper_submission_package_sync`

The current archive/release closeout sync wave is:

- `P58_post_h64_archive_release_closeout_sync`

The current control/handoff sync wave is:

- `P59_post_h64_control_and_handoff_sync`

The preserved prior active packet is:

- `H63_post_p50_p51_p52_f38_archive_first_closeout_packet`

The current dormant future dossier is:

- `F38_post_h62_r63_dormant_eligibility_profile_dossier`

The default downstream lane is:

- `archive_or_hygiene_stop`

## Current Machine-State Meaning

- `P56` keeps explicit clean-descendant merge-candidate posture above `H64`
  without executing a merge.
- `P57` keeps paper-facing and submission-facing package wording synchronized
  to the current `H64 + P56/P57/P58/P59` follow-through stack.
- `P58` keeps archive-facing and release-facing closeout wording synchronized
  to the same stack.
- `P59` keeps the driver, indexes, active-wave file, and next handoff in sync
  while preserving `H64` as the active docs-only packet.
- merge posture remains `clean_descendant_only_never_dirty_root_main`.
- `F38` records the only surviving future family as a dormant no-go dossier and
  leaves the key cost-profile fields unresolved.
- `H64` is now the current active docs-only packet and selects
  `archive_first_freeze_becomes_current_active_route_and_r63_remains_dormant`.
- archive-first freeze remains the active route.
