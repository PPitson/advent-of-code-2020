from day18.solution import part_one, part_two


def test_solution_part_one():
    assert part_one("data/test_input.txt") == 71 + 51 + 26 + 437 + 12240 + 13632


def test_solution_part_two():
    assert part_two("data/test_input.txt") == 231 + 51 + 46 + 1445 + 669060 + 23340
