# Blocked Hypotheses

- "Current `M4` already reproduces a neural causal executor."
  Blocked because the new branch fits structured rules from traces; it does not
  yet learn a token/event decoder end to end.
- "Mixed memory plus stack is already solved under learning."
  Blocked because the induced branch is exact on the current toy slice, but the
  neural branch still only learns stack retrieval.
