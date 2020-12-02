from day1.solution import part_one


def test_solution_part_one():
    expected_result = 514579

    result = part_one("data/test_input.txt")

    assert result == expected_result
