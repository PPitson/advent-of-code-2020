from typing import Iterator


def part_one(input_filename: str) -> int:
    numbers = _get_numbers_from_file(input_filename)
    first, second = _find_pair_which_sums_to(numbers, desired_sum=2020)
    return first * second


def _get_numbers_from_file(input_filename: str) -> Iterator[int]:
    with open(input_filename) as file:
        for line in file:
            yield int(line)


def _find_pair_which_sums_to(numbers: Iterator[int], *, desired_sum: int) -> tuple[int, int]:
    unique_numbers = set(numbers)
    for number in unique_numbers:
        remainder = desired_sum - number
        if remainder in unique_numbers:
            return number, remainder
    return -1, -1


if __name__ == "__main__":
    result = part_one("data/input.txt")
    print(result)
