# Future Family Matrix

This matrix is downstream of `F5` and `F6`. It is a roadmap, not an activation
surface.

| Family | What it would cover | Current status | Preconditions before any activation | Why inactive now |
| --- | --- | --- | --- | --- |
| Current Origin-core same-substrate line | append-only trace, exact retrieval, small exact executor, and the current narrow compiled boundary | `supported_here` | preserve `H32/H34` exactly | this is the current scientific baseline, not a future family |
| `F8_post_h34_beyond_origin_bridge_roadmap` | classify beyond-Origin bridge families and target order | `planning_only` | keep the `H34` no-reopen state explicit | it is a routing aid only |
| `F9_post_h34_restricted_wasm_semantic_boundary_roadmap` | define what a verifier-visible restricted semantic boundary beyond the current tiny bytecode line would need to preserve | `blocked_by_scope` | later explicit scope decision, stronger evidence, and no momentum widening | Wasm-like widening is currently out of scope |
| `F10_post_h34_executor_value_comparator_matrix` | compare richer executor-visible value semantics or obligations before any frontend widening | `planning_only` | stay docs-only, keep comparator obligations explicit, and avoid creating a runtime lane | comparator clarification may help later planning, but no implementation is authorized |
| `F11_post_h34_hybrid_planner_executor_bridge_roadmap` | frame a planner-plus-executor hybrid story beyond the current exact executor substrate | `requires_new_substrate` | new substrate or hybrid-system packet plus broader evidence | the repo has no active hybrid integration line |

No row in this matrix overrides `F5` or `F6`. Any future activation still needs
an explicit later packet.
