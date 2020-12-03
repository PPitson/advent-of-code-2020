from day2.solution import part_one, part_two


def test_passwords_valid_part_one():
    assert part_one("data/test_input.txt") == 2


def test_passwords_valid_part_two():
    assert part_two("data/test_input.txt") == 1
