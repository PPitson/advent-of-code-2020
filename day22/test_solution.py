from collections import deque

import pytest

from day22.solution import (
    part_one,
    parse_input,
    play_round,
    compute_score,
    play_game,
    play_recursive_game,
    play_round_of_recursive_game,
    part_two,
)


def test_solution_part_one():
    assert part_one("data/test_input.txt") == 306


def test_solution_part_two():
    assert part_two("data/test_input.txt") == 291


def test_parse_input():
    file_content = """Player 1:
9
2
6

Player 2:
5
8
4"""
    expected_result = (deque([9, 2, 6]), deque([5, 8, 4]))

    result = parse_input(file_content)

    assert result == expected_result


def test_play_round():
    player_1_deck = deque([9, 2, 6, 3, 1])
    player_2_deck = deque([5, 8, 4, 7, 10])

    play_round(player_1_deck, player_2_deck)

    assert player_1_deck == deque([2, 6, 3, 1, 9, 5])
    assert player_2_deck == deque([8, 4, 7, 10])


def test_play_game():
    player_1_deck = deque([9, 2, 6])
    player_2_deck = deque([5, 8, 4])
    winning_player_deck = deque([6, 4, 9, 8, 5, 2])

    result = play_game(player_1_deck, player_2_deck)

    assert result == winning_player_deck


@pytest.mark.parametrize(
    "description, player_1_deck, player_2_deck, expected_player_1_deck, expected_player_2_deck",
    [
        ("simple higher card wins", [9, 2, 6, 3, 1], [5, 8, 4, 7, 10], [2, 6, 3, 1, 9, 5], [8, 4, 7, 10]),
        ("subgame winner wins", [4, 9, 8, 5, 2], [3, 10, 1, 7, 6], [9, 8, 5, 2], [10, 1, 7, 6, 3, 4]),
        ("subgame(s) winner wins", [2, 8, 1], [6, 3, 4, 10, 9, 7, 5], [8, 1], [3, 4, 10, 9, 7, 5, 6, 2]),
    ],
)
def test_play_round_of_recursive_game(
    description, player_1_deck, player_2_deck, expected_player_1_deck, expected_player_2_deck
):
    player_1_deck = deque(player_1_deck)
    player_2_deck = deque(player_2_deck)

    play_round_of_recursive_game(player_1_deck, player_2_deck)

    assert player_1_deck == deque(expected_player_1_deck)
    assert player_2_deck == deque(expected_player_2_deck)


def test_play_recursive_game():
    player_1_deck = deque([9, 2, 6, 3, 1])
    player_2_deck = deque([5, 8, 4, 7, 10])
    winning_player_deck = deque([7, 5, 6, 2, 4, 1, 10, 8, 9, 3])

    result = play_recursive_game(player_1_deck, player_2_deck)

    assert result == winning_player_deck


def test_play_recursive_game_player_one_wins_if_infinite_loop_spotted():
    player_1_deck = deque([43, 19])
    player_2_deck = deque([2, 29, 14])
    winning_player_deck = deque([43, 19])

    result = play_recursive_game(player_1_deck, player_2_deck)

    assert result == winning_player_deck


def test_compute_score():
    deck = deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])

    score = compute_score(deck)

    assert score == 306
