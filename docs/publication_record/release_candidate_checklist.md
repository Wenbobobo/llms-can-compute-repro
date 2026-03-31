# Release Candidate Checklist

State: `standing_gate`.

This checklist defines the minimum outward-facing sync required for a
restrained release-candidate posture after the current
`H64_post_p53_p54_p55_f38_archive_first_freeze_packet` plus
`P56/P57/P58/P59` follow-through stack.

## Wording and scope

- [ ] `README.md` keeps the narrow endpoint and blocked non-goals explicit.
- [ ] `STATUS.md` matches active `H64`, preserved prior active `H63`, current
  `P56/P57/P58/P59/F38`, default downstream lane
  `archive_or_hygiene_stop`, and closed runtime.
- [ ] `release_summary_draft.md` remains the short public-surface source for
  archive-first partial falsification.
- [ ] No outward wording implies a new runtime lane, a same-lane replay, broad
  Wasm, arbitrary `C`, or a dirty-root-`main` merge.

## Paper-facing dependencies

- [ ] `submission_candidate_criteria.md` is satisfied on the current repo
  state.
- [ ] `paper_bundle_status.md`, `review_boundary_summary.md`,
  `publication_record/README.md`, and `current_stage_driver.md` all describe
  the same current `H64/P56/P57/P58/P59/F38` package together with preserved
  `H58/H43`.
- [ ] `submission_packet_index.md` and `archival_repro_manifest.md` present
  the same handoff: `H64` as current active packet, `P56` as clean
  merge-candidate packet, `P57` as paper/submission sync wave, `P58` as
  archive/release sync wave, `P59` as control/handoff sync wave, `F38` as the
  dormant future dossier, and `H58/H43` as preserved scientific endpoints
  underneath.
- [ ] `external_release_note_skeleton.md` stays downstream of archive-first
  partial falsification, keeps the broad headline negative, and keeps `R63`
  dormant and non-runtime only.
- [ ] The blocked-blog rule remains explicit in both `blog_release_rules.md`
  and any derivative release-note surface.

## Machine-audited guards

- [ ] `results/P1_paper_readiness/summary.json` still reports `10/10` ready
  items on the frozen scope.
- [ ] `results/H64_post_p53_p54_p55_f38_archive_first_freeze_packet/summary.json`
  reports the current active packet and archive-first closeout outcome.
- [ ] `results/P56_post_h64_clean_merge_candidate_packet/summary.json`
  reports explicit merge-candidate posture with `merge_execution_state = false`.
- [ ] `results/P57_post_h64_paper_submission_package_sync/summary.json`
  reports synchronized paper/submission package surfaces.
- [ ] `results/P58_post_h64_archive_release_closeout_sync/summary.json`
  reports synchronized archive/release closeout surfaces.
- [ ] `results/P59_post_h64_control_and_handoff_sync/summary.json`
  reports synchronized control and handoff surfaces.
- [ ] `results/F38_post_h62_r63_dormant_eligibility_profile_dossier/summary.json`
  keeps runtime closed and the cost-profile fields unresolved.
- [ ] `results/H58_post_r62_origin_value_boundary_closeout_packet/summary.json`
  preserves the strongest justified executor-value lane as closed negative.
- [ ] `results/H43_post_r44_useful_case_refreeze/summary.json` preserves the
  paper-grade endpoint.
- [ ] `results/release_preflight_checklist_audit/summary.json` reports
  `docs_and_audits_green`.
- [ ] `results/release_worktree_hygiene_snapshot/summary.json` reports a clean
  or warnings-only diff state.

## Release hygiene

- [ ] Any outward commit is blocked if `release_worktree_hygiene_snapshot`
  reports a dirty release state.
- [ ] No release or archive step routes through dirty root `main`.
- [ ] No public-facing note cites `docs/origin/` or `docs/Origin/` directly.
