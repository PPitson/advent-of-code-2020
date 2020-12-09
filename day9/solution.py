import collections
import itertools
from typing import Iterator, Iterable, Any


def part_one(input_filename: str, preamble_length: int) -> int:
    numbers = _get_numbers(input_filename)
    return _find_number(numbers, preamble_length=preamble_length)


def _get_numbers(input_filename: str) -> Iterator[int]:
    with open(input_filename) as file:
        for line in file:
            yield int(line)


def _find_number(numbers: Iterator[int], preamble_length: int) -> int:
    deque = collections.deque(_take_first_n_numbers(preamble_length, numbers), maxlen=preamble_length)
    for number in numbers:
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


if __name__ == "__main__":
    print(part_one("data/input.txt", preamble_length=25))
