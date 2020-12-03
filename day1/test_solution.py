from day1.solution import part_one, part_two


def test_solution_part_one():
    assert part_one("data/test_input.txt") == 514579


def test_solution_part_one_doesnt_pick_same_entry_twice():
    assert part_one("data/test_doesnt_pick_same_entry_part_one.txt") == 1


def test_solution_part_two():
    assert part_two("data/test_input.txt") == 241861950


def test_solution_part_two_doesnt_pick_same_entry_twice():
    assert part_two("data/test_doesnt_pick_same_entry_part_two.txt") == -1
