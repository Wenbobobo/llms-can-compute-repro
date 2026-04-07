"""Export the post-P86 paper-spine refresh and salvage-shortlist packet for P87."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

from utils import detect_runtime_environment


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "results" / "P87_post_p86_paper_spine_refresh_and_salvage_shortlist"
P86_SUMMARY_PATH = ROOT / "results" / "P86_post_p85_dirty_root_inventory_and_archive_replace_map" / "summary.json"
CURRENT_BRANCH = "wip/p85-post-p84-main-rebaseline"
DOC_REQUIREMENTS = {
    "README.md": [
        "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
        CURRENT_BRANCH,
        "paper spine refresh",
        "salvage shortlist",
    ],
    "STATUS.md": [
        "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
        "paper spine refresh",
        "salvage shortlist",
        "archive-then-replace closeout",
    ],
    "docs/README.md": [
        "H65 + P87 + P86 + P85",
        "publication_record/current_stage_driver.md",
        "branch_worktree_registry.md",
        "plans/README.md",
    ],
    "docs/plans/README.md": [
        "2026-04-07-post-p87-next-planmode-handoff.md",
        "2026-04-07-post-p87-next-planmode-startup-prompt.md",
        "2026-04-07-post-p87-next-planmode-brief-prompt.md",
        "P87",
    ],
    "docs/milestones/README.md": [
        "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
        "P86_post_p85_dirty_root_inventory_and_archive_replace_map",
        "P85_post_p84_main_rebaseline_and_control_resync",
    ],
    "docs/publication_record/README.md": [
        "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
        "paper_bundle_status.md",
        "root_salvage_shortlist.md",
        "release_summary_draft.md",
    ],
    "docs/publication_record/current_stage_driver.md": [
        "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
        "paper spine refresh",
        "salvage shortlist",
        "archive-then-replace closeout",
    ],
    "docs/publication_record/paper_bundle_status.md": [
        "H65_post_p66_p67_p68_archive_first_terminal_freeze_packet",
        "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
        "P86_post_p85_dirty_root_inventory_and_archive_replace_map",
        "value-negative closeout",
    ],
    "docs/publication_record/release_summary_draft.md": [
        "narrow execution-substrate claim",
        "H65_post_p66_p67_p68_archive_first_terminal_freeze_packet",
        "P87_post_p86_paper_spine_refresh_and_salvage_shortlist",
        "dormant non-runtime dossier",
    ],
    "docs/publication_record/root_salvage_shortlist.md": [
        "salvage now",
        "paper_bundle_status.md",
        "release_summary_draft.md",
        "claim_evidence_table.md",
    ],
    "docs/plans/2026-04-07-post-p87-next-planmode-handoff.md": [
        CURRENT_BRANCH,
        "selective salvage import",
        "docs consolidation",
        "archive-then-replace closeout",
    ],
    "docs/plans/2026-04-07-post-p87-next-planmode-startup-prompt.md": [
        CURRENT_BRANCH,
        "selective salvage import",
        "archive-then-replace closeout",
    ],
    "docs/plans/2026-04-07-post-p87-next-planmode-brief-prompt.md": [
        "p85-post-p84-main-rebaseline",
        "selective salvage import",
        "archive-then-replace closeout",
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
    p86_summary = read_json(P86_SUMMARY_PATH)["summary"]
    if p86_summary["selected_outcome"] != "dirty_root_inventory_and_archive_replace_map_after_p85":
        raise RuntimeError("P87 expects the landed green P86 inventory summary.")
    if p86_summary["blocked_count"] != 0:
        raise RuntimeError("P87 expects a green P86 summary before paper-spine refresh.")

    current_branch_name = git_output(["rev-parse", "--abbrev-ref", "HEAD"])
    current_head = git_output(["rev-parse", "--short", "HEAD"])
    origin_main_head = git_output(["rev-parse", "--short", "origin/main"])
    branch_divergence = ahead_behind("origin/main", "HEAD")
    doc_rows = doc_sync_rows()

    checklist_rows = [
        {
            "item_id": "p87_reads_green_p86_summary",
            "status": "pass",
            "notes": "P87 begins only after the landed green P86 dirty-root inventory.",
        },
        {
            "item_id": "p87_runs_on_clean_p85_branch",
            "status": "pass" if current_branch_name == CURRENT_BRANCH else "blocked",
            "notes": "Paper-spine refresh must run from the clean p85 branch.",
        },
        {
            "item_id": "p87_live_docs_shift_current_control_to_paper_refresh_wave",
            "status": "pass" if all(bool(row["ok"]) for row in doc_rows) else "blocked",
            "notes": "Routers and publication docs should make P87 the current paper-facing refresh wave.",
        },
    ]

    claim_packet = {
        "supports": [
            "P87 refreshes the paper-facing spine to the current H65 + P86 + P85 closeout posture.",
            "P87 records a clean-branch salvage shortlist for high-value dirty-root publication docs.",
            "P87 narrows the next route to selective salvage import, docs consolidation, and archive-then-replace closeout.",
        ],
        "does_not_support": [
            "dirty-root integration",
            "runtime reopen",
            "same-lane executor-value reopen",
            "broad Wasm or arbitrary C scope expansion",
        ],
        "distilled_result": {
            "current_paper_wave": "p87_post_p86_paper_spine_refresh_and_salvage_shortlist",
            "current_branch": CURRENT_BRANCH,
            "current_branch_head": current_head,
            "merged_main_head": origin_main_head,
            "origin_main_to_p87_left_right": f"{branch_divergence['left_only']}/{branch_divergence['right_only']}",
            "selected_outcome": "paper_spine_refreshed_and_salvage_shortlist_synced_after_p86",
            "next_recommended_route": "selective_salvage_import_docs_consolidation_and_archive_replace_closeout",
        },
    }
    summary = {
        "summary": {
            **claim_packet["distilled_result"],
            "paper_docs_checked": 4,
            "router_docs_checked": len(doc_rows) - 4,
            "pass_count": sum(row["status"] == "pass" for row in checklist_rows),
            "blocked_count": sum(row["status"] != "pass" for row in checklist_rows),
        },
        "runtime_environment": environment_payload(),
    }
    snapshot = {
        "rows": [
            {"field": "p86_summary", "value": p86_summary},
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
