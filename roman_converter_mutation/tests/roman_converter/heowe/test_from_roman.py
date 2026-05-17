from types import ModuleType


# Basic numerals
def test_basic_numerals(impl: ModuleType):
    assert impl.from_roman("I") == 1
    assert impl.from_roman("V") == 5
    assert impl.from_roman("X") == 10
    assert impl.from_roman("L") == 50
    assert impl.from_roman("C") == 100
    assert impl.from_roman("D") == 500
    assert impl.from_roman("M") == 1000


# Subtractive notation
def test_subtractive_notation(impl: ModuleType):
    assert impl.from_roman("IV") == 4
    assert impl.from_roman("IX") == 9
    assert impl.from_roman("XL") == 40
    assert impl.from_roman("XC") == 90
    assert impl.from_roman("CD") == 400
    assert impl.from_roman("CM") == 900


# Repetition
def test_repetition(impl: ModuleType):
    assert impl.from_roman("II") == 2
    assert impl.from_roman("III") == 3
    assert impl.from_roman("XX") == 20
    assert impl.from_roman("XXX") == 30
    assert impl.from_roman("CCC") == 300
    assert impl.from_roman("MMM") == 3000


# Compound numerals
def test_compound_numerals(impl: ModuleType):
    assert impl.from_roman("XIV") == 14
    assert impl.from_roman("XLII") == 42
    assert impl.from_roman("XCIX") == 99
    assert impl.from_roman("CCCXCIX") == 399
    assert impl.from_roman("MCMXCIV") == 1994
    assert impl.from_roman("MMXXIV") == 2024
    assert impl.from_roman("MMMCMXCIX") == 3999


# Misc values
def test_misc_values(impl: ModuleType):
    assert impl.from_roman("LVIII") == 58
    assert impl.from_roman("DCXXI") == 621
    assert impl.from_roman("MDCCLXXVI") == 1776
    assert impl.from_roman("MMCDXXI") == 2421
