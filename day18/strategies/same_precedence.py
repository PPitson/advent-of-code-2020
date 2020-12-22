from typing import Callable

from day18.strategies.base import ExpressionEvaluator


class SamePrecedenceExpressionEvaluator(ExpressionEvaluator):
    def _evaluate(self, numbers: list[int], operators: list[Callable[[int, int], int]]) -> int:
        result = numbers[0]
        for number, op in zip(numbers[1:], operators):
            result = op(result, number)
        return result
