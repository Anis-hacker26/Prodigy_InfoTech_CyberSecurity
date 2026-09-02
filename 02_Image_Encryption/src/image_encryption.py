"""
Pixel Manipulation for Image Encryption
---------------------------------------

Educational implementation of reversible image encryption
using XOR-based pixel manipulation.
"""

from pathlib import Path

from PIL import Image


def validate_key(key: int) -> None:
    """Validate that the encryption key is an integer from 0 to 255."""

    if not isinstance(key, int):
        raise TypeError("Key must be an integer.")

    if not 0 <= key <= 255:
        raise ValueError("Key must be between 0 and 255.")


def transform_pixel(pixel: tuple[int, ...], key: int) -> tuple[int, ...]:
    """
    Transform a pixel using XOR.

    The same operation performs both encryption and decryption.
    """

    return tuple(channel ^ key for channel in pixel)


def transform_image(
    input_path: str | Path,
    output_path: str | Path,
    key: int,
) -> None:
    """
    Encrypt or decrypt an image using XOR pixel manipulation.

    The original image dimensions and color mode are preserved.
    """

    validate_key(key)

    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    with Image.open(input_path) as image:
        image = image.convert("RGB")

        transformed = image.copy()
        pixels = transformed.load()

        for y in range(transformed.height):
            for x in range(transformed.width):
                pixels[x, y] = transform_pixel(pixels[x, y], key)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        transformed.save(output_path)


def encrypt_image(
    input_path: str | Path,
    output_path: str | Path,
    key: int,
) -> None:
    """Encrypt an image using XOR pixel manipulation."""

    transform_image(input_path, output_path, key)


def decrypt_image(
    input_path: str | Path,
    output_path: str | Path,
    key: int,
) -> None:
    """Decrypt an image using the same XOR transformation."""

    transform_image(input_path, output_path, key)


def main() -> None:
    """Run the interactive image encryption tool."""

    print("=" * 50)
    print("       PIXEL IMAGE ENCRYPTION TOOL")
    print("=" * 50)

    while True:
        print("\nChoose an operation:")
        print("1. Encrypt image")
        print("2. Decrypt image")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "3":
            print("\nExiting Image Encryption Tool.")
            break

        if choice not in {"1", "2"}:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        input_path = input("Enter input image path: ").strip()
        output_path = input("Enter output image path: ").strip()

        try:
            key = int(input("Enter encryption key (0-255): "))
            validate_key(key)
        except ValueError:
            print("Invalid key. Please enter an integer from 0 to 255.")
            continue
        except TypeError as error:
            print(f"Invalid key: {error}")
            continue

        try:
            if choice == "1":
                encrypt_image(input_path, output_path, key)
                print(f"\nImage encrypted successfully: {output_path}")
            else:
                decrypt_image(input_path, output_path, key)
                print(f"\nImage decrypted successfully: {output_path}")

        except FileNotFoundError as error:
            print(f"\nError: {error}")
        except OSError as error:
            print(f"\nImage processing error: {error}")


if __name__ == "__main__":
    main()