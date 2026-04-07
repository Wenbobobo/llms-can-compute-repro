from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


def _load_module():
    module_path = (
        Path(__file__).resolve().parents[1]
        / "scripts"
        / "export_p87_post_p86_paper_spine_refresh_and_salvage_shortlist.py"
    )
    assert module_path.exists(), f"missing exporter: {module_path}"
    spec = importlib.util.spec_from_file_location(
        "export_p87_post_p86_paper_spine_refresh_and_salvage_shortlist",
        module_path,
    )
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_export_p87_writes_paper_spine_refresh_summary(tmp_path: Path, monkeypatch) -> None:
    module = _load_module()

    temp_p86 = tmp_path / "p86_summary.json"
    temp_p86.write_text(
        json.dumps(
            {
                "summary": {
                    "selected_outcome": "dirty_root_inventory_and_archive_replace_map_after_p85",
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
                "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
                "wip/p85-post-p84-main-rebaseline",
                "paper spine refresh",
                "salvage shortlist",
            ]
        ),
        "STATUS.md": "\n".join(
            [
                "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
                "paper spine refresh",
                "salvage shortlist",
                "archive-then-replace closeout",
            ]
        ),
        "docs/README.md": "\n".join(
            [
                "H65 + P87 + P86 + P85",
                "publication_record/current_stage_driver.md",
                "branch_worktree_registry.md",
                "plans/README.md",
            ]
        ),
        "docs/plans/README.md": "\n".join(
            [
                "2026-04-07-post-p87-next-planmode-handoff.md",
                "2026-04-07-post-p87-next-planmode-startup-prompt.md",
                "2026-04-07-post-p87-next-planmode-brief-prompt.md",
                "P87",
            ]
        ),
        "docs/milestones/README.md": "\n".join(
            [
                "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
                "P86_post_p85_dirty_root_inventory_and_archive_replace_map",
                "P85_post_p84_main_rebaseline_and_control_resync",
            ]
        ),
        "docs/publication_record/README.md": "\n".join(
            [
                "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
                "paper_bundle_status.md",
                "root_salvage_shortlist.md",
                "release_summary_draft.md",
            ]
        ),
        "docs/publication_record/current_stage_driver.md": "\n".join(
            [
                "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
                "paper spine refresh",
                "salvage shortlist",
                "archive-then-replace closeout",
            ]
        ),
        "docs/publication_record/paper_bundle_status.md": "\n".join(
            [
                "H65_post_p66_p67_p68_archive_first_terminal_freeze_packet",
                "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
                "P86_post_p85_dirty_root_inventory_and_archive_replace_map",
                "value-negative closeout",
            ]
        ),
        "docs/publication_record/release_summary_draft.md": "\n".join(
            [
                "narrow execution-substrate claim",
                "H65_post_p66_p67_p68_archive_first_terminal_freeze_packet",
                "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
                "dormant non-runtime dossier",
            ]
        ),
        "docs/publication_record/root_salvage_shortlist.md": "\n".join(
            [
                "salvage now",
                "paper_bundle_status.md",
                "release_summary_draft.md",
                "claim_evidence_table.md",
            ]
        ),
        "docs/plans/2026-04-07-post-p87-next-planmode-handoff.md": "\n".join(
            [
                "wip/p85-post-p84-main-rebaseline",
                "selective salvage import",
                "docs consolidation",
                "archive-then-replace closeout",
            ]
        ),
        "docs/plans/2026-04-07-post-p87-next-planmode-startup-prompt.md": "\n".join(
            [
                "wip/p85-post-p84-main-rebaseline",
                "selective salvage import",
                "archive-then-replace closeout",
            ]
        ),
        "docs/plans/2026-04-07-post-p87-next-planmode-brief-prompt.md": "\n".join(
            [
                "p85-post-p84-main-rebaseline",
                "selective salvage import",
                "archive-then-replace closeout",
            ]
        ),
    }
    for relative, body in docs.items():
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body + "\n", encoding="utf-8")

    temp_out_dir = tmp_path / "results" / "P87_post_p86_paper_spine_refresh_and_salvage_shortlist"
    original_out_dir = module.OUT_DIR
    original_root = module.ROOT
    original_p86_path = module.P86_SUMMARY_PATH
    module.OUT_DIR = temp_out_dir
    module.ROOT = tmp_path
    module.P86_SUMMARY_PATH = temp_p86

    monkeypatch.setattr(
        module,
        "git_output",
        lambda args: {
            ("rev-parse", "--abbrev-ref", "HEAD"): "wip/p85-post-p84-main-rebaseline",
            ("rev-parse", "--short", "HEAD"): "e87abc1",
            ("rev-parse", "--short", "origin/main"): "b82b566",
            ("rev-list", "--left-right", "--count", "origin/main...HEAD"): "0 3",
        }[tuple(args)],
    )
    monkeypatch.setattr(module, "environment_payload", lambda: {"runtime_detection": "test"})

    try:
        module.main()
    finally:
        module.OUT_DIR = original_out_dir
        module.ROOT = original_root
        module.P86_SUMMARY_PATH = original_p86_path

    payload = json.loads((temp_out_dir / "summary.json").read_text(encoding="utf-8"))
    assert payload["summary"]["selected_outcome"] == "paper_spine_refreshed_and_salvage_shortlist_synced_after_p86"
    assert payload["summary"]["blocked_count"] == 0
