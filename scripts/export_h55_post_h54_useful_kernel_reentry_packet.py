"""Export the saved post-H54 useful-kernel reentry packet for H55."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from utils import detect_runtime_environment


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "results" / "H55_post_h54_useful_kernel_reentry_packet"


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


def load_inputs() -> dict[str, Any]:
    milestone = ROOT / "docs" / "milestones" / "H55_post_h54_useful_kernel_reentry_packet"
    return {
        "design_text": read_text(ROOT / "docs" / "plans" / "2026-03-25-post-h54-useful-kernel-stopgo-design.md"),
        "milestones_readme_text": read_text(ROOT / "docs" / "milestones" / "README.md"),
        "h55_readme_text": read_text(milestone / "README.md"),
        "h55_status_text": read_text(milestone / "status.md"),
        "h55_todo_text": read_text(milestone / "todo.md"),
        "h55_acceptance_text": read_text(milestone / "acceptance.md"),
        "h55_artifact_index_text": read_text(milestone / "artifact_index.md"),
        "decision_matrix_text": read_text(milestone / "decision_matrix.md"),
        "h54_summary": read_json(ROOT / "results" / "H54_post_r58_r59_compiled_boundary_decision_packet" / "summary.json"),
        "h43_summary": read_json(ROOT / "results" / "H43_post_r44_useful_case_refreeze" / "summary.json"),
    }


def build_checklist_rows(inputs: dict[str, Any]) -> list[dict[str, object]]:
    h54 = inputs["h54_summary"]["summary"]
    h43 = inputs["h43_summary"]["summary"]
    return [
        {
            "item_id": "h55_docs_record_saved_successor_reentry_decision_only",
            "status": "pass"
            if contains_all(
                inputs["h55_readme_text"],
                [
                    "saved successor docs-only interpretation packet above `h54`",
                    "saved_successor_design_only",
                    "not active",
                    "`r60` only",
                ],
            )
            and contains_all(
                inputs["h55_status_text"],
                [
                    "saved_successor_design_only",
                    "active: `false`",
                    "`authorize_useful_kernel_carryover_through_r60_first`",
                ],
            )
            and contains_all(
                inputs["h55_todo_text"],
                [
                    "preserve `h54` as the current closeout",
                    "preserve `h52` as prior mechanism closeout",
                    "preserve `h43` as paper-grade endpoint",
                    "decide only whether `r60` may open",
                ],
            )
            and contains_all(
                inputs["h55_acceptance_text"],
                [
                    "stays docs-only",
                    "preserves negative `h54` on bounded fast-path value",
                    "does not reopen `f27`, `r53`, or `r54`",
                    "authorizes at most `r60`",
                ],
            )
            and contains_all(
                inputs["decision_matrix_text"],
                [
                    "`authorize_useful_kernel_carryover_through_r60_first`",
                    "`keep_h54_terminal_and_stop_before_useful_kernel_reentry`",
                ],
            )
            else "blocked",
            "notes": "H55 should remain a saved successor decision packet only, with one admissible positive route through R60.",
        },
        {
            "item_id": "upstream_h54_closeout_and_h43_ceiling_are_preserved",
            "status": "pass"
            if str(h54["selected_outcome"]) == "freeze_restricted_compiled_boundary_supported_narrowly_without_fastpath_value"
            and str(h54["next_required_lane"]) == "no_active_downstream_runtime_lane"
            and str(h43["active_stage"]) == "h43_post_r44_useful_case_refreeze"
            and str(h43["claim_ceiling"]) == "bounded_useful_cases_only"
            else "blocked",
            "notes": "H55 must preserve H54 as current closeout storage and keep H43 as the paper-grade endpoint.",
        },
        {
            "item_id": "indices_record_h55_as_saved_successor_not_active_packet",
            "status": "pass"
            if contains_all(
                inputs["design_text"],
                [
                    "`h55_post_h54_useful_kernel_reentry_packet`",
                    "`authorize_useful_kernel_carryover_through_r60_first`",
                    "`keep_h54_terminal_and_stop_before_useful_kernel_reentry`",
                ],
            )
            and contains_all(
                inputs["milestones_readme_text"],
                [
                    "`h55_post_h54_useful_kernel_reentry_packet/`",
                    "saved successor docs-only reentry packet; not active",
                ],
            )
            else "blocked",
            "notes": "Shared successor indexes should expose H55 as saved decision storage rather than as the active packet.",
        },
    ]


def build_claim_packet() -> dict[str, object]:
    return {
        "supported_here": [
            "H55 stores one saved successor decision matrix above H54 without activating a new runtime lane yet.",
            "H55 preserves H54 as the current compiled-boundary closeout and keeps H43 as the paper-grade endpoint.",
            "H55 allows at most one future positive route through R60 if the successor wave is later activated.",
        ],
        "unsupported_here": [
            "H55 does not replace H54 as the current active docs-only packet.",
            "H55 does not reopen F27, R53, or R54.",
            "H55 does not itself claim useful-kernel carryover success.",
        ],
        "disconfirmed_here": [
            "The idea that post-H54 successor storage should silently reopen a new runtime lane without an explicit reentry packet.",
        ],
        "distilled_result": {
            "active_stage": "h55_post_h54_useful_kernel_reentry_packet",
            "preserved_prior_docs_only_closeout": "h54_post_r58_r59_compiled_boundary_decision_packet",
            "preserved_prior_mechanism_closeout": "h52_post_r55_r56_r57_origin_mechanism_decision_packet",
            "current_paper_grade_endpoint": "h43_post_r44_useful_case_refreeze",
            "current_planning_bundle": "f30_post_h54_useful_kernel_bridge_bundle",
            "selected_outcome": "saved_successor_reentry_packet_only",
            "admissible_positive_outcome": "authorize_useful_kernel_carryover_through_r60_first",
            "non_selected_alternatives": [
                "keep_h54_terminal_and_stop_before_useful_kernel_reentry",
            ],
            "saved_successor_low_priority_wave": "p39_post_h54_successor_worktree_hygiene_sync",
            "only_next_runtime_candidate_if_activated": "r60_origin_compiled_useful_kernel_carryover_gate",
            "next_required_lane_if_activated": "r60_origin_compiled_useful_kernel_carryover_gate",
        },
    }


def build_snapshot(inputs: dict[str, Any]) -> list[dict[str, object]]:
    rows = [
        (
            "docs/milestones/H55_post_h54_useful_kernel_reentry_packet/README.md",
            inputs["h55_readme_text"],
            ["saved successor docs-only interpretation packet", "`R60` only"],
        ),
        (
            "docs/milestones/H55_post_h54_useful_kernel_reentry_packet/decision_matrix.md",
            inputs["decision_matrix_text"],
            ["`authorize_useful_kernel_carryover_through_r60_first`", "`keep_h54_terminal_and_stop_before_useful_kernel_reentry`"],
        ),
        (
            "docs/milestones/H55_post_h54_useful_kernel_reentry_packet/status.md",
            inputs["h55_status_text"],
            ["`saved_successor_design_only`", "`authorize_useful_kernel_carryover_through_r60_first`"],
        ),
        (
            "docs/plans/2026-03-25-post-h54-useful-kernel-stopgo-design.md",
            inputs["design_text"],
            ["`H55_post_h54_useful_kernel_reentry_packet`", "`R60_origin_compiled_useful_kernel_carryover_gate`"],
        ),
        (
            "docs/milestones/README.md",
            inputs["milestones_readme_text"],
            ["`H55_post_h54_useful_kernel_reentry_packet/`", "saved successor docs-only reentry packet; not active"],
        ),
    ]
    return [{"path": path, "matched_lines": extract_matching_lines(text, needles=needles)} for path, text, needles in rows]


def build_summary(checklist_rows: list[dict[str, object]], claim_packet: dict[str, object]) -> dict[str, object]:
    blocked_items = [row["item_id"] for row in checklist_rows if row["status"] != "pass"]
    distilled = claim_packet["distilled_result"]
    return {
        "active_stage": distilled["active_stage"],
        "preserved_prior_docs_only_closeout": distilled["preserved_prior_docs_only_closeout"],
        "preserved_prior_mechanism_closeout": distilled["preserved_prior_mechanism_closeout"],
        "current_paper_grade_endpoint": distilled["current_paper_grade_endpoint"],
        "current_planning_bundle": distilled["current_planning_bundle"],
        "selected_outcome": distilled["selected_outcome"],
        "admissible_positive_outcome": distilled["admissible_positive_outcome"],
        "non_selected_alternatives": distilled["non_selected_alternatives"],
        "saved_successor_low_priority_wave": distilled["saved_successor_low_priority_wave"],
        "only_next_runtime_candidate_if_activated": distilled["only_next_runtime_candidate_if_activated"],
        "next_required_lane_if_activated": distilled["next_required_lane_if_activated"],
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
    claim_packet = build_claim_packet()
    snapshot_rows = build_snapshot(inputs)
    summary = build_summary(checklist_rows, claim_packet)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(OUT_DIR / "checklist.json", {"rows": checklist_rows})
    write_json(OUT_DIR / "claim_packet.json", {"summary": claim_packet})
    write_json(OUT_DIR / "snapshot.json", {"rows": snapshot_rows})
    write_json(OUT_DIR / "summary.json", {"summary": summary, "runtime_environment": environment_payload()})


if __name__ == "__main__":
    main()
