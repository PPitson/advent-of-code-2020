from dataclasses import dataclass
from enum import Enum


class Action(str, Enum):
    MOVE_NORTH = "N"
    MOVE_SOUTH = "S"
    MOVE_WEST = "W"
    MOVE_EAST = "E"
    TURN_LEFT = "L"
    TURN_RIGHT = "R"
    MOVE_FORWARD = "F"


class Direction(str, Enum):
    NORTH = "N"
    SOUTH = "S"
    WEST = "W"
    EAST = "E"


@dataclass
class Instruction:
    action: Action
    argument: int


def part_one(input_filename: str) -> int:
    instructions = _get_instructions(input_filename)
    coordinates = _move_ship(instructions, starting_direction=Direction.EAST)
    return _manhattan_distance(coordinates)


def _get_instructions(input_filename: str) -> list[Instruction]:
    with open(input_filename) as file:
        return [_parse_instruction(line) for line in file]


def _parse_instruction(line: str) -> Instruction:
    return Instruction(action=Action(line[0]), argument=int(line[1:]))


def _move_ship(instructions: list[Instruction], starting_direction: Direction) -> tuple[int, int]:
    longitude, latitude = 0, 0
    direction = starting_direction
    degrees_by_direction = {Direction.NORTH: 0, Direction.EAST: 90, Direction.SOUTH: 180, Direction.WEST: 270}
    direction_by_degrees = {degrees: direction for direction, degrees in degrees_by_direction.items()}

    def handle_move_north(arg: int) -> None:
        nonlocal latitude
        latitude += arg

    def handle_move_south(arg: int) -> None:
        nonlocal latitude
        latitude -= arg

    def handle_move_west(arg: int) -> None:
        nonlocal longitude
        longitude -= arg

    def handle_move_east(arg: int) -> None:
        nonlocal longitude
        longitude += arg

    def handle_turn_left(arg: int) -> None:
        nonlocal direction
        new_degrees = (degrees_by_direction[direction] - arg) % 360
        direction = direction_by_degrees[new_degrees]

    def handle_turn_right(arg: int) -> None:
        nonlocal direction
        new_degrees = (degrees_by_direction[direction] + arg) % 360
        direction = direction_by_degrees[new_degrees]

    def handle_move_forward(arg: int) -> None:
        return functions[Action(direction)](arg)

    functions = {
        Action.MOVE_NORTH: handle_move_north,
        Action.MOVE_SOUTH: handle_move_south,
        Action.MOVE_WEST: handle_move_west,
        Action.MOVE_EAST: handle_move_east,
        Action.TURN_LEFT: handle_turn_left,
        Action.TURN_RIGHT: handle_turn_right,
        Action.MOVE_FORWARD: handle_move_forward
    }
    for instruction in instructions:
        functions[instruction.action](instruction.argument)

    return latitude, longitude


def _manhattan_distance(coordinates: tuple[int, int]) -> int:
    return sum(map(abs, coordinates))


if __name__ == '__main__':
    print(part_one("data/input.txt"))
