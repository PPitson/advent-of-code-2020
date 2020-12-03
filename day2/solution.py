import abc
import re
from dataclasses import dataclass
from typing import Iterator, Type


@dataclass
class Policy(abc.ABC):
    first_number: int
    second_number: int
    letter: str

    @abc.abstractmethod
    def is_password_valid(self, password: str) -> bool:
        pass


class LetterOcurrencesInRangePolicy(Policy):
    def is_password_valid(self, password: str) -> bool:
        lower_bound, upper_bound = self.first_number, self.second_number
        letter_ocurrences = password.count(self.letter)
        return lower_bound <= letter_ocurrences <= upper_bound


class LetterOnOneOfPositionsPolicy(Policy):
    def is_password_valid(self, password: str) -> bool:
        first_position = self.first_number - 1
        second_position = self.second_number - 1
        return (password[first_position] == self.letter and password[second_position] != self.letter) or (
            password[first_position] != self.letter and password[second_position] == self.letter
        )


def part_one(input_filename: str) -> int:
    return valid_passwords_count(input_filename, LetterOcurrencesInRangePolicy)


def part_two(input_filename: str) -> int:
    return valid_passwords_count(input_filename, LetterOnOneOfPositionsPolicy)


def valid_passwords_count(input_filename: str, policy_factory: Type[Policy]) -> int:
    return sum(
        1 for policy, password in _parse_file(input_filename, policy_factory) if policy.is_password_valid(password)
    )


def _parse_file(input_filename: str, policy_factory: Type[Policy]) -> Iterator[tuple[Policy, str]]:
    with open(input_filename) as file:
        for line in file:
            yield _parse_line(line, policy_factory)


def _parse_line(line: str, policy_factory: Type[Policy]) -> tuple[Policy, str]:
    match = re.match(r"(?P<first_number>\d+)-(?P<second_number>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)", line)
    group_dict = match.groupdict()
    policy = policy_factory(
        first_number=int(group_dict["first_number"]),
        second_number=int(group_dict["second_number"]),
        letter=group_dict["letter"],
    )
    return policy, group_dict["password"]


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
