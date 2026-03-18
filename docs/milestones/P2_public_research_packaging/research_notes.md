# Research Notes

- The public story must center on `append-only exact traces`, exact
  latest-write retrieval, and the narrow `D0` typed-bytecode boundary; avoid
  broader "LLMs-as-computers" rhetoric.
- Linked Python 3.12 + `uv` tooling keeps the exported artifacts reproducible
  by anyone in the workspace without extra dependencies.
- Maintain a strict ledger: each unattended export must append the datetime,
  scripts run, and claim references so the paper can cite machine-readable
  provenance.

## Current claim-to-artifact map

- `D0` frontend boundary:
  `results/M6_typed_bytecode_harness/verifier_rows.json`,
  `results/M6_typed_bytecode_harness/short_exact_trace.json`,
  `results/M6_typed_bytecode_harness/long_exact_final_state.json`,
  `results/M6_memory_surface_followup/summary.json`,
  `results/P1_paper_readiness/exact_trace_final_state_table.md`,
  `results/P1_paper_readiness/m6_memory_surface_diagnostic_table.md`.
- `C2h` staged mask-dependence closure:
  `results/M4_mask_dependence_executor_gap/summary.json`,
  `results/M4_failure_provenance/summary.json`,
  `results/P1_paper_readiness/m4_failure_taxonomy_figure.svg`.
- `C3e` broader real-trace precision taxonomy:
  `results/M4_precision_generalization/screening.json`,
  `results/M4_precision_organic_traces/claim_impact.json`,
  `results/P1_paper_readiness/m4_real_trace_boundary_figure.svg`.

## Paper-first workflow

1. Regenerate any changed `M4` / `M6` result bundle.
2. Regenerate `P1` sources with:
   `uv run python scripts/export_p1_figure_table_sources.py`,
   `uv run python scripts/render_p1_paper_artifacts.py`,
   `uv run python scripts/export_p1_paper_readiness.py`.
3. Update root `README.md`, root `STATUS.md`, and the relevant milestone docs.
4. Update `artifact_release_ledger.md` with public-safe / restricted status and
   reproduction commands.
5. Only then reconsider outward paper/blog packaging language.
