# M5 Standard 2D Baseline Results

## Current Scope

`M5` is now a runnable baseline branch, but still an early one.

Current capability:

- structured trace-sequence serialization from `exec_trace` programs,
- vocabulary construction and sequence statistics,
- a paper-like 2D-head softmax transformer definition,
- CUDA runtime export and device detection,
- teacher-forced training,
- instruction-conditioned free-running rollout evaluation.

## Current Artifact

- `dataset_preview.json` records the current example count, vocabulary size,
  sequence-length range, and token/id previews for the first structured dataset
  slice.
- `training_run.json` records the first tiny CUDA run, including:
  - `torch==2.10.0+cu128` on Python `3.12.9`,
  - train loss about `0.10`,
  - train token accuracy about `0.97`,
  - held-out teacher-forced token accuracy about `0.70`,
  - exact free-running rollout accuracy `0.0` on current countdown, branch,
    and memory eval groups.

## Interpretation

The first softmax baseline result is already informative:

- teacher forcing alone overstates progress,
- the current verbose structured serialization is not enough to support exact
  free-running execution in this branch,
- and `M4` currently has a much stronger exact-rollout story than `M5`.

## Not Yet Included

- factorized numeric tokenization,
- alternative prompt/rollout boundaries,
- model-size ablations,
- any positive free-running exact-rollout result.
