"""Export the post-P88 docs-consolidation and live-router sync packet for P89."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

from utils import detect_runtime_environment


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "results" / "P89_post_p88_docs_consolidation_and_live_router_sync"
P88_SUMMARY_PATH = ROOT / "results" / "P88_post_p87_salvage_screen_and_no_import_decision" / "summary.json"
CURRENT_BRANCH = "wip/p85-post-p84-main-rebaseline"
DOC_REQUIREMENTS = {
    "README.md": [
        "P89_post_p88_docs_consolidation_and_live_router_sync",
        CURRENT_BRANCH,
        "docs consolidation",
        "archive-then-replace closeout",
    ],
    "STATUS.md": [
        "P89_post_p88_docs_consolidation_and_live_router_sync",
        "P88_post_p87_salvage_screen_and_no_import_decision",
        "archive-then-replace closeout",
        "explicit stop",
    ],
    "docs/README.md": [
        "H65 + P89 + P88 + P87 + P86 + P85",
        "publication_record/current_stage_driver.md",
        "branch_worktree_registry.md",
        "plans/README.md",
    ],
    "docs/branch_worktree_registry.md": [
        "P89_post_p88_docs_consolidation_and_live_router_sync",
        CURRENT_BRANCH,
        "archive-then-replace closeout",
        "file-specific salvage case",
    ],
    "docs/plans/README.md": [
        "2026-04-07-post-p89-next-planmode-handoff.md",
        "2026-04-07-post-p89-next-planmode-startup-prompt.md",
        "2026-04-07-post-p89-next-planmode-brief-prompt.md",
        "P89",
    ],
    "docs/milestones/README.md": [
        "P89_post_p88_docs_consolidation_and_live_router_sync",
        "P88_post_p87_salvage_screen_and_no_import_decision",
        "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
    ],
    "docs/publication_record/README.md": [
        "P89_post_p88_docs_consolidation_and_live_router_sync",
        "current_stage_driver.md",
        "root_salvage_shortlist.md",
        "partial_falsification_boundary.md",
    ],
    "docs/publication_record/current_stage_driver.md": [
        "P89_post_p88_docs_consolidation_and_live_router_sync",
        "docs consolidation",
        "archive-then-replace closeout",
        "explicit stop",
    ],
    "docs/plans/2026-04-07-post-p89-next-planmode-handoff.md": [
        CURRENT_BRANCH,
        "archive-then-replace closeout",
        "explicit stop",
        "file-specific salvage case",
    ],
    "docs/plans/2026-04-07-post-p89-next-planmode-startup-prompt.md": [
        CURRENT_BRANCH,
        "archive-then-replace closeout",
        "explicit stop",
    ],
    "docs/plans/2026-04-07-post-p89-next-planmode-brief-prompt.md": [
        "p85-post-p84-main-rebaseline",
        "archive-then-replace closeout",
        "explicit stop",
    ],
}


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def environment_payload() -> dict[str, object]:
    try:
        return detect_runtime_environment().as_dict()
    except Exception as exc:  # pragma: no cover
        return {"runtime_detection": "fallback", "error": f"{type(exc).__name__}: {exc}"}


def git_output(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=str(ROOT),
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout.strip()


def normalize(text: str) -> str:
    return " ".join(text.split()).lower()


def contains_all(text: str, needles: list[str]) -> bool:
    lowered = normalize(text)
    return all(normalize(needle) in lowered for needle in needles)


def ahead_behind(left: str, right: str) -> dict[str, int]:
    left_only, right_only = git_output(["rev-list", "--left-right", "--count", f"{left}...{right}"]).split()
    return {"left_only": int(left_only), "right_only": int(right_only)}


def doc_sync_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for relative_path, needles in DOC_REQUIREMENTS.items():
        path = ROOT / relative_path
        exists = path.exists()
        text = read_text(path) if exists else ""
        rows.append(
            {
                "path": relative_path,
                "exists": exists,
                "needle_count": len(needles),
                "ok": exists and contains_all(text, needles),
            }
        )
    return rows


def main() -> None:
    p88_summary = read_json(P88_SUMMARY_PATH)["summary"]
    if p88_summary["selected_outcome"] != "salvage_screen_completed_with_no_import_for_first_tier_docs":
        raise RuntimeError("P89 expects the landed green P88 no-import summary.")
    if p88_summary["blocked_count"] != 0:
        raise RuntimeError("P89 expects a green P88 summary before router consolidation.")

    current_branch_name = git_output(["rev-parse", "--abbrev-ref", "HEAD"])
    current_head = git_output(["rev-parse", "--short", "HEAD"])
    origin_main_head = git_output(["rev-parse", "--short", "origin/main"])
    branch_divergence = ahead_behind("origin/main", "HEAD")
    doc_rows = doc_sync_rows()

    checklist_rows = [
        {
            "item_id": "p89_reads_green_p88_summary",
            "status": "pass",
            "notes": "P89 begins only after the landed green P88 no-import decision.",
        },
        {
            "item_id": "p89_runs_on_clean_p85_branch",
            "status": "pass" if current_branch_name == CURRENT_BRANCH else "blocked",
            "notes": "Docs consolidation must run from the clean p85 branch.",
        },
        {
            "item_id": "p89_live_docs_shift_current_control_to_docs_consolidation_wave",
            "status": "pass" if all(bool(row["ok"]) for row in doc_rows) else "blocked",
            "notes": "Routers and handoff surfaces should make P89 the current docs-consolidation wave.",
        },
    ]

    claim_packet = {
        "supports": [
            "P89 consolidates the live router surfaces around the H65 plus P89 posture on the clean p85 branch.",
            "P89 preserves P88 as the first-tier no-import decision underneath the current docs-consolidation wave.",
            "P89 narrows the next route to archive-then-replace closeout or explicit stop unless a later file-specific salvage case appears.",
        ],
        "does_not_support": [
            "dirty-root integration",
            "runtime reopen",
            "same-lane executor-value reopen",
            "broad Wasm or arbitrary C scope expansion",
        ],
        "distilled_result": {
            "current_docs_wave": "p89_post_p88_docs_consolidation_and_live_router_sync",
            "current_branch": CURRENT_BRANCH,
            "current_branch_head": current_head,
            "merged_main_head": origin_main_head,
            "origin_main_to_p89_left_right": f"{branch_divergence['left_only']}/{branch_divergence['right_only']}",
            "selected_outcome": "docs_consolidation_and_live_router_sync_after_p88",
            "next_recommended_route": "archive_then_replace_closeout_or_explicit_stop",
        },
    }
    summary = {
        "summary": {
            **claim_packet["distilled_result"],
            "router_docs_checked": len(doc_rows),
            "pass_count": sum(row["status"] == "pass" for row in checklist_rows),
            "blocked_count": sum(row["status"] != "pass" for row in checklist_rows),
        },
        "runtime_environment": environment_payload(),
    }
    snapshot = {
        "rows": [
            {"field": "p88_summary", "value": p88_summary},
            {"field": "branch_divergence", "value": branch_divergence},
            {"field": "doc_sync_rows", "value": doc_rows},
        ]
    }

    write_json(OUT_DIR / "checklist.json", {"rows": checklist_rows})
    write_json(OUT_DIR / "claim_packet.json", {"summary": claim_packet})
    write_json(OUT_DIR / "snapshot.json", snapshot)
    write_json(OUT_DIR / "summary.json", summary)


if __name__ == "__main__":
    main()
