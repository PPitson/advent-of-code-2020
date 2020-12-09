import collections
import itertools
from typing import Iterator, Iterable, Any


def part_one(input_filename: str, preamble_length: int) -> int:
    numbers = _get_numbers(input_filename)
    return _find_invalid_number(numbers, preamble_length=preamble_length)


def part_two(input_filename: str, preamble_length: int) -> int:
    numbers = _get_numbers(input_filename)
    invalid_number = _find_invalid_number(numbers, preamble_length=preamble_length)
    return _find_encryption_weakness(numbers, invalid_number)


def _get_numbers(input_filename: str) -> list[int]:
    with open(input_filename) as file:
        return [int(line) for line in file]


def _find_invalid_number(numbers: list[int], preamble_length: int) -> int:
    deque = collections.deque(_take_first_n_numbers(preamble_length, numbers), maxlen=preamble_length)
    for number in numbers[preamble_length:]:
        if not _is_sum_of_pair_of_numbers(number, deque):
            return number
        deque.append(number)


def _take_first_n_numbers(n: int, iterable: Iterable[Any]) -> Iterator[Any]:
    return itertools.islice(iterable, n)


def _is_sum_of_pair_of_numbers(number: int, numbers: Iterator[int]) -> bool:
    return _is_sum_of_n_numbers(number, numbers, numbers_combination_length=2)


def _is_sum_of_n_numbers(number: int, numbers: Iterator[int], numbers_combination_length: int) -> bool:
    return any(
        sum(combination) == number for combination in itertools.combinations(numbers, numbers_combination_length)
    )


def _find_encryption_weakness(numbers: list[int], invalid_number: int) -> int:
    numbers_sequence = _find_contiguous_sequence_of_numbers_which_sums_to_desired_sum(numbers, invalid_number)
    return min(numbers_sequence) + max(numbers_sequence)


def _find_contiguous_sequence_of_numbers_which_sums_to_desired_sum(numbers: list[int], desired_sum: int) -> list[int]:
    return next(
        numbers[i : i + set_length]
        for set_length in range(2, len(numbers))
        for i in range(len(numbers) - set_length + 1)
        if sum(numbers[i : i + set_length]) == desired_sum
    )


if __name__ == "__main__":
    print(part_one("data/input.txt", preamble_length=25))
    print(part_two("data/input.txt", preamble_length=25))
