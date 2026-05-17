from types import ModuleType


def test_from_roman(impl: ModuleType):
    # Base Case Coverage - Variations
    assert impl.from_roman("MCDXLVII") == 1447 # uses all letters at least once
    assert impl.from_roman("MMCDXLVII") == 2447 # Change thousands value
    assert impl.from_roman("MDXLVII") == 1547 # Change hundreds value
    assert impl.from_roman("MCDXXVII") == 1427 # Change tens value
    assert impl.from_roman("MCDXLIX") == 1449 # Change ones value
    # Base Case Coverage - Boundaries
    assert impl.from_roman("I") == 1 # Lower boundary
    assert impl.from_roman("MMMCMXCIX") == 3999 # Upper boundary
