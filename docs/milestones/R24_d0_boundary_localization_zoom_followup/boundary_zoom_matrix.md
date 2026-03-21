# Boundary Zoom Matrix

## Purpose

This file turns the post-`R21/R22/H21` boundary story into one bounded
planning-only handoff. It does not authorize execution. It records where a
later explicit reopen should zoom first if the project wants a tighter answer
than “the bounded grid still stayed exact.”

## Candidate Core

The future reopen should not start from the full historical grid again. It
should start from one compact five-family candidate core that preserves both
`R22` lane classes:

| Family | Role | Anchor setting | Why it stays in the core |
| --- | --- | --- | --- |
| `checkpoint_replay_long` | extended probe | `u32 / h3.0 / plus_two / flattened` | hardest surviving address/horizon-style exact row from the current packet |
| `helper_checkpoint_braid_long` | extended probe | `u20 / h3.0 / plus_two / flattened` | keeps the long braid family that already mattered in prior runtime work |
| `subroutine_braid_long` | extended probe | `u20 / h3.0 / plus_two / flattened` | keeps the long call/control family in the candidate core |
| `helper_checkpoint_braid` | continuity anchor | `u8 / h2.0 / plus_one / flattened` | preserves one shorter braid anchor so a later failure can still be localized against a nearby exact row |
| `subroutine_braid` | continuity anchor | `u6 / h2.0 / plus_one / flattened` | preserves one shorter subroutine/control anchor for the same reason |

## Zoom Axes

The first later reopen should keep the four already justified `R21/R22` axes:

- `unique_address_target`
- `horizon_multiplier`
- `checkpoint_depth`
- `hot_address_skew`

The rule is to push beyond the current maxima, not to re-scan the whole box.

| Axis | Current ceiling carried from `R22` | First later zoom target |
| --- | --- | --- |
| `unique_address_target` | up to `32` on `checkpoint_replay_long`; up to `20` on long braid families | push beyond those family-local maxima first |
| `horizon_multiplier` | up to `3.0` | push beyond `3.0` first |
| `checkpoint_depth` | up to `plus_two` | push beyond `plus_two` first |
| `hot_address_skew` | `baseline`, `flattened` | keep both, but prioritize `flattened` because the hardest surviving exact rows already live there |

If a fifth axis is added later, it should stay family-local and generator-local,
for example read/write interleaving or control-flow density on existing
families only. It should not introduce new families or a wider endpoint.

## Stop Rules

- Stop a branch after `2` reproduced exactness failures.
- Stop the whole lane if every candidate-core branch either fails cleanly or
  exhausts the predeclared zoom matrix without a failure.
- Require one `first_fail` plus at least one neighboring exact row before any
  claim of boundary localization.
- If no failure appears, end with a principled no-localization verdict rather
  than expanding again by momentum.

## Predeclared Verdict Vocabulary

- `first_boundary_failure_localized`
- `near_boundary_mixed_signal_needs_confirmation`
- `grid_extended_still_not_localized`
- `resource_limited_before_localization`
