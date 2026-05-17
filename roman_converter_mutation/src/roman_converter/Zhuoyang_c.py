def to_roman(arabic: int) -> str:
    # BUG: Ignores subtraction rules (e.g., IV, IX)
    val_map = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    result = ""
    for value in sorted(val_map.keys(), reverse=True):
        while arabic >= value:
            result += val_map[value]
            arabic -= value
    return result

def from_roman(roman: str) -> int:
    # BUG: Adds everything blindly (e.g., IV becomes 6 instead of 4)
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for char in roman.upper():
        total += roman_map[char]
    return total