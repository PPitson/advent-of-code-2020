from collections import deque

from day22.solution import part_one, parse_input, play_round, compute_score, play_game


def test_solution_part_one():
    assert part_one("data/test_input.txt") == 306


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


def test_compute_score():
    deck = deque([3, 2, 10, 6, 8, 5, 9, 4, 7, 1])

    score = compute_score(deck)

    assert score == 306
