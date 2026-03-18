# Status

## Working State

- M0 scaffold: complete
- M1 claims/scope docs: complete
- M2 geometry exactness: initial implementation added
- M3 trace executor: stack plus bounded-RAM reference semantics implemented
- M4 exact hard-max decode: deterministic latest-write bridge implemented for immediate and dynamic memory addressing plus stack-slot retrieval
- M4 narrow trainable slice: two-parameter stack latest-write scorer fitted and validated on held-out longer traces
- M4 free-running exact executor: linear and accelerated online rollout now match the reference trace on current countdown, branch, and bounded-RAM programs
- M4 induced causal executor: structured transition rules fitted from reference traces now generate exact online events on held-out countdown, branch, and indirect-memory programs
- M4 neural event executor: a trainable structured-event decoder now learns opcode-conditioned transition labels and reaches exact rollout on current held-out countdown, branch, and memory families
- M4 finite-precision stress: scheme-aware address-range failure sweeps now compare single-head, radix-2, and block-recentered latest-write addressing
- M5 scaffold: structured trace dataset, vocabulary helpers, optional Torch baseline definition, and dataset preview artifact added
- M5 CUDA baseline run: first teacher-forced training run completed on the tiny 2D-head softmax model, with nontrivial teacher-forced accuracy but zero exact free-running rollout on current eval groups
- M5 representation ablation: atomic whole-token vs factorized digit-level vs event-grouped serializations now run side by side; event grouping reduces sequence length and improves held-out teacher-forced accuracy slightly, but exact rollout still remains zero
- Runtime environment export: Python 3.12.9, `torch==2.10.0+cu128`, and CUDA device info are now recorded under `results/runtime_environment.json`
- Packaging fix: renamed the trace package to avoid the Python stdlib conflict
- Public GitHub repo created and initial push completed

## Immediate Next Actions

1. Push `M4` past the current opcode-conditioned neural rule table into a context-richer event decoder without losing exact held-out rollout.
2. Extend `M4-B` beyond synthetic local sweeps into real mixed trace reads and larger horizons, because the current decomposition checkpoint still stops at `8192`.
3. Decide whether `M5` should get one architecture-side intervention after `event_grouped`, or whether it has earned a stable negative-control status for the current claim ladder.

## Known Blockers

- None at the repository/bootstrap layer.
- The main remaining risks are scientific: representation choices, tie semantics
  at scale, finite-precision address collapse beyond the current decomposition
  sweep, baseline rollout brittleness despite better serialization, and how far
  the current neural event branch generalizes beyond the present toy executor.
