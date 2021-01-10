from day23.solution import part_one, play_game, get_result_label, part_two


def test_solution_part_one():
    assert part_one("389125467") == "67384529"


def test_solution_part_two():
    assert part_two("389125467") == 149245887792


def test_play_game():
    expected_result = {5: 8, 8: 3, 3: 7, 7: 4, 4: 1, 1: 9, 9: 2, 2: 6, 6: 5}

    assert play_game([3, 8, 9, 1, 2, 5, 4, 6, 7], moves=10) == expected_result


def test_get_result_label():
    cups = {5: 8, 8: 3, 3: 7, 7: 4, 4: 1, 1: 9, 9: 2, 2: 6, 6: 5}
    expected_result = "92658374"

    result = get_result_label(cups)

    assert result == expected_result
