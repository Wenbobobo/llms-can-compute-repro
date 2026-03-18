"""Small deterministic programs for the trace milestone."""

from __future__ import annotations

from .dsl import Instruction, Opcode, Program


def countdown_program(start: int) -> Program:
    if start < 0:
        raise ValueError("countdown_program expects a non-negative start.")

    instructions = (
        Instruction(Opcode.PUSH_CONST, start),
        Instruction(Opcode.DUP),
        Instruction(Opcode.JZ, 6),
        Instruction(Opcode.PUSH_CONST, 1),
        Instruction(Opcode.SUB),
        Instruction(Opcode.JMP, 1),
        Instruction(Opcode.HALT),
    )
    return Program(instructions=instructions, name=f"countdown_{start}")


def equality_branch_program(lhs: int, rhs: int) -> Program:
    instructions = (
        Instruction(Opcode.PUSH_CONST, lhs),
        Instruction(Opcode.PUSH_CONST, rhs),
        Instruction(Opcode.EQ),
        Instruction(Opcode.JZ, 6),
        Instruction(Opcode.PUSH_CONST, 1),
        Instruction(Opcode.HALT),
        Instruction(Opcode.PUSH_CONST, 0),
        Instruction(Opcode.HALT),
    )
    return Program(instructions=instructions, name=f"eq_{lhs}_{rhs}")


def latest_write_program() -> Program:
    """Overwrite one address and read it back to expose last-write semantics."""

    instructions = (
        Instruction(Opcode.PUSH_CONST, 7),
        Instruction(Opcode.STORE, 0),
        Instruction(Opcode.PUSH_CONST, 9),
        Instruction(Opcode.STORE, 0),
        Instruction(Opcode.LOAD, 0),
        Instruction(Opcode.HALT),
    )
    return Program(instructions=instructions, name="latest_write")


def memory_accumulator_program() -> Program:
    """Write, read, and combine two explicit memory slots."""

    instructions = (
        Instruction(Opcode.PUSH_CONST, 7),
        Instruction(Opcode.STORE, 0),
        Instruction(Opcode.PUSH_CONST, 5),
        Instruction(Opcode.STORE, 1),
        Instruction(Opcode.LOAD, 0),
        Instruction(Opcode.LOAD, 1),
        Instruction(Opcode.ADD),
        Instruction(Opcode.STORE, 2),
        Instruction(Opcode.LOAD, 2),
        Instruction(Opcode.HALT),
    )
    return Program(instructions=instructions, name="memory_accumulator")


def dynamic_memory_program() -> Program:
    """Use runtime-computed addresses for reads and writes."""

    instructions = (
        Instruction(Opcode.PUSH_CONST, 7),
        Instruction(Opcode.PUSH_CONST, 2),
        Instruction(Opcode.STORE_AT),
        Instruction(Opcode.PUSH_CONST, 11),
        Instruction(Opcode.PUSH_CONST, 1),
        Instruction(Opcode.PUSH_CONST, 1),
        Instruction(Opcode.ADD),
        Instruction(Opcode.STORE_AT),
        Instruction(Opcode.PUSH_CONST, 2),
        Instruction(Opcode.LOAD_AT),
        Instruction(Opcode.PUSH_CONST, 3),
        Instruction(Opcode.PUSH_CONST, 1),
        Instruction(Opcode.SUB),
        Instruction(Opcode.LOAD_AT),
        Instruction(Opcode.ADD),
        Instruction(Opcode.HALT),
    )
    return Program(instructions=instructions, name="dynamic_memory")


def dynamic_latest_write_program() -> Program:
    """Exercise indirect latest-write behavior on one runtime-computed address."""

    instructions = (
        Instruction(Opcode.PUSH_CONST, 13),
        Instruction(Opcode.PUSH_CONST, 4),
        Instruction(Opcode.STORE_AT),
        Instruction(Opcode.PUSH_CONST, 17),
        Instruction(Opcode.PUSH_CONST, 4),
        Instruction(Opcode.STORE_AT),
        Instruction(Opcode.PUSH_CONST, 4),
        Instruction(Opcode.LOAD_AT),
        Instruction(Opcode.HALT),
    )
    return Program(instructions=instructions, name="dynamic_latest_write")


def dynamic_memory_transfer_program() -> Program:
    """Read two indirect addresses, combine them, and write the result back indirectly."""

    instructions = (
        Instruction(Opcode.PUSH_CONST, 4),
        Instruction(Opcode.PUSH_CONST, 1),
        Instruction(Opcode.STORE_AT),
        Instruction(Opcode.PUSH_CONST, 9),
        Instruction(Opcode.PUSH_CONST, 2),
        Instruction(Opcode.STORE_AT),
        Instruction(Opcode.PUSH_CONST, 1),
        Instruction(Opcode.LOAD_AT),
        Instruction(Opcode.PUSH_CONST, 2),
        Instruction(Opcode.LOAD_AT),
        Instruction(Opcode.ADD),
        Instruction(Opcode.PUSH_CONST, 3),
        Instruction(Opcode.STORE_AT),
        Instruction(Opcode.PUSH_CONST, 3),
        Instruction(Opcode.LOAD_AT),
        Instruction(Opcode.HALT),
    )
    return Program(instructions=instructions, name="dynamic_memory_transfer")
