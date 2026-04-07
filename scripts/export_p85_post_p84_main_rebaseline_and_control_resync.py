"""Export the post-P84 merged-main rebaseline and control-resync packet for P85."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

from utils import detect_runtime_environment


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "results" / "P85_post_p84_main_rebaseline_and_control_resync"
P84_SUMMARY_PATH = ROOT / "results" / "P84_post_p83_keep_set_contraction_and_closeout" / "summary.json"
CURRENT_BRANCH = "wip/p85-post-p84-main-rebaseline"
MERGED_SOURCE_BRANCH = "wip/p83-post-p82-promotion-branch-and-pr-handoff"
REQUIRED_WORKTREE_PATHS = [
    "D:/zWenbo/AI/LLMCompute",
    "D:/zWenbo/AI/LLMCompute-worktrees/h27-promotion",
    "D:/zWenbo/AI/wt/p56-main-scratch",
    "D:/zWenbo/AI/wt/p69-post-h65-hygiene-only-cleanup",
    "D:/zWenbo/AI/wt/p72-post-p71-archive-polish-stop-handoff",
    "D:/zWenbo/AI/wt/p73-post-p72-hygiene-shrink-mergeprep",
    "D:/zWenbo/AI/wt/p74-post-p73-successor-publication-review",
    "D:/zWenbo/AI/wt/p75-post-p74-published-successor-freeze",
    "D:/zWenbo/AI/wt/p83-post-p82-promotion-branch-and-pr-handoff",
    "D:/zWenbo/AI/wt/p85-post-p84-main-rebaseline",
]
DOC_REQUIREMENTS = {
    "README.md": [
        "P85_post_p84_main_rebaseline_and_control_resync",
        CURRENT_BRANCH,
        "P84_post_p83_keep_set_contraction_and_closeout",
        "P83_post_p82_promotion_branch_and_pr_handoff",
    ],
    "STATUS.md": [
        "P85_post_p84_main_rebaseline_and_control_resync",
        CURRENT_BRANCH,
        MERGED_SOURCE_BRANCH,
        "root-main-parking-2026-03-24",
    ],
    "docs/README.md": [
        "H65 + P85 + P84 + P83",
        "publication_record/current_stage_driver.md",
        "branch_worktree_registry.md",
        "plans/README.md",
    ],
    "docs/branch_worktree_registry.md": [
        CURRENT_BRANCH,
        MERGED_SOURCE_BRANCH,
        "preserved merged-source lineage",
        "root-main-parking-2026-03-24",
    ],
    "docs/plans/README.md": [
        "2026-04-07-post-p85-next-planmode-handoff.md",
        "2026-04-07-post-p85-next-planmode-startup-prompt.md",
        "2026-04-07-post-p85-next-planmode-brief-prompt.md",
        "P85",
    ],
    "docs/milestones/README.md": [
        "P85_post_p84_main_rebaseline_and_control_resync",
        "P84_post_p83_keep_set_contraction_and_closeout",
        "P83_post_p82_promotion_branch_and_pr_handoff",
    ],
    "docs/publication_record/README.md": [
        "P85_post_p84_main_rebaseline_and_control_resync",
        "current_stage_driver.md",
        "paper_bundle_status.md",
    ],
    "docs/publication_record/current_stage_driver.md": [
        "P85_post_p84_main_rebaseline_and_control_resync",
        CURRENT_BRANCH,
        "preserved merged-source branch",
        MERGED_SOURCE_BRANCH,
    ],
    "docs/plans/2026-04-07-post-p85-next-planmode-handoff.md": [
        CURRENT_BRANCH,
        "root archive/replace",
        "docs consolidation",
        "paper spine refresh",
    ],
    "docs/plans/2026-04-07-post-p85-next-planmode-startup-prompt.md": [
        CURRENT_BRANCH,
        "root archive/replace",
        "paper spine refresh",
    ],
    "docs/plans/2026-04-07-post-p85-next-planmode-brief-prompt.md": [
        "p85-post-p84-main-rebaseline",
        "root archive/replace",
        "paper spine refresh",
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


def parse_worktree_rows(raw: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    current: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            if current:
                rows.append(current)
                current = {}
            continue
        key, _, value = line.partition(" ")
        current[key] = value.strip()
    if current:
        rows.append(current)
    return rows


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
    p84_summary = read_json(P84_SUMMARY_PATH)["summary"]
    if p84_summary["selected_outcome"] != "keep_set_contracted_and_closeout_synced_after_p83":
        raise RuntimeError("P85 expects the landed green P84 closeout summary.")
    if p84_summary["blocked_count"] != 0:
        raise RuntimeError("P85 expects a green P84 summary before merged-main rebaseline.")

    current_branch_name = git_output(["rev-parse", "--abbrev-ref", "HEAD"])
    current_head = git_output(["rev-parse", "--short", "HEAD"])
    origin_main_head = git_output(["rev-parse", "--short", "origin/main"])
    branch_divergence = ahead_behind("origin/main", "HEAD")
    worktree_rows = parse_worktree_rows(git_output(["worktree", "list", "--porcelain"]))
    mounted_paths = [row["worktree"] for row in worktree_rows]
    doc_rows = doc_sync_rows()

    checklist_rows = [
        {
            "item_id": "p85_reads_green_p84_summary",
            "status": "pass",
            "notes": "P85 starts only after the landed green P84 keep-set closeout.",
        },
        {
            "item_id": "p85_runs_on_clean_main_rebaseline_branch",
            "status": "pass" if current_branch_name == CURRENT_BRANCH else "blocked",
            "notes": "The merged-main rebaseline must run from the dedicated clean p85 branch.",
        },
        {
            "item_id": "p85_branch_stays_ahead_only_from_merged_main",
            "status": "pass" if branch_divergence["left_only"] == 0 else "blocked",
            "notes": "The p85 branch should remain a clean descendant of merged origin/main.",
        },
        {
            "item_id": "p85_required_keep_set_remains_mounted",
            "status": "pass" if all(path in mounted_paths for path in REQUIRED_WORKTREE_PATHS) else "blocked",
            "notes": "The current mounted keep set should include p85 plus the short-term preserved p83 lineage.",
        },
        {
            "item_id": "p85_live_docs_shift_current_control_to_merged_main",
            "status": "pass" if all(bool(row["ok"]) for row in doc_rows) else "blocked",
            "notes": "Live control docs should make p85 current and p83 preserved merged-source lineage.",
        },
    ]

    claim_packet = {
        "supports": [
            "P85 establishes a clean post-merge rebaseline branch on top of merged origin/main.",
            "P85 preserves p83 as short-term merged-source lineage rather than the current live promotion branch.",
            "P85 moves the next engineering route from promotion-prep to root archive/replace, docs consolidation, and paper spine refresh.",
        ],
        "does_not_support": [
            "dirty-root integration",
            "runtime reopen",
            "same-lane executor-value reopen",
            "broad Wasm or arbitrary C scope expansion",
        ],
        "distilled_result": {
            "current_rebaseline_wave": "p85_post_p84_main_rebaseline_and_control_resync",
            "current_branch": CURRENT_BRANCH,
            "current_branch_head": current_head,
            "merged_main_head": origin_main_head,
            "merged_source_branch": MERGED_SOURCE_BRANCH,
            "origin_main_to_p85_left_right": f"{branch_divergence['left_only']}/{branch_divergence['right_only']}",
            "selected_outcome": "merged_main_rebaseline_and_control_resync_after_p84",
            "next_recommended_route": "root_archive_replace_docs_consolidation_and_paper_spine_refresh",
        },
    }
    summary = {
        "summary": {
            **claim_packet["distilled_result"],
            "mounted_worktree_count": len(mounted_paths),
            "pass_count": sum(row["status"] == "pass" for row in checklist_rows),
            "blocked_count": sum(row["status"] != "pass" for row in checklist_rows),
        },
        "runtime_environment": environment_payload(),
    }
    snapshot = {
        "rows": [
            {"field": "current_branch", "value": current_branch_name},
            {"field": "worktree_rows", "value": worktree_rows},
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
