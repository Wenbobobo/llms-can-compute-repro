from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


def _load_module():
    module_path = (
        Path(__file__).resolve().parents[1]
        / "scripts"
        / "export_p88_post_p87_salvage_screen_and_no_import_decision.py"
    )
    assert module_path.exists(), f"missing exporter: {module_path}"
    spec = importlib.util.spec_from_file_location(
        "export_p88_post_p87_salvage_screen_and_no_import_decision",
        module_path,
    )
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_export_p88_writes_salvage_screen_summary(tmp_path: Path, monkeypatch) -> None:
    module = _load_module()

    temp_p87 = tmp_path / "p87_summary.json"
    temp_p87.write_text(
        json.dumps(
            {
                "summary": {
                    "selected_outcome": "paper_spine_refreshed_and_salvage_shortlist_synced_after_p86",
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
                "P88_post_p87_salvage_screen_and_no_import_decision",
                "wip/p85-post-p84-main-rebaseline",
                "no-import decision",
                "docs consolidation",
            ]
        ),
        "STATUS.md": "\n".join(
            [
                "P88_post_p87_salvage_screen_and_no_import_decision",
                "no-import decision",
                "docs consolidation",
                "archive-then-replace closeout",
            ]
        ),
        "docs/README.md": "\n".join(
            [
                "H65 + P88 + P87 + P86 + P85",
                "publication_record/current_stage_driver.md",
                "branch_worktree_registry.md",
                "plans/README.md",
            ]
        ),
        "docs/plans/README.md": "\n".join(
            [
                "2026-04-07-post-p88-next-planmode-handoff.md",
                "2026-04-07-post-p88-next-planmode-startup-prompt.md",
                "2026-04-07-post-p88-next-planmode-brief-prompt.md",
                "P88",
            ]
        ),
        "docs/milestones/README.md": "\n".join(
            [
                "P88_post_p87_salvage_screen_and_no_import_decision",
                "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
                "P86_post_p85_dirty_root_inventory_and_archive_replace_map",
            ]
        ),
        "docs/publication_record/README.md": "\n".join(
            [
                "P88_post_p87_salvage_screen_and_no_import_decision",
                "root_salvage_shortlist.md",
                "review_boundary_summary.md",
                "threats_to_validity.md",
            ]
        ),
        "docs/publication_record/current_stage_driver.md": "\n".join(
            [
                "P88_post_p87_salvage_screen_and_no_import_decision",
                "no-import decision",
                "docs consolidation",
                "archive-then-replace closeout",
            ]
        ),
        "docs/publication_record/root_salvage_shortlist.md": "\n".join(
            [
                "screened and no import now",
                "claim_evidence_table.md",
                "negative_results.md",
                "review_boundary_summary.md",
                "threats_to_validity.md",
            ]
        ),
        "docs/plans/2026-04-07-post-p88-next-planmode-handoff.md": "\n".join(
            [
                "wip/p85-post-p84-main-rebaseline",
                "docs consolidation",
                "archive-then-replace closeout",
                "no-import decision",
            ]
        ),
        "docs/plans/2026-04-07-post-p88-next-planmode-startup-prompt.md": "\n".join(
            [
                "wip/p85-post-p84-main-rebaseline",
                "docs consolidation",
                "archive-then-replace closeout",
            ]
        ),
        "docs/plans/2026-04-07-post-p88-next-planmode-brief-prompt.md": "\n".join(
            [
                "p85-post-p84-main-rebaseline",
                "docs consolidation",
                "archive-then-replace closeout",
            ]
        ),
    }
    for relative, body in docs.items():
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body + "\n", encoding="utf-8")

    temp_out_dir = tmp_path / "results" / "P88_post_p87_salvage_screen_and_no_import_decision"
    original_out_dir = module.OUT_DIR
    original_root = module.ROOT
    original_p87_path = module.P87_SUMMARY_PATH
    module.OUT_DIR = temp_out_dir
    module.ROOT = tmp_path
    module.P87_SUMMARY_PATH = temp_p87

    monkeypatch.setattr(
        module,
        "git_output",
        lambda args: {
            ("rev-parse", "--abbrev-ref", "HEAD"): "wip/p85-post-p84-main-rebaseline",
            ("rev-parse", "--short", "HEAD"): "p88abc1",
            ("rev-parse", "--short", "origin/main"): "b82b566",
            ("rev-list", "--left-right", "--count", "origin/main...HEAD"): "0 4",
        }[tuple(args)],
    )
    monkeypatch.setattr(module, "environment_payload", lambda: {"runtime_detection": "test"})

    try:
        module.main()
    finally:
        module.OUT_DIR = original_out_dir
        module.ROOT = original_root
        module.P87_SUMMARY_PATH = original_p87_path

    payload = json.loads((temp_out_dir / "summary.json").read_text(encoding="utf-8"))
    assert payload["summary"]["selected_outcome"] == "salvage_screen_completed_with_no_import_for_first_tier_docs"
    assert payload["summary"]["blocked_count"] == 0
    assert payload["summary"]["screened_now_count"] == 4
    assert payload["summary"]["import_now_count"] == 0
