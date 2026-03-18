# Status

Not started. Still intentionally blocked.

Current blocker summary:

- `M4` now has exact, induced, and neural structured-event executors, but the
  neural branch is still an opcode-conditioned rule decoder rather than a
  richer token/event model.
- `M5` now has a runnable CUDA baseline, but its first exact free-running
  rollout result is still zero on the current eval slice even after the
  event-grouped serialization pass.
- `M4-B` now has a useful decomposition checkpoint, but the current precision
  story still stops short of any serious million-step claim.
