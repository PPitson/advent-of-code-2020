from collections import deque


def part_one(input_filename: str) -> int:
    player_decks = _get_player_decks(input_filename)
    winning_player_deck = play_game(*player_decks)
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
    player_1_card = player_1_deck.popleft()
    player_2_card = player_2_deck.popleft()
    deck = player_1_deck if player_1_card > player_2_card else player_2_deck
    higher_card = player_1_card if player_1_card > player_2_card else player_2_card
    lower_card = player_2_card if player_1_card > player_2_card else player_1_card
    deck.append(higher_card)
    deck.append(lower_card)


def compute_score(deck: deque[int]) -> int:
    return sum(card * multiplier for multiplier, card in enumerate(reversed(deck), start=1))


if __name__ == "__main__":
    print(part_one("data/input.txt"))
