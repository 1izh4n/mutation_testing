from types import ModuleType

# We expect Zhuoyang_c.py to fail these tests.
# Pytest will show us exactly which implementation failed.


def test_to_roman_standard_cases(impl: ModuleType):
    assert impl.to_roman(1) == "I"
    assert impl.to_roman(10) == "X"
    assert impl.to_roman(2023) == "MMXXIII"


def test_to_roman_subtractive_cases(impl: ModuleType):
    # This is where Zhuoyang_c will fail!
    assert impl.to_roman(4) == "IV"
    assert impl.to_roman(9) == "IX"
    assert impl.to_roman(40) == "XL"


def test_from_roman_standard_cases(impl: ModuleType):
    assert impl.from_roman("I") == 1
    assert impl.from_roman("X") == 10
    assert impl.from_roman("MMXXIII") == 2023


def test_from_roman_subtractive_cases(impl: ModuleType):
    # Zhuoyang_c will fail here too.
    assert impl.from_roman("IV") == 4
    assert impl.from_roman("IX") == 9
    assert impl.from_roman("XL") == 40
