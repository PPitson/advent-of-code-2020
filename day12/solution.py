from day12.models import Direction, Instruction, Action
from day12.strategies.base import ShipMovementStrategy
from day12.strategies.default import DefaultMovementStrategy


def part_one(input_filename: str) -> int:
    strategy = DefaultMovementStrategy(starting_direction=Direction.EAST)
    return _get_manhattan_distance_after_moving_ship(input_filename, strategy)


def _get_manhattan_distance_after_moving_ship(input_filename: str, strategy: ShipMovementStrategy) -> int:
    instructions = _get_instructions(input_filename)
    coordinates = strategy.move_ship(instructions)
    return _manhattan_distance(coordinates)


def _get_instructions(input_filename: str) -> list[Instruction]:
    with open(input_filename) as file:
        return [_parse_instruction(line) for line in file]


def _parse_instruction(line: str) -> Instruction:
    return Instruction(action=Action(line[0]), argument=int(line[1:]))


def _manhattan_distance(coordinates: tuple[int, int]) -> int:
    return sum(map(abs, coordinates))


if __name__ == "__main__":
    print(part_one("data/input.txt"))
