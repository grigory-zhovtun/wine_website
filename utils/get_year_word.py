def get_year_word(n: int) -> str:
    n = abs(n)
    last_two = n % 100
    if 11 <= last_two <= 14:
        return f"{n} лет"

    last_digit = n % 10
    if last_digit == 1:
        return f"{n} год"
    elif 2 <= last_digit <= 4:
        return f"{n} года"
    else:
        return f"{n} лет"
