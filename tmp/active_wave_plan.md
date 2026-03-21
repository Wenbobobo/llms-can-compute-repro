# Active Wave Plan

## Current Wave

`P12_manuscript_and_manifest_maintenance`

## Immediate Objectives

1. Treat `H21_refreeze_after_r22_r23` as the current frozen scientific input.
2. Align claim ladders, evidence tables, manifests, and negative-result ledgers
   to the landed `R22/R23/H21` packet without widening scope.
3. In parallel, pre-lay
   `R24_d0_boundary_localization_zoom_followup` as the boundary-first planning
   package for a later explicit reopen decision.
4. Park `R25_d0_same_endpoint_systems_recovery_hypotheses` as same-endpoint
   systems notes without treating it as an active repair lane.
5. Keep `README.md`, `STATUS.md`, and publication-facing summaries downstream of
   the landed mixed systems result, with `P13` still later and downstream-only.

## Suggested Worktree Map

Use these after the next path-scoped doc closeout commit:

- `wip/p12-ledger` -> sibling worktree `../LLMCompute-wt-p12`
- `wip/r24-boundary-plan` -> sibling worktree `../LLMCompute-wt-r24`
- `wip/r25-systems-notes` -> sibling worktree `../LLMCompute-wt-r25`
- `wip/p13-hygiene` -> sibling worktree `../LLMCompute-wt-p13`

Suggested ownership:

- main agent: `main`
- worker A: `wt-p12`
- worker B: `wt-r24`
- background worker: `wt-r25`
- later downstream worker: `wt-p13`

## Acceptance For This Wave

- `H21` is the frozen handoff anchor for the current wave;
- `P12` documents the post-`R22/R23/H21` claim and manifest impact explicitly;
- `R24` exists as a planning-only boundary-first reopen package with explicit
  axes and stop rules;
- `R25` exists as a parked same-endpoint systems hypotheses package with
  explicit thresholds and disconfirmers;
- `P13` is recorded as downstream-only rather than immediate next priority;
- no widened runtime scope, frontend widening, or softened mixed-systems prose
  is introduced in this wave.

## If Blocked

- first continue with `P12` ledger upkeep if one root/publication doc is
  blocked;
- then continue `R24` and `R25` planning-only writeups rather than opening a
  new runtime lane early;
- only after that, tighten the current split map and `P13` hygiene notes;
- do not start widened runtime, repair, or frontend experiments.
