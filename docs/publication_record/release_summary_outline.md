# Release Summary Outline

Status: downstream companion to the current `H32`/`H34`-controlled paper
bundle. This file is for future release-facing summaries that must stay
shorter than the manuscript bundle and must not redefine claims.

## Purpose

The manuscript bundle is now large enough that it should remain the primary
paper-facing draft. Future release-facing updates should therefore use a
separate short summary rather than repeatedly compressing the manuscript bundle
back into `README.md`-style prose. This keeps the long-form paper argument and
the short public-facing repository summary aligned without forcing them to be
the same document.

## Scope

This summary should contain only:

- one paragraph on the narrowed scientific target;
- one paragraph on the current control chain
  (`H28 -> H29 -> R36 -> R37 -> H30 -> H31 -> R38 -> H32 -> H33 -> R39 -> H34`);
- one paragraph on the present compiled endpoint and blocked non-goals;
- one short reproducibility pointer block.

This summary should not contain:

- new claim wording absent from the manuscript bundle;
- speculative future frontends;
- demo-oriented rhetoric;
- broader systems claims than the current mixed systems evidence supports.

## Draft structure

### 1. Narrow target

Reproduction of a narrow execution-substrate claim: append-only traces, exact
latest-write retrieval, and a small exact executor under explicit boundaries.

### 2. Current control chain

`H32` is the current active routing/refreeze packet, `H34` is the current
docs-only control packet above it, `H33` is the preserved prior
question-selection step, and `R39` is the completed same-substrate audit that
did not reopen a downstream runtime lane. Older controls such as
`P3`/`R1`/`R2`/`M7`/`P4` remain preserved historical context rather than the
current routing summary by themselves.

### 3. Current endpoint

The current compiled endpoint is a narrow same-substrate bytecode line, backed
by the landed `R37 -> H30 -> H31 -> R38 -> H32 -> H33 -> R39 -> H34` packet:
verifier coverage, exact-trace / exact-final-state agreement on one tiny
lowered subset, one richer control/call family, and one declared helper-body
permutation audit that still ends in
`freeze_compiled_boundary_as_complete_for_now`. The preserved first `D0`
boundary remains useful historical context, but the active endpoint is the
whole narrow same-substrate line, not a bridge to arbitrary `C`.

### 4. Reproducibility pointers

Point to:

- `README.md`
- `STATUS.md`
- `docs/publication_record/current_stage_driver.md`
- `docs/publication_record/claim_ladder.md`
- `docs/publication_record/manuscript_bundle_draft.md`
- `results/P1_paper_readiness/summary.json`
