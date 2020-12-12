from day11.strategies.base import OccupiedSeatsStrategy


class AdjacentSeatsStrategy(OccupiedSeatsStrategy):
    @property
    def min_count_of_visible_occupied_seats_for_occupied_seat_to_become_empty(self) -> int:
        return 4

    def _get_visible_seats_indices(self, seats_layout: list[str], row: int, column: int) -> list[tuple[int, int]]:
        max_column = len(seats_layout[0])
        max_row = len(seats_layout)
        return (
            self._get_adjacent_seats_indices_for_upper_row(row, column, max_column)
            + self._get_adjacent_seats_indices_for_same_row(row, column, max_column)
            + self._get_adjacent_seats_indices_for_lower_row(row, column, max_column, max_row)
        )

    def _get_adjacent_seats_indices_for_upper_row(
        self, row: int, column: int, max_column: int
    ) -> list[tuple[int, int]]:
        adjacent_seats = []
        if row - 1 >= 0:
            if column - 1 >= 0:
                adjacent_seats += [(row - 1, column - 1)]
            adjacent_seats += [(row - 1, column)]
            if column + 1 < max_column:
                adjacent_seats += [(row - 1, column + 1)]
        return adjacent_seats

    def _get_adjacent_seats_indices_for_same_row(self, row: int, column: int, max_column: int) -> list[tuple[int, int]]:
        adjacent_seats = []
        if column - 1 >= 0:
            adjacent_seats += [(row, column - 1)]
        if column + 1 < max_column:
            adjacent_seats += [(row, column + 1)]
        return adjacent_seats

    def _get_adjacent_seats_indices_for_lower_row(
        self, row: int, column: int, max_column: int, max_row: int
    ) -> list[tuple[int, int]]:
        adjacent_seats = []
        if row + 1 < max_row:
            if column - 1 >= 0:
                adjacent_seats += [(row + 1, column - 1)]
            adjacent_seats += [(row + 1, column)]
            if column + 1 < max_column:
                adjacent_seats += [(row + 1, column + 1)]
        return adjacent_seats
