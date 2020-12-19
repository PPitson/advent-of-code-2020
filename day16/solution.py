import itertools
import re
from dataclasses import dataclass
from typing import Iterable, Optional

Ticket = list[int]


@dataclass
class Field:
    name: str
    correct_values_ranges: list[range]


@dataclass
class Notes:
    fields: list[Field]
    my_ticket: Ticket
    nearby_tickets: list[Ticket]

    @property
    def possible_field_values_ranges(self) -> Iterable[range]:
        return itertools.chain(values_range for field in self.fields for values_range in field.correct_values_ranges)


def part_one(input_filename: str) -> int:
    notes = _read_notes(input_filename)
    return _compute_ticket_scanning_error_rate(notes)


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


if __name__ == "__main__":
    print(part_one("data/input.txt"))
