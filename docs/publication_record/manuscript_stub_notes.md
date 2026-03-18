# Manuscript Stub Notes

This file holds near-prose draft stubs for the most scope-sensitive parts of
the paper bundle. They are not final paper text, but they are intended to be
close enough that later drafting can proceed by editing rather than by
re-deciding claim scope.

## Usage rules

- Keep the wording aligned with the frozen claim/evidence ledgers.
- Treat the mixed `R2` result and the `M7` no-go decision as part of the paper
  contribution, not as language to soften away.
- Do not reuse this text directly for README or blog material unless the
  publication ledgers are updated first.

## Abstract seed

We revisit a field-note claim that large language model mechanisms can behave
like computation, but we freeze the paper around a narrower reproduction target:
append-only execution traces, exact latest-write retrieval, and a small exact
executor under explicit boundaries. On the current public artifact surface, the
mechanism story remains positive at this narrower level: append-only trace
semantics and exact retrieval survive, and a tiny typed-bytecode `D0` slice
achieves exact trace or exact final-state agreement on the frozen starter
suite. The precision story is positive but bounded rather than open-ended:
float32 single-head fails on 12 of 25 tracked real-trace streams, with 7
failing already at `1x`, while at least one decomposition configuration
remains exact on all 25 tracked streams in the validated suite. The systems
story is mixed: cached retrieval retains a strong asymptotic advantage on the
geometry benchmark, but the current lowered `exec_trace` path remains about
`1.82x` slower than the best current reference/oracle path on the positive
`D0` suites. We therefore keep the compiled endpoint at tiny typed bytecode and
treat broader claims about arbitrary C, general LLM computation, or current
end-to-end competitiveness as unsupported.

## Introduction opening seed

The motivating source text is valuable because it points toward a concrete
mechanistic idea: computation can be rewritten as an append-only execution
trace, and key read operations can be phrased as exact latest-write retrieval.
What it does not provide is a paper-grade boundary for which parts of that
story actually survive when every claim must be tied to auditable artifacts,
free-running exactness, and explicit negative results. The present work
therefore treats reproduction as a narrowing process rather than a branding
exercise. Its target is not “LLMs are computers” in the broad rhetorical sense,
but a smaller question: which mechanism-level and compiled-boundary claims
remain defensible after the evidence is frozen and mixed or negative results
are kept in view?

Under that narrower reading, the paper makes three contributions. First, it
keeps the append-only trace substrate and exact retrieval story intact on the
current validated scope. Second, it closes two important boundaries instead of
silently skipping them: staged-neural execution remains caveated by legality
structure, and real-trace precision remains positive only within an explicitly
narrow current-suite boundary. Third, it shows that the first compiled endpoint
should remain at tiny typed bytecode `D0`: the current slice is exact and
auditable, but the systems gate is mixed and therefore does not justify
widening to a broader frontend.

## Systems gate section stub

The systems result is deliberately reported as a gate rather than as a victory
lap. On the positive side, the original mechanism intuition still has genuine
system-level content: on the current geometry benchmark, cached retrieval is
faster than brute-force history search at every tested history size and yields
speedups from about `42.8x` to `249.2x` as history grows. That asymptotic
signal, however, is not the same thing as present end-to-end competitiveness on
the compiled scope that the paper actually validates. When measured on the
current positive `D0` suites, the lowered `exec_trace` path still has a median
cost of roughly `6458 ns/step`, compared with about `6028 ns/step` for the
bytecode path and `3540 ns/step` for the best current reference/oracle path.
The correct conclusion is therefore mixed and operational: the specialized
retrieval mechanism is real, but on the present validated scope it does not yet
justify broader frontend widening or a general system-superiority claim.

## Compiled boundary section stub

The compiled result should be presented as an endpoint, not as a teaser. The
current paper validates a tiny typed-bytecode `D0` slice with deterministic
verification, exact-trace and exact-final-state agreement on the frozen starter
suite, one stress/reference follow-up tied to a standalone Python spec oracle,
and appendix-level memory-surface diagnostics that help audit the boundary
without widening it. This is sufficient for a first compiled boundary claim,
but not for a broader source-language claim. The subsequent `M7` decision is
therefore not an administrative footnote; it is part of the scientific
conclusion. Because the systems gate remains mixed and because the current
evidence bundle already closes the narrow compiled claim, the project stops at
tiny typed bytecode rather than widening toward Wasm-like or arbitrary-C
language coverage.
