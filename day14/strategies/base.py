import abc


class MemoryUpdateStrategy(abc.ABC):
    @abc.abstractmethod
    def update_memory(self, memory: dict[int, int], address: int, mask: str, value: int) -> dict[int, int]:
        pass
