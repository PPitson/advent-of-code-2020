from typing import Iterator


def part_one(input_filename: str) -> int:
    return sum(_count_unique_answers_in_group(answers_in_group) for answers_in_group in _parse_file(input_filename))


def _parse_file(input_filename: str) -> Iterator[str]:
    with open(input_filename) as file:
        all_answers = file.read()
        for answers_in_group in all_answers.split("\n\n"):
            yield answers_in_group


def _count_unique_answers_in_group(answers_in_group: str) -> int:
    return len(set(answers_in_group.replace("\n", "")))


if __name__ == "__main__":
    print(part_one("data/input.txt"))
