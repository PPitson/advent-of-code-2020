import dataclasses
import itertools
import operator
import re
from collections import defaultdict
from dataclasses import dataclass
from functools import reduce
from typing import Optional, Iterator

Ticket = list[int]


@dataclass
class Field:
    name: str
    correct_values_ranges: list[range]

    def is_value_valid(self, value: int) -> bool:
        return any(value in values_range for values_range in self.correct_values_ranges)


@dataclass
class Notes:
    fields: list[Field]
    my_ticket: Ticket
    nearby_tickets: list[Ticket]

    @property
    def possible_field_values_ranges(self) -> Iterator[range]:
        return itertools.chain(values_range for field in self.fields for values_range in field.correct_values_ranges)


def part_one(input_filename: str) -> int:
    notes = _read_notes(input_filename)
    return _compute_ticket_scanning_error_rate(notes)


def part_two(input_filename: str, prefix: str) -> int:
    notes = _read_notes(input_filename)
    notes_without_incorrect_tickets = _remove_incorrect_tickets(notes)
    field_positions = _determine_fields_positions(notes_without_incorrect_tickets)
    positions_of_fields_starting_with_prefix = _get_positions_of_fields_starting_with_prefix(field_positions, prefix)
    field_values = (notes.my_ticket[index] for index in positions_of_fields_starting_with_prefix)
    return reduce(operator.mul, field_values, 1)


def _read_notes(input_filename: str) -> Notes:
    with open(input_filename) as file:
        return _parse_notes(file.read())


def _parse_notes(content: str) -> Notes:
    fields, my_ticket, nearby_tickets = content.split("\n\n")
    return Notes(
        fields=_parse_fields(fields),
        my_ticket=_parse_my_ticket(my_ticket),
        nearby_tickets=_parse_tickets(nearby_tickets),
    )


def _parse_fields(content: str) -> list[Field]:
    return [_parse_field_from_line(line) for line in content.split("\n")]


def _parse_field_from_line(line: str) -> Field:
    name = _parse_field_name(line)
    correct_values_ranges = _parse_field_ranges(line)
    return Field(name=name, correct_values_ranges=correct_values_ranges)


def _parse_field_name(line: str) -> str:
    return line[: line.index(":")]


def _parse_field_ranges(line: str) -> list[range]:
    ranges = re.findall(r"(?P<lower_bound>\d+)-(?P<upper_bound>\d+)", line)
    return [range(int(lower_bound), int(upper_bound) + 1) for lower_bound, upper_bound in ranges]


def _parse_my_ticket(content: str) -> Ticket:
    return _parse_tickets(content)[0]


def _parse_tickets(content: str) -> list[Ticket]:
    _header, *tickets = content.split("\n")
    return [[int(number) for number in ticket.split(",")] for ticket in tickets]


def _compute_ticket_scanning_error_rate(notes: Notes) -> int:
    invalid_values = (_value_invalid_for_any_field(notes, nearby_ticket) for nearby_ticket in notes.nearby_tickets)
    return sum(invalid_value for invalid_value in invalid_values if invalid_value is not None)


def _value_invalid_for_any_field(notes: Notes, nearby_ticket: Ticket) -> Optional[int]:
    try:
        return next(
            value
            for value in nearby_ticket
            if not any(value in values_range for values_range in notes.possible_field_values_ranges)
        )
    except StopIteration:
        return None


def _remove_incorrect_tickets(notes: Notes) -> Notes:
    correct_nearby_tickets = [
        ticket for ticket in notes.nearby_tickets if _value_invalid_for_any_field(notes, ticket) is None
    ]
    return dataclasses.replace(notes, nearby_tickets=correct_nearby_tickets)


def _determine_fields_positions(correct_notes: Notes) -> dict[str, int]:
    possible_positions = _create_possible_positions(correct_notes)
    field_positions = {}
    while len(field_positions) != len(correct_notes.fields):
        field_name, taken_position = _find_field_with_only_one_possible_position(possible_positions)
        field_positions[field_name] = taken_position
        possible_positions = _remove_taken_position_from_possible_positions(possible_positions, taken_position)

    return field_positions


def _create_possible_positions(correct_notes: Notes) -> dict[str, list[int]]:
    possible_positions = defaultdict(list)
    columns = len(correct_notes.nearby_tickets[0])
    for column in range(columns):
        values_in_column = [ticket[column] for ticket in correct_notes.nearby_tickets]
        for field in correct_notes.fields:
            if all(field.is_value_valid(value) for value in values_in_column):
                possible_positions[field.name].append(column)
    return possible_positions


def _find_field_with_only_one_possible_position(possible_positions: dict[str, list[int]]) -> tuple[str, int]:
    return next(
        (field_name, positions[0]) for field_name, positions in possible_positions.items() if len(positions) == 1
    )


def _remove_taken_position_from_possible_positions(
    possible_positions: dict[str, list[int]], taken_position: int
) -> dict[str, list[int]]:
    return {
        field_name: [position for position in positions if position != taken_position]
        for field_name, positions in possible_positions.items()
    }


def _get_positions_of_fields_starting_with_prefix(field_positions: dict[str, int], prefix: str) -> Iterator[int]:
    return (position for field_name, position in field_positions.items() if field_name.startswith(prefix))


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt", prefix="departure"))
