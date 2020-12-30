def part_one(labels_input: str) -> str:
    return play_game(labels_input, moves=100)


def play_game(labels_input: str, moves: int) -> str:
    cups = list(map(int, labels_input))
    current_cup_index = 0
    for i in range(moves):
        cups, current_cup_index = make_move(cups, current_cup_index)

    return get_result_label(cups)


def make_move(cups: list[int], current_cup_index: int) -> tuple[list[int], int]:
    current_cup = cups[current_cup_index]
    picked_cups = _pick_cups_clockwise_of_current_cup(cups, current_cup_index)
    cups = _remove_picked_cups(cups, picked_cups)
    destination_cup = _get_destination_cup(cups, current_cup)
    cups = _place_picked_cups(cups, picked_cups, destination_cup)
    current_cup_index = _get_new_current_cup_index(cups, current_cup)
    return cups, current_cup_index


def _pick_cups_clockwise_of_current_cup(cups: list[int], current_cup_index: int) -> list[int]:
    indices = ((current_cup_index + n) % len(cups) for n in range(1, 4))
    return [cups[index] for index in indices]


def _remove_picked_cups(cups: list[int], picked_cups: list[int]) -> list[int]:
    return [label for label in cups if label not in picked_cups]


def _get_destination_cup(cups: list[int], current_cup: int) -> int:
    candidate = current_cup - 1
    while candidate > 0:
        if candidate in cups:
            return candidate
        candidate -= 1

    return max(cups)


def _place_picked_cups(cups: list[int], picked_cups: list[int], destination_cup: int) -> list[int]:
    destination_cup_index = cups.index(destination_cup)
    return cups[: destination_cup_index + 1] + picked_cups + cups[destination_cup_index + 1 :]


def _get_new_current_cup_index(cups: list[int], current_cup: int) -> int:
    return (cups.index(current_cup) + 1) % len(cups)


def get_result_label(cups: list[int]) -> str:
    one_index = cups.index(1)
    return "".join(str(label) for label in cups[one_index + 1 :]) + "".join(str(label) for label in cups[:one_index])


if __name__ == "__main__":
    print(part_one("562893147"))
