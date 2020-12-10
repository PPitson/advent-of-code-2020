import itertools
from collections import defaultdict
from typing import Any, Iterable

CHARGING_OUTLET_JOLTAGE = 0
DIFFERENCE_BETWEEN_DEVICE_JOLTAGE_AND_ADAPTER_JOLTAGE = 3
MAX_JOLTAGE_DIFFERENCE_BETWEEN_ADAPTERS = 3


def part_one(input_filename: str) -> int:
    joltages = _get_sorted_joltages(input_filename)
    differences = _get_joltage_differences(joltages)
    return differences[1] * differences[3]


def part_two(input_filename: str) -> int:
    joltages = _get_sorted_joltages(input_filename)
    return _count_ways_of_arranging_adapters_to_connect_to_charging_outlet_of_device(joltages)


def _get_sorted_joltages(input_filename: str) -> list[int]:
    with open(input_filename) as file:
        return sorted([CHARGING_OUTLET_JOLTAGE] + [int(line) for line in file])


def _get_joltage_differences(sorted_joltages: list[int]) -> dict[int, int]:
    differences = defaultdict(int)
    for previous_joltage, joltage in _pairwise(sorted_joltages):
        differences[joltage - previous_joltage] += 1
    differences[DIFFERENCE_BETWEEN_DEVICE_JOLTAGE_AND_ADAPTER_JOLTAGE] += 1
    return differences


def _pairwise(iterable: Iterable[Any]) -> Iterable[tuple[Any, Any]]:
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def _count_ways_of_arranging_adapters_to_connect_to_charging_outlet_of_device(joltages: list[int]) -> int:
    max_index = len(joltages)
    memo = [-1 for _ in range(max_index)]

    def joltage_at_index_inside_max_difference(index: int, joltage: int) -> bool:
        return index < max_index and (joltages[index] - joltage) <= MAX_JOLTAGE_DIFFERENCE_BETWEEN_ADAPTERS

    def count_ways(index: int) -> int:
        if memo[index] != -1:
            return memo[index]

        if index == max_index - 1:
            return 1

        joltage = joltages[index]
        a = count_ways(index + 1) if joltage_at_index_inside_max_difference(index + 1, joltage) else 0
        b = count_ways(index + 2) if joltage_at_index_inside_max_difference(index + 2, joltage) else 0
        c = count_ways(index + 3) if joltage_at_index_inside_max_difference(index + 3, joltage) else 0
        memo[index] = a + b + c
        return memo[index]

    return count_ways(0)


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
