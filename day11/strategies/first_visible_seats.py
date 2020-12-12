from typing import Callable

from day11.constants import FLOOR
from day11.strategies.base import OccupiedSeatsStrategy


class FirstVisibleSeatsStrategy(OccupiedSeatsStrategy):
    @property
    def min_count_of_visible_occupied_seats_for_occupied_seat_to_become_empty(self) -> int:
        return 5

    def _get_visible_seats_indices(self, seats_layout: list[str], row: int, column: int) -> list[tuple[int, int]]:
        max_column = len(seats_layout[0])
        max_row = len(seats_layout)

        def _lesser_than_max_row(x: int) -> bool:
            return x < max_row

        def _lesser_than_max_column(x: int) -> bool:
            return x < max_column

        indices = (
            self._get_visible_seat_left_upper(seats_layout, row, column),
            self._get_visible_seat_upper(seats_layout, row, column),
            self._get_visible_seat_right_upper(seats_layout, row, column, _lesser_than_max_column),
            self._get_visible_seat_left(seats_layout, row, column),
            self._get_visible_seat_right(seats_layout, row, column, _lesser_than_max_column),
            self._get_visible_seat_left_down(seats_layout, row, column, _lesser_than_max_row),
            self._get_visible_seat_down(seats_layout, row, column, _lesser_than_max_row),
            self._get_visible_seat_right_down(seats_layout, row, column, _lesser_than_max_row, _lesser_than_max_column),
        )
        return list(filter(None, indices))

    def _get_visible_seat_left_upper(self, seats_layout: list[str], row: int, column: int) -> tuple[int, int]:
        return self._get_visible_seat(
            seats_layout,
            row,
            column,
            update_row=_decrement,
            update_column=_decrement,
            is_row_valid=_greater_than_or_equal_zero,
            is_column_valid=_greater_than_or_equal_zero,
        )

    def _get_visible_seat_upper(self, seats_layout: list[str], row: int, column: int) -> tuple[int, int]:
        return self._get_visible_seat(
            seats_layout,
            row,
            column,
            update_row=_decrement,
            update_column=_identity,
            is_row_valid=_greater_than_or_equal_zero,
            is_column_valid=_always_valid,
        )

    def _get_visible_seat_right_upper(
        self, seats_layout: list[str], row: int, column: int, column_lesser_than_max_column: Callable[[int], bool]
    ) -> tuple[int, int]:
        return self._get_visible_seat(
            seats_layout,
            row,
            column,
            update_row=_decrement,
            update_column=_increment,
            is_row_valid=_greater_than_or_equal_zero,
            is_column_valid=column_lesser_than_max_column,
        )

    def _get_visible_seat_left(self, seats_layout: list[str], row: int, column: int) -> tuple[int, int]:
        return self._get_visible_seat(
            seats_layout,
            row,
            column,
            update_row=_identity,
            update_column=_decrement,
            is_row_valid=_always_valid,
            is_column_valid=_greater_than_or_equal_zero,
        )

    def _get_visible_seat_right(
        self, seats_layout: list[str], row: int, column: int, column_lesser_than_max_column: Callable[[int], bool]
    ) -> tuple[int, int]:
        return self._get_visible_seat(
            seats_layout,
            row,
            column,
            update_row=_identity,
            update_column=_increment,
            is_row_valid=_always_valid,
            is_column_valid=column_lesser_than_max_column,
        )

    def _get_visible_seat_left_down(
        self, seats_layout: list[str], row: int, column: int, row_lesser_than_max_row: Callable[[int], bool]
    ) -> tuple[int, int]:
        return self._get_visible_seat(
            seats_layout,
            row,
            column,
            update_row=_increment,
            update_column=_decrement,
            is_row_valid=row_lesser_than_max_row,
            is_column_valid=_greater_than_or_equal_zero,
        )

    def _get_visible_seat_down(
        self, seats_layout: list[str], row: int, column: int, row_lesser_than_max_row: Callable[[int], bool]
    ) -> tuple[int, int]:
        return self._get_visible_seat(
            seats_layout,
            row,
            column,
            update_row=_increment,
            update_column=_identity,
            is_row_valid=row_lesser_than_max_row,
            is_column_valid=_always_valid,
        )

    def _get_visible_seat_right_down(
        self,
        seats_layout: list[str],
        row: int,
        column: int,
        row_lesser_than_max_row: Callable[[int], bool],
        column_lesser_than_max_column: Callable[[int], bool],
    ) -> tuple[int, int]:
        return self._get_visible_seat(
            seats_layout,
            row,
            column,
            update_row=_increment,
            update_column=_increment,
            is_row_valid=row_lesser_than_max_row,
            is_column_valid=column_lesser_than_max_column,
        )

    def _get_visible_seat(
        self,
        seats_layout: list[str],
        row: int,
        column: int,
        update_row: Callable[[int], int],
        update_column: Callable[[int], int],
        is_row_valid: Callable[[int], bool],
        is_column_valid: Callable[[int], bool],
    ) -> tuple[int, int]:
        row = update_row(row)
        column = update_column(column)
        while is_row_valid(row) and is_column_valid(column):
            if seats_layout[row][column] != FLOOR:
                return row, column
            row = update_row(row)
            column = update_column(column)
        return tuple()


def _identity(x: int) -> int:
    return x


def _increment(x: int) -> int:
    return x + 1


def _decrement(x: int) -> int:
    return x - 1


def _greater_than_or_equal_zero(x: int) -> bool:
    return x >= 0


def _always_valid(_x: int) -> bool:
    return True
