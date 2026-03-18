from __future__ import annotations

from exec_trace.dsl import Opcode
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


def _training_programs():
    return [
        countdown_program(start) for start in range(0, 7)
    ] + [
        equality_branch_program(0, 0),
        equality_branch_program(0, 1),
        latest_write_program(),
        memory_accumulator_program(),
        dynamic_latest_write_program(),
    ]


def test_fit_transition_library_recovers_expected_rule_shapes() -> None:
    library = fit_transition_library(_training_programs())
    add_rule = library.rule_for(Opcode.ADD)
    sub_rule = library.rule_for(Opcode.SUB)
    eq_rule = library.rule_for(Opcode.EQ)
    dup_rule = library.rule_for(Opcode.DUP)
    load_at_rule = library.rule_for(Opcode.LOAD_AT)
    store_at_rule = library.rule_for(Opcode.STORE_AT)
    jz_rule = library.rule_for(Opcode.JZ)

    assert add_rule.push_exprs == ("add",)
    assert sub_rule.push_exprs == ("sub",)
    assert eq_rule.push_exprs == ("eq",)
    assert dup_rule.stack_read_count == 1
    assert dup_rule.pop_count == 0
    assert dup_rule.push_exprs == ("read0",)
    assert load_at_rule.memory_read_address_expr == "read0"
    assert load_at_rule.push_exprs == ("memory_read_value",)
    assert store_at_rule.memory_write_address_expr == "read1"
    assert store_at_rule.memory_write_value_expr == "read0"
    assert jz_rule.branch_expr == "read0_is_zero"
    assert jz_rule.next_pc_mode == "branch_arg_else_seq"


def test_induced_transition_executor_matches_heldout_program_families() -> None:
    library = fit_transition_library(_training_programs())
    programs = [
        countdown_program(start) for start in range(7, 13)
    ] + [
        equality_branch_program(5, 5),
        equality_branch_program(2, 9),
        dynamic_memory_program(),
        dynamic_memory_transfer_program(),
    ]

    evaluation = evaluate_free_running_programs(
        programs,
        lambda program: run_free_running_with_induced_rules(program, library, decode_mode="accelerated"),
    )

    assert evaluation.exact_trace_accuracy == 1.0
    assert evaluation.exact_final_state_accuracy == 1.0


def test_induced_transition_executor_can_use_trainable_stack_reads() -> None:
    library = fit_transition_library(_training_programs())
    scorer = fit_scorer(build_countdown_stack_samples(range(0, 7))).scorer
    programs = [
        countdown_program(10),
        equality_branch_program(3, 3),
        equality_branch_program(3, 8),
    ]

    evaluation = evaluate_free_running_programs(
        programs,
        lambda program: run_free_running_with_induced_rules_and_stack_scorer(program, library, scorer),
    )

    assert evaluation.exact_trace_accuracy == 1.0
    assert evaluation.exact_final_state_accuracy == 1.0
