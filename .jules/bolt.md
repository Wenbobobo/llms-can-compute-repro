
## 2026-04-04 - Eager Dict Default Argument Evaluation in Hot Loops
**Learning:** `dict.setdefault(key, complex_default)` unconditionally evaluates `complex_default` *before* checking key existence. If the default involves list comprehensions or dictionary allocations, this adds an invisible O(N) penalty to every loop iteration when accumulating data across multiple files.
**Action:** Replace `dict.setdefault` with explicit `if key not in dict:` when defaults are computationally expensive.
