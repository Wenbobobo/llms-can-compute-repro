# M4 Exact Hard-Max Model Results

## Current Scope

This milestone now contains the first deterministic bridge from `M3` trace
semantics to `M2` hard-max retrieval.

Current capability:

- immediate-address latest-write memory reads are encoded as exact 2D hard-max
  queries,
- runtime dynamic-address memory reads are also encoded and checked through the
  same exact hard-max bridge,
- stack-slot reads/writes are also decoded through the same latest-write bridge
  over logical stack-slot addresses,
- a narrow trainable scorer can be fitted on short stack traces and checked on
  longer traces and one cross-family stack example,
- both decode modes are present:
  - brute-force linear scan,
  - `HullKVCache` accelerated retrieval,
- both modes are required to agree exactly on every exported read event.

## Current Artifacts

- `decode_examples.json` records the latest-write and memory-accumulator trace
  examples, plus a dynamic-address memory example and stack-slot examples,
  together with exact linear/accelerated decode observations.
- `trainable_stack_latest_write.json` records the first narrow learned slice:
  fit on short countdown stack traces, then exact evaluation on held-out longer
  countdowns and a dynamic-memory stack trace.
- `free_running_executor.json` records free-running exact rollout for:
  - exact linear retrieval,
  - exact accelerated retrieval,
  - and the current trainable stack scorer with exact memory retrieval.
- `induced_causal_executor.json` records the next M4 slice:
  - fitted structured transition rules per opcode,
  - exact online rollout on held-out countdown, branch, and indirect-memory
    programs,
  - and a combined run where induced event generation uses the current
    trainable stack latest-write scorer.
- `precision_stress.json` records the original single-head finite-precision
  address-range failures for `float64`, `float32`, `bfloat16`, and `float16`.
- `../M4_neural_event_executor/summary.json` records the new neural
  structured-event executor.
- `../M4_precision_scaling/summary.json` records the scheme-aware precision
  decomposition sweeps.

For the current grid search, the selected scorer uses
`quadratic_scale=0.25` and `time_scale=0.0005`. It reaches exact program
accuracy `1.0` on:

- 7 short countdown training programs,
- 14 held-out longer countdown programs, including the `steps>=49` bucket,
- 1 dynamic-memory stack trace from a different program family.

The free-running executor artifact extends this further:

- exact linear rollout matches the reference trace on current countdown, branch,
  and bounded-RAM program families,
- exact accelerated rollout matches the same reference traces,
- the current trainable stack scorer also stays exact on the exported
  countdown, branch, and current bounded-RAM slice because only stack-slot
  retrieval is learned in this checkpoint.

The induced causal artifact extends this again:

- the fitted transition library reaches exact trace accuracy `1.0` on its train
  programs,
- it also stays exact on held-out countdown, equality, and indirect-memory
  programs,
- and it remains exact when paired with the current trainable stack latest-write
  scorer on the exported held-out slice.

The neural event artifact extends this one step further:

- it trains a neural multi-head decoder over the same structured transition
  label space,
- it reaches exact structured-label accuracy `1.0` on both the exported train
  and eval slices,
- and it reaches exact rollout `1.0` on held-out countdown, branch, and memory
  program families.

The current dynamic-address example still targets a single effective address at
runtime. It is evidence that the bridge survives runtime address selection, not
yet evidence for broad dynamic-address workloads. The new stack examples should
be read the same way: they validate the bridge on real stack evolution. The
trainable scorer result is also narrow: it shows that a tiny parameterized
latest-write rule can fit and extrapolate on the current candidate-set task, not
that a full causal neural executor has been reproduced.

The precision artifact should be read as a warning label:

- `float64` stays locally stable through the current sweep up to `8192`,
- `float32` identity retrieval stays locally stable to `4096` but its
  latest-write time bias already breaks by `512`,
- `float16` and `bfloat16` collapse much earlier.

The new scheme-aware precision artifact should be read as a partial repair:

- `single_head` keeps the current `float32` latest-write stability only through
  local address limit `256`,
- `radix2` extends that to `4096`,
- and `block_recentered` does the same on the current local sweep.

## Not Yet Included

- token-level neural event decoders,
- million-step-stable addressing,
- broader mixed-memory workloads under a context-richer learned branch.
