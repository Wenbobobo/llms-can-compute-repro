from __future__ import annotations

import importlib.util

import pytest

from exec_trace import (
    countdown_program,
    dynamic_latest_write_program,
    dynamic_memory_transfer_program,
    equality_branch_program,
    latest_write_program,
    memory_accumulator_program,
)
from model import (
    evaluate_free_running_programs,
    train_neural_event_executor,
    NeuralEventTrainingConfig,
    run_free_running_with_neural_executor,
    StructuredEventCodec,
)


def test_structured_event_codec_builds_examples_from_reference_traces() -> None:
    codec = StructuredEventCodec()
    examples = codec.build_examples(
        (
            countdown_program(2),
            equality_branch_program(1, 1),
            latest_write_program(),
        )
    )

    assert len(examples) > 0
    assert all(example.context.opcode is not None for example in examples)
    assert all(example.label.next_pc_mode for example in examples)


@pytest.mark.skipif(importlib.util.find_spec("torch") is None, reason="torch is not installed")
def test_neural_event_executor_training_pipeline_fits_structured_labels() -> None:
    train_programs = [countdown_program(start) for start in range(0, 5)] + [
        equality_branch_program(0, 0),
        equality_branch_program(0, 1),
        latest_write_program(),
        dynamic_latest_write_program(),
    ]
    eval_programs = [countdown_program(start) for start in range(5, 8)]

    run = train_neural_event_executor(
        train_programs,
        eval_programs=eval_programs,
        training_config=NeuralEventTrainingConfig(
            epochs=24,
            batch_size=8,
            learning_rate=1e-2,
            hidden_dim=48,
            embedding_dim=12,
            device="cpu",
        ),
    )

    assert run.train_metrics.exact_label_accuracy == 1.0
    assert run.eval_metrics is not None
    assert run.eval_metrics.exact_label_accuracy == 1.0


@pytest.mark.skipif(importlib.util.find_spec("torch") is None, reason="torch is not installed")
def test_neural_event_executor_runs_exact_rollout_on_heldout_programs() -> None:
    train_programs = [countdown_program(start) for start in range(0, 7)] + [
        equality_branch_program(0, 0),
        equality_branch_program(0, 1),
        latest_write_program(),
        memory_accumulator_program(),
        dynamic_latest_write_program(),
    ]
    heldout_programs = [
        countdown_program(9),
        equality_branch_program(5, 5),
        equality_branch_program(2, 9),
        dynamic_memory_transfer_program(),
    ]

    run = train_neural_event_executor(
        train_programs,
        eval_programs=heldout_programs,
        training_config=NeuralEventTrainingConfig(
            epochs=28,
            batch_size=8,
            learning_rate=1e-2,
            hidden_dim=64,
            embedding_dim=12,
            device="cpu",
        ),
    )
    evaluation = evaluate_free_running_programs(
        heldout_programs,
        lambda program: run_free_running_with_neural_executor(program, run, decode_mode="accelerated"),
    )

    assert evaluation.exact_trace_accuracy == 1.0
    assert evaluation.exact_final_state_accuracy == 1.0
