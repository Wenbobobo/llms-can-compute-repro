# M5 Standard 2D Baseline Results

## Current Scope

`M5` is now a runnable baseline branch, but still an early one.

Current capability:

- structured trace-sequence serialization from `exec_trace` programs,
- vocabulary construction and sequence statistics,
- a paper-like 2D-head softmax transformer definition,
- CUDA runtime export and device detection,
- paired atomic-vs-factorized teacher-forced training,
- an event-grouped sequence-compression variant,
- instruction-conditioned free-running rollout evaluation.

## Current Artifact

- `dataset_preview.json` now compares three serializations:
  - `atomic`: vocab size `190`, mean length about `252`,
  - `factorized`: vocab size `53`, mean length about `838`,
  - `event_grouped`: vocab size `49`, mean length about `511`.
- `training_run.json` now records three tiny CUDA variants:
  - `atomic_union_vocab`: vocab size `249`, held-out teacher-forced token
    accuracy about `0.72`, exact rollout still `0.0`,
  - `factorized_train_vocab`: vocab size `53`, held-out teacher-forced token
    accuracy about `0.73`, exact rollout still `0.0`, but first held-out
    countdown error moves from token `28` to token `94`,
  - `event_grouped_train_vocab`: vocab size `49`, held-out teacher-forced token
    accuracy about `0.735`, exact rollout still `0.0`, with held-out countdown
    first error at token `86`.

## Interpretation

The first softmax baseline result is already informative:

- teacher forcing alone overstates progress,
- the atomic whole-token serialization is not enough to support exact
  free-running execution in this branch,
- factorization helps with vocabulary pressure but does not by itself solve
  long structured rollout,
- event grouping shortens the sequence and helps teacher forcing slightly, but
  still does not break the zero-rollout barrier,
- and `M4` currently has a much stronger exact-rollout story than `M5`.

## Not Yet Included

- alternative prompt/rollout boundaries,
- model-size ablations,
- any positive free-running exact-rollout result.
