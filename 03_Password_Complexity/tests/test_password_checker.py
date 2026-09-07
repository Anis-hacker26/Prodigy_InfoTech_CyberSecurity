from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from password_checker import (
    analyze_password,
    check_common_pattern,
)


def test_strong_password():
    """Verify that a complex password is classified as strong."""

    result = analyze_password("Secure@2026Pass!")

    assert result.strength == "Strong"
    assert result.score == 6
    assert result.has_lowercase is True
    assert result.has_uppercase is True
    assert result.has_digit is True
    assert result.has_special is True
    assert result.has_common_pattern is False


def test_moderate_password():
    """Verify that a partially complex password is classified as moderate."""

    result = analyze_password("BlueSky2026")

    assert result.strength == "Moderate"
    assert result.has_lowercase is True
    assert result.has_uppercase is True
    assert result.has_digit is True
    assert result.has_special is False


def test_weak_password():
    """Verify that a short simple password is classified as weak."""

    result = analyze_password("abc")

    assert result.strength == "Weak"
    assert result.score <= 2
    assert result.has_lowercase is True
    assert result.has_uppercase is False
    assert result.has_digit is False
    assert result.has_special is False


def test_common_password_detection():
    """Verify that known common passwords are detected."""

    assert check_common_pattern("password") is True
    assert check_common_pattern("PASSWORD") is True
    assert check_common_pattern("12345678") is True


def test_repeated_character_detection():
    """Verify that repeated characters are detected."""

    assert check_common_pattern("aaaSecure2026!") is True


def test_sequential_number_detection():
    """Verify that predictable number sequences are detected."""

    assert check_common_pattern("Secure1234!") is True


def test_case_sensitive_complexity():
    """Verify that uppercase and lowercase checks are independent."""

    result = analyze_password("abcdefgh123!")

    assert result.has_lowercase is True
    assert result.has_uppercase is False
    assert result.has_digit is True
    assert result.has_special is True


def test_invalid_password_type():
    """Verify that non-string passwords are rejected."""

    with pytest.raises(TypeError):
        analyze_password(12345678)


def test_empty_password():
    """Verify that an empty password is classified as weak."""

    result = analyze_password("")

    assert result.strength == "Weak"
    assert result.length == 0
    assert result.score == 0