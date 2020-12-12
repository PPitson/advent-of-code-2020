from day11.constants import EMPTY_SEAT, OCCUPIED_SEAT
from day11.strategies.adjacent_seats import AdjacentSeatsStrategy
from day11.strategies.base import OccupiedSeatsStrategy


def part_one(input_filename: str) -> int:
    seat_layout = _get_initial_seat_layout(input_filename)
    layout = _get_layout_for_which_seats_dont_change_anymore(seat_layout, AdjacentSeatsStrategy())
    return _count_occupied_seats(layout)


def _get_initial_seat_layout(input_filename: str) -> list[str]:
    with open(input_filename) as file:
        return [line for line in file]


def _get_layout_for_which_seats_dont_change_anymore(
    seats_layout: list[str], occupied_seats_strategy: OccupiedSeatsStrategy
) -> list[str]:
    previous_layout = seats_layout
    new_layout = _apply_rules(previous_layout, occupied_seats_strategy)
    while new_layout != previous_layout:
        previous_layout = new_layout
        new_layout = _apply_rules(new_layout, occupied_seats_strategy)

    return new_layout


def _apply_rules(seats_layout: list[str], occupied_seats_strategy: OccupiedSeatsStrategy) -> list[str]:
    columns = len(seats_layout[0])
    rows = len(seats_layout)
    return [
        "".join(_determine_new_seat(seats_layout, row, column, occupied_seats_strategy) for column in range(columns))
        for row in range(rows)
    ]


def _determine_new_seat(
    seats_layout: list[str], row: int, column: int, occupied_seats_strategy: OccupiedSeatsStrategy
) -> str:
    seat = seats_layout[row][column]
    occupied_seats = occupied_seats_strategy.count_occupied_seats(seats_layout, row, column)
    if seat == EMPTY_SEAT and occupied_seats == 0:
        return OCCUPIED_SEAT

    min_occupied_seats = occupied_seats_strategy.min_count_of_visible_occupied_seats_for_occupied_seat_to_become_empty
    if seat == OCCUPIED_SEAT and occupied_seats >= min_occupied_seats:
        return EMPTY_SEAT

    return seat


def _count_occupied_seats(seats_layout: list[str]) -> int:
    return sum(row.count(OCCUPIED_SEAT) for row in seats_layout)


if __name__ == "__main__":
    print(part_one("data/input.txt"))
