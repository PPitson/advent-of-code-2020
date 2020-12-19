import abc


class MemoryUpdateStrategy(abc.ABC):
    @abc.abstractmethod
    def update_memory(self, memory: dict[int, int], address: int, mask: str, value: int) -> dict[int, int]:
        pass

    @staticmethod
    def _binary_value_of_integer_with_bits_length(number: int, length: int) -> str:
        return bin(number).removeprefix("0b").rjust(length, "0")
