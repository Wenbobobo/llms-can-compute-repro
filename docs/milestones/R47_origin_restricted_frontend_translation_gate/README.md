# R47 Origin Restricted Frontend Translation Gate

Planned exact frontend bridge gate after positive `R46` and later explicit
authorization.

`R47` will test one tiny restricted Wasm-like / tiny-C-like bridge onto the
existing useful-case contract. It stays below heap, alias-heavy pointers,
recursion, float, IO, and any broader compiler/runtime claim.
