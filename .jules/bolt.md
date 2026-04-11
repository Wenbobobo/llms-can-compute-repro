## 2024-05-24 - Expensive defaults in dict.setdefault
**Learning:** Using `dict.setdefault(key, complex_default)` in a hot loop (like `_rebuild_if_needed` in `HullKVCache`) eagerly evaluates `complex_default` on every iteration, even if the key exists. This is especially problematic when the default involves expensive constructors like `Fraction` or list comprehensions (`[Fraction(0) for _ in value]`).
**Action:** Use explicit `if key not in dict:` checks for complex defaults to avoid expensive eager evaluation on every iteration.
