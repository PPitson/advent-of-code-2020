from typing import Optional


def raise_value_error_if_value_not_in_range(
    value: str, min_value: int, max_value: int, error_message: Optional[str] = None
) -> None:
    if min_value <= int(value) <= max_value:
        return

    if not error_message:
        error_message = f"value must be between {min_value} and {max_value}"
    raise ValueError(error_message)
