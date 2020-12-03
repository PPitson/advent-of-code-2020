import pytest

from day1.solution import part_one, part_two, EntriesNotFound


def test_solution_part_one():
    assert part_one("data/test_input.txt") == 514579


def test_solution_part_one_doesnt_pick_same_entry_twice():
    with pytest.raises(EntriesNotFound):
        part_one("data/test_doesnt_pick_same_entry_part_one.txt")


def test_solution_part_two():
    assert part_two("data/test_input.txt") == 241861950


def test_solution_part_two_doesnt_pick_same_entry_twice():
    with pytest.raises(EntriesNotFound):
        part_two("data/test_doesnt_pick_same_entry_part_two.txt")
