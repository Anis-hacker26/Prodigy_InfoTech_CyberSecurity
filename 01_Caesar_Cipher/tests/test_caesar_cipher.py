"""
Automated tests for the Caesar Cipher implementation.
"""

import sys
from pathlib import Path

# Add the src directory to Python's import path.
SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from caesar_cipher import caesar_cipher, encrypt, decrypt


def test_basic_encryption():
    assert encrypt("HELLO", 3) == "KHOOR"


def test_basic_decryption():
    assert decrypt("KHOOR", 3) == "HELLO"


def test_wraparound():
    assert encrypt("XYZ", 3) == "ABC"


def test_lowercase_preservation():
    assert encrypt("hello", 3) == "khoor"


def test_mixed_case():
    assert encrypt("Hello", 3) == "Khoor"


def test_spaces_and_punctuation():
    assert encrypt("Hello, World!", 5) == "Mjqqt, Btwqi!"


def test_numbers_are_preserved():
    assert encrypt("Hello 123", 3) == "Khoor 123"


def test_large_shift():
    assert encrypt("HELLO", 29) == "KHOOR"


def test_negative_shift():
    assert decrypt("HELLO", 3) == "EBIIL"


def test_zero_shift():
    assert encrypt("HELLO", 0) == "HELLO"


def test_empty_string():
    assert encrypt("", 5) == ""


def test_shift_greater_than_alphabet():
    assert encrypt("ABC", 52) == "ABC"