# R55 Origin 2D Hardmax Retrieval Equivalence Gate

Next required exact mechanism gate under active `H51`.

Current status: `authorized_next_runtime_candidate`.

`R55` tests whether the claimed `2D` hard-max retrieval primitive is exactly
equivalent to a transparent reference latest-relevant-state lookup on a fixed
bounded suite. It does not authorize transformed-model entry, trainable entry,
or broader runtime widening.

The gate must record:

- one fixed retrieval-equivalence contract;
- one fixed task matrix covering overwrite-after-gap, stack-slot, duplicate
  maximizer, and declared tie cases;
- exact value parity and maximizer-row parity on every read; and
- one explicit lane verdict that either keeps or falsifies the mechanism route
  before any trace-VM semantics gate begins.
