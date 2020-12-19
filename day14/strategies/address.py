import re
from typing import Iterator

from day14.constants import MASK_LENGTH
from day14.strategies.base import MemoryUpdateStrategy


class MemoryAddressDecoderStrategy(MemoryUpdateStrategy):
    def update_memory(self, memory: dict[int, int], address: int, mask: str, value: int) -> dict[int, int]:
        address_after_mask_appliance = self._apply_mask_to_address(mask, address)
        for address in self._generate_possible_addresses(address_after_mask_appliance):
            memory[address] = value
        return memory

    def _apply_mask_to_address(self, mask: str, address: int) -> str:
        binary_value = bin(address).removeprefix("0b").rjust(MASK_LENGTH, "0")
        result = "".join(self._determine_bit(mask_bit, value_bit) for mask_bit, value_bit in zip(mask, binary_value))
        return result

    @staticmethod
    def _determine_bit(mask_bit: str, value_bit: str) -> str:
        return value_bit if mask_bit == "0" else mask_bit

    def _generate_possible_addresses(self, address: str) -> Iterator[int]:
        indexes_to_replace = [m.start() for m in re.finditer("X", address)]
        count = len(indexes_to_replace)
        replacements = [bin(value).removeprefix("0b").rjust(count, "0") for value in range(2 ** count)]
        for replacement in replacements:
            yield self._create_new_address(address, indexes_to_replace, replacement)

    @staticmethod
    def _create_new_address(address: str, indexes_to_replace: list[int], characters_to_replace: str) -> str:
        chopped_address = list(address)
        for index, char in zip(indexes_to_replace, characters_to_replace):
            chopped_address[index] = char
        return "".join(chopped_address)
