# Layout Decision Log

This file records paper-layout choices that affect claim wording, evidence
placement, or later drafting effort.

| Item | Decision | Why | Revisit only if | Primary sources |
| --- | --- | --- | --- | --- |
| `R2` systems gate | Keep as a quantified main-text paragraph in the current draft; do not add a standalone main-text table yet. | The main scientific fact is the mixed gate decision, not a broad positive systems win. A full table would spend scarce main-text space on still-negative timing detail and could overstate the maturity of the systems story. | A later paper-layout pass needs a compact quantitative anchor, or a future systems pass materially changes the gate outcome. | `results/R2_systems_baseline_gate/summary.json`, `results/R2_systems_baseline_gate/runtime_profile_rows.csv`, `results/R2_systems_baseline_gate/baseline_matrix.json` |

## Promotion rule

If `R2` later needs a table in the main text, it should be a compact gate table
derived from the existing `decision_table` in
`results/R2_systems_baseline_gate/summary.json`, not a wholesale promotion of
the full runtime matrix.
