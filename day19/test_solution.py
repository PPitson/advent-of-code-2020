import pytest
import regex

from day19.solution import (
    part_one,
    decode_rule,
    replace_id_with_its_rule,
    get_ids,
    get_boundaries_of_number_in_string,
    part_two,
)


def test_solution_part_one():
    assert part_one("data/test_input.txt") == 2
    assert part_one("data/test_input2.txt") == 3


def test_solution_part_two():
    assert part_two("data/test_input2.txt") == 12


def test_decode_rule():
    rules = {0: "4 1 5", 1: "2 3 | 3 2", 2: "4 4 | 5 5", 3: "4 5 | 5 4", 4: "a", 5: "b"}
    expected_result = regex.compile(r"^(a)(((a)(a)|(b)(b))((a)(b)|(b)(a))|((a)(b)|(b)(a))((a)(a)|(b)(b)))(b)$")

    result = decode_rule(rules, rule_id_to_decode=0)

    assert result == expected_result


@pytest.mark.parametrize(
    "rule, id_to_replace, expected_result",
    [
        ("4 1 5", 1, "4 (2 3 | 3 2) 5"),
        ("4 1 5", 5, "4 1 (b)"),
        ("4 1 51", 5, "4 1 51"),
        ("4 1 5", 4, "(a) 1 5"),
        ("24 1 5", 4, "24 1 5"),
        ("2 3 | 3 2", 2, "(4 4 | 5 5) 3 | 3 (4 4 | 5 5)"),
        ("2 3 | 3 2 | 6", 2, "(4 4 | 5 5) 3 | 3 (4 4 | 5 5) | 6"),
        ("6 | 2 3 | 3 2", 2, "6 | (4 4 | 5 5) 3 | 3 (4 4 | 5 5)"),
    ],
)
def test_replace_id_with_its_rule(rule, id_to_replace, expected_result):
    rules = {
        0: "4 1 5",
        1: "2 3 | 3 2",
        2: "4 4 | 5 5",
        3: "4 5 | 5 4",
        4: "a",
        5: "b",
    }

    result = replace_id_with_its_rule(rules, rule, id_to_replace)

    assert result == expected_result


@pytest.mark.parametrize(
    "rule, expected_result", [("4 1 5 | 3 2", {4, 1, 5, 3, 2}), ("(a) (2 (4 5 | 5 4) | (4 5 | 5 4) 2) (b)", {2, 4, 5})]
)
def test_get_ids(rule, expected_result):
    assert get_ids(rule) == expected_result


@pytest.mark.parametrize(
    "rule, number, expected_result",
    [
        ("4 1 5", 5, [(4, 5)]),
        ("4 1 5", 1, [(2, 3)]),
        ("4 1 51", 5, []),
        ("24 1 5", 4, []),
        ("22 3 | 3 22", 22, [(0, 2), (9, 11)]),
    ],
)
def test_get_boundaries_of_number_in_string(rule, number, expected_result):
    result = get_boundaries_of_number_in_string(rule, number)

    assert result == expected_result
