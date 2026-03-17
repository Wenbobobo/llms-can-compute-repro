# Status

Initial `M4` prototype implemented.

Current scope:

- exact 2D hard-max latest-write encoding,
- linear-scan reference decode,
- `HullKVCache` accelerated decode,
- validation against real `exec_trace` memory examples, including dynamic
  addressing,
- validation against logical stack-slot reads extracted from real traces.

This is still a deterministic bridge layer, not yet a learned model branch.
