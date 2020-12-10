from day10.solution import part_one, part_two


def test_solution_part_one():
    assert part_one("data/test_input.txt") == 35


def test_solution_part_one_second_example():
    assert part_one("data/test_input2.txt") == 220


def test_solution_part_two():
    assert part_two("data/test_input.txt") == 8


def test_solution_part_two_second_example():
    assert part_two("data/test_input2.txt") == 19208
