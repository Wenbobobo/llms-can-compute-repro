# TODO

- [x] Define the exact hard-max attention API for latest-write memory retrieval
- [x] Build a minimal causal decode loop that compares linear scan and `HullKVCache`
- [x] Validate the decode loop on exported `exec_trace` memory examples
- [x] Generalize beyond immediate-address memory to a richer addressing mode
- [x] Validate the same bridge on logical stack-slot retrieval
- [x] Train a narrow scorer on reference-generated stack traces
- [x] Evaluate exact success by held-out length bucket for the narrow scorer
- [x] Implement exact free-running rollout with linear and accelerated latest-write retrieval
- [x] Evaluate free-running rollout by length bucket
- [x] Record finite-precision failure ranges for parabolic addressing
- [x] Fit and validate an induced structured causal executor over exact event semantics
- [ ] Replace the induced structured executor with a token/event-level neural causal decoder
- [ ] Extend neural or induced rollout deeper into mixed memory/stack execution under finite-precision constraints
