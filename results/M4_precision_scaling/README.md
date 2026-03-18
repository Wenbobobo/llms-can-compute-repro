# M4 Precision Scaling Results

- `summary.json` records single-head vs decomposition precision sweeps.
- On the current float32 local latest-write sweep, `single_head` stays stable to
  `256`, while `radix2` and `block_recentered` stay stable to `4096`.
- These are still synthetic/local results, not yet the final long-horizon
  precision story.
