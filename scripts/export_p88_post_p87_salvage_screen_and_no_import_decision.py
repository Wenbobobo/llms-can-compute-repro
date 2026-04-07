"""Export the post-P87 first-tier salvage screen and no-import decision packet for P88."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

from utils import detect_runtime_environment


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "results" / "P88_post_p87_salvage_screen_and_no_import_decision"
P87_SUMMARY_PATH = ROOT / "results" / "P87_post_p86_paper_spine_refresh_and_salvage_shortlist" / "summary.json"
CURRENT_BRANCH = "wip/p85-post-p84-main-rebaseline"
DOC_REQUIREMENTS = {
    "README.md": [
        "P88_post_p87_salvage_screen_and_no_import_decision",
        CURRENT_BRANCH,
        "no-import decision",
        "docs consolidation",
    ],
    "STATUS.md": [
        "P88_post_p87_salvage_screen_and_no_import_decision",
        "no-import decision",
        "docs consolidation",
        "archive-then-replace closeout",
    ],
    "docs/README.md": [
        "H65 + P88 + P87 + P86 + P85",
        "publication_record/current_stage_driver.md",
        "branch_worktree_registry.md",
        "plans/README.md",
    ],
    "docs/plans/README.md": [
        "2026-04-07-post-p88-next-planmode-handoff.md",
        "2026-04-07-post-p88-next-planmode-startup-prompt.md",
        "2026-04-07-post-p88-next-planmode-brief-prompt.md",
        "P88",
    ],
    "docs/milestones/README.md": [
        "P88_post_p87_salvage_screen_and_no_import_decision",
        "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
        "P86_post_p85_dirty_root_inventory_and_archive_replace_map",
    ],
    "docs/publication_record/README.md": [
        "P88_post_p87_salvage_screen_and_no_import_decision",
        "root_salvage_shortlist.md",
        "review_boundary_summary.md",
        "threats_to_validity.md",
    ],
    "docs/publication_record/current_stage_driver.md": [
        "P88_post_p87_salvage_screen_and_no_import_decision",
        "no-import decision",
        "docs consolidation",
        "archive-then-replace closeout",
    ],
    "docs/publication_record/root_salvage_shortlist.md": [
        "screened and no import now",
        "claim_evidence_table.md",
        "negative_results.md",
        "review_boundary_summary.md",
        "threats_to_validity.md",
    ],
    "docs/plans/2026-04-07-post-p88-next-planmode-handoff.md": [
        CURRENT_BRANCH,
        "docs consolidation",
        "archive-then-replace closeout",
        "no-import decision",
    ],
    "docs/plans/2026-04-07-post-p88-next-planmode-startup-prompt.md": [
        CURRENT_BRANCH,
        "docs consolidation",
        "archive-then-replace closeout",
    ],
    "docs/plans/2026-04-07-post-p88-next-planmode-brief-prompt.md": [
        "p85-post-p84-main-rebaseline",
        "docs consolidation",
        "archive-then-replace closeout",
    ],
}
SCREENED_NOW = [
    "docs/publication_record/claim_evidence_table.md",
    "docs/publication_record/negative_results.md",
    "docs/publication_record/review_boundary_summary.md",
    "docs/publication_record/threats_to_validity.md",
]


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
    p87_summary = read_json(P87_SUMMARY_PATH)["summary"]
    if p87_summary["selected_outcome"] != "paper_spine_refreshed_and_salvage_shortlist_synced_after_p86":
        raise RuntimeError("P88 expects the landed green P87 paper-spine summary.")
    if p87_summary["blocked_count"] != 0:
        raise RuntimeError("P88 expects a green P87 summary before salvage no-import decision.")

    current_branch_name = git_output(["rev-parse", "--abbrev-ref", "HEAD"])
    current_head = git_output(["rev-parse", "--short", "HEAD"])
    origin_main_head = git_output(["rev-parse", "--short", "origin/main"])
    branch_divergence = ahead_behind("origin/main", "HEAD")
    doc_rows = doc_sync_rows()

    checklist_rows = [
        {
            "item_id": "p88_reads_green_p87_summary",
            "status": "pass",
            "notes": "P88 begins only after the landed green P87 paper-spine refresh.",
        },
        {
            "item_id": "p88_runs_on_clean_p85_branch",
            "status": "pass" if current_branch_name == CURRENT_BRANCH else "blocked",
            "notes": "The no-import decision packet must run from the clean p85 branch.",
        },
        {
            "item_id": "p88_live_docs_shift_current_control_to_no_import_wave",
            "status": "pass" if all(bool(row["ok"]) for row in doc_rows) else "blocked",
            "notes": "Routers and salvage docs should make P88 the current no-import decision wave.",
        },
    ]

    screen_rows = [
        {
            "path": path,
            "decision": "no_import_now",
            "reason": "dirty-root version is stale or not materially better than the clean-branch version",
        }
        for path in SCREENED_NOW
    ]

    claim_packet = {
        "supports": [
            "P88 screens the first-tier salvage shortlist and decides no immediate imports for the four highest-value candidates.",
            "P88 narrows the next clean-branch route toward docs consolidation and archive-then-replace closeout.",
            "P88 keeps dirty root quarantine-only and treats selective salvage as optional rather than mandatory.",
        ],
        "does_not_support": [
            "dirty-root integration",
            "runtime reopen",
            "same-lane executor-value reopen",
            "broad Wasm or arbitrary C scope expansion",
        ],
        "distilled_result": {
            "current_salvage_wave": "p88_post_p87_salvage_screen_and_no_import_decision",
            "current_branch": CURRENT_BRANCH,
            "current_branch_head": current_head,
            "merged_main_head": origin_main_head,
            "origin_main_to_p88_left_right": f"{branch_divergence['left_only']}/{branch_divergence['right_only']}",
            "selected_outcome": "salvage_screen_completed_with_no_import_for_first_tier_docs",
            "next_recommended_route": "docs_consolidation_and_archive_replace_closeout",
        },
    }
    summary = {
        "summary": {
            **claim_packet["distilled_result"],
            "screened_now_count": len(screen_rows),
            "import_now_count": 0,
            "pass_count": sum(row["status"] == "pass" for row in checklist_rows),
            "blocked_count": sum(row["status"] != "pass" for row in checklist_rows),
        },
        "runtime_environment": environment_payload(),
    }
    snapshot = {
        "rows": [
            {"field": "p87_summary", "value": p87_summary},
            {"field": "screen_rows", "value": screen_rows},
            {"field": "doc_sync_rows", "value": doc_rows},
        ]
    }

    write_json(OUT_DIR / "checklist.json", {"rows": checklist_rows})
    write_json(OUT_DIR / "claim_packet.json", {"summary": claim_packet})
    write_json(OUT_DIR / "snapshot.json", snapshot)
    write_json(OUT_DIR / "summary.json", summary)


if __name__ == "__main__":
    main()
