"""Export induced causal-transition executor results for the next M4 checkpoint."""

from __future__ import annotations

import json
from pathlib import Path

from exec_trace import (
    countdown_program,
    dynamic_latest_write_program,
    dynamic_memory_program,
    dynamic_memory_transfer_program,
    equality_branch_program,
    latest_write_program,
    memory_accumulator_program,
)
from model import (
    build_countdown_stack_samples,
    evaluate_free_running_programs,
    fit_scorer,
    fit_transition_library,
    run_free_running_with_induced_rules,
    run_free_running_with_induced_rules_and_stack_scorer,
)


def encode_evaluation(evaluation):
    return {
        "exact_trace_accuracy": evaluation.exact_trace_accuracy,
        "exact_final_state_accuracy": evaluation.exact_final_state_accuracy,
        "program_count": evaluation.program_count,
        "by_length_bucket": [
            {"bucket": bucket, **metrics} for bucket, metrics in evaluation.by_length_bucket
        ],
        "outcomes": [
            {
                "program_name": outcome.program_name,
                "program_steps": outcome.program_steps,
                "exact_trace_match": outcome.exact_trace_match,
                "exact_final_state_match": outcome.exact_final_state_match,
                "first_mismatch_step": outcome.first_mismatch_step,
                "failure_reason": outcome.failure_reason,
            }
            for outcome in evaluation.outcomes
        ],
    }


def main() -> None:
    train_programs = [countdown_program(start) for start in range(0, 7)] + [
        equality_branch_program(0, 0),
        equality_branch_program(0, 1),
        latest_write_program(),
        memory_accumulator_program(),
        dynamic_latest_write_program(),
    ]
    countdown_heldout = [countdown_program(start) for start in range(7, 21)]
    branch_heldout = [
        equality_branch_program(5, 5),
        equality_branch_program(2, 9),
    ]
    memory_heldout = [
        dynamic_memory_program(),
        dynamic_memory_transfer_program(),
    ]

    library = fit_transition_library(train_programs)
    stack_scorer = fit_scorer(build_countdown_stack_samples(range(0, 7))).scorer

    output = {
        "experiment": "m4_induced_causal_executor",
        "notes": [
            "This branch fits structured transition rules from reference traces instead of hard-coding opcode semantics.",
            "The induced executor still operates on exact structured events, not on raw token sequences.",
            "A second evaluation combines induced event generation with the existing trainable stack latest-write scorer.",
        ],
        "fitted_rules": library.as_dict(),
        "evaluations": {
            "induced_exact": {
                "train_programs": encode_evaluation(
                    evaluate_free_running_programs(
                        train_programs,
                        lambda program: run_free_running_with_induced_rules(program, library),
                    )
                ),
                "countdown_heldout": encode_evaluation(
                    evaluate_free_running_programs(
                        countdown_heldout,
                        lambda program: run_free_running_with_induced_rules(program, library),
                    )
                ),
                "branch_heldout": encode_evaluation(
                    evaluate_free_running_programs(
                        branch_heldout,
                        lambda program: run_free_running_with_induced_rules(program, library),
                    )
                ),
                "memory_heldout": encode_evaluation(
                    evaluate_free_running_programs(
                        memory_heldout,
                        lambda program: run_free_running_with_induced_rules(program, library),
                    )
                ),
            },
            "induced_with_trainable_stack": {
                "countdown_heldout": encode_evaluation(
                    evaluate_free_running_programs(
                        countdown_heldout,
                        lambda program: run_free_running_with_induced_rules_and_stack_scorer(
                            program,
                            library,
                            stack_scorer,
                        ),
                    )
                ),
                "branch_heldout": encode_evaluation(
                    evaluate_free_running_programs(
                        branch_heldout,
                        lambda program: run_free_running_with_induced_rules_and_stack_scorer(
                            program,
                            library,
                            stack_scorer,
                        ),
                    )
                ),
                "memory_heldout": encode_evaluation(
                    evaluate_free_running_programs(
                        memory_heldout,
                        lambda program: run_free_running_with_induced_rules_and_stack_scorer(
                            program,
                            library,
                            stack_scorer,
                        ),
                    )
                ),
            },
        },
    }

    out_path = Path("results/M4_exact_hardmax_model/induced_causal_executor.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(out_path.as_posix())


if __name__ == "__main__":
    main()
