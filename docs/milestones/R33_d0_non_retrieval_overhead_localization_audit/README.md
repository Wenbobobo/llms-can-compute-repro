# R33 D0 Non-Retrieval Overhead Localization Audit

Planned deferred systems-audit lane after `H25`.

`R33` exists because current evidence suggests that same-endpoint systems
noncompetitiveness is still dominated by non-retrieval overhead rather than by
retrieval correctness itself. It is a narrower prerequisite lane, not a direct
systems-overturn lane.

The lane now has an explicit planning-only component-localization manifest in
`component_localization_manifest.md`. That manifest fixes the comparator set,
final audit scope, component targets, required outputs, and kill criteria
before execution.

The intended unattended order is:

1. keep `R33` deferred while `R32` remains the primary science lane;
2. use `R33` only if a later packet explicitly activates the systems-audit
   prerequisite;
3. keep the lane attribution-only, with no direct `R29` activation by
   momentum.
