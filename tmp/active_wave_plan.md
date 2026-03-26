# Active Wave Plan

## Current Wave

Current scientific/control stack:

- current active docs-only packet:
  `H63_post_p50_p51_p52_f38_archive_first_closeout_packet`;
- preserved prior active docs-only packet:
  `H62_post_p47_p48_p49_f37_hygiene_first_scope_decision_packet`;
- current control sync wave:
  `P50_post_h62_archive_first_control_sync`;
- current paper-facing package wave:
  `P51_post_h62_paper_facing_partial_falsification_package`;
- current repo-hygiene sidecar:
  `P52_post_h62_clean_descendant_hygiene_and_merge_prep`;
- current dormant future dossier:
  `F38_post_h62_r63_dormant_eligibility_profile_dossier`;
- default downstream lane:
  `archive_or_hygiene_stop`;
- only conditional later gate:
  `r63_post_h62_coprocessor_eligibility_profile_gate`.

Immediate active wave:

`H63_post_p50_p51_p52_f38_archive_first_closeout_packet` is the current active
packet and selects
`archive_first_closeout_becomes_current_active_route_and_r63_stays_dormant`.

## Execution Closeout Status

- standing release/archive audits now read the `H63` state directly;
- `release_preflight_checklist_audit` is green;
- `P10_submission_archive_ready` is green;
- the clean descendant branch is published and clean; and
- there is no remaining open execution-side wave under the current `H63`
  packet.
