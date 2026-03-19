# Status

## Current Scientific State

- `A1/B1`: append-only trace semantics and exact 2D hard-max retrieval remain
  validated on the current scope.
- `C2h`: staged-neural execution stays caveated by legality structure; the
  widened `opcode_shape` regime fails on held-out rollout, and the provenance
  follow-up ties many later `step_budget` rows to earlier semantic divergence.
- `C3e/R1`: the precision story is a bounded positive, not a broad robustness
  claim; float32 single-head fails on `12/25` tracked real/organic streams,
  `7/25` already at `1x`, while at least one decomposition stays exact on
  `25/25` tracked streams in the validated suite.
- `D0`: the current compiled endpoint is tiny typed bytecode, with deterministic
  verifier coverage, exact-trace / exact-final-state agreement on the frozen
  starter suite, memory-surface diagnostics, and a stress/reference companion.
- `R2`: the systems result is mixed; geometry shows a strong asymptotic
  cache-vs-bruteforce win, but the lowered `exec_trace` path is still about
  `1.82x` slower than the best current reference/oracle path on positive `D0`
  suites.
- `M7/P4`: frontend widening is not authorized, README-level release is
  acceptable, and broader blog/demo prose remains blocked.

## Current Paper State

- `P5` now has a sentence-polished manuscript section draft, appendix draft,
  caption candidates, layout decisions, and machine-audited public-surface /
  callout guards under `docs/publication_record/`.
- `results/P1_paper_readiness/summary.json` now reports `10/10` ready
  figure/table items and no blocked or partial items on the frozen current
  scope.
- The sentence-level polish and callout-alignment pass is now complete;
  remaining paper-facing work is layout tightening, figure/table integration,
  and restrained public-surface maintenance, not new claim expansion.

## Immediate Next Actions

1. Keep `README.md`, `STATUS.md`, and future short public-surface syncs
   downstream of `docs/publication_record/release_summary_draft.md`.
2. Run the next paper-facing wave as layout tightening and release-readiness
   work while keeping the current manuscript artifact pairings fixed unless a
   deliberate layout pass records a different choice.
3. Reopen `R1`, `R2`, or frontend widening only if the project deliberately
   starts a new evidence wave; otherwise keep the current `D0` endpoint fixed.

## Known Blockers

- Broader compiled demos remain blocked by `M7`.
- Broader outward narrative remains blocked by `P4`.
- Current-scope end-to-end systems superiority remains unsupported by `R2`.
- No operational repo-hygiene blocker is active on the current worktrees.
