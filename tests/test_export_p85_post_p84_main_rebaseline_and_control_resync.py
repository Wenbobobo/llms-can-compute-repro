from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


def _load_module():
    module_path = (
        Path(__file__).resolve().parents[1]
        / "scripts"
        / "export_p85_post_p84_main_rebaseline_and_control_resync.py"
    )
    spec = importlib.util.spec_from_file_location(
        "export_p85_post_p84_main_rebaseline_and_control_resync",
        module_path,
    )
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_export_p85_writes_post_merge_rebaseline_summary(tmp_path: Path, monkeypatch) -> None:
    module = _load_module()

    temp_p84 = tmp_path / "p84_summary.json"
    temp_p84.write_text(
        json.dumps(
            {
                "summary": {
                    "selected_outcome": "keep_set_contracted_and_closeout_synced_after_p83",
                    "blocked_count": 0,
                }
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    docs = {
        "README.md": "\n".join(
            [
                "P85_post_p84_main_rebaseline_and_control_resync",
                "wip/p85-post-p84-main-rebaseline",
                "P84_post_p83_keep_set_contraction_and_closeout",
                "P83_post_p82_promotion_branch_and_pr_handoff",
            ]
        ),
        "STATUS.md": "\n".join(
            [
                "P85_post_p84_main_rebaseline_and_control_resync",
                "wip/p85-post-p84-main-rebaseline",
                "wip/p83-post-p82-promotion-branch-and-pr-handoff",
                "root-main-parking-2026-03-24",
            ]
        ),
        "docs/README.md": "\n".join(
            [
                "H65 + P85 + P84 + P83",
                "publication_record/current_stage_driver.md",
                "branch_worktree_registry.md",
                "plans/README.md",
            ]
        ),
        "docs/branch_worktree_registry.md": "\n".join(
            [
                "wip/p85-post-p84-main-rebaseline",
                "wip/p83-post-p82-promotion-branch-and-pr-handoff",
                "preserved merged-source lineage",
                "root-main-parking-2026-03-24",
            ]
        ),
        "docs/plans/README.md": "\n".join(
            [
                "2026-04-07-post-p85-next-planmode-handoff.md",
                "2026-04-07-post-p85-next-planmode-startup-prompt.md",
                "2026-04-07-post-p85-next-planmode-brief-prompt.md",
                "P85",
            ]
        ),
        "docs/milestones/README.md": "\n".join(
            [
                "P85_post_p84_main_rebaseline_and_control_resync",
                "P84_post_p83_keep_set_contraction_and_closeout",
                "P83_post_p82_promotion_branch_and_pr_handoff",
            ]
        ),
        "docs/publication_record/README.md": "\n".join(
            [
                "P85_post_p84_main_rebaseline_and_control_resync",
                "current_stage_driver.md",
                "paper_bundle_status.md",
            ]
        ),
        "docs/publication_record/current_stage_driver.md": "\n".join(
            [
                "P85_post_p84_main_rebaseline_and_control_resync",
                "wip/p85-post-p84-main-rebaseline",
                "preserved merged-source branch",
                "wip/p83-post-p82-promotion-branch-and-pr-handoff",
            ]
        ),
        "docs/plans/2026-04-07-post-p85-next-planmode-handoff.md": "\n".join(
            [
                "wip/p85-post-p84-main-rebaseline",
                "root archive/replace",
                "docs consolidation",
                "paper spine refresh",
            ]
        ),
        "docs/plans/2026-04-07-post-p85-next-planmode-startup-prompt.md": "\n".join(
            [
                "wip/p85-post-p84-main-rebaseline",
                "root archive/replace",
                "paper spine refresh",
            ]
        ),
        "docs/plans/2026-04-07-post-p85-next-planmode-brief-prompt.md": "\n".join(
            [
                "p85-post-p84-main-rebaseline",
                "root archive/replace",
                "paper spine refresh",
            ]
        ),
    }
    for relative, body in docs.items():
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body + "\n", encoding="utf-8")

    temp_out_dir = tmp_path / "results" / "P85_post_p84_main_rebaseline_and_control_resync"
    original_out_dir = module.OUT_DIR
    original_root = module.ROOT
    original_p84_path = module.P84_SUMMARY_PATH
    module.OUT_DIR = temp_out_dir
    module.ROOT = tmp_path
    module.P84_SUMMARY_PATH = temp_p84

    monkeypatch.setattr(
        module,
        "git_output",
        lambda args: {
            ("rev-parse", "--abbrev-ref", "HEAD"): "wip/p85-post-p84-main-rebaseline",
            ("rev-parse", "--short", "HEAD"): "c1a2b3d",
            ("rev-parse", "--short", "origin/main"): "b82b566",
            ("rev-list", "--left-right", "--count", "origin/main...HEAD"): "0 1",
            ("worktree", "list", "--porcelain"): "\n".join(
                [
                    "worktree D:/zWenbo/AI/LLMCompute",
                    "HEAD 56ff106",
                    "branch refs/heads/wip/root-main-parking-2026-03-24",
                    "",
                    "worktree D:/zWenbo/AI/LLMCompute-worktrees/h27-promotion",
                    "HEAD eaa4fb0",
                    "branch refs/heads/wip/h27-promotion",
                    "",
                    "worktree D:/zWenbo/AI/wt/p56-main-scratch",
                    "HEAD eff98f8",
                    "branch refs/heads/wip/p56-main-scratch",
                    "",
                    "worktree D:/zWenbo/AI/wt/p69-post-h65-hygiene-only-cleanup",
                    "HEAD 55c7bb7",
                    "branch refs/heads/wip/p69-post-h65-hygiene-only-cleanup",
                    "",
                    "worktree D:/zWenbo/AI/wt/p72-post-p71-archive-polish-stop-handoff",
                    "HEAD bc03069",
                    "branch refs/heads/wip/p72-post-p71-archive-polish-stop-handoff",
                    "",
                    "worktree D:/zWenbo/AI/wt/p73-post-p72-hygiene-shrink-mergeprep",
                    "HEAD b45902e",
                    "branch refs/heads/wip/p73-post-p72-hygiene-shrink-mergeprep",
                    "",
                    "worktree D:/zWenbo/AI/wt/p74-post-p73-successor-publication-review",
                    "HEAD ad03aca",
                    "branch refs/heads/wip/p74-post-p73-successor-publication-review",
                    "",
                    "worktree D:/zWenbo/AI/wt/p75-post-p74-published-successor-freeze",
                    "HEAD 53962ca",
                    "branch refs/heads/wip/p75-post-p74-published-successor-freeze",
                    "",
                    "worktree D:/zWenbo/AI/wt/p83-post-p82-promotion-branch-and-pr-handoff",
                    "HEAD 91c2800",
                    "branch refs/heads/wip/p83-post-p82-promotion-branch-and-pr-handoff",
                    "",
                    "worktree D:/zWenbo/AI/wt/p85-post-p84-main-rebaseline",
                    "HEAD c1a2b3d",
                    "branch refs/heads/wip/p85-post-p84-main-rebaseline",
                    "",
                ]
            ),
        }[tuple(args)],
    )
    monkeypatch.setattr(module, "environment_payload", lambda: {"runtime_detection": "test"})

    try:
        module.main()
    finally:
        module.OUT_DIR = original_out_dir
        module.ROOT = original_root
        module.P84_SUMMARY_PATH = original_p84_path

    payload = json.loads((temp_out_dir / "summary.json").read_text(encoding="utf-8"))
    assert payload["summary"]["selected_outcome"] == "merged_main_rebaseline_and_control_resync_after_p84"
    assert payload["summary"]["blocked_count"] == 0
