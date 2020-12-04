import re
from typing import Iterator

ALL_FIELDS = frozenset({"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"})
OPTIONAL_FIELDS = frozenset({"cid"})


def part_one(input_filename: str) -> int:
    return sum(1 for passport in _parse_file(input_filename) if _is_valid(passport))


def _parse_file(input_filename: str) -> Iterator[dict]:
    with open(input_filename) as file:
        file_content = file.read()
        for raw_passport in file_content.split("\n\n"):
            yield _parse_passport(raw_passport)


def _parse_passport(raw_passport: str) -> dict:
    key_value_pairs = re.findall(r"([a-z]+:\S+)[ \n]*", raw_passport)
    return dict(key_value_pair.split(":") for key_value_pair in key_value_pairs)


def _is_valid(passport: dict) -> bool:
    required_fields = ALL_FIELDS - OPTIONAL_FIELDS
    return not bool(required_fields - passport.keys())


if __name__ == "__main__":
    print(part_one("data/input.txt"))
