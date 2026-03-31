# P56 Worktree Runbook

1. start from `wip/p56-post-h64-clean-merge-candidate`, not dirty root
   `main`;
2. confirm `wip/h64-post-h63-archive-first-freeze` is synced to
   `origin/wip/h64-post-h63-archive-first-freeze`;
3. confirm dirty root `main` is still parked via
   `git worktree list --porcelain`;
4. inspect `git diff --stat main..wip/h64-post-h63-archive-first-freeze`;
5. inspect the packet-only candidate delta against
   `wip/h64-post-h63-archive-first-freeze`;
6. use `wip/p56-main-scratch` only as a clean `main` comparison snapshot;
7. perform dry conflict inspection only inside the clean descendant worktrees;
8. never treat `D:/zWenbo/AI/LLMCompute` as an integration base or conflict
   resolution source.
