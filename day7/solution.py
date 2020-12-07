import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Iterator


@dataclass
class Content:
    bag_color: str
    quantity: int


@dataclass
class Rule:
    bag_color: str
    contents: list[Content]


def part_one(input_filename: str) -> int:
    rules = _create_rules_dict(_parse_file(input_filename))
    reverse_rules = _create_reverse_rules_dict(rules)
    return _count_bag_colors_which_can_contain_color(reverse_rules, desired_color="shiny gold")


def part_two(input_filename: str) -> int:
    rules = _create_rules_dict(_parse_file(input_filename))
    return _count_bags_inside_bag_of_given_color(rules, desired_color="shiny gold")


def _parse_file(input_filename: str) -> Iterator[Rule]:
    with open(input_filename) as file:
        for line in file:
            yield _parse_rule(line)


def _parse_rule(line: str) -> Rule:
    color_regex = r"(?P<color>[a-z]+ [a-z]+)"
    bag_color_match = re.match(rf"{color_regex} bags contain", line)
    bag_color = bag_color_match.groupdict()["color"]
    contents = [
        Content(bag_color=color, quantity=int(quantity))
        for quantity, color in re.findall(rf"(?P<quantity>\d+) {color_regex} bags*", line)
    ]
    return Rule(bag_color=bag_color, contents=contents)


def _create_rules_dict(rules: Iterator[Rule]) -> dict[str, list[Content]]:
    return {rule.bag_color: rule.contents for rule in rules}


def _create_reverse_rules_dict(rules_dict: dict[str, list[Content]]) -> dict[str, set[str]]:
    """
    returns dict, where key is the color, and value is set of colors, which can directly contain key color
    e.g. light red bags contain 1 bright white bag, 2 muted yellow bags would produce
    {'yellow bag': {'light red'}, 'bright white': {'light red'}}
    """
    reverse_rules_dict = defaultdict(set)
    for container_color, bags_inside in rules_dict.items():
        for bag in bags_inside:
            reverse_rules_dict[bag.bag_color].add(container_color)
    return reverse_rules_dict


def _count_bag_colors_which_can_contain_color(reverse_rules: dict[str, set[str]], desired_color: str) -> int:
    def bag_colors_which_contain_color(current_color: str) -> set[str]:
        if not reverse_rules[current_color]:
            return set()

        bag_colors_which_directly_contain_desired_color = reverse_rules[current_color]
        return bag_colors_which_directly_contain_desired_color.union(
            *(bag_colors_which_contain_color(color) for color in bag_colors_which_directly_contain_desired_color)
        )

    return len(bag_colors_which_contain_color(desired_color))


def _count_bags_inside_bag_of_given_color(rules: dict[str, list[Content]], desired_color: str) -> int:
    contents = rules[desired_color]
    if not contents:
        return 0

    return sum(
        content.quantity * (1 + _count_bags_inside_bag_of_given_color(rules, content.bag_color)) for content in contents
    )


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
