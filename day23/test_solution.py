from day23.solution import part_one, play_game, get_result_label


def test_solution_part_one():
    assert part_one("389125467") == "67384529"


def test_play_game():
    assert play_game("389125467", moves=10) == "92658374"


def test_get_result_label():
    cups = {5: 8, 8: 3, 3: 7, 7: 4, 4: 1, 1: 9, 9: 2, 2: 6, 6: 5}
    expected_result = "92658374"

    result = get_result_label(cups)

    assert result == expected_result
