import abc

from day12.models import Instruction, Action


class ShipMovementStrategy(abc.ABC):
    def __init__(self) -> None:
        self.latitude = 0
        self.longitude = 0
        self.functions = {
            Action.MOVE_NORTH: self.handle_move_north,
            Action.MOVE_SOUTH: self.handle_move_south,
            Action.MOVE_WEST: self.handle_move_west,
            Action.MOVE_EAST: self.handle_move_east,
            Action.TURN_LEFT: self.handle_turn_left,
            Action.TURN_RIGHT: self.handle_turn_right,
            Action.MOVE_FORWARD: self.handle_move_forward,
        }

    def move_ship(self, instructions: list[Instruction]) -> tuple[int, int]:
        for instruction in instructions:
            self.functions[instruction.action](instruction.argument)

        return self.longitude, self.latitude

    @abc.abstractmethod
    def handle_move_north(self, arg: int) -> None:
        pass

    @abc.abstractmethod
    def handle_move_south(self, arg: int) -> None:
        pass

    @abc.abstractmethod
    def handle_move_west(self, arg: int) -> None:
        pass

    @abc.abstractmethod
    def handle_move_east(self, arg: int) -> None:
        pass

    @abc.abstractmethod
    def handle_turn_left(self, arg: int) -> None:
        pass

    @abc.abstractmethod
    def handle_turn_right(self, arg: int) -> None:
        pass

    @abc.abstractmethod
    def handle_move_forward(self, arg: int) -> None:
        pass
