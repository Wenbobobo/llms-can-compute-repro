# Acceptance

- Every variant must report exact rollout, not only teacher forcing.
- A representation change counts as progress only if it shifts either exact
  rollout or first-error behavior in a meaningful way.
- If exact rollout stays zero after the next targeted intervention, the branch
  should be frozen as a negative control.
