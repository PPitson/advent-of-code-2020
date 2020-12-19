def part_one(input_filename: str) -> int:
    return _get_last_spoken_number_in_the_game_after_number_of_turns(input_filename, number_of_turns=2020)


def part_two(input_filename: str) -> int:
    return _get_last_spoken_number_in_the_game_after_number_of_turns(input_filename, number_of_turns=30000000)


def _get_last_spoken_number_in_the_game_after_number_of_turns(input_filename: str, number_of_turns: int) -> int:
    starting_numbers = _get_starting_numbers(input_filename)
    return play_game(starting_numbers, number_of_turns)


def _get_starting_numbers(input_filename: str) -> list[int]:
    with open(input_filename) as file:
        numbers_string = file.read()
        return [int(number) for number in numbers_string.split(",")]


def play_game(starting_numbers: list[int], number_of_turns: int) -> int:
    if number_of_turns <= len(starting_numbers):
        return starting_numbers[number_of_turns - 1]

    seen_numbers = {number: turn for turn, number in enumerate(starting_numbers[:-1], start=1)}
    last_spoken = starting_numbers[-1]
    for turn in range(len(starting_numbers) + 1, number_of_turns + 1):
        previous_number_was_first_time_spoken = last_spoken not in seen_numbers
        if previous_number_was_first_time_spoken:
            seen_numbers[last_spoken] = turn - 1
            last_spoken = 0
        else:
            number = turn - 1 - seen_numbers[last_spoken]
            seen_numbers[last_spoken] = turn - 1
            last_spoken = number
    return last_spoken


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
