from day1.solution import part_one, part_two


def test_solution_part_one():
    assert part_one("data/test_input.txt") == 514579


def test_solution_part_two():
    assert part_two("data/test_input.txt") == 241861950


def test_solution_part_two_not_found():
    assert part_two("data/test_not_found.txt") == -1
