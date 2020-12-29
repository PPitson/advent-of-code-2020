from collections import deque
from collections.abc import Callable
from enum import Enum


class Player(Enum):
    ONE = "Player 1"
    TWO = "Player 2"


def part_one(input_filename: str) -> int:
    player_decks = _get_player_decks(input_filename)
    winning_player_deck = play_game(*player_decks)
    return compute_score(winning_player_deck)


def part_two(input_filename: str) -> int:
    player_decks = _get_player_decks(input_filename)
    winning_player_deck = play_recursive_game(*player_decks)
    return compute_score(winning_player_deck)


def _get_player_decks(input_filename: str) -> tuple[deque[int], deque[int]]:
    with open(input_filename) as file:
        return parse_input(file.read())


def parse_input(file_content: str) -> tuple[deque[int], deque[int]]:
    first_player_deck, second_player_deck = file_content.split("\n\n")
    return _parse_deck(first_player_deck), _parse_deck(second_player_deck)


def _parse_deck(player_deck: str) -> deque[int]:
    heading, *cards = player_deck.split("\n")
    return deque(map(int, cards))


def play_game(player_1_deck: deque[int], player_2_deck: deque[int]) -> deque[int]:
    while player_1_deck and player_2_deck:
        play_round(player_1_deck, player_2_deck)

    return player_1_deck if player_1_deck else player_2_deck


def play_round(player_1_deck: deque[int], player_2_deck: deque[int]) -> None:
    return _play_round(player_1_deck, player_2_deck, _higher_card_wins)


def _play_round(
    player_1_deck: deque[int],
    player_2_deck: deque[int],
    determine_winner: Callable[[deque[int], deque[int], int, int], Player],
) -> None:
    player_1_card = player_1_deck.popleft()
    player_2_card = player_2_deck.popleft()
    winner = determine_winner(player_1_deck, player_2_deck, player_1_card, player_2_card)
    deck = player_1_deck if winner == Player.ONE else player_2_deck
    higher_card = player_1_card if winner == Player.ONE else player_2_card
    lower_card = player_2_card if winner == Player.ONE else player_1_card
    deck.append(higher_card)
    deck.append(lower_card)


def _higher_card_wins(
    _player_1_deck: deque[int], _player_2_deck: deque[int], player_1_card: int, player_2_card: int
) -> Player:
    return Player.ONE if player_1_card > player_2_card else Player.TWO


def play_recursive_game(player_1_deck: deque[int], player_2_deck: deque[int]) -> deque[int]:
    _winner, winning_deck = _play_recursive_game(player_1_deck, player_2_deck, previous_states=set())
    return winning_deck


def _play_recursive_game(
    player_1_deck: deque[int], player_2_deck: deque[int], previous_states: set[tuple[tuple[int], tuple[int]]],
) -> tuple[Player, deque[int]]:
    while player_1_deck and player_2_deck:
        current_state = (tuple(player_1_deck), tuple(player_2_deck))
        if current_state in previous_states:
            return Player.ONE, player_1_deck

        previous_states.add(current_state)
        play_round_of_recursive_game(player_1_deck, player_2_deck)

    return (Player.ONE, player_1_deck) if player_1_deck else (Player.TWO, player_2_deck)


def play_round_of_recursive_game(player_1_deck: deque[int], player_2_deck: deque[int]) -> None:
    _play_round(player_1_deck, player_2_deck, _determine_round_winner_of_recursive_game)


def _determine_round_winner_of_recursive_game(
    player_1_deck: deque[int], player_2_deck: deque[int], player_1_card: int, player_2_card: int
) -> Player:
    if len(player_1_deck) >= player_1_card and len(player_2_deck) >= player_2_card:
        winner, _winning_deck = _play_recursive_game(
            _get_first_n(player_1_deck, player_1_card),
            _get_first_n(player_2_deck, player_2_card),
            previous_states=set(),
        )
        return winner

    return _higher_card_wins(player_1_deck, player_2_deck, player_1_card, player_2_card)


def _get_first_n(deq: deque[int], n: int) -> deque[int]:
    return deque(list(deq)[:n])


def compute_score(deck: deque[int]) -> int:
    return sum(card * multiplier for multiplier, card in enumerate(reversed(deck), start=1))


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
