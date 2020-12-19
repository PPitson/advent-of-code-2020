import re
from typing import Iterator

MASK_LENGTH = 36
MASK_ASSIGNMENT_INSTRUCTION_PREFIX = "mask = "


def part_one(input_filename: str) -> int:
    instructions = _get_program_instructions(input_filename)
    memory = _run_program(instructions)
    return sum(memory.values())


def _get_program_instructions(input_filename: str) -> Iterator[str]:
    with open(input_filename) as file:
        for line in file:
            yield line


def _run_program(instructions: Iterator[str]) -> dict[int, int]:
    mask = "X" * MASK_LENGTH
    memory = {}
    for instruction in instructions:
        if _is_mask_assignment(instruction):
            mask = instruction.removeprefix(MASK_ASSIGNMENT_INSTRUCTION_PREFIX)
        else:
            address, value = _parse_memory_assignment_instruction(instruction)
            memory[address] = _apply_mask_to_value(mask, value)
    return memory


def _is_mask_assignment(instruction: str) -> bool:
    return instruction.startswith(MASK_ASSIGNMENT_INSTRUCTION_PREFIX)


def _parse_memory_assignment_instruction(instruction: str) -> tuple[int, int]:
    match = re.match(r"mem\[(?P<address>\d+)]\s=\s(?P<value>\d+)", instruction)
    match_dict = match.groupdict()
    return int(match_dict["address"]), int(match_dict["value"])


def _apply_mask_to_value(mask: str, value: int) -> int:
    binary_value = bin(value).removeprefix("0b").rjust(MASK_LENGTH, "0")
    result = "".join(_determine_bit(mask_bit, value_bit) for mask_bit, value_bit in zip(mask, binary_value))
    return int(result, 2)


def _determine_bit(mask_bit: str, value_bit: str) -> str:
    return value_bit if mask_bit == "X" else mask_bit


if __name__ == "__main__":
    print(part_one("data/input.txt"))
