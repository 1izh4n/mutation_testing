def to_roman(arabic: int) -> str:
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    return M[arabic // 1000] + C[(arabic % 1000) // 100] + X[(arabic % 100) // 10] + I[arabic % 10]


def from_roman(roman: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman_map[roman[i]] < roman_map[roman[i + 1]]:
            total += roman_map[roman[i + 1]] - roman_map[roman[i]]
            i += 2
        else:
            total += roman_map[roman[i]]
            i += 1
    return total