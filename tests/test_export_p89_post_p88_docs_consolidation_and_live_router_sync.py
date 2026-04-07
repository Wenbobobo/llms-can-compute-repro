from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


def _load_module():
    module_path = (
        Path(__file__).resolve().parents[1]
        / "scripts"
        / "export_p89_post_p88_docs_consolidation_and_live_router_sync.py"
    )
    assert module_path.exists(), f"missing exporter: {module_path}"
    spec = importlib.util.spec_from_file_location(
        "export_p89_post_p88_docs_consolidation_and_live_router_sync",
        module_path,
    )
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_export_p89_writes_docs_consolidation_summary(tmp_path: Path, monkeypatch) -> None:
    module = _load_module()

    temp_p88 = tmp_path / "p88_summary.json"
    temp_p88.write_text(
        json.dumps(
            {
                "summary": {
                    "selected_outcome": "salvage_screen_completed_with_no_import_for_first_tier_docs",
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
                "P89_post_p88_docs_consolidation_and_live_router_sync",
                "wip/p85-post-p84-main-rebaseline",
                "docs consolidation",
                "archive-then-replace closeout",
            ]
        ),
        "STATUS.md": "\n".join(
            [
                "P89_post_p88_docs_consolidation_and_live_router_sync",
                "P88_post_p87_salvage_screen_and_no_import_decision",
                "archive-then-replace closeout",
                "explicit stop",
            ]
        ),
        "docs/README.md": "\n".join(
            [
                "H65 + P89 + P88 + P87 + P86 + P85",
                "publication_record/current_stage_driver.md",
                "branch_worktree_registry.md",
                "plans/README.md",
            ]
        ),
        "docs/branch_worktree_registry.md": "\n".join(
            [
                "P89_post_p88_docs_consolidation_and_live_router_sync",
                "wip/p85-post-p84-main-rebaseline",
                "archive-then-replace closeout",
                "file-specific salvage case",
            ]
        ),
        "docs/plans/README.md": "\n".join(
            [
                "2026-04-07-post-p89-next-planmode-handoff.md",
                "2026-04-07-post-p89-next-planmode-startup-prompt.md",
                "2026-04-07-post-p89-next-planmode-brief-prompt.md",
                "P89",
            ]
        ),
        "docs/milestones/README.md": "\n".join(
            [
                "P89_post_p88_docs_consolidation_and_live_router_sync",
                "P88_post_p87_salvage_screen_and_no_import_decision",
                "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
            ]
        ),
        "docs/publication_record/README.md": "\n".join(
            [
                "P89_post_p88_docs_consolidation_and_live_router_sync",
                "current_stage_driver.md",
                "root_salvage_shortlist.md",
                "partial_falsification_boundary.md",
            ]
        ),
        "docs/publication_record/current_stage_driver.md": "\n".join(
            [
                "P89_post_p88_docs_consolidation_and_live_router_sync",
                "docs consolidation",
                "archive-then-replace closeout",
                "explicit stop",
            ]
        ),
        "docs/plans/2026-04-07-post-p89-next-planmode-handoff.md": "\n".join(
            [
                "wip/p85-post-p84-main-rebaseline",
                "archive-then-replace closeout",
                "explicit stop",
                "file-specific salvage case",
            ]
        ),
        "docs/plans/2026-04-07-post-p89-next-planmode-startup-prompt.md": "\n".join(
            [
                "wip/p85-post-p84-main-rebaseline",
                "archive-then-replace closeout",
                "explicit stop",
            ]
        ),
        "docs/plans/2026-04-07-post-p89-next-planmode-brief-prompt.md": "\n".join(
            [
                "p85-post-p84-main-rebaseline",
                "archive-then-replace closeout",
                "explicit stop",
            ]
        ),
    }
    for relative, body in docs.items():
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body + "\n", encoding="utf-8")

    temp_out_dir = tmp_path / "results" / "P89_post_p88_docs_consolidation_and_live_router_sync"
    original_out_dir = module.OUT_DIR
    original_root = module.ROOT
    original_p88_path = module.P88_SUMMARY_PATH
    module.OUT_DIR = temp_out_dir
    module.ROOT = tmp_path
    module.P88_SUMMARY_PATH = temp_p88

    monkeypatch.setattr(
        module,
        "git_output",
        lambda args: {
            ("rev-parse", "--abbrev-ref", "HEAD"): "wip/p85-post-p84-main-rebaseline",
            ("rev-parse", "--short", "HEAD"): "p89abc1",
            ("rev-parse", "--short", "origin/main"): "b82b566",
            ("rev-list", "--left-right", "--count", "origin/main...HEAD"): "0 5",
        }[tuple(args)],
    )
    monkeypatch.setattr(module, "environment_payload", lambda: {"runtime_detection": "test"})

    try:
        module.main()
    finally:
        module.OUT_DIR = original_out_dir
        module.ROOT = original_root
        module.P88_SUMMARY_PATH = original_p88_path

    payload = json.loads((temp_out_dir / "summary.json").read_text(encoding="utf-8"))
    assert payload["summary"]["selected_outcome"] == "docs_consolidation_and_live_router_sync_after_p88"
    assert payload["summary"]["blocked_count"] == 0
    assert payload["summary"]["router_docs_checked"] == 11
    assert payload["summary"]["next_recommended_route"] == "archive_then_replace_closeout_or_explicit_stop"
