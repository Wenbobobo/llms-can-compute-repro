"""Export the saved post-H54 successor-worktree hygiene packet for P39."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
from typing import Any

from utils import detect_runtime_environment


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "results" / "P39_post_h54_successor_worktree_hygiene_sync"
LARGE_ARTIFACT_THRESHOLD_BYTES = 10 * 1024 * 1024
RAW_ROW_IGNORE_PATTERNS = [
    "results/**/probe_read_rows.json",
    "results/**/per_read_rows.json",
    "results/**/trace_rows.json",
    "results/**/step_rows.json",
]


def read_text(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def read_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def environment_payload() -> dict[str, object]:
    try:
        return detect_runtime_environment().as_dict()
    except Exception as exc:  # pragma: no cover
        return {"runtime_detection": "fallback", "error": f"{type(exc).__name__}: {exc}"}


def normalize_text_space(text: str) -> str:
    return " ".join(text.split())


def contains_all(text: str, needles: list[str]) -> bool:
    lowered = normalize_text_space(text).lower()
    return all(normalize_text_space(needle).lower() in lowered for needle in needles)


def extract_matching_lines(text: str, *, needles: list[str], max_lines: int = 8) -> list[str]:
    lowered_needles = [needle.lower() for needle in needles]
    hits: list[str] = []
    seen: set[str] = set()
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        lowered = line.lower()
        if any(needle in lowered for needle in lowered_needles) and line not in seen:
            hits.append(line)
            seen.add(line)
        if len(hits) >= max_lines:
            break
    return hits


def git_output(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout


def collect_tracked_large_artifacts(
    root: Path = ROOT,
    *,
    tracked_paths: list[str] | None = None,
    threshold_bytes: int = LARGE_ARTIFACT_THRESHOLD_BYTES,
) -> list[dict[str, object]]:
    if tracked_paths is None:
        tracked_paths = [path for path in git_output(["ls-files", "-z"]).split("\0") if path]

    oversized: list[dict[str, object]] = []
    for rel_path in tracked_paths:
        path = root / rel_path
        if not path.exists() or not path.is_file():
            continue
        size_bytes = path.stat().st_size
        if size_bytes < threshold_bytes:
            continue
        oversized.append(
            {
                "path": rel_path.replace("\\", "/"),
                "size_bytes": size_bytes,
                "size_mib": round(size_bytes / (1024 * 1024), 2),
            }
        )
    return sorted(oversized, key=lambda row: (int(row["size_bytes"]), str(row["path"])), reverse=True)


def load_inputs() -> dict[str, Any]:
    tracked_large_artifacts = collect_tracked_large_artifacts()
    milestone = ROOT / "docs" / "milestones" / "P39_post_h54_successor_worktree_hygiene_sync"
    return {
        "plans_readme_text": read_text(ROOT / "docs" / "plans" / "README.md"),
        "milestones_readme_text": read_text(ROOT / "docs" / "milestones" / "README.md"),
        "p39_readme_text": read_text(milestone / "README.md"),
        "p39_status_text": read_text(milestone / "status.md"),
        "p39_todo_text": read_text(milestone / "todo.md"),
        "p39_acceptance_text": read_text(milestone / "acceptance.md"),
        "p39_artifact_index_text": read_text(milestone / "artifact_index.md"),
        "artifact_policy_text": read_text(milestone / "artifact_policy.md"),
        "commit_cadence_text": read_text(milestone / "commit_cadence.md"),
        "worktree_strategy_text": read_text(milestone / "worktree_strategy.md"),
        "gitignore_text": read_text(ROOT / ".gitignore"),
        "h54_summary": read_json(ROOT / "results" / "H54_post_r58_r59_compiled_boundary_decision_packet" / "summary.json"),
        "tracked_large_artifacts": tracked_large_artifacts,
    }


def build_checklist_rows(inputs: dict[str, Any]) -> list[dict[str, object]]:
    h54 = inputs["h54_summary"]["summary"]
    return [
        {
            "item_id": "p39_docs_define_saved_successor_hygiene_sidecar",
            "status": "pass"
            if contains_all(
                inputs["p39_readme_text"],
                [
                    "saved successor operational/docs sidecar",
                    "saved_successor_design_only",
                    "not active",
                ],
            )
            and contains_all(
                inputs["p39_status_text"],
                [
                    "saved_successor_design_only",
                    "active: `false`",
                    "successor_worktree_hygiene_sidecar",
                ],
            )
            and contains_all(
                inputs["p39_todo_text"],
                [
                    "keep a clean successor worktree",
                    "keep `uv` as default execution path",
                    "keep large raw artifacts out of git",
                    "keep dirty root `main` unmerged",
                ],
            )
            and contains_all(
                inputs["p39_acceptance_text"],
                [
                    "clean-worktree-only execution",
                    "no-merge posture for dirty root `main`",
                    "artifact slimming",
                    "split commit cadence",
                ],
            )
            else "blocked",
            "notes": "P39 should stay a saved successor hygiene sidecar and should not present itself as the current low-priority wave.",
        },
        {
            "item_id": "p39_records_successor_worktree_artifact_and_commit_policy",
            "status": "pass"
            if contains_all(
                inputs["worktree_strategy_text"],
                [
                    "keep `f29` preserved as the closed execution surface",
                    "do new planning in a clean successor worktree",
                    "do not run science on dirty root `main`",
                ],
            )
            and contains_all(
                inputs["artifact_policy_text"],
                [
                    "keep summaries and manifests in git",
                    "keep raw row dumps and long per-step traces out of git by default",
                    "files above roughly `10 mib` as out-of-git",
                ],
            )
            and contains_all(
                inputs["commit_cadence_text"],
                [
                    "planning packet commit",
                    "runtime carryover gate commit",
                    "value gate commit",
                    "docs-only decision commit",
                ],
            )
            else "blocked",
            "notes": "P39 should save the successor worktree strategy, artifact policy, and commit cadence before any later execution wave opens.",
        },
        {
            "item_id": "p39_repo_state_matches_large_artifact_policy",
            "status": "pass"
            if contains_all(inputs["gitignore_text"], RAW_ROW_IGNORE_PATTERNS)
            and not inputs["tracked_large_artifacts"]
            else "blocked",
            "notes": "The clean successor branch should keep tracked artifacts under the roughly 10 MiB default limit.",
        },
        {
            "item_id": "indices_record_p39_as_saved_successor_not_current_low_priority_wave",
            "status": "pass"
            if str(h54["selected_outcome"]) == "freeze_restricted_compiled_boundary_supported_narrowly_without_fastpath_value"
            and str(h54["next_required_lane"]) == "no_active_downstream_runtime_lane"
            and contains_all(
                inputs["plans_readme_text"],
                [
                    "`2026-03-25-post-h54-useful-kernel-stopgo-design.md`",
                    "saved successor design for the next explicit post-`h54` stop/go packet",
                ],
            )
            and contains_all(
                inputs["milestones_readme_text"],
                [
                    "`p39_post_h54_successor_worktree_hygiene_sync/`",
                    "saved successor hygiene sidecar; not active",
                    "`p38_post_h52_compiled_boundary_hygiene_sync/`",
                    "current low-priority operational/docs wave",
                ],
            )
            else "blocked",
            "notes": "Shared indexes should keep P38 current and record P39 only as saved successor hygiene storage.",
        },
    ]


def build_claim_packet(tracked_large_artifacts: list[dict[str, object]]) -> dict[str, object]:
    return {
        "supported_here": [
            "P39 stores clean successor-worktree hygiene rules before any later post-H54 runtime wave opens.",
            "P39 keeps uv as the default execution path and keeps large raw artifacts out of git by default.",
            "P39 preserves the rule that science should not run on dirty root main.",
        ],
        "unsupported_here": [
            "P39 does not replace P38 as the current low-priority operational/docs wave.",
            "P39 does not change the active scientific stage from H54.",
            "P39 does not merge dirty root main into the clean line.",
        ],
        "disconfirmed_here": [
            "The idea that successor planning hygiene can be deferred until after a new runtime wave has already opened.",
        ],
        "distilled_result": {
            "current_active_stage": "h54_post_r58_r59_compiled_boundary_decision_packet",
            "current_low_priority_wave": "p38_post_h52_compiled_boundary_hygiene_sync",
            "saved_successor_hygiene_packet": "p39_post_h54_successor_worktree_hygiene_sync",
            "selected_outcome": "successor_worktree_hygiene_packet_saved_not_activated",
            "current_merge_posture": "explicit_no_merge_during_closed_h54_wave",
            "root_dirty_main_quarantined": True,
            "large_artifact_default_policy": "raw_step_trace_and_per_read_rows_out_of_git",
            "tracked_large_artifact_count": len(tracked_large_artifacts),
            "next_required_lane": "no_active_downstream_runtime_lane",
        },
    }


def build_snapshot(inputs: dict[str, Any]) -> list[dict[str, object]]:
    rows = [
        (
            "docs/milestones/P39_post_h54_successor_worktree_hygiene_sync/worktree_strategy.md",
            inputs["worktree_strategy_text"],
            ["keep `f29` preserved as the closed execution surface", "do not run science on dirty root `main`"],
        ),
        (
            "docs/milestones/P39_post_h54_successor_worktree_hygiene_sync/artifact_policy.md",
            inputs["artifact_policy_text"],
            ["keep raw row dumps and long per-step traces out of git by default", "files above roughly `10 MiB` as out-of-git"],
        ),
        (
            "docs/milestones/P39_post_h54_successor_worktree_hygiene_sync/commit_cadence.md",
            inputs["commit_cadence_text"],
            ["planning packet commit", "docs-only decision commit"],
        ),
        (
            ".gitignore",
            inputs["gitignore_text"],
            RAW_ROW_IGNORE_PATTERNS,
        ),
        (
            "docs/plans/README.md",
            inputs["plans_readme_text"],
            ["`2026-03-25-post-h54-useful-kernel-stopgo-design.md`", "saved successor design"],
        ),
        (
            "docs/milestones/README.md",
            inputs["milestones_readme_text"],
            ["`P39_post_h54_successor_worktree_hygiene_sync/`", "saved successor hygiene sidecar; not active"],
        ),
    ]
    return [{"path": path, "matched_lines": extract_matching_lines(text, needles=needles)} for path, text, needles in rows]


def build_summary(
    checklist_rows: list[dict[str, object]],
    claim_packet: dict[str, object],
    tracked_large_artifacts: list[dict[str, object]],
) -> dict[str, object]:
    blocked_items = [row["item_id"] for row in checklist_rows if row["status"] != "pass"]
    distilled = claim_packet["distilled_result"]
    return {
        "current_active_stage": distilled["current_active_stage"],
        "current_low_priority_wave": distilled["current_low_priority_wave"],
        "saved_successor_hygiene_packet": distilled["saved_successor_hygiene_packet"],
        "selected_outcome": distilled["selected_outcome"],
        "current_merge_posture": distilled["current_merge_posture"],
        "root_dirty_main_quarantined": distilled["root_dirty_main_quarantined"],
        "large_artifact_default_policy": distilled["large_artifact_default_policy"],
        "tracked_large_artifact_count": len(tracked_large_artifacts),
        "tracked_large_artifact_paths": [str(row["path"]) for row in tracked_large_artifacts],
        "next_required_lane": distilled["next_required_lane"],
        "supported_here_count": len(claim_packet["supported_here"]),
        "unsupported_here_count": len(claim_packet["unsupported_here"]),
        "disconfirmed_here_count": len(claim_packet["disconfirmed_here"]),
        "check_count": len(checklist_rows),
        "pass_count": sum(row["status"] == "pass" for row in checklist_rows),
        "blocked_count": len(blocked_items),
        "blocked_items": blocked_items,
    }


def main() -> None:
    inputs = load_inputs()
    checklist_rows = build_checklist_rows(inputs)
    claim_packet = build_claim_packet(inputs["tracked_large_artifacts"])
    snapshot_rows = build_snapshot(inputs)
    summary = build_summary(checklist_rows, claim_packet, inputs["tracked_large_artifacts"])

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(OUT_DIR / "checklist.json", {"rows": checklist_rows})
    write_json(OUT_DIR / "claim_packet.json", {"summary": claim_packet})
    write_json(OUT_DIR / "snapshot.json", {"rows": snapshot_rows})
    write_json(OUT_DIR / "summary.json", {"summary": summary, "runtime_environment": environment_payload()})


if __name__ == "__main__":
    main()
