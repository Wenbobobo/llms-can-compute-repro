# Status

`M4` now has three implemented checkpoints:

- exact latest-write decode over extracted read events,
- a narrow trainable stack latest-write scorer,
- a free-running online executor that recovers value state through
  latest-write retrieval during rollout,
- and a fitted structured transition library that reproduces opcode effects
  online without hand-coded opcode semantics.
- a trainable neural structured-event decoder that learns the same transition
  label space and reaches exact held-out rollout on the current exported slice.

Current scope:

- exact 2D hard-max latest-write encoding,
- linear-scan reference decode,
- `HullKVCache` accelerated decode,
- validation against real `exec_trace` memory and stack examples,
- a two-parameter trainable scorer fitted on short countdown stack traces,
- free-running exact linear and accelerated executors,
- an induced causal executor fitted from reference traces,
- a neural event-level executor over structured transition labels,
- finite-precision stress checks for parabolic 2D addressing,
- and scheme-aware decomposition sweeps for the same precision bottleneck.

Current exported results:

- the trainable scorer still selects `quadratic_scale=0.25` and
  `time_scale=0.0005`,
- exact linear and accelerated free-running executors both match the reference
  trace on current countdown, branch, and bounded-RAM program families,
- the trainable stack scorer also reaches exact trace accuracy `1.0` on
  countdown train, countdown held-out, branch, and current memory program
  families, while memory reads remain exact in that checkpoint,
- the induced causal executor reaches exact trace accuracy `1.0` on its train
  slice, held-out countdowns, held-out equality branches, and held-out
  indirect-memory programs,
- the same induced executor also stays exact when combined with the current
  trainable stack latest-write scorer on the exported held-out slice,
- the new neural event executor reaches exact structured-label accuracy `1.0`
  on both its train and eval slices, and exact trace accuracy `1.0` on the
  exported held-out countdown, branch, and memory families,
- finite-precision stress shows local identity retrieval staying stable to
  address limit `8192` in `float64`, to `4096` in `float32`, failing by `64` in
  `float16`, and by `32` in `bfloat16`,
- latest-write time bias is much more fragile: the first local failure appears
  by `512` in `float32`, by `16` in `float16`, and immediately in small ranges
  for `bfloat16`,
- under the new decomposition sweeps, both `radix2` and
  `block_recentered` extend `float32` local latest-write stability from `256`
  to `4096`, although neither stays stable through `8192`.

This is still not yet a token-level learned executor branch. The current neural
checkpoint is an opcode-conditioned structured rule decoder, not a raw token
language model over trace events. It is a stronger `C2c` result than the
previous stack-only scorer, but still narrower than a general neural event
executor claim.
