# Scripts

- `benchmark_geometry.py` — compare brute-force hard-max lookup with
  `HullKVCache`
- `export_runtime_environment.py` — record the current Python/Torch/CUDA runtime
- `export_m4_free_running.py` — export the exact free-running executor artifact
- `export_m4_induced_causal.py` — export the induced structured transition
  executor artifact
- `export_m4_factorized_event_decoder.py` — export the richer direct
  event-value decoder artifact
- `export_m4_precision_stress.py` — export finite-precision addressing sweeps
- `export_m4_real_trace_precision.py` — export finite-precision checks over
  real trace streams
- `export_m5_dataset_preview.py` — export the softmax-baseline dataset preview
- `export_m5_training_run.py` — train and export the first runnable softmax
  baseline checkpoint
- `export_m5_event_level_baseline.py` — train and export the final event-level
  standard softmax baseline
- `export_p3_paper_freeze.py` — export the paper-freeze claim/artifact map
- `export_h0_release_hygiene.py` — export the current release-hygiene audit
  and preferred commit split
- `export_m7_frontend_candidate_decision.py` — export the post-`P3/R1/R2`
  frontend no-go / candidate decision bundle
- `export_p4_blog_release_gate.py` — export the outward blog/README release
  gate and public-claim audit
- `export_r1_precision_mechanism_closure.py` — export the unified precision
  boundary closure bundle
- `export_r2_systems_baseline_gate.py` — profile the current systems gate and
  emit a stop/go baseline bundle
- `setup_unattended_worktrees.ps1` — create the default unattended worktree
  layout after the tree is clean enough to branch
