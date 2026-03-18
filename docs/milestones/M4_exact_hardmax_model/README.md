# M4 Exact Hard-Max Model

Current milestone: causal executor experiments over exact hard-max latest-write
retrieval.

This branch now covers three layers:

- deterministic latest-write decode over extracted trace reads,
- a narrow trainable scorer over stack latest-write candidates,
- a free-running online executor that uses append-only latest-write
  retrieval to reproduce reference traces,
- and an induced structured transition executor that fits opcode semantics
  directly from reference traces and then emits exact events online.

The learned part is still narrow. The project now has a data-induced
event-generation branch, but it is still an event-level structured executor,
not yet a token-level neural causal model.
