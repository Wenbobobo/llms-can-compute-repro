# Open Questions

- How close should the baseline stay to the field note's tiny PyTorch snippet
  once training actually starts?
- Should the first baseline training run use the current verbose structured
  event serialization, or a more compact tokenization that still preserves
  interpretability?
- Is the right next move factorized numeric tokenization, a larger model, or a
  different prompt/rollout boundary given that teacher-forced metrics improved
  but free-running exact rollout stayed at zero?
