import re
from typing import Pattern


def part_one(input_filename: str) -> int:
    rules, messages = _parse_file(input_filename)
    decoded_rule = decode_rule(rules, rule_id_to_decode=0)
    return _count_valid_messages(decoded_rule, messages)


def _parse_file(input_filename: str) -> tuple[dict[int, str], list[str]]:
    with open(input_filename) as file:
        content = file.read().split("\n\n")
        rules_content, messages_content = content
        rules = _parse_rules(rules_content)
        messages = [line for line in messages_content.split("\n")]
        return rules, messages


def _parse_rules(content: str) -> dict[int, str]:
    return dict(_parse_rule(line) for line in content.split("\n"))


def _parse_rule(line: str) -> tuple[int, str]:
    rule_id, _, rule_matches = line.partition(": ")
    if '"' in rule_matches:
        rule_matches = rule_matches.removeprefix('"').removesuffix('"')
    return int(rule_id), rule_matches


def decode_rule(rules: dict[int, str], rule_id_to_decode: int) -> Pattern[str]:
    rule = rules[rule_id_to_decode]
    while not is_rule_finished(rule):
        other_rule_ids = get_ids(rule)
        for other_rule_id in other_rule_ids:
            rule = replace_id_with_its_rule(rules, rule, other_rule_id)

    rule = rule.replace(" ", "")
    rule = f"^{rule}$"
    return re.compile(rule)


def replace_id_with_its_rule(rules: dict[int, str], rule: str, id_to_replace: int) -> str:
    boundaries = get_boundaries_of_number_in_string(rule, id_to_replace)
    replacement = f"({rules[id_to_replace]})"
    result = []
    last_end = 0
    for start_index, end_index in boundaries:
        result.append(rule[last_end:start_index])
        result.append(replacement)
        last_end = end_index
    result.append(rule[last_end:])
    return "".join(result)


def is_rule_finished(rule: str) -> bool:
    return not re.findall(r"\d+", rule)


def get_ids(rule: str) -> set[int]:
    return {int(number) for number in re.findall(r"\d+", rule)}


def get_boundaries_of_number_in_string(rule: str, number: int) -> list[tuple[int, int]]:
    return [match.span() for match in re.finditer(r"\d+", rule) if int(match.group()) == number]


def _count_valid_messages(decoded_rule: Pattern[str], messages: list[str]) -> int:
    return sum(1 for message in messages if re.match(decoded_rule, message))


if __name__ == "__main__":
    print(part_one("data/input.txt"))
