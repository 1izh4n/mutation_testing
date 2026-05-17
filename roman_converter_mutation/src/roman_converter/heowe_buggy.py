def to_roman(arabic: int) -> str:
    # missing subtractive notation (4, 9, 40, 90, 400, 900).
    values = [
        (1000, "M"),
        (500, "D"),
        (100, "C"),
        (50, "L"),
        (10, "X"),
        (5, "V"),
        (1, "I"),
    ]
    result = ""
    for value, numeral in values:
        while arabic >= value:
            result += numeral
            arabic -= value
    return result


def from_roman(roman: str) -> int:
    # doesn't handle subtractive notation (treats IV as I + V = 6).
    roman_map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    return sum(roman_map[c] for c in roman)
