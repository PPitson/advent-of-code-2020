from day14.constants import MASK_LENGTH
from day14.strategies.base import MemoryUpdateStrategy


class ValueDecoderStrategy(MemoryUpdateStrategy):
    def update_memory(self, memory: dict[int, int], address: int, mask: str, value: int) -> dict[int, int]:
        memory[address] = self._apply_mask_to_value(mask, value)
        return memory

    def _apply_mask_to_value(self, mask: str, value: int) -> int:
        binary_value = self._binary_value_of_integer_with_bits_length(value, MASK_LENGTH)
        result = "".join(self._determine_bit(mask_bit, value_bit) for mask_bit, value_bit in zip(mask, binary_value))
        return int(result, 2)

    @staticmethod
    def _determine_bit(mask_bit: str, value_bit: str) -> str:
        return value_bit if mask_bit == "X" else mask_bit
