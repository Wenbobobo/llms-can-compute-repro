# Open Questions

- How much context should the next decoder see without overfitting to trace
  position?
- Should the next step predict richer event fields directly, or predict a small
  rule schema plus values?
- When this branch fails on larger programs, will the first fault be branch,
  memory, or halting behavior?
