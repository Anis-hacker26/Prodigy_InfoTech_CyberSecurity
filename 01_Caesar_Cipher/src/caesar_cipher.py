"""
Caesar Cipher
--------------
A simple implementation of the Caesar Cipher algorithm.
"""


def caesar_cipher(text, shift):
    """
    Transform text using the Caesar Cipher.

    Positive shift values encrypt.
    Negative shift values decrypt.
    """

    result = []

    # Normalize the shift to the alphabet range.
    shift = shift % 26

    for character in text:

        if character.isupper():
            shifted = chr(
                (ord(character) - ord("A") + shift) % 26
                + ord("A")
            )
            result.append(shifted)

        elif character.islower():
            shifted = chr(
                (ord(character) - ord("a") + shift) % 26
                + ord("a")
            )
            result.append(shifted)

        else:
            # Preserve spaces, numbers and punctuation.
            result.append(character)

    return "".join(result)


def encrypt(text, shift):
    """Encrypt plaintext."""
    return caesar_cipher(text, shift)


def decrypt(text, shift):
    """Decrypt ciphertext."""
    return caesar_cipher(text, -shift)


def main():
    """Run the interactive Caesar Cipher tool."""

    print("=" * 45)
    print("        CAESAR CIPHER TOOL")
    print("=" * 45)

    while True:
        print("\nChoose an operation:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "3":
            print("\nExiting Caesar Cipher Tool.")
            break

        if choice not in {"1", "2"}:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        message = input("Enter your message: ")

        try:
            shift = int(input("Enter shift value: "))
        except ValueError:
            print("Invalid shift. Please enter an integer.")
            continue

        if choice == "1":
            result = encrypt(message, shift)
            print(f"\nEncrypted text: {result}")

        else:
            result = decrypt(message, shift)
            print(f"\nDecrypted text: {result}")


if __name__ == "__main__":
    main()