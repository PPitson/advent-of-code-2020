from day12.strategies.base import ShipMovementStrategy


class RealMovementStrategy(ShipMovementStrategy):
    def __init__(self, waypoint_relative_longitude: int, waypoint_relative_latitude: int) -> None:
        super().__init__()
        self.waypoint_relative_longitude = waypoint_relative_longitude
        self.waypoint_relative_latitude = waypoint_relative_latitude

    def handle_move_north(self, arg: int) -> None:
        self.waypoint_relative_latitude += arg

    def handle_move_south(self, arg: int) -> None:
        self.waypoint_relative_latitude -= arg

    def handle_move_west(self, arg: int) -> None:
        self.waypoint_relative_longitude -= arg

    def handle_move_east(self, arg: int) -> None:
        self.waypoint_relative_longitude += arg

    def handle_turn_left(self, arg: int) -> None:
        arg %= 360
        if arg == 90:
            self.waypoint_relative_longitude, self.waypoint_relative_latitude = (
                -self.waypoint_relative_latitude,
                self.waypoint_relative_longitude,
            )
        if arg == 180:
            self.waypoint_relative_longitude, self.waypoint_relative_latitude = (
                -self.waypoint_relative_longitude,
                -self.waypoint_relative_latitude,
            )
        if arg == 270:
            self.waypoint_relative_longitude, self.waypoint_relative_latitude = (
                self.waypoint_relative_latitude,
                -self.waypoint_relative_longitude,
            )

    def handle_turn_right(self, arg: int) -> None:
        arg %= 360
        if arg == 90:
            self.waypoint_relative_longitude, self.waypoint_relative_latitude = (
                self.waypoint_relative_latitude,
                -self.waypoint_relative_longitude,
            )
        if arg == 180:
            self.waypoint_relative_longitude, self.waypoint_relative_latitude = (
                -self.waypoint_relative_longitude,
                -self.waypoint_relative_latitude,
            )
        if arg == 270:
            self.waypoint_relative_longitude, self.waypoint_relative_latitude = (
                -self.waypoint_relative_latitude,
                self.waypoint_relative_longitude,
            )

    def handle_move_forward(self, arg: int) -> None:
        self.longitude += arg * self.waypoint_relative_longitude
        self.latitude += arg * self.waypoint_relative_latitude
