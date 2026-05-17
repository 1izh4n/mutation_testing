from types import ModuleType


def test_to_roman(impl: ModuleType):
    # Base Case Coverage - Variations
    assert impl.to_roman(1447) == "MCDXLVII" # uses all letters at least once
    assert impl.to_roman(2447) == "MMCDXLVII" # Change thousands value
    assert impl.to_roman(1547) == "MDXLVII" # Change hundreds value
    assert impl.to_roman(1427) == "MCDXXVII" # Change tens value
    assert impl.to_roman(1449) == "MCDXLIX" # Change ones value
    # Base Case Coverage - Boundaries
    assert impl.to_roman(1) == "I" # Lower boundary
    assert impl.to_roman(3999) == "MMMCMXCIX" # Upper boundary

