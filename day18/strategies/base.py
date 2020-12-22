import abc
import operator
from typing import Callable


class ExpressionEvaluator(abc.ABC):
    def evaluate_expression_without_parens(self, expression: str) -> int:
        symbols = expression.split(" ")
        numbers = map(int, symbols[::2])
        operators = map(self._operator_function_from_symbol, symbols[1::2])
        return self._evaluate(list(numbers), list(operators))

    @abc.abstractmethod
    def _evaluate(self, numbers: list[int], operators: list[Callable[[int, int], int]]) -> int:
        pass

    @staticmethod
    def _operator_function_from_symbol(symbol: str) -> Callable[[int, int], int]:
        operator_functions = {"+": operator.add, "*": operator.mul}
        return operator_functions[symbol]
