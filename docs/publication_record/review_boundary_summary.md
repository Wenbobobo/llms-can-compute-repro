# Review Boundary Summary

Status: packet-level summary for reviewers, archivists, and future submission
formatting passes. The authoritative evidence still lives in the manuscript,
appendix, claim/evidence ledgers, and landed `H23` packet, while
`H25_refreeze_after_r30_r31_decision_packet` is the current active operational
decision packet for downstream routing.

## Supported here on the current frozen scope

- deterministic computation can be encoded as an append-only execution trace;
- exact latest-write retrieval over that trace can be implemented with the
  current structured 2D hard-max mechanism;
- those primitives support one small exact executor and a tiny typed-bytecode
  `D0` compiled endpoint on the validated slice;
- same-endpoint runtime generalization is supported inside the admitted-plus-
  heldout `R19` envelope, the bounded `R20` mechanism result is supported on
  the fixed `16`-row probe set, the harder `R22`, `R26`, and `R27` executor
  grids still did not expose a failure inside their executed ranges, `R28`
  supports the current mechanism contract with only partial control isolation,
  and `R23` kept pointer-like exact exact on the full positive `D0` systems
  suite;
- the systems result remains mixed rather than triumphant.

## Unsupported here

- no general “LLMs are computers” claim;
- no arbitrary C reproduction claim;
- no broader compiled demos beyond the current `D0` boundary;
- no claim that the bounded `R21/R22` scans found the true executor failure
  boundary, or that the later `R26/R27` follow-up packet localized it;
- no current-scope end-to-end runtime-superiority claim.

## Disconfirmed here

- shuffled pointer-like retrieval does not preserve the current
  speed-and-exactness packet on the fixed `R20` probe set;
- the address-oblivious control does not preserve that packet on the same
  probe set;
- the narrower expectation that the executed `R21` grid had already exposed an
  exactness failure is disconfirmed on the current bounded scan and remains
  disconfirmed after `R22`, `R26`, and `R27`.

## Canonical evidence anchors

- `results/H23_refreeze_after_r26_r27_r28/summary.json`
- `results/H25_refreeze_after_r30_r31_decision_packet/summary.json`
- `results/R30_d0_boundary_reauthorization_packet/summary.json`
- `results/R31_d0_same_endpoint_systems_recovery_reauthorization_packet/summary.json`
- `results/H21_refreeze_after_r22_r23/summary.json`
- `claim_ladder.md`
- `claim_evidence_table.md`
- `manuscript_bundle_draft.md`
- `negative_results.md`
- `threats_to_validity.md`

## Reopen routing

If review requires materially new evidence, route it through exactly one named
lane in `conditional_reopen_protocol.md`:

- `E1a_precision_patch`
- `E1b_systems_patch`
- `E1c_compiled_boundary_patch`

Any later broader frontier review remains planning-only under
`F2_future_frontier_recheck_activation_matrix`, now downstream of active `H25`
while preserving `H23` as the frozen scientific state, until a later explicit
packet changes that status. The current same-endpoint order remains
`R32 -> deferred R33 -> blocked R29/F3`, with `F2` only as the planning
surface beyond that. Review questions that can be answered by wording, packet
indexing, or existing ledgers should stay downstream of the landed `H25/H23`
stack rather than reopening science.
