import abc

from day11.constants import OCCUPIED_SEAT


class OccupiedSeatsStrategy(abc.ABC):
    def count_occupied_seats(self, seats_layout: list[str], row: int, column: int) -> int:
        visible_seats_indices = self._get_visible_seats_indices(seats_layout, row, column)
        return sum(
            1
            for seat_row, seat_column in visible_seats_indices
            if seats_layout[seat_row][seat_column] == OCCUPIED_SEAT
        )

    @property
    @abc.abstractmethod
    def min_count_of_visible_occupied_seats_for_occupied_seat_to_become_empty(self) -> int:
        pass

    @abc.abstractmethod
    def _get_visible_seats_indices(self, seats_layout: list[str], row: int, column: int) -> list[tuple[int, int]]:
        pass
