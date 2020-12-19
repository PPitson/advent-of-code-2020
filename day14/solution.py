import re
from typing import Iterator

from day14.constants import MASK_LENGTH, MASK_ASSIGNMENT_INSTRUCTION_PREFIX
from day14.strategies.base import MemoryUpdateStrategy
from day14.strategies.value import ValueModifiedByMaskStrategy


def part_one(input_filename: str) -> int:
    instructions = _get_program_instructions(input_filename)
    memory = _run_program(instructions, ValueModifiedByMaskStrategy())
    return sum(memory.values())


def _get_program_instructions(input_filename: str) -> Iterator[str]:
    with open(input_filename) as file:
        for line in file:
            yield line


def _run_program(instructions: Iterator[str], memory_update_strategy: MemoryUpdateStrategy) -> dict[int, int]:
    mask = "X" * MASK_LENGTH
    memory = {}
    for instruction in instructions:
        if _is_mask_assignment(instruction):
            mask = instruction.removeprefix(MASK_ASSIGNMENT_INSTRUCTION_PREFIX)
        else:
            address, value = _parse_memory_assignment_instruction(instruction)
            memory = memory_update_strategy.update_memory(memory, address, mask, value)
    return memory


def _is_mask_assignment(instruction: str) -> bool:
    return instruction.startswith(MASK_ASSIGNMENT_INSTRUCTION_PREFIX)


def _parse_memory_assignment_instruction(instruction: str) -> tuple[int, int]:
    match = re.match(r"mem\[(?P<address>\d+)]\s=\s(?P<value>\d+)", instruction)
    match_dict = match.groupdict()
    return int(match_dict["address"]), int(match_dict["value"])


if __name__ == "__main__":
    print(part_one("data/input.txt"))
