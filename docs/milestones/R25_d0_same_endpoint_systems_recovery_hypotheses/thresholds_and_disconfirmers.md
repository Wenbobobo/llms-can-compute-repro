# Thresholds And Disconfirmers

## Verdict Thresholds

- `systems_materially_positive`
  Exactness stays intact on the bounded positive `D0` suite and the median
  ratio versus the best current reference path is `<= 1.1`.
- `systems_still_mixed`
  Exactness stays intact, but the runtime ratio versus the best current
  reference path remains `> 1.1`.
- `stronger_negative_same_endpoint`
  Exactness regresses, or runtime remains clearly noncompetitive without a
  credible bounded explanation.

## Kill Criteria

- If a later candidate still shows `non_retrieval` overhead as the dominant
  component on the bounded suite, kill any retrieval-first recovery story as
  the primary explanation.
- If a later candidate only looks better against imported `accelerated` but not
  against `spec_reference` or `lowered_exec_trace`, kill any “systems
  overturn” framing.
- If the lag remains suite-stable rather than collapsing to one bounded family,
  kill any one-suite repair narrative.
- If a later candidate requires widened suites, widened endpoints, or softened
  comparators to look competitive, treat that as scope drift rather than as
  same-endpoint recovery.
