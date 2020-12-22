from typing import Iterator

from day18.strategies.add_before_mul import AdditionBeforeMultiplicationExpressionEvaluator
from day18.strategies.base import ExpressionEvaluator
from day18.strategies.same_precedence import SamePrecedenceExpressionEvaluator


def part_one(input_filename: str) -> int:
    return sum(
        _evaluate_expression(expression, SamePrecedenceExpressionEvaluator())
        for expression in _get_expressions(input_filename)
    )


def part_two(input_filename: str) -> int:
    return sum(
        _evaluate_expression(expression, AdditionBeforeMultiplicationExpressionEvaluator())
        for expression in _get_expressions(input_filename)
    )


def _get_expressions(input_filename: str) -> Iterator[str]:
    with open(input_filename) as file:
        for line in file:
            yield line


def _evaluate_expression(expression: str, expression_evaluator: ExpressionEvaluator) -> int:
    if "(" not in expression:
        return expression_evaluator.evaluate_expression_without_parens(expression)

    left_paren_index = 0
    for index, symbol in enumerate(expression):
        if symbol == "(":
            left_paren_index = index
        elif symbol == ")":
            result_of_expression_inside_parens = expression_evaluator.evaluate_expression_without_parens(
                expression[left_paren_index + 1 : index]
            )
            new_expression = (
                expression[:left_paren_index] + str(result_of_expression_inside_parens) + expression[index + 1 :]
            )
            return _evaluate_expression(new_expression, expression_evaluator)


if __name__ == "__main__":
    print(part_one("data/input.txt"))
    print(part_two("data/input.txt"))
