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
- both decode modes are present:
  - brute-force linear scan,
  - `HullKVCache` accelerated retrieval,
- both modes are required to agree exactly on every exported read event.

## Current Artifact

- `decode_examples.json` records the latest-write and memory-accumulator trace
  examples, plus a dynamic-address memory example and stack-slot examples,
  together with exact linear/accelerated decode observations.

The current dynamic-address example still targets a single effective address at
runtime. It is evidence that the bridge survives runtime address selection, not
yet evidence for broad dynamic-address workloads. The new stack examples should
be read the same way: they validate the bridge on real stack evolution, not yet
on full mixed-state learned execution.

## Not Yet Included

- trainable attention modules,
- token-level parameterized models,
- free-running learned rollouts,
- sequence-length generalization experiments.
