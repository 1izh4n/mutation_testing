ROMAN_VALUES = {
    "I": 1, "V": 5, "X": 10,
    "L": 50, "C": 100,
    "D": 500, "M": 1000
}


def to_roman(arabic: int) -> str:
    if not isinstance(arabic, int):
        raise ValueError
    if arabic <= 0:
        raise ValueError
    if arabic >= 4000:
        return "MMMM"

    result = ""
    for value, symbol in [
        (1000, "M"), (500, "D"),
        (100, "C"), (50, "L"),
        (10, "X"), (5, "V"),
        (1, "I")
    ]:
        while arabic >= value:
            result += symbol
            arabic -= value
    return result


def from_roman(roman: str) -> int:
    if not roman:
        raise ValueError

    total = 0
    prev = 0
    for c in reversed(roman):
        value = ROMAN_VALUES.get(c, 0)
        if value < prev:
            total -= value
        else:
            total += value
        prev = value

    return total