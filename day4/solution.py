import re
from enum import Enum
from typing import Iterator, Optional, Callable

from pydantic import Field, BaseModel, validator, ValidationError

from day4.range_validator import raise_value_error_if_value_not_in_range

ALL_FIELDS = frozenset({"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"})
OPTIONAL_FIELDS = frozenset({"cid"})

INCHES = "in"
CENTIMETERS = "cm"


class EyeColor(Enum):
    AMBER = "amb"
    BLUE = "blu"
    BROWN = "brn"
    GREY = "gry"
    GREEN = "grn"
    HAZEL = "hzl"
    OTHER = "oth"


class Passport(BaseModel):
    birth_year: str = Field(alias="byr", min_length=4, max_length=4)
    issue_year: str = Field(alias="iyr", min_length=4, max_length=4)
    expiration_year: str = Field(alias="eyr", min_length=4, max_length=4)
    height: str = Field(alias="hgt", min_length=4, max_length=5)
    hair_color: str = Field(alias="hcl", regex="#[a-f0-9]{6}")
    eye_color: EyeColor = Field(alias="ecl")
    passport_id: str = Field(alias="pid", min_length=9, max_length=9)
    country_id: Optional[str] = Field(alias="cid")

    @validator("birth_year")
    def birth_year_in_proper_range(cls, birth_year: str) -> str:
        raise_value_error_if_value_not_in_range(birth_year, min_value=1920, max_value=2002)
        return birth_year

    @validator("issue_year")
    def issue_year_in_proper_range(cls, issue_year: str) -> str:
        raise_value_error_if_value_not_in_range(issue_year, min_value=2010, max_value=2020)
        return issue_year

    @validator("expiration_year")
    def expiration_year_in_proper_range(cls, expiration_year: str) -> str:
        raise_value_error_if_value_not_in_range(expiration_year, min_value=2020, max_value=2030)
        return expiration_year

    @validator("height")
    def height_in_proper_range(cls, height: str) -> str:
        value, unit = height[:-2], height[-2:]
        if unit == INCHES:
            raise_value_error_if_value_not_in_range(
                value, min_value=59, max_value=76, error_message="height must be between 59 in and 76 in"
            )
        elif unit == CENTIMETERS:
            raise_value_error_if_value_not_in_range(
                value, min_value=150, max_value=193, error_message="height must be between 150 cm and 193 cm"
            )
        else:
            raise ValueError("Unit of height must be either in or cm")
        return height


def part_one(input_filename: str) -> int:
    return _count_valid_passports(input_filename, passport_validator=_has_required_fields)


def part_two(input_filename: str) -> int:
    return _count_valid_passports(input_filename, passport_validator=_has_required_fields_and_correct_values)


def _count_valid_passports(input_filename: str, passport_validator: Callable[[dict], bool]) -> int:
    return sum(1 for passport in _parse_file(input_filename) if passport_validator(passport))


def _parse_file(input_filename: str) -> Iterator[dict]:
    with open(input_filename) as file:
        file_content = file.read()
        for raw_passport in file_content.split("\n\n"):
            yield _parse_passport(raw_passport)


def _parse_passport(raw_passport: str) -> dict:
    key_value_pairs = re.findall(r"([a-z]+:\S+)[ \n]*", raw_passport)
    return dict(key_value_pair.split(":") for key_value_pair in key_value_pairs)


def _has_required_fields(passport: dict) -> bool:
    required_fields = ALL_FIELDS - OPTIONAL_FIELDS
    return not bool(required_fields - passport.keys())


def _has_required_fields_and_correct_values(passport: dict) -> bool:
    try:
        Passport.parse_obj(passport)
        return True
    except ValidationError:
        return False


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
