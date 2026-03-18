# M4 Precision Scaling

This milestone isolates finite-precision behavior for the 2D latest-write
addressing family.

Current implementation compares:

- `single_head`
- `radix2`
- `block_recentered`

across `float64`, `float32`, `bfloat16`, and `float16`.
