import itertools
from collections import defaultdict
from typing import Any, Iterable

CHARGING_OUTLET_JOLTAGE = 0
DIFFERENCE_BETWEEN_DEVICE_JOLTAGE_AND_ADAPTER_JOLTAGE = 3


def part_one(input_filename: str) -> int:
    joltages = _get_joltages(input_filename)
    differences = _get_joltage_differences(joltages)
    return differences[1] * differences[3]


def _get_joltages(input_filename: str) -> list[int]:
    with open(input_filename) as file:
        return [int(line) for line in file]


def _get_joltage_differences(joltages: list[int]) -> dict[int, int]:
    sorted_joltages = sorted([CHARGING_OUTLET_JOLTAGE] + joltages)
    differences = defaultdict(int)
    for previous_joltage, joltage in _pairwise(sorted_joltages):
        differences[joltage - previous_joltage] += 1
    differences[DIFFERENCE_BETWEEN_DEVICE_JOLTAGE_AND_ADAPTER_JOLTAGE] += 1
    return differences


def _pairwise(iterable: Iterable[Any]) -> Iterable[tuple[Any, Any]]:
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


if __name__ == "__main__":
    print(part_one("data/input.txt"))
