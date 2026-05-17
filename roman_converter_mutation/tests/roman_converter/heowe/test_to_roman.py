from types import ModuleType


# Basic numerals
def test_basic_numerals(impl: ModuleType):
    assert impl.to_roman(1) == "I"
    assert impl.to_roman(5) == "V"
    assert impl.to_roman(10) == "X"
    assert impl.to_roman(50) == "L"
    assert impl.to_roman(100) == "C"
    assert impl.to_roman(500) == "D"
    assert impl.to_roman(1000) == "M"


# Subtractive notation
def test_subtractive_notation(impl: ModuleType):
    assert impl.to_roman(4) == "IV"
    assert impl.to_roman(9) == "IX"
    assert impl.to_roman(40) == "XL"
    assert impl.to_roman(90) == "XC"
    assert impl.to_roman(400) == "CD"
    assert impl.to_roman(900) == "CM"


# Repetition
def test_repetition(impl: ModuleType):
    assert impl.to_roman(2) == "II"
    assert impl.to_roman(3) == "III"
    assert impl.to_roman(20) == "XX"
    assert impl.to_roman(30) == "XXX"
    assert impl.to_roman(300) == "CCC"
    assert impl.to_roman(3000) == "MMM"


# Compound numerals
def test_compound_numerals(impl: ModuleType):
    assert impl.to_roman(14) == "XIV"
    assert impl.to_roman(42) == "XLII"
    assert impl.to_roman(99) == "XCIX"
    assert impl.to_roman(399) == "CCCXCIX"
    assert impl.to_roman(1994) == "MCMXCIV"
    assert impl.to_roman(2024) == "MMXXIV"
    assert impl.to_roman(3999) == "MMMCMXCIX"


# Misc values
def test_misc_values(impl: ModuleType):
    assert impl.to_roman(58) == "LVIII"
    assert impl.to_roman(621) == "DCXXI"
    assert impl.to_roman(1776) == "MDCCLXXVI"
    assert impl.to_roman(2421) == "MMCDXXI"
