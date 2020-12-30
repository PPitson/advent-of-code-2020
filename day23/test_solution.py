from day23.solution import part_one, play_game, make_move, get_result_label


def test_solution_part_one():
    assert part_one("389125467") == "67384529"


def test_play_game():
    assert play_game("389125467", moves=10) == "92658374"


def test_make_move():
    assert make_move([3, 8, 9, 1, 2, 5, 4, 6, 7], 0) == ([3, 2, 8, 9, 1, 5, 4, 6, 7], 1)
    assert make_move([3, 2, 8, 9, 1, 5, 4, 6, 7], 1) == ([3, 2, 5, 4, 6, 7, 8, 9, 1], 2)


def test_get_result_label():
    cups = [5, 3, 7, 4, 1, 9, 2, 6]
    expected_result = "9265374"

    result = get_result_label(cups)

    assert result == expected_result
