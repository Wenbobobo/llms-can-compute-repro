# Root Salvage Shortlist

This file translates `P86`'s root inventory into a narrow clean-branch import
plan. The dirty root remains quarantine-only. Nothing listed here should be
merged blindly.

## Already Refreshed On Clean Branch

- `docs/publication_record/paper_bundle_status.md`
- `docs/publication_record/release_summary_draft.md`

These were the highest-value wording candidates and were already refreshed on
the clean branch during `P87`.

## Screened And No Import Now

- `docs/publication_record/claim_evidence_table.md`
  dirty-root version is older and not materially better than the clean-branch
  version.
- `docs/publication_record/negative_results.md`
  dirty-root version drops later closeout-era negatives and should not replace
  the cleaner current version.
- `docs/publication_record/review_boundary_summary.md`
  dirty-root version is stale and still keyed to older `H63/P50/P51/P52`
  routing rather than the current `H65/P88` posture.
- `docs/publication_record/threats_to_validity.md`
  dirty-root version is shorter and omits later closeout-era caveats that the
  clean branch already preserves.

## Salvage Later If Still Needed

- `docs/publication_record/archival_repro_manifest.md`
- `docs/publication_record/release_candidate_checklist.md`
- `docs/publication_record/release_preflight_checklist.md`
- `docs/publication_record/submission_candidate_criteria.md`
- `docs/publication_record/submission_packet_index.md`
- `docs/publication_record/experiment_manifest.md`

These remain potentially useful, but they should only be imported after the
paper-facing narrative is fully aligned with `H65`, `P87/P88`, and the
value-negative closeout.

## Do Not Salvage Blindly

- root `README.md` / `STATUS.md`
- root router duplicates such as `docs/README.md` and `docs/plans/README.md`
- generated `results/` payloads
- `tmp/active_wave_plan.md`

These are either duplicated by cleaner control surfaces, generated artifacts,
or temporary planning state that should not be promoted into the clean branch
without a separate reason.
