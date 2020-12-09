from copy import copy
from dataclasses import dataclass
from enum import Enum


class InstructionType(str, Enum):
    NO_OPERATION = "nop"
    JUMP = "jmp"
    UPDATE_ACCUMULATOR = "acc"


@dataclass
class Instruction:
    kind: InstructionType
    argument: int


@dataclass
class ProgramExecutionResult:
    accumulator_value: int
    infinite_loop: bool


def part_one(input_filename: str) -> int:
    instructions = _parse_file(input_filename)
    execution_result = _execute_program(instructions)
    return execution_result.accumulator_value


def part_two(input_filename: str) -> int:
    instructions = _parse_file(input_filename)
    return _get_accumulator_value_after_correcting_program(instructions)


def _parse_file(input_filename: str) -> list[Instruction]:
    with open(input_filename) as file:
        return [_parse_instruction(line) for line in file]


def _parse_instruction(line: str) -> Instruction:
    kind, argument = line.split(" ")
    return Instruction(kind=kind, argument=int(argument))


def _execute_program(instructions: list[Instruction]) -> ProgramExecutionResult:
    visited = [False for _ in range(len(instructions))]
    index = 0
    max_index = len(instructions)
    accumulator_value = 0
    infinite_loop = False
    while index < max_index:
        if visited[index]:
            infinite_loop = True
            break
        instruction = instructions[index]
        visited[index] = True
        if instruction.kind == InstructionType.JUMP:
            index += instruction.argument
        elif instruction.kind == InstructionType.UPDATE_ACCUMULATOR:
            accumulator_value += instruction.argument
            index += 1
        else:
            index += 1
    return ProgramExecutionResult(accumulator_value=accumulator_value, infinite_loop=infinite_loop)


def _get_accumulator_value_after_correcting_program(instructions: list[Instruction]) -> int:
    instruction_replacements = {
        InstructionType.JUMP: InstructionType.NO_OPERATION,
        InstructionType.NO_OPERATION: InstructionType.JUMP,
    }
    for index, instruction in enumerate(instructions):
        if instruction.kind not in instruction_replacements:
            continue

        instructions_copy = copy(instructions)
        instructions_copy[index] = Instruction(
            kind=instruction_replacements[instruction.kind], argument=instruction.argument
        )
        execution_result = _execute_program(instructions_copy)
        if not execution_result.infinite_loop:
            return execution_result.accumulator_value


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
