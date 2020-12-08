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


def part_one(input_filename: str) -> int:
    instructions = _parse_file(input_filename)
    return _retrieve_accumulator_value_before_infinite_loop(instructions)


def _parse_file(input_filename: str) -> list[Instruction]:
    with open(input_filename) as file:
        return [_parse_instruction(line) for line in file]


def _parse_instruction(line: str) -> Instruction:
    kind, argument = line.split(" ")
    return Instruction(kind=kind, argument=int(argument))


def _retrieve_accumulator_value_before_infinite_loop(instructions: list[Instruction]) -> int:
    visited = [False for _ in range(len(instructions))]
    index = 0
    accumulator_value = 0
    while not visited[index]:
        instruction = instructions[index]
        visited[index] = True
        if instruction.kind == InstructionType.JUMP:
            index += instruction.argument
        elif instruction.kind == InstructionType.UPDATE_ACCUMULATOR:
            accumulator_value += instruction.argument
            index += 1
        else:
            index += 1
    return accumulator_value


if __name__ == "__main__":
    print(part_one("data/input.txt"))
