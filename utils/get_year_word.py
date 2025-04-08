"""Module for determining the correct Russian word 'year' based on a number."""


def get_year_word(n: int) -> str:
    """
    Return the correct Russian word for 'year' based on the given number.

    The function determines the appropriate form of the word 'год' in Russian
    based on the number `n`. It follows Russian grammatical rules:

    Args:
        n (int): The number of years.

    Returns:
        str: A string containing the number and the correct word 'year'.
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
