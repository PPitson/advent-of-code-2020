import re
from dataclasses import dataclass
from typing import Iterator


@dataclass
class Policy:
    lower_bound: int
    upper_bound: int
    letter: str

    def is_password_valid(self, password: str) -> bool:
        letter_ocurrences = password.count(self.letter)
        return self.lower_bound <= letter_ocurrences <= self.upper_bound


def valid_passwords_count(input_filename: str) -> int:
    return sum(1 for policy, password in _parse_file(input_filename) if policy.is_password_valid(password))


def _parse_file(input_filename: str) -> Iterator[tuple[Policy, str]]:
    with open(input_filename) as file:
        for line in file:
            yield _parse_line(line)


def _parse_line(line: str) -> tuple[Policy, str]:
    match = re.match(r"(?P<lower_bound>\d+)-(?P<upper_bound>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)", line)
    group_dict = match.groupdict()
    policy = Policy(
        lower_bound=int(group_dict["lower_bound"]),
        upper_bound=int(group_dict["upper_bound"]),
        letter=group_dict["letter"],
    )
    return policy, group_dict["password"]


if __name__ == "__main__":
    print(valid_passwords_count("data/input.txt"))
