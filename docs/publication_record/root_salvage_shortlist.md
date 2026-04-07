# Root Salvage Shortlist

This file translates `P86`'s root inventory into a narrow clean-branch import
plan. The dirty root remains quarantine-only. Nothing listed here should be
merged blindly.

## Salvage Now

- `docs/publication_record/paper_bundle_status.md`
  dirty-root wording had a fuller paper-facing summary than the clean branch;
  `P87` refreshed the clean version and this file remains a reference point.
- `docs/publication_record/release_summary_draft.md`
  dirty-root wording contained a stronger narrow-target summary; `P87`
  refreshed the clean version accordingly.
- `docs/publication_record/claim_evidence_table.md`
  likely still contains useful evidence indexing that may need a careful
  terminal-freeze refresh rather than a rewrite from scratch.
- `docs/publication_record/negative_results.md`
  already rich on the clean branch, but dirty-root edits may still contain
  wording deltas worth selective comparison.
- `docs/publication_record/review_boundary_summary.md`
  candidate for later refresh once the paper spine and claim/evidence table are
  stable.
- `docs/publication_record/threats_to_validity.md`
  candidate for later refresh once the release summary and paper bundle status
  are stable.

## Salvage Later If Still Needed

- `docs/publication_record/archival_repro_manifest.md`
- `docs/publication_record/release_candidate_checklist.md`
- `docs/publication_record/release_preflight_checklist.md`
- `docs/publication_record/submission_candidate_criteria.md`
- `docs/publication_record/submission_packet_index.md`
- `docs/publication_record/experiment_manifest.md`

These remain potentially useful, but they should only be imported after the
paper-facing narrative is fully aligned with `H65`, `P86`, and the value-negative
closeout.

## Do Not Salvage Blindly

- root `README.md` / `STATUS.md`
- root router duplicates such as `docs/README.md` and `docs/plans/README.md`
- generated `results/` payloads
- `tmp/active_wave_plan.md`

These are either duplicated by cleaner control surfaces, generated artifacts,
or temporary planning state that should not be promoted into the clean branch
without a separate reason.
