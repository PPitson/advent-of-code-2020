from typing import Iterator


def part_one(input_filename: str) -> int:
    return max(_decode_seat_id(seat) for seat in _parse_file(input_filename))


def _parse_file(input_filename: str) -> Iterator[str]:
    with open(input_filename) as file:
        for line in file:
            yield line


def _decode_seat_id(seat: str) -> int:
    row = _decode_row(seat)
    column = _decode_column(seat)
    return row * 8 + column


def _decode_row(seat: str) -> int:
    return _convert_binary_number_string_to_int(seat[:7].replace("F", "0").replace("B", "1"))


def _decode_column(seat: str) -> int:
    return _convert_binary_number_string_to_int(seat[-3:].replace("R", "1").replace("L", "0"))


def _convert_binary_number_string_to_int(binary: str) -> int:
    return int(binary, 2)


if __name__ == '__main__':
    print(part_one("data/input.txt"))
