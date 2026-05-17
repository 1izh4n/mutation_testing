from types import ModuleType


def test_roman_isp(impl: ModuleType) -> None:
    assert impl.to_roman(1) == "I"
    assert impl.to_roman(15) == "XV"

    assert impl.to_roman(4) == "IV"
    assert impl.to_roman(9) == "IX"
    assert impl.to_roman(90) == "XC"

    assert impl.to_roman(3999) == "MMMCMXCIX"
