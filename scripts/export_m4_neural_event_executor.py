"""Export a neural structured-event executor checkpoint for M4."""

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
    evaluate_free_running_programs,
    NeuralEventTrainingConfig,
    run_free_running_with_neural_executor,
    train_neural_event_executor,
)


def encode_event_metrics(metrics):
    return {
        "loss": metrics.loss,
        "exact_label_accuracy": metrics.exact_label_accuracy,
        "example_count": metrics.example_count,
        "head_accuracies": [
            {"head": head, "accuracy": accuracy} for head, accuracy in metrics.head_accuracies
        ],
    }


def encode_rollout(evaluation):
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
    eval_programs = countdown_heldout + branch_heldout + memory_heldout

    run = train_neural_event_executor(
        train_programs,
        eval_programs=eval_programs,
        training_config=NeuralEventTrainingConfig(epochs=48, batch_size=16, learning_rate=5e-3),
    )

    output = {
        "experiment": "m4_neural_event_executor",
        "notes": [
            "This branch keeps the event-level trace substrate but replaces exact rule induction at decode time with a neural multi-head classifier over structured transition labels.",
            "Labels are derived from the fitted induced transition library so the neural model learns a stable event schema instead of raw whole-event tokens.",
            "Rollout still uses exact append-only retrieval for stack and memory values; the learned component decides which structured transition to apply next.",
        ],
        "training_config": {
            "epochs": 48,
            "batch_size": 16,
            "learning_rate": 5e-3,
        },
        "train_metrics": encode_event_metrics(run.train_metrics),
        "eval_metrics": None if run.eval_metrics is None else encode_event_metrics(run.eval_metrics),
        "history": [
            {
                "epoch": epoch.epoch,
                "train_loss": epoch.train_loss,
                "eval_loss": epoch.eval_loss,
            }
            for epoch in run.history
        ],
        "rollout": {
            "train_programs": encode_rollout(
                evaluate_free_running_programs(
                    train_programs,
                    lambda program: run_free_running_with_neural_executor(program, run, decode_mode="accelerated"),
                )
            ),
            "countdown_heldout": encode_rollout(
                evaluate_free_running_programs(
                    countdown_heldout,
                    lambda program: run_free_running_with_neural_executor(program, run, decode_mode="accelerated"),
                )
            ),
            "branch_heldout": encode_rollout(
                evaluate_free_running_programs(
                    branch_heldout,
                    lambda program: run_free_running_with_neural_executor(program, run, decode_mode="accelerated"),
                )
            ),
            "memory_heldout": encode_rollout(
                evaluate_free_running_programs(
                    memory_heldout,
                    lambda program: run_free_running_with_neural_executor(program, run, decode_mode="accelerated"),
                )
            ),
        },
    }

    out_path = Path("results/M4_neural_event_executor/summary.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(out_path.as_posix())


if __name__ == "__main__":
    main()
