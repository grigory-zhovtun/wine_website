"""Module for determining the correct Russian word 'year' based on a number."""


def get_year_word(n: int) -> str:
    """
    Return the correct Russian word for 'year' based on the given number.

    The function determines the appropriate form of the word 'год' in Russian
    based on the number `n`. It follows Russian grammatical rules:

    - 'год' for numbers ending in 1 (except 11)
    - 'года' for numbers ending in 2, 3, or 4 (except 12, 13, 14)
    - 'лет' for all other cases

    Args:
        n (int): The number of years.

    Returns:
        str: A string containing the number and the correct word 'year'.

    Examples:
        >>> get_year_word(1)
        '1 год'
        >>> get_year_word(2)
        '2 года'
        >>> get_year_word(5)
        '5 лет'
        >>> get_year_word(21)
        '21 год'
        >>> get_year_word(112)
        '112 лет'
    """
    n = abs(n)
    last_two = n % 100
    if 11 <= last_two <= 14:
        return f"{n} лет"

    last_digit = n % 10
    if last_digit == 1:
        return f"{n} год"
    if 2 <= last_digit <= 4:
        return f"{n} года"
    return f"{n} лет"
