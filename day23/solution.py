def part_one(labels_input: str) -> str:
    return play_game(labels_input, moves=100)


def play_game(labels_input: str, moves: int) -> str:
    cups = _create_cups(labels_input)
    current_cup = int(labels_input[0])
    for i in range(moves):
        cups, current_cup = make_move(cups, current_cup)

    return get_result_label(cups)


def _create_cups(labels_input: str) -> dict[int, int]:
    cups = list(map(int, labels_input))
    result = {cup: cups[index + 1] for index, cup in enumerate(cups[:-1])}
    result[cups[-1]] = cups[0]
    return result


def make_move(cups: dict[int, int], current_cup: int) -> tuple[dict[int, int], int]:
    first_picked_cup = cups[current_cup]
    second_picked_cup = cups[first_picked_cup]
    third_picked_cup = cups[second_picked_cup]

    destination = _get_destination(current_cup, cups, {first_picked_cup, second_picked_cup, third_picked_cup})

    cup_next_to_destination = cups[destination]
    cup_next_to_third_picked_cup = cups[third_picked_cup]
    cups[current_cup] = cup_next_to_third_picked_cup
    cups[destination] = first_picked_cup
    cups[third_picked_cup] = cup_next_to_destination

    return cups, cups[current_cup]


def _get_destination(current_cup: int, cups: dict[int, int], picked_cups: set[int]) -> int:
    candidate = current_cup - 1
    while candidate > 0:
        if candidate not in picked_cups:
            return candidate
        candidate -= 1

    return max(set(cups.values()) - picked_cups)


def get_result_label(cups: dict[int, int]) -> str:
    value = cups[1]
    result = []
    while value != 1:
        result.append(str(value))
        value = cups[value]
    return "".join(result)


if __name__ == "__main__":
    print(part_one("562893147"))
