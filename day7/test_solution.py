from day7.solution import part_one, part_two


def test_solution_part_one():
    assert part_one("data/test_input.txt") == 4


def test_solution_part_two_simple():
    assert part_two("data/test_input.txt") == 32


def test_solution_part_two():
    assert part_two("data/test_input2.txt") == 126
