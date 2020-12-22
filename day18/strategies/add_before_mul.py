import operator
from functools import reduce
from typing import Callable

from day18.strategies.base import ExpressionEvaluator


class AdditionBeforeMultiplicationExpressionEvaluator(ExpressionEvaluator):
    def _evaluate(self, numbers: list[int], operators: list[Callable[[int, int], int]]) -> int:
        try:
            index = next(index for index, op in enumerate(operators) if op == operator.add)
        except StopIteration:  # only multiplication operators are left
            return reduce(operator.mul, numbers, 1)
        else:
            return self._evaluate(
                numbers[:index] + [numbers[index] + numbers[index + 1]] + numbers[index + 2 :],
                operators[:index] + operators[index + 1 :],
            )
