import math
from dataclasses import dataclass
from functools import partial

BUS_OUT_OF_SERVICE = "x"


@dataclass
class Notes:
    earliest_departure_timestamp: int
    bus_ids_in_service: list[int]


def part_one(input_filename: str) -> int:
    notes = _parse_notes(input_filename)
    bus_id = _get_earliest_bus_id(notes)
    return _get_number_of_minutes_to_wait_for_bus(notes, bus_id) * bus_id


def _parse_notes(input_filename: str) -> Notes:
    with open(input_filename) as file:
        earliest_departure_timestamp = int(next(file))
        bus_ids_in_service = [int(bus_id) for bus_id in next(file).split(",") if bus_id != BUS_OUT_OF_SERVICE]
        return Notes(earliest_departure_timestamp, bus_ids_in_service)


def _get_earliest_bus_id(notes: Notes) -> int:
    return min(notes.bus_ids_in_service, key=partial(_earliest_timestamp_to_take_bus_id, notes))


def _earliest_timestamp_to_take_bus_id(notes: Notes, bus_id: int) -> int:
    return math.ceil(notes.earliest_departure_timestamp / bus_id) * bus_id


def _get_number_of_minutes_to_wait_for_bus(notes: Notes, bus_id: int) -> int:
    bus_arrival_timestamp = _earliest_timestamp_to_take_bus_id(notes, bus_id)
    return bus_arrival_timestamp - notes.earliest_departure_timestamp


if __name__ == "__main__":
    print(part_one("data/input.txt"))
