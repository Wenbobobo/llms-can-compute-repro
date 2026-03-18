# Artifact Release Ledger

| Artifact bundle | Public status | Regenerate command | Notes |
| --- | --- | --- | --- |
| `results/M6_typed_bytecode_harness/` | public-safe | `uv run python scripts/export_m6_typed_bytecode_harness.py` | Primary `D0` evidence: verifier rows, lowering equivalence, exact-trace rows, and exact-final-state rows. |
| `results/M6_memory_surface_followup/` | public-safe | `uv run python scripts/export_m6_memory_surface_followup.py` | Appendix-level diagnostic companion to `D0`; does not justify a broader frontend claim. |
| `results/M6_stress_reference_followup/` | public-safe | `uv run python scripts/export_m6_stress_reference_followup.py` | One branch-selected helper checkpoint braid family plus one standalone Python spec oracle; strengthens `D0` without widening semantics. |
| `results/P1_paper_readiness/` | public-safe | `uv run python scripts/export_p1_figure_table_sources.py`; `uv run python scripts/render_p1_paper_artifacts.py`; `uv run python scripts/export_p1_paper_readiness.py` | Canonical paper-source tables, rendered figures, and bundle-status ledgers. |
| `results/H0_repo_consolidation_and_release_hygiene/` | public-safe | `uv run python scripts/export_h0_release_hygiene.py` | Machine-readable snapshot of the current public surface, dirty worktree, and preferred commit split before the next outward sync. |
| `results/M7_frontend_candidate_decision/` | public-safe | `uv run python scripts/export_m7_frontend_candidate_decision.py` | Explicit no-go / candidate decision bundle after `P3`, `R1`, and `R2`; keeps widening blocked unless later evidence changes the gate. |
| `results/P4_blog_release_gate/` | public-safe | `uv run python scripts/export_p4_blog_release_gate.py` | Outward release gate: README may stay restrained, but broader blog release remains blocked on the current decision bundle. |
| `docs/publication_record/` | public-safe | no single command; update in same batch as any claim-boundary change | Ledger source of truth for claim wording, figures, threats, and experiment provenance. |
| `docs/Origin/` | restricted / local-only | none | Raw source materials remain excluded from version control and should not be copied into public packaging. |
