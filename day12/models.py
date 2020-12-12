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
