# Active Wave Plan

## Current Wave

Current scientific/control stack:

- current active docs-only packet:
  `H64_post_p53_p54_p55_f38_archive_first_freeze_packet`;
- current clean merge-candidate packet:
  `P56_post_h64_clean_merge_candidate_packet`;
- current paper/submission package sync wave:
  `P57_post_h64_paper_submission_package_sync`;
- current archive/release closeout sync wave:
  `P58_post_h64_archive_release_closeout_sync`;
- current control/handoff sync wave:
  `P59_post_h64_control_and_handoff_sync`;
- preserved prior active docs-only packet:
  `H63_post_p50_p51_p52_f38_archive_first_closeout_packet`;
- current dormant future dossier:
  `F38_post_h62_r63_dormant_eligibility_profile_dossier`;
- default downstream lane:
  `archive_or_hygiene_stop`;
- only conditional later gate:
  `r63_post_h62_coprocessor_eligibility_profile_gate`.

Immediate active wave:

`P59_post_h64_control_and_handoff_sync` is the current control sync wave while
`H64_post_p53_p54_p55_f38_archive_first_freeze_packet` remains the current
active docs-only packet.

## Execution Closeout Status

- the current clean descendant line now carries `P56/P57/P58/P59` above `H64`;
- the current local integration branch is `wip/p56-main-scratch`;
- the former local merge-candidate branch
  `wip/p56-post-h64-clean-merge-candidate` has been absorbed and removed
  locally;
- standing release/archive audits now read the `H64` state directly;
- `release_preflight_checklist_audit` is green;
- `P10_submission_archive_ready` is green;
- the active clean descendant branch remains merge-prep only; and
- there is no remaining open execution-side runtime wave under the current
  `H64` packet.
