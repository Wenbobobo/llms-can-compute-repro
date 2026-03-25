from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


def _load_export_module():
    module_path = (
        Path(__file__).resolve().parents[1]
        / "scripts"
        / "export_p39_post_h54_successor_worktree_hygiene_sync.py"
    )
    spec = importlib.util.spec_from_file_location(
        "export_p39_post_h54_successor_worktree_hygiene_sync",
        module_path,
    )
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_export_p39_writes_saved_successor_hygiene_packet(tmp_path: Path) -> None:
    module = _load_export_module()
    original_out_dir = module.OUT_DIR
    temp_out_dir = tmp_path / "P39_post_h54_successor_worktree_hygiene_sync"
    module.OUT_DIR = temp_out_dir

    try:
        module.main()
    finally:
        module.OUT_DIR = original_out_dir

    payload = json.loads((temp_out_dir / "summary.json").read_text(encoding="utf-8"))
    checklist_rows = json.loads((temp_out_dir / "checklist.json").read_text(encoding="utf-8"))["rows"]
    claim_packet = json.loads((temp_out_dir / "claim_packet.json").read_text(encoding="utf-8"))["summary"]
    snapshot_rows = json.loads((temp_out_dir / "snapshot.json").read_text(encoding="utf-8"))["rows"]

    assert payload["summary"]["current_active_stage"] == "h54_post_r58_r59_compiled_boundary_decision_packet"
    assert payload["summary"]["current_low_priority_wave"] == "p38_post_h52_compiled_boundary_hygiene_sync"
    assert payload["summary"]["saved_successor_hygiene_packet"] == (
        "p39_post_h54_successor_worktree_hygiene_sync"
    )
    assert payload["summary"]["selected_outcome"] == "successor_worktree_hygiene_packet_saved_not_activated"
    assert payload["summary"]["tracked_large_artifact_count"] == 0
    assert payload["summary"]["blocked_count"] == 0
    assert payload["summary"]["pass_count"] == len(checklist_rows)
    assert claim_packet["distilled_result"]["current_low_priority_wave"] == (
        "p38_post_h52_compiled_boundary_hygiene_sync"
    )
    assert len(snapshot_rows) == 6

