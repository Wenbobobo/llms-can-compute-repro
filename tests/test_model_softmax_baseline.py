from __future__ import annotations

import importlib.util

import pytest

from exec_trace import countdown_program, dynamic_memory_program, equality_branch_program
from model.softmax_baseline import (
    build_trace_sequence,
    build_trace_sequences,
    encode_trace_examples,
    evaluate_free_running_rollout,
    evaluate_teacher_forced_model,
    require_torch,
    serialize_event_tokens,
    SoftmaxBaselineConfig,
    SoftmaxTrainingConfig,
    summarize_trace_sequences,
    train_teacher_forced_baseline,
    TraceVocabulary,
)


def test_build_trace_sequence_contains_instruction_and_trace_markers() -> None:
    example = build_trace_sequence(countdown_program(3))

    assert example.tokens[0] == "<bos>"
    assert "<instructions>" in example.tokens
    assert "<trace>" in example.tokens
    assert example.tokens[-1] == "<eos>"


def test_trace_vocabulary_roundtrips_tokens() -> None:
    examples = build_trace_sequences((countdown_program(2), dynamic_memory_program()))
    vocabulary = TraceVocabulary.from_examples(examples)
    encoded = vocabulary.encode(examples[0].tokens[:12])

    assert vocabulary.decode(encoded) == examples[0].tokens[:12]
    assert len(vocabulary) >= len(set(examples[0].tokens[:12]))


def test_trace_sequence_summary_reports_lengths_and_vocab() -> None:
    examples = build_trace_sequences((countdown_program(2), countdown_program(5)))
    stats = summarize_trace_sequences(examples)

    assert stats.example_count == 2
    assert stats.max_length >= stats.min_length > 0
    assert stats.vocab_size > 0


def test_event_serialization_captures_memory_annotations() -> None:
    example = build_trace_sequence(dynamic_memory_program())
    memory_write_tokens = [token for token in example.tokens if token.startswith("memory_write=")]

    assert any(token != "memory_write=none" for token in memory_write_tokens)


def test_require_torch_matches_environment() -> None:
    torch_present = importlib.util.find_spec("torch") is not None
    if torch_present:
        require_torch()
    else:
        with pytest.raises(RuntimeError):
            require_torch()


@pytest.mark.skipif(importlib.util.find_spec("torch") is None, reason="torch is not installed")
def test_teacher_forced_training_pipeline_returns_metrics() -> None:
    examples = build_trace_sequences((countdown_program(0), countdown_program(1), countdown_program(2)))
    vocabulary = TraceVocabulary.from_examples(examples)
    encoded = encode_trace_examples(examples, vocabulary)
    config = SoftmaxBaselineConfig(vocab_size=len(vocabulary), d_model=8, n_heads=4, n_layers=2, d_ffn=8, max_seq_len=256)
    training = SoftmaxTrainingConfig(epochs=4, batch_size=2, learning_rate=1e-2, device="cpu")

    run = train_teacher_forced_baseline(encoded, model_config=config, training_config=training, eval_examples=encoded)
    metrics = evaluate_teacher_forced_model(run.model, encoded, device="cpu")

    assert len(run.history) == 4
    assert run.train_metrics.token_count > 0
    assert metrics.loss >= 0.0
    assert metrics.token_accuracy >= 0.0
    assert run.history[-1].train_loss <= run.history[0].train_loss


@pytest.mark.skipif(importlib.util.find_spec("torch") is None, reason="torch is not installed")
def test_free_running_rollout_evaluation_reports_outcomes() -> None:
    examples = build_trace_sequences((countdown_program(0), equality_branch_program(1, 1)))
    vocabulary = TraceVocabulary.from_examples(examples)
    encoded = encode_trace_examples(examples, vocabulary)
    config = SoftmaxBaselineConfig(vocab_size=len(vocabulary), d_model=8, n_heads=4, n_layers=2, d_ffn=8, max_seq_len=256)
    training = SoftmaxTrainingConfig(epochs=2, batch_size=2, learning_rate=1e-2, device="cpu")

    run = train_teacher_forced_baseline(encoded, model_config=config, training_config=training)
    rollout = evaluate_free_running_rollout(run.model, encoded, vocabulary=vocabulary, device="cpu", max_total_tokens=256)

    assert rollout.example_count == len(encoded)
    assert len(rollout.outcomes) == len(encoded)
    assert rollout.exact_sequence_accuracy >= 0.0
