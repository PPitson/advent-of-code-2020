from day9.solution import part_one, part_two


def test_solution_part_one():
    assert part_one("data/test_input.txt", preamble_length=5) == 127


def test_solution_part_two():
    assert part_two("data/test_input.txt", preamble_length=5) == 62
