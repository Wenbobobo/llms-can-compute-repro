# Status

First runnable checkpoint completed.

Current scope:

- structured tokenization of reference programs plus emitted trace events,
- baseline vocabulary construction and dataset statistics,
- a standard 2D-head softmax transformer definition,
- CUDA runtime validation in the project `uv` environment,
- one teacher-forced training run and one free-running rollout evaluation.

Current result:

- `torch==2.10.0+cu128` is installed and CUDA is available on the local GTX
  1650,
- the first tiny baseline run reaches train loss about `0.10` and train token
  accuracy about `0.97`,
- held-out teacher-forced token accuracy is about `0.70`,
- exact free-running rollout is still `0.0` on current countdown, branch, and
  memory eval groups.

Not yet included:

- factorized numeric tokenization or a similarly robust anti-OOV representation,
- a baseline result that survives free-running rollout,
- a clean fairness study against `M4` under multiple tokenization choices.
