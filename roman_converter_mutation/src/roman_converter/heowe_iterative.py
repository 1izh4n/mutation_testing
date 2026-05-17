def to_roman(arabic: int) -> str:
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    result = ""
    for value, numeral in values:
        while arabic >= value:
            result += numeral
            arabic -= value
    return result


def from_roman(roman: str) -> int:
    roman_map = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }
    result = 0
    for i, char in enumerate(roman):
        value = roman_map[char]
        if i + 1 < len(roman) and value < roman_map[roman[i + 1]]:
            result -= value
        else:
            result += value
    return result
