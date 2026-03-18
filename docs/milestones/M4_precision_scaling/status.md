# Status

Implemented and exported.

Current result:

- `single_head` float32 latest-write stays locally stable only through `256`
- `radix2` float32 latest-write stays locally stable through `4096`
- `block_recentered` float32 latest-write also stays locally stable through
  `4096`

Interpretation:

- decomposition materially improves the current float32 story,
- but the current sweep still stops at `8192`, so long-horizon claims remain
  narrow.
