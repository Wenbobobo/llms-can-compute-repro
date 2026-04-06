## 2025-04-06 - Dict setdefault in hot loops
**Learning:** `dict.setdefault(key, complex_default)` eagerly evaluates `complex_default` on every iteration, leading to massive memory allocation and performance overhead when creating default lists/dicts in hot loops (like in `HullKVCache._rebuild_if_needed`).
**Action:** Replace `setdefault` with an explicit `if key not in dict:` membership check to lazily evaluate the default structure only when necessary.
