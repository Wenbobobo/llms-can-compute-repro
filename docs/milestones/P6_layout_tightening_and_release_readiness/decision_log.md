# Decision Log

## 2026-03-19

- Open `P6` only after closing `P5`; do not blend post-assembly layout work
  back into the manuscript-assembly milestone.
- Keep the scientific scope frozen at append-only traces, exact latest-write
  retrieval, free-running exact execution, and tiny typed bytecode `D0`.
- Reuse the existing narrow `P5` audits as guards during `P6` rather than
  creating a broader new export surface immediately.
