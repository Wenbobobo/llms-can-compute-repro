# Hypothesis Matrix

## Purpose

This file turns the parked `R25` lane into an explicit same-endpoint systems
hypothesis packet. It does not authorize execution. It records what the current
mixed `R2/E1b/R23` chain actually suggests about the bottleneck.

| Hypothesis | Current evidence | Planning implication |
| --- | --- | --- |
| `non_retrieval_overhead_dominates` | In `R23`, `pointer_like_exact` median retrieval share is about `0.023`, and `non_retrieval` is dominant on `25/25` rows. | More retrieval-only work is unlikely to overturn the systems gate by itself. |
| `best_reference_comparator_gap_remains_the_blocker` | `spec_reference` stays at ratio `1.0`, `lowered_exec_trace` is about `1.7169`, and `pointer_like_exact` is about `4.1643`. | A later same-endpoint recovery must close against the best current reference, not merely beat imported accelerated. |
| `lag_is_suite_stable_rather_than_isolated` | `pointer_like_exact` median ratio vs best current reference stays in a narrow bad band across all `5` suites, roughly `3.55x` to `4.67x`. | Do not frame the mixed result as one family-specific pathology waiting for a local fix. |
| `retrieval_mechanism_success_does_not_imply_systems_success` | `R20` supports the mechanism story through exact negative controls, while `R23` still ends at `systems_still_mixed`. | Keep mechanism and systems claims separate in any later reopen design. |

## Scope Discipline

- These hypotheses stay on the current positive `D0` suites only.
- They do not authorize a widened frontend, a broader compiled-language target,
  or new suites by momentum.
- They exist so a later explicit reopen can start from falsifiable systems
  hypotheses instead of from vague “maybe the runtime is close” prose.
