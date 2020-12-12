import abc


class OccupiedSeatsStrategy(abc.ABC):
    @abc.abstractmethod
    def count_occupied_seats(self, seats_layout: list[str], row: int, column: int) -> int:
        pass

    @property
    @abc.abstractmethod
    def min_count_of_visible_occupied_seats_for_occupied_seat_to_become_empty(self) -> int:
        pass
