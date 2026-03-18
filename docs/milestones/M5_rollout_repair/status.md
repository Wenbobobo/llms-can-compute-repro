# Status

Implemented and exported.

Current result:

- atomic held-out teacher-forced accuracy: about `0.7235`
- factorized held-out teacher-forced accuracy: about `0.7265`
- event-grouped held-out teacher-forced accuracy: about `0.7348`
- exact rollout remains `0.0` for all three exported variants

Interpretation:

- serialization matters,
- but serialization changes alone still do not fix rollout drift.
