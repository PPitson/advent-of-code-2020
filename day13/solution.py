import itertools
import math
from dataclasses import dataclass
from functools import partial

BUS_OUT_OF_SERVICE = "x"


@dataclass
class Notes:
    earliest_departure_timestamp: int
    bus_ids_in_service: list[int]


def part_one(input_filename: str) -> int:
    file_lines = _get_file_lines(input_filename)
    notes = _parse_notes(file_lines)
    bus_id = _get_earliest_bus_id(notes)
    return _get_number_of_minutes_to_wait_for_bus(notes, bus_id) * bus_id


def part_two(input_filename: str) -> int:
    file_lines = _get_file_lines(input_filename)
    bus_ids = _get_bus_ids(file_lines)
    return _find_timestamp(bus_ids)


def _get_file_lines(input_filename: str) -> list[str]:
    with open(input_filename) as file:
        return list(file)


def _parse_notes(file_lines: list[str]) -> Notes:
    earliest_departure_timestamp = int(file_lines[0])
    bus_ids_in_service = [int(bus_id) for bus_id in file_lines[1].split(",") if bus_id != BUS_OUT_OF_SERVICE]
    return Notes(earliest_departure_timestamp, bus_ids_in_service)


def _get_earliest_bus_id(notes: Notes) -> int:
    return min(notes.bus_ids_in_service, key=partial(_earliest_timestamp_to_take_bus_id, notes))


def _earliest_timestamp_to_take_bus_id(notes: Notes, bus_id: int) -> int:
    return math.ceil(notes.earliest_departure_timestamp / bus_id) * bus_id


def _get_number_of_minutes_to_wait_for_bus(notes: Notes, bus_id: int) -> int:
    bus_arrival_timestamp = _earliest_timestamp_to_take_bus_id(notes, bus_id)
    return bus_arrival_timestamp - notes.earliest_departure_timestamp


def _get_bus_ids(file_lines: list[str]) -> list[int]:
    return [int(bus_id) if bus_id != BUS_OUT_OF_SERVICE else -1 for bus_id in file_lines[1].split(",")]


def _find_timestamp(bus_ids: list[int]) -> int:
    max_bus_id = max(bus_ids)
    max_bus_id_index = bus_ids.index(max_bus_id)
    other_bus_ids_with_time_diff = [
        (bus_id, index - max_bus_id_index)
        for index, bus_id in enumerate(bus_ids)
        if bus_id != -1 and bus_id != max_bus_id
    ]
    candidate = next(
        candidate
        for candidate in itertools.count(start=max_bus_id, step=max_bus_id)
        if all((candidate + time_diff) % bus_id == 0 for bus_id, time_diff in other_bus_ids_with_time_diff)
    )
    return candidate - max_bus_id_index


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
