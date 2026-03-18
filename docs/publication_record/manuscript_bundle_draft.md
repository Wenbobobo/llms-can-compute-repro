# Manuscript Bundle Draft

Status: section-ordered draft bundle for monotonic expansion after the `M7`
no-go decision. This file is not final paper prose, but future drafting should
prefer extending it over re-planning section scope.

## 1. Abstract

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

## 2. Introduction and Claim Ladder

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

Main items:
- claim ladder + evidence matrix;
- supported vs unsupported claims table.

Boundary note:
- unsupported claims are outputs of the paper, not future-work placeholders.

## 3. Methods: Trace Substrate and Exact Retrieval

Section target:
- define append-only traces, exact latest-write retrieval, and the reference
  execution setting as mechanism primitives rather than as a finished system
  claim.

Required beats:
- tie this section to `A1` and `B1`;
- use the geometry benchmark only to establish the retrieval signal;
- keep broader runtime or language claims out of the methods framing.

## 4. Executor Branches and Negative Controls

Section target:
- compare exact/reference branches, staged branches, and negative controls on
  the axis that matters here: free-running exactness.

Required beats:
- distinguish teacher-forced success from free-running success;
- show why softmax baselines remain informative negative controls;
- avoid model-leaderboard framing.

Main items:
- staged decode regime comparison;
- negative-control comparison.

## 5. Mask Dependence and Failure Provenance

Section target:
- explain why the fair staged positive claim does not survive the widened
  suite.

Required beats:
- state that `opcode_shape` and later `step_budget` do not define surviving
  fair regimes;
- use provenance to show that later nontermination is downstream of earlier
  semantic divergence.

Main item:
- provenance-backed staged failure taxonomy figure.

## 6. Precision Boundary on Real / Organic Traces

Section target:
- present the `C3e` boundary as a suite-specific positive-with-boundary result.

Required beats:
- single-head fails early on many current streams;
- decomposition remains exact on the validated suite;
- broader long-horizon robustness remains unsupported.

Main items:
- real-trace precision boundary figure;
- real-trace precision boundary table.

## 7. Systems Gate

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

Current layout choice:
- keep `R2` as a main-text paragraph with quantitative sentences;
- keep the full baseline matrix and runtime rows out of the main text unless a
  later layout pass specifically promotes a compact table.

## 8. Compiled Boundary

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

Main items:
- frontend boundary diagram;
- exact-trace / final-state success table.

Appendix companions:
- memory-surface diagnostics;
- stress/reference companion rows beyond the main `D0` summary.

## 9. Negative Results and Threats

Section target:
- unify unsupported claims, failed baselines, staged closure, narrow precision,
  and mixed systems value into one explicit boundary statement.

Required beats:
- keep `negative_results.md` and `threats_to_validity.md` aligned;
- state that mixed systems evidence remains part of the argument;
- avoid recasting blocked claims as deferred engineering tasks.

Main item:
- threats-to-validity table.

## 10. Reproducibility Appendix

Section target:
- collect regeneration commands, artifact ledgers, public-safe packaging
  boundaries, and companion diagnostics.

Required beats:
- point to `experiment_manifest.md` and `results/P1_paper_readiness/`;
- keep release-hygiene details downstream of the scientific argument;
- preserve appendix-only placement for memory-surface and per-stream precision
  artifacts.
