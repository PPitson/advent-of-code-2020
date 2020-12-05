from typing import Iterator

ROWS = 128
COLUMNS = 8


def part_one(input_filename: str) -> int:
    return max(_decode_seat_id(seat) for seat in _parse_file(input_filename))


def part_two(input_filename: str) -> int:
    seats = _parse_file(input_filename)
    return _find_free_seat_id(seats)


def _parse_file(input_filename: str) -> Iterator[str]:
    with open(input_filename) as file:
        for line in file:
            yield line.strip()


def _decode_seat_id(seat: str) -> int:
    row, column = _decode_seat_row_and_column(seat)
    return _compute_id(row, column)


def _decode_seat_row_and_column(seat: str) -> tuple[int, int]:
    return _decode_row(seat), _decode_column(seat)


def _decode_row(seat: str) -> int:
    return _convert_binary_number_string_to_int(seat[:7].replace("F", "0").replace("B", "1"))


def _decode_column(seat: str) -> int:
    return _convert_binary_number_string_to_int(seat[-3:].replace("R", "1").replace("L", "0"))


def _convert_binary_number_string_to_int(binary: str) -> int:
    return int(binary, 2)


def _compute_id(row: int, column: int) -> int:
    return row * COLUMNS + column


def _find_free_seat_id(seats: Iterator[str]) -> int:
    row, column = _find_free_seat_row_and_column(seats)
    return _compute_id(row, column)


def _find_free_seat_row_and_column(seats: Iterator[str]) -> tuple[int, int]:
    occupied = _create_occupied_array(seats)
    first_row = _find_first_occupied_row(occupied)
    return next(
        (row, column) for row in range(first_row + 1, ROWS) for column in range(COLUMNS) if not occupied[row][column]
    )


def _create_occupied_array(seats: Iterator[str]) -> list[list[bool]]:
    occupied = [[False for _ in range(COLUMNS)] for _ in range(ROWS)]
    for seat in seats:
        row, column = _decode_seat_row_and_column(seat)
        occupied[row][column] = True
    return occupied


def _find_first_occupied_row(occupied: list[list[bool]]) -> int:
    return next(row for row in range(ROWS) if any(occupied[row]))


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
