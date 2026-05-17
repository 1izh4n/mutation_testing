def to_roman(arabic: int) -> str:
    if arabic <= 0:
        return ""
        
    mapping = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    for value, symbol in mapping:
        if arabic >= value:
            return symbol + to_roman(arabic - value)
    return ""
