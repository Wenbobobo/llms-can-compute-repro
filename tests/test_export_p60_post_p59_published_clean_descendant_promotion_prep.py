from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys


def _load_module():
    module_path = (
        Path(__file__).resolve().parents[1]
        / "scripts"
        / "export_p60_post_p59_published_clean_descendant_promotion_prep.py"
    )
    spec = importlib.util.spec_from_file_location(
        "export_p60_post_p59_published_clean_descendant_promotion_prep",
        module_path,
    )
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_export_p60_writes_published_clean_descendant_prep_summary(tmp_path: Path) -> None:
    module = _load_module()
    original_out_dir = module.OUT_DIR
    temp_out_dir = tmp_path / "P60_post_p59_published_clean_descendant_promotion_prep"
    module.OUT_DIR = temp_out_dir
    try:
        module.main()
    finally:
        module.OUT_DIR = original_out_dir

    payload = json.loads((temp_out_dir / "summary.json").read_text(encoding="utf-8"))
    assert payload["summary"]["selected_outcome"] == "published_clean_descendant_promotion_prep_locked_after_p59"
    assert payload["summary"]["merge_execution_state"] is False
    assert payload["summary"]["blocked_count"] == 0
