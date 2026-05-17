def to_roman(arabic: int) -> str:
    # ignore CM, CD, XC, XL, IX, IV to make an incorrect example
    mapping = [
        (1000, 'M'), (500, 'D'), (100, 'C'), 
        (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')
    ]
    
    result = ""
    for value, symbol in mapping:
        while arabic >= value:
            result += symbol
            arabic -= value
    return result
 
