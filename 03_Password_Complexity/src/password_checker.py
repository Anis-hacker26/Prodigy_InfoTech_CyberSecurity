"""
Password Complexity Checker
---------------------------

Educational password-strength assessment tool.

This module evaluates passwords using basic complexity indicators
and provides improvement feedback.
"""

from dataclasses import dataclass
import re


@dataclass
class PasswordAnalysis:
    """Store the results of a password complexity analysis."""

    length: int
    has_lowercase: bool
    has_uppercase: bool
    has_digit: bool
    has_special: bool
    has_common_pattern: bool
    score: int
    strength: str
    feedback: list[str]


COMMON_PATTERNS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "qwerty123",
    "admin",
    "letmein",
    "welcome",
    "iloveyou",
}


def check_common_pattern(password: str) -> bool:
    """
    Check whether a password contains an obvious common pattern.

    The comparison is case-insensitive.
    """
    normalized = password.lower()

    if normalized in COMMON_PATTERNS:
        return True

    if re.search(r"(.)\1{2,}", normalized):
        return True

    if re.search(r"1234|2345|3456|4567|5678|6789", normalized):
        return True

    return False


def analyze_password(password: str) -> PasswordAnalysis:
    """
    Analyze password complexity and return a structured result.

    Scoring criteria:
    - At least 8 characters
    - At least 12 characters
    - Lowercase letter
    - Uppercase letter
    - Digit
    - Special character
    - No obvious common/predictable pattern
    """

    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    length = len(password)

    has_lowercase = bool(re.search(r"[a-z]", password))
    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))
    has_common_pattern = check_common_pattern(password)

    score = 0
    feedback = []

    # Length checks
    if length >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if length >= 12:
        score += 1
    else:
        feedback.append("Use 12 or more characters for better strength.")

    # Character-type checks
    if has_lowercase:
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if has_uppercase:
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if has_digit:
        score += 1
    else:
        feedback.append("Add numbers.")

    if has_special:
        score += 1
    else:
        feedback.append("Add special characters.")

    # Predictability check
    if has_common_pattern:
        score -= 2
        feedback.append(
            "Avoid common passwords and predictable character patterns."
        )

    # Keep score between 0 and 6
    score = max(0, min(score, 6))

    # Strength classification
    if has_common_pattern or score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    if not feedback:
        feedback.append(
            "Good complexity. Avoid password reuse and consider MFA."
        )

    return PasswordAnalysis(
        length=length,
        has_lowercase=has_lowercase,
        has_uppercase=has_uppercase,
        has_digit=has_digit,
        has_special=has_special,
        has_common_pattern=has_common_pattern,
        score=score,
        strength=strength,
        feedback=feedback,
    )


def display_analysis(password: str) -> None:
    """Display password complexity results without printing the password."""

    analysis = analyze_password(password)

    print("\n" + "=" * 50)
    print("       PASSWORD COMPLEXITY CHECKER")
    print("=" * 50)

    print(f"\nLength: {analysis.length}")
    print(
        f"Lowercase letters: "
        f"{'Yes' if analysis.has_lowercase else 'No'}"
    )
    print(
        f"Uppercase letters: "
        f"{'Yes' if analysis.has_uppercase else 'No'}"
    )
    print(f"Numbers: {'Yes' if analysis.has_digit else 'No'}")
    print(
        f"Special characters: "
        f"{'Yes' if analysis.has_special else 'No'}"
    )
    print(
        f"Common/predictable pattern: "
        f"{'Yes' if analysis.has_common_pattern else 'No'}"
    )

    print(f"\nScore: {analysis.score}/6")
    print(f"Strength: {analysis.strength}")

    print("\nFeedback:")
    for item in analysis.feedback:
        print(f"- {item}")


def main() -> None:
    """Run the interactive password complexity checker."""

    print("=" * 50)
    print("       PASSWORD COMPLEXITY CHECKER")
    print("=" * 50)

    while True:
        password = input(
            "\nEnter a password to analyze "
            "(or type 'exit' to quit): "
        )

        if password.lower() == "exit":
            print("\nExiting Password Complexity Checker.")
            break

        try:
            display_analysis(password)
        except TypeError as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()