def part_one(input_filename: str) -> int:
    numbers = _get_numbers_from_file(input_filename)
    first, second = _find_pair_which_sums_to(numbers, desired_sum=2020)
    return first * second


def _get_numbers_from_file(input_filename: str) -> list[int]:
    def _numbers_generator():
        with open(input_filename) as file:
            for line in file:
                yield int(line)

    return list(_numbers_generator())


def _find_pair_which_sums_to(numbers: list[int], *, desired_sum: int) -> tuple[int, int]:
    for index, number in enumerate(numbers):
        remainder = desired_sum - number
        if remainder in numbers[index + 1 :]:
            return number, remainder
    return -1, -1


def part_two(input_filename: str) -> int:
    numbers = _get_numbers_from_file(input_filename)
    first, second, third = _find_triple_which_sums_to(numbers, desired_sum=2020)
    return first * second * third


def _find_triple_which_sums_to(numbers: list[int], *, desired_sum: int) -> tuple[int, int, int]:
    for index, first_number in enumerate(numbers):
        for second_index, second_number in enumerate(numbers[index + 1 :]):
            remainder = desired_sum - first_number - second_number
            if remainder in numbers[second_index + 1 :]:
                return first_number, second_number, remainder
    return -1, -1, -1


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
