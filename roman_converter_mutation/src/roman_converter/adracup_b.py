def to_roman(arabic: int) -> str:
    result = ""
    Map_roman = [
        (1000,"M"), (900,"CM"), (500, "D"), (100, "C"), (90,"XC"), (50,"L"), (10, "X"), (9, "IX"), (5,"V"), (1,"I")
    ]
    for number, string in Map_roman:
        while arabic >= number:
            result += string
            arabic -= number
    return result

def from_roman(roman: str) -> int:
    Map_arabic = dict([
        ("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10),
        ("XL", 40), ("L", 50), ("XC", 90), ("C", 100),
        ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)
    ])
    result = 0
    for string, number in Map_arabic.items():
        count = 0
        while roman.startswith(string):
            result += number
            count += 1
            roman = roman[len(string):]
    return result