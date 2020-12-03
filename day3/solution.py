import operator
from functools import reduce

TREE = "#"


def part_one(input_filename: str) -> int:
    area_map = _read_area_map(input_filename)
    return _count_trees(area_map, positions_to_move_right=3, positions_to_move_down=1)


def part_two(input_filename: str) -> int:
    area_map = _read_area_map(input_filename)
    move_rules = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = (
        _count_trees(area_map, positions_to_move_right, positions_to_move_down)
        for positions_to_move_right, positions_to_move_down in move_rules
    )
    return reduce(operator.mul, trees, 1)


def _read_area_map(input_filename: str) -> list[str]:
    with open(input_filename) as file:
        return [line.strip() for line in file]


def _count_trees(area_map: list[str], positions_to_move_right: int, positions_to_move_down: int) -> int:
    row_length = len(area_map[0])
    column = 0
    trees = 0
    for row in range(positions_to_move_down, len(area_map), positions_to_move_down):
        column = (column + positions_to_move_right) % row_length
        if area_map[row][column] == TREE:
            trees += 1
    return trees


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
