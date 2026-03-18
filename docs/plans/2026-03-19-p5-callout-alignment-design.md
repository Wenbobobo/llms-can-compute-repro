# P5 Callout Alignment Design

## Context

The paper lane now has:

- a section-draft manuscript bundle;
- fixed figure/table narrative roles;
- caption candidate notes;
- a section map that records which artifacts each main-text section depends on;
- a public-surface sync audit that keeps `README.md`, `STATUS.md`, and the
  downstream release summary aligned.

What is still missing is a narrow machine-readable check that the internal
paper-facing layer stays aligned on which main-text artifacts actually carry
the argument. This matters most for the sections where evidence pairing is part
of the scientific restraint: the introduction claim pair, the precision
figure/table pair, the compiled-boundary diagram/table pair, and the
threats-to-validity table.

## Options considered

### 1. Continue prose-only edits

Pros:
- immediately improves readability.

Cons:
- drift between manuscript prose and caption/role ledgers can reappear in later
  unattended passes;
- harder to audit mechanically.

### 2. Add one narrow `P5` callout-alignment export

Audit whether four key main-text callout groups remain synchronized across:

- `docs/publication_record/manuscript_bundle_draft.md`
- `docs/publication_record/caption_candidate_notes.md`
- `docs/publication_record/figure_table_narrative_roles.md`
- `docs/publication_record/manuscript_section_map.md`

Pros:
- small and directly useful for unattended paper drafting;
- complements the public-surface sync audit instead of duplicating it;
- keeps the current claim-bearing artifact pairs explicit.

Cons:
- uses text-level alignment checks, so it should stay narrow rather than trying
  to infer full manuscript semantics.

### 3. Build a broader paper-assembly control plane

Pros:
- could centralize many paper-lane checks.

Cons:
- too large for the current unattended batch;
- higher duplication risk with existing `P1`, `P3`, `P4`, and `P5` ledgers.

## Decision

Implement Option 2.

The audit should only check high-value, claim-bearing pairings:

- introduction: claim-ladder figure + supported/unsupported claims table;
- precision: real-trace boundary figure + real-trace boundary table;
- compiled boundary: frontend boundary diagram + exact-trace/final-state table;
- threats: threats-to-validity table;
- section-map coverage for those same main-text groups.

## Acceptance

- one `P5` callout-alignment export exists under `results/`;
- the export reports pass/fail rows for the current key artifact groups;
- the export includes a small line snapshot for human audit;
- the script is covered by targeted regression tests;
- the batch does not widen the scientific scope.
