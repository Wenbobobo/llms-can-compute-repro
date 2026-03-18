# P5 Public-Surface Sync Design

## Context

The paper-first lane is now structurally past claim freeze, precision closure,
systems gating, and the `M7` no-go decision. The main unattended drift risk is
no longer the claim ledger itself. It is the short public-facing layer:
`README.md`, `STATUS.md`, and the downstream summary material that now sits
between the manuscript draft and any future outward sync.

The repository already has coarse-grained outward checks:

- `scripts/export_h0_release_hygiene.py` audits release hygiene and commit
  grouping;
- `scripts/export_p4_blog_release_gate.py` audits whether the README/blog
  posture stays within the frozen scope.

What is still missing is a narrower `P5`-lane audit that checks whether the
current short public surface is actually synchronized with the newer section-
draft phase and with the explicit decision to derive future short updates from
`docs/publication_record/release_summary_draft.md`.

## Options considered

### 1. Add a `P5` public-surface sync audit

Audit the current alignment among `README.md`, `STATUS.md`,
`docs/publication_record/release_summary_draft.md`,
`docs/publication_record/manuscript_bundle_draft.md`, and the `P5` milestone
ledgers.

- smallest useful addition;
- directly reduces unattended wording drift;
- complements `H0` and `P4` instead of duplicating them.

### 2. Add one aggregate publication control-plane export

Create a single top-level summary that merges `P1/P3/R1/R2/M7/P4/H0`.

- easier to browse;
- higher duplication risk with existing result bundles;
- weaker direct protection against README/STATUS drift.

### 3. Add a paper-scope navigation index only

Export a compact active-artifact index for the current paper scope.

- useful for navigation;
- does not actually enforce public-surface consistency.

## Decision

Implement Option 1.

The chosen batch should add one machine-readable `P5` audit that:

- treats `release_summary_draft.md` as the downstream short-update source;
- checks that `README.md` and `STATUS.md` describe the current section-draft
  phase rather than an older bundle-assembly phase;
- confirms that the `P5` status/todo ledgers record the same transition; and
- leaves the scientific scope untouched.

## Acceptance

- one export bundle exists under `results/` for the current `P5` public-surface
  sync state;
- the bundle reports pass/fail rows for the narrow public-surface checks;
- the bundle captures a quick human-auditable snapshot of the key lines from
  README / STATUS / release summary / manuscript / `P5` ledgers;
- the new script is covered by targeted regression tests.
