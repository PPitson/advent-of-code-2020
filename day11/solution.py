FLOOR = "."
EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"


def part_one(input_filename: str) -> int:
    seat_layout = _get_initial_seat_layout(input_filename)
    layout = _get_layout_for_which_seats_dont_change_anymore(seat_layout)
    return _count_occupied_seats(layout)


def _get_initial_seat_layout(input_filename: str) -> list[str]:
    with open(input_filename) as file:
        return [line for line in file]


def _get_layout_for_which_seats_dont_change_anymore(seats_layout: list[str]) -> list[str]:
    previous_layout = seats_layout
    new_layout = _apply_rules(previous_layout)
    while new_layout != previous_layout:
        previous_layout = new_layout
        new_layout = _apply_rules(new_layout)

    return new_layout


def _apply_rules(seats_layout: list[str]) -> list[str]:
    columns = len(seats_layout[0])
    rows = len(seats_layout)
    return ["".join(_determine_new_seat(seats_layout, row, column) for column in range(columns)) for row in range(rows)]


def _determine_new_seat(seats_layout: list[str], row: int, column: int) -> str:
    seat = seats_layout[row][column]
    adjacent_occupied_seats = _count_adjacent_occupied_seats(seats_layout, row, column)
    if seat == EMPTY_SEAT and adjacent_occupied_seats == 0:
        return OCCUPIED_SEAT

    if seat == OCCUPIED_SEAT and adjacent_occupied_seats >= 4:
        return EMPTY_SEAT

    return seat


def _count_adjacent_occupied_seats(seats_layout: list[str], row: int, column: int) -> int:
    adjacent_seats_indices = _get_adjacent_seats_indices(seats_layout, row, column)
    return sum(
        1 for seat_row, seat_column in adjacent_seats_indices if seats_layout[seat_row][seat_column] == OCCUPIED_SEAT
    )


def _get_adjacent_seats_indices(seats_layout: list[str], row: int, column: int) -> list[tuple[int, int]]:
    max_column = len(seats_layout[0])
    max_row = len(seats_layout)
    return (
        _get_adjacent_seats_indices_for_upper_row(row, column, max_column)
        + _get_adjacent_seats_indices_for_same_row(row, column, max_column)
        + _get_adjacent_seats_indices_for_lower_row(row, column, max_column, max_row)
    )


def _get_adjacent_seats_indices_for_upper_row(row: int, column: int, max_column: int) -> list[tuple[int, int]]:
    adjacent_seats = []
    if row - 1 >= 0:
        if column - 1 >= 0:
            adjacent_seats += [(row - 1, column - 1)]
        adjacent_seats += [(row - 1, column)]
        if column + 1 < max_column:
            adjacent_seats += [(row - 1, column + 1)]
    return adjacent_seats


def _get_adjacent_seats_indices_for_same_row(row: int, column: int, max_column: int) -> list[tuple[int, int]]:
    adjacent_seats = []
    if column - 1 >= 0:
        adjacent_seats += [(row, column - 1)]
    if column + 1 < max_column:
        adjacent_seats += [(row, column + 1)]
    return adjacent_seats


def _get_adjacent_seats_indices_for_lower_row(
    row: int, column: int, max_column: int, max_row: int
) -> list[tuple[int, int]]:
    adjacent_seats = []
    if row + 1 < max_row:
        if column - 1 >= 0:
            adjacent_seats += [(row + 1, column - 1)]
        adjacent_seats += [(row + 1, column)]
        if column + 1 < max_column:
            adjacent_seats += [(row + 1, column + 1)]
    return adjacent_seats


def _count_occupied_seats(seats_layout: list[str]) -> int:
    return sum(row.count(OCCUPIED_SEAT) for row in seats_layout)


if __name__ == "__main__":
    print(part_one("data/input.txt"))
