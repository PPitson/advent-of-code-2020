import itertools
import operator
from functools import reduce
from typing import Iterator


class EntriesNotFound(Exception):
    """ Raised when there were no entries that sum to the desired number """


def part_one(input_filename: str) -> int:
    numbers = _get_numbers_from_file(input_filename)
    return _find_multiplication_of_numbers_which_sum_to_desired_sum(numbers, combination_length=2, desired_sum=2020)


def part_two(input_filename: str) -> int:
    numbers = _get_numbers_from_file(input_filename)
    return _find_multiplication_of_numbers_which_sum_to_desired_sum(numbers, combination_length=3, desired_sum=2020)


def _get_numbers_from_file(input_filename: str) -> Iterator[int]:
    with open(input_filename) as file:
        for line in file:
            yield int(line)


def _find_multiplication_of_numbers_which_sum_to_desired_sum(
    numbers: Iterator[int], combination_length: int, desired_sum: int
) -> int:
    try:
        numbers_combination = next(
            combination
            for combination in itertools.combinations(numbers, combination_length)
            if sum(combination) == desired_sum
        )
    except StopIteration:
        raise EntriesNotFound
    else:
        return reduce(operator.mul, numbers_combination, 1)


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
