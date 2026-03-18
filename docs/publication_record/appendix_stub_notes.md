# Appendix Stub Notes

This file turns the current appendix boundary and reproduction ledger into a
near-prose appendix draft. It should be used to expand the reproducibility
appendix without reopening any main-text claim boundary.

## Reproducibility appendix seed

The appendix should make the current paper bundle auditable and regenerable
without inflating companion diagnostics into new main-text claims. The guiding
rule is simple: main text carries the distilled claim-bearing evidence, while
the appendix carries regeneration commands, artifact maps, and companion views
that strengthen auditability on the same frozen scope. The current appendix
therefore has three jobs. First, it points readers to the canonical paper-ready
bundle under `results/P1_paper_readiness/`, which contains rendered figures,
table sources, and machine-readable bundle summaries. Second, it records how to
regenerate the public-safe result bundles that matter for the compiled
boundary, paper assembly, and release gate. Third, it keeps companion
diagnostics such as memory-surface views, per-stream precision catalogs, and
full staged failure digests visible and inspectable without letting them mutate
into broader claims.

## Appendix artifact-map seed

The artifact map should group appendix material by role rather than by file
type. One group covers paper assembly and rendering: `results/P1_paper_readiness/`
plus its export and render commands. A second group covers `D0` companions:
`results/M6_memory_surface_followup/` and the appendix-level parts of
`results/M6_stress_reference_followup/`, which deepen confidence in the frozen
compiled boundary without widening it. A third group covers mechanism
diagnostics that remain secondary to the main argument: per-stream precision
catalogs and full staged failure/provenance rows. A final group covers outward
discipline and packaging: the `P2` artifact release ledger, the `H0` hygiene
bundle, and the `P4` release gate. These materials belong in the appendix
because they make the research engineering process inspectable, not because
they support a broader scientific claim.

## Regeneration-command seed

The appendix should include a compact regeneration block rather than burying
commands across milestones. The current public-safe command set is already
stable enough for that purpose: `uv run python scripts/export_p1_figure_table_sources.py`,
`uv run python scripts/render_p1_paper_artifacts.py`, and
`uv run python scripts/export_p1_paper_readiness.py` regenerate the paper-ready
bundle; `uv run python scripts/export_m6_typed_bytecode_harness.py`,
`uv run python scripts/export_m6_memory_surface_followup.py`, and
`uv run python scripts/export_m6_stress_reference_followup.py` regenerate the
compiled-boundary core and companion bundles; `uv run python scripts/export_m7_frontend_candidate_decision.py`,
`uv run python scripts/export_p4_blog_release_gate.py`, and
`uv run python scripts/export_h0_release_hygiene.py` regenerate the decision
and release-discipline bundles. The appendix should present these as one frozen
current-scope recipe rather than as an invitation to widen the claim set.

## Appendix-only guardrail seed

The appendix must explicitly keep some material out of the main text. Memory-
surface diagnostics remain appendix-only unless a later revision turns memory
surface behavior into a main-text claim. Per-stream precision catalogs remain
appendix-only unless one trace family becomes central to a revised precision
argument. Full staged failure digests remain appendix-only unless reviewer
feedback makes row-level evidence necessary in-line. Packaging and hygiene
ledgers also remain appendix-only because they regulate outward release, not
the scientific core. The appendix should say this plainly so later editing does
not silently promote companion evidence into broader narrative claims.
