# M4 Neural Event Executor

This milestone isolates the first learned event-generation branch that reaches
exact held-out rollout without falling back to the reference interpreter.

Current implementation:

- learns structured transition labels by SGD,
- runs online over the append-only retrieval substrate,
- stays exact on the exported countdown, branch, and memory held-out slice.

Current limitation:

- the model is still an opcode-conditioned structured rule decoder, not a raw
  token/event language model.
