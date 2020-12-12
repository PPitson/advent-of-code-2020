from day12.models import Direction
from day12.strategies.base import ShipMovementStrategy


class DefaultMovementStrategy(ShipMovementStrategy):
    def __init__(self, starting_direction: Direction) -> None:
        super().__init__()
        self.direction = starting_direction
        self.degrees_by_direction = {Direction.NORTH: 0, Direction.EAST: 90, Direction.SOUTH: 180, Direction.WEST: 270}
        self.direction_by_degrees = {degrees: direction for direction, degrees in self.degrees_by_direction.items()}

    def handle_move_north(self, arg: int) -> None:
        self.latitude += arg

    def handle_move_south(self, arg: int) -> None:
        self.latitude -= arg

    def handle_move_west(self, arg: int) -> None:
        self.longitude -= arg

    def handle_move_east(self, arg: int) -> None:
        self.longitude += arg

    def handle_turn_left(self, arg: int) -> None:
        new_degrees = (self.degrees_by_direction[self.direction] - arg) % 360
        self.direction = self.direction_by_degrees[new_degrees]

    def handle_turn_right(self, arg: int) -> None:
        new_degrees = (self.degrees_by_direction[self.direction] + arg) % 360
        self.direction = self.direction_by_degrees[new_degrees]

    def handle_move_forward(self, arg: int) -> None:
        return getattr(self, f"handle_move_{self.direction.name.lower()}")(arg)
