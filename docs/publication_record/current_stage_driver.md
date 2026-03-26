# Current Stage Driver

## Active Driver

The current active stage is:

- `H63_post_p50_p51_p52_f38_archive_first_closeout_packet`

The preserved prior active packet is:

- `H62_post_p47_p48_p49_f37_hygiene_first_scope_decision_packet`

The current control sync wave is:

- `P50_post_h62_archive_first_control_sync`

The current paper-facing package wave is:

- `P51_post_h62_paper_facing_partial_falsification_package`

The current repo hygiene sidecar is:

- `P52_post_h62_clean_descendant_hygiene_and_merge_prep`

The current dormant future dossier is:

- `F38_post_h62_r63_dormant_eligibility_profile_dossier`

The default downstream lane is:

- `archive_or_hygiene_stop`

## Current Machine-State Meaning

- `P50` locks root and control surfaces to the post-`H62` archive-first
  closeout state.
- `P51` locks paper/review/archive wording to archive-first partial
  falsification.
- `P52` keeps clean-descendant-only hygiene and merge-prep explicit while dirty
  root `main` remains quarantined.
- merge posture remains `clean_descendant_only_never_dirty_root_main`.
- `F38` records the only surviving future family as a dormant no-go dossier and
  leaves the key cost-profile fields unresolved.
- `H63` is now the current active docs-only packet and selects
  `archive_first_closeout_becomes_current_active_route_and_r63_stays_dormant`.
- archive-first closeout is now the active route.
