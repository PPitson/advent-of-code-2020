import pytest

from day15.solution import part_one, play_game, part_two


@pytest.mark.parametrize(
    "starting_numbers, expected_result",
    [("1,3,2", 1), ("2,1,3", 10), ("1,2,3", 27), ("2,3,1", 78), ("3,2,1", 438), ("3,1,2", 1836), ("0,3,6", 436)],
)
def test_solution_part_one(tmp_path, starting_numbers, expected_result):
    input_filename = tmp_path / "test_input.txt"
    input_filename.write_text(starting_numbers)

    assert part_one(input_filename.as_posix()) == expected_result


def test_play_game_when_number_of_turns_is_no_greater_than_starting_numbers_count():
    assert play_game([6, 11, 3, 10, 9], number_of_turns=5) == 9
    assert play_game([6, 11, 3, 10, 9], number_of_turns=4) == 10


@pytest.mark.parametrize(
    "starting_numbers, expected_result",
    [
        ("1,3,2", 2578),
        ("2,1,3", 3544142),
        ("1,2,3", 261214),
        ("2,3,1", 6895259),
        ("3,2,1", 18),
        ("3,1,2", 362),
        ("0,3,6", 175594),
    ],
)
def test_solution_part_two(tmp_path, starting_numbers, expected_result):
    input_filename = tmp_path / "test_input.txt"
    input_filename.write_text(starting_numbers)

    assert part_two(input_filename.as_posix()) == expected_result
