from pathlib import Path
import sys

import pytest
from PIL import Image
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from image_encryption import (
    decrypt_image,
    encrypt_image,
    transform_pixel,
)

def create_test_image(path: Path) -> None:
    """Create a small RGB image for automated testing."""
    image = Image.new("RGB", (10, 10))

    pixels = image.load()

    for y in range(10):
        for x in range(10):
            pixels[x, y] = (
                (x * 25) % 256,
                (y * 25) % 256,
                ((x + y) * 15) % 256,
            )

    image.save(path)


def test_transform_pixel():
    """Verify that XOR transforms pixel values correctly."""
    pixel = (10, 20, 30)
    key = 123

    result = transform_pixel(pixel, key)

    assert result == (
        10 ^ 123,
        20 ^ 123,
        30 ^ 123,
    )


def test_encrypt_and_decrypt_restore_original(tmp_path):
    """Verify that encryption followed by decryption restores the image."""
    original = tmp_path / "original.png"
    encrypted = tmp_path / "encrypted.png"
    decrypted = tmp_path / "decrypted.png"

    create_test_image(original)

    encrypt_image(original, encrypted, 123)
    decrypt_image(encrypted, decrypted, 123)

    with Image.open(original) as original_image:
        with Image.open(decrypted) as decrypted_image:
            assert original_image.size == decrypted_image.size
            assert original_image.mode == decrypted_image.mode
            assert list(original_image.get_flattened_data()) == list(
                decrypted_image.get_flattened_data()
            )


def test_encryption_changes_image(tmp_path):
    """Verify that encryption produces different pixel data."""
    original = tmp_path / "original.png"
    encrypted = tmp_path / "encrypted.png"

    create_test_image(original)
    encrypt_image(original, encrypted, 123)

    with Image.open(original) as original_image:
        with Image.open(encrypted) as encrypted_image:
            assert list(original_image.get_flattened_data()) != list(
                encrypted_image.get_flattened_data()
            )


def test_invalid_key_type():
    """Verify that non-integer keys are rejected."""
    with pytest.raises(TypeError):
        transform_pixel((10, 20, 30), "123")


def test_invalid_key_range():
    """Verify that keys outside the valid range are rejected."""
    with pytest.raises(ValueError):
        encrypt_image("missing.png", "output.png", 256)


def test_missing_input_file(tmp_path):
    """Verify that a missing input image raises an error."""
    missing_file = tmp_path / "missing.png"
    output_file = tmp_path / "output.png"

    with pytest.raises(FileNotFoundError):
        encrypt_image(missing_file, output_file, 123)