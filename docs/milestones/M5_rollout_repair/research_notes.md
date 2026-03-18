# Research Notes

- Factorization reduced vocab sharply but stretched sequences too far.
- Event grouping shortened the sequence and improved teacher forcing slightly,
  but did not surpass factorized rollout behavior.
- The next M5 decision should be about architecture or branch termination, not
  more ad hoc token tweaks.
