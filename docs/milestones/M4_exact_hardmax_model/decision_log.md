# Decision Log

- Reserve this milestone for exact hard-max semantics only.
- Start with latest-write memory retrieval before any trainable model work.
- Require linear-scan and accelerated decode modes to agree exactly on each
  read event.
- Extend from immediate-address reads to dynamic-address reads before moving
  toward learned decode.
- Treat stack-slot retrieval as the next exact hard-max target because it uses
  the same causal latest-write structure without needing a new compiler layer.
