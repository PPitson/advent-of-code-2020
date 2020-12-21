import operator
from typing import Iterator, Callable


def part_one(input_filename: str) -> int:
    return sum(_evaluate_expression(expression) for expression in _get_expressions(input_filename))


def _get_expressions(input_filename: str) -> Iterator[str]:
    with open(input_filename) as file:
        for line in file:
            yield line


def _evaluate_expression(expression: str) -> int:
    if "(" not in expression:
        return _evaluate_expression_without_parens(expression)

    left_paren_index = 0
    for index, symbol in enumerate(expression):
        if symbol == "(":
            left_paren_index = index
        elif symbol == ")":
            result_of_expression_inside_parens = _evaluate_expression_without_parens(
                expression[left_paren_index + 1 : index]
            )
            new_expression = (
                expression[:left_paren_index] + str(result_of_expression_inside_parens) + expression[index + 1 :]
            )
            return _evaluate_expression(new_expression)


def _evaluate_expression_without_parens(expression: str) -> int:
    symbols = expression.split(" ")
    numbers = map(int, symbols[::2])
    operators = map(_operator_function_from_symbol, symbols[1::2])
    result = next(numbers)
    for number, op in zip(numbers, operators):
        result = op(result, number)
    return result


def _operator_function_from_symbol(symbol: str) -> Callable[[int, int], int]:
    operator_functions = {"+": operator.add, "*": operator.mul}
    return operator_functions[symbol]


if __name__ == "__main__":
    print(part_one("data/input.txt"))
