import pytest


# =========================
# to_roman Blocks
# =========================

# Block 1: Valid range (1–3999)
# Verifies correct Roman numeral output for valid values
def test_to_roman_valid_range(impl):
    assert impl.to_roman(1) == "I"
    assert impl.to_roman(3999) == "MMMCMXCIX"
    assert impl.to_roman(4) == "IV"

# Block 2: Zero
# Ensures 0 throws an error
def test_to_roman_zero(impl):
    with pytest.raises(ValueError):
        impl.to_roman(0)

# Block 3: Negative numbers
# Confirms negative integers throw an error
def test_to_roman_negative(impl):
    with pytest.raises(ValueError):
        impl.to_roman(-5)

# Block 4: int ≥ 4000
# Validates that numbers greater than 4000 throw an error
def test_to_roman_too_large(impl):
    with pytest.raises(ValueError):
        impl.to_roman(4000)

# Block 5: Non-integer
# Ensures non-integer inputs are rejected
def test_to_roman_non_integer(impl):
    with pytest.raises(ValueError):
        impl.to_roman(3.14)


# =========================
# from_roman Blocks
# =========================

# Block 1: Valid Roman numeral
# Tests correct parsing of simple, subtractive, and maximum valid numerals
def test_from_roman_valid(impl):
    assert impl.from_roman("I") == 1
    assert impl.from_roman("IV") == 4
    assert impl.from_roman("MMMCMXCIX") == 3999

# Block 2: Invalid characters
# Ensures characters outside IVXLCDM are rejected
def test_from_roman_invalid_character(impl):
    with pytest.raises(ValueError):
        impl.from_roman("A")
    with pytest.raises(ValueError):
        impl.from_roman("37")
    with pytest.raises(ValueError):
        impl.from_roman(";['.")

# Block 3: Invalid repetition
# Ensures illegal repetition patterns throw errors
def test_from_roman_invalid_repetition(impl):
    with pytest.raises(ValueError):
        impl.from_roman("IIII")
    with pytest.raises(ValueError):
        impl.from_roman("VV")

# Block 4: Invalid subtraction
# Verifies illegal subtraction combinations throw errors
def test_from_roman_invalid_subtraction(impl):
    with pytest.raises(ValueError):
        impl.from_roman("IL")
    with pytest.raises(ValueError):
        impl.from_roman("IC")

# Block 5: Empty string
# Ensures empty inputs are not accepted
def test_from_roman_empty(impl):
    with pytest.raises(ValueError):
        impl.from_roman("")

# Block 6: Case violation
# Ensures lowercase Roman numerals are rejected if lowercase letters are used
def test_from_roman_case_violation(impl):
    with pytest.raises(ValueError):
        impl.from_roman("iv")