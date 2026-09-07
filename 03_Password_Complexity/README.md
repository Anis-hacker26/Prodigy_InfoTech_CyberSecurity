# Task 03 — Password Complexity Checker

## Overview

The **Password Complexity Checker** is a Python-based cybersecurity utility developed as part of the **Prodigy InfoTech Cyber Security Internship**.

The tool evaluates a password against several basic security and complexity criteria, calculates a score, identifies common or predictable patterns, and classifies the password as:

- 🔴 **Weak**
- 🟡 **Moderate**
- 🟢 **Strong**

The application also provides actionable feedback explaining how the password could be improved.

> **Security Disclaimer:** This project is an educational password-complexity assessment tool. A high complexity score does **not** guarantee that a password is secure or resistant to dictionary attacks, brute-force attacks, password reuse, or credential-stuffing attacks.

---

## Objectives

The primary objectives of this task are to:

1. Analyze password length.
2. Detect lowercase characters.
3. Detect uppercase characters.
4. Detect numerical characters.
5. Detect special characters.
6. Identify common and predictable password patterns.
7. Calculate an overall complexity score.
8. Classify password strength.
9. Provide security-focused improvement feedback.
10. Validate the implementation using automated tests.
11. Practice secure handling of password-related input.

---

## Features

### 1. Password Length Analysis

The checker evaluates the length of the supplied password.

- At least **8 characters** → +1 point
- At least **12 characters** → +1 additional point

Longer passwords generally provide a larger search space than shorter passwords.

---

### 2. Lowercase Detection

The application checks whether the password contains at least one lowercase character:

```text
a-z
```

Example:

```text
password
```

---

### 3. Uppercase Detection

The application checks whether the password contains at least one uppercase character:

```text
A-Z
```

Example:

```text
Password
```

---

### 4. Number Detection

The checker identifies whether the password contains numerical characters:

```text
0-9
```

Example:

```text
Password2026
```

---

### 5. Special Character Detection

The application checks for characters outside letters and numbers.

Examples:

```text
!
@
#
$
%
^
&
*
```

Example:

```text
Secure@2026
```

---

### 6. Common and Predictable Pattern Detection

The application detects several obvious patterns that can make passwords easier to guess.

Examples include:

```text
password
password123
123456
12345678
qwerty
admin
welcome
letmein
```

It also detects:

- Repeated characters such as `aaa`
- Sequential number patterns such as `1234`, `2345`, `3456`, etc.

The common-password comparison is case-insensitive.

---

## Scoring System

The checker uses a **0–6 point scoring model**.

| Security Criterion | Score |
|---|---:|
| Password has at least 8 characters | +1 |
| Password has at least 12 characters | +1 |
| Contains lowercase letters | +1 |
| Contains uppercase letters | +1 |
| Contains numbers | +1 |
| Contains special characters | +1 |
| Common/predictable pattern detected | −2 |

The final score is restricted to a range of:

```text
0–6
```

---

## Strength Classification

| Score | Strength |
|---:|---|
| 0–2 | 🔴 Weak |
| 3–4 | 🟡 Moderate |
| 5–6 | 🟢 Strong |

A password containing an identified common or predictable pattern is classified as **Weak**, even if it otherwise satisfies several complexity requirements.

This is intentional because predictable passwords can remain vulnerable despite containing multiple character types.

---

## Example Results

### Weak Password

Example input:

```text
abc
```

Result:

```text
Length: 3
Lowercase letters: Yes
Uppercase letters: No
Numbers: No
Special characters: No
Common/predictable pattern: No

Score: 1/6
Strength: Weak
```

Feedback:

```text
- Use at least 8 characters.
- Use 12 or more characters for better strength.
- Add uppercase letters.
- Add numbers.
- Add special characters.
```

---

### Moderate Password

Example input:

```text
BlueSky2026
```

Result:

```text
Length: 11
Lowercase letters: Yes
Uppercase letters: Yes
Numbers: Yes
Special characters: No
Common/predictable pattern: No

Score: 4/6
Strength: Moderate
```

Feedback:

```text
- Use 12 or more characters for better strength.
- Add special characters.
```

---

### Strong Password

Example input:

```text
Secure@2026Pass!
```

Result:

```text
Length: 16
Lowercase letters: Yes
Uppercase letters: Yes
Numbers: Yes
Special characters: Yes
Common/predictable pattern: No

Score: 6/6
Strength: Strong
```

Feedback:

```text
- Good complexity. Avoid password reuse and consider MFA.
```

---

### Predictable Password

Example input:

```text
password123
```

Result:

```text
Length: 11
Lowercase letters: Yes
Uppercase letters: No
Numbers: Yes
Special characters: No
Common/predictable pattern: Yes

Score: 1/6
Strength: Weak
```

The predictable-password detection demonstrates that simply adding numbers to a common password does not necessarily make it secure.

---

## Feedback System

The application generates feedback based on the characteristics missing from the password.

Possible recommendations include:

```text
Use at least 8 characters.
Use 12 or more characters for better strength.
Add lowercase letters.
Add uppercase letters.
Add numbers.
Add special characters.
Avoid common passwords and predictable character patterns.
```

When all complexity requirements are satisfied, the tool provides additional security guidance:

```text
Good complexity. Avoid password reuse and consider MFA.
```

---

## Implementation Approach

The checker follows a rule-based analysis process:

```text
                 Password Input
                       |
                       v
              Validate Input Type
                       |
                       v
             Analyze Password Length
                       |
          +------------+------------+
          |            |            |
          v            v            v
     Lowercase      Uppercase     Numbers
          |            |            |
          +------------+------------+
                       |
                       v
              Special Characters
                       |
                       v
          Common/Pattern Detection
                       |
                       v
                Calculate Score
                       |
                       v
             Classify Strength
                       |
                       v
             Generate Feedback
                       |
                       v
                Display Result
```

---

## Project Structure

```text
03_Password_Complexity/
│
├── README.md
│
├── screenshots/
│   ├── 01_weak_password.png
│   ├── 02_moderate_password.png
│   ├── 03_strong_password.png
│   ├── 04_predictable_password.png
│   └── 05_automated_tests.png
│
├── src/
│   ├── __init__.py
│   └── password_checker.py
│
└── tests/
    └── test_password_checker.py
```

---

## Technologies Used

- **Python 3.11**
- **Regular Expressions (`re`)**
- **Python Dataclasses**
- **Pytest**
- **Visual Studio Code**
- **Git**
- **GitHub**

---

## Requirements

The project requires:

- Python **3.11 or later**
- Pytest for automated testing

Check the installed Python version:

```powershell
python --version
```

Example:

```text
Python 3.11.9
```

Install Pytest if required:

```powershell
python -m pip install pytest
```

---

## Running the Application

From the repository root:

```powershell
python .\03_Password_Complexity\src\password_checker.py
```

The application starts an interactive command-line interface.

Example:

```text
==================================================
       PASSWORD COMPLEXITY CHECKER
==================================================

Enter a password to analyze (or type 'exit' to quit):
```

Enter a **dummy password for testing**.

To exit the application:

```text
exit
```

---

## Running Automated Tests

Run the complete Task 03 test suite using:

```powershell
python -m pytest .\03_Password_Complexity\tests\ -v
```

### Test Coverage

The automated test suite validates:

- Strong password classification
- Moderate password classification
- Weak password classification
- Common-password detection
- Repeated-character detection
- Sequential-number detection
- Uppercase/lowercase detection
- Numeric detection
- Special-character detection
- Invalid input handling
- Empty-password handling

### Test Result

The current implementation passes all automated tests:

```text
9 passed
```

Example:

```text
============================= test session starts =============================

collected 9 items

test_strong_password PASSED
test_moderate_password PASSED
test_weak_password PASSED
test_common_password_detection PASSED
test_repeated_character_detection PASSED
test_sequential_number_detection PASSED
test_case_sensitive_complexity PASSED
test_invalid_password_type PASSED
test_empty_password PASSED

============================== 9 passed ==============================
```

---

## Security Considerations

This project demonstrates an important cybersecurity concept:

> **Password complexity and password security are not the same thing.**

A password can satisfy multiple complexity requirements and still be vulnerable.

### Dictionary Attacks

Attackers can use large dictionaries containing commonly used words and passwords.

Examples include:

```text
password
welcome
admin
qwerty
```

A password based on a common word may therefore be easier to guess.

---

### Brute-Force Attacks

Brute-force attacks systematically attempt possible password combinations.

Increasing password length can increase the number of possible combinations, making exhaustive guessing more difficult.

However, actual resistance depends on factors such as password generation, attack resources, rate limiting, and authentication controls.

---

### Password Reuse

Using the same password across multiple websites creates significant risk.

If credentials from one service are compromised, attackers may attempt the same credentials against other services.

Using **unique passwords for different accounts** reduces this risk.

---

### Credential Stuffing

Credential stuffing attacks use previously leaked username/password combinations against other services.

Even a complex password can become a security problem if it has already been exposed and reused elsewhere.

---

## Password Managers

Password managers can help users:

- Generate unique passwords.
- Store complex passwords securely.
- Avoid password reuse.
- Reduce the need to memorize many passwords.

For security-conscious environments, using unique randomly generated passwords is generally preferable to relying only on manually created complexity rules.

---

## Multi-Factor Authentication (MFA)

Multi-factor authentication adds another layer of protection beyond the password.

Depending on the implementation, authentication can involve factors such as:

- Something you know
- Something you have
- Something you are

Enabling MFA can reduce the impact of a compromised password.

---

## Limitations

This project intentionally uses a simple rule-based scoring system for educational purposes.

It does **not**:

- Calculate true password entropy.
- Simulate password-cracking attacks.
- Perform real brute-force testing.
- Query breached-password databases.
- Detect every dictionary word.
- Detect every predictable phrase.
- Determine whether a password has been reused.
- Determine whether an account has MFA enabled.
- Guarantee resistance against credential stuffing.
- Guarantee that a password is secure.

Therefore, the score should be treated as an **educational complexity indicator**, not a definitive security rating.

---

## Privacy and Safe Testing

The application is designed so that the entered password is **not printed in the analysis output**.

Passwords should not be stored in source code, screenshots, logs, or Git commits.

For demonstrations and testing, use only dummy passwords such as:

```text
abc
BlueSky2026
Secure@2026Pass!
password123
```

> **Never enter a real personal, work, banking, email, or production password into an educational demonstration tool.**

---

## Evidence

Screenshots documenting the implementation and testing process are stored in:

```text
03_Password_Complexity/screenshots/
```

The evidence includes:

1. Weak password analysis
2. Moderate password analysis
3. Strong password analysis
4. Predictable password detection
5. Automated test results

---

## Learning Outcomes

Through this task, the following cybersecurity and programming concepts were practiced:

- Python programming
- Regular expressions
- Password complexity analysis
- Rule-based security scoring
- Input validation
- Common-password detection
- Predictable-pattern detection
- Secure handling of password input
- Automated testing with Pytest
- Cybersecurity documentation
- Git and GitHub workflow

---

## Future Improvements

Possible future enhancements include:

- More comprehensive dictionary-based detection.
- Detection of common password substitutions such as `@` for `a`.
- Password entropy estimation.
- Integration with a trusted breached-password checking mechanism using privacy-preserving techniques.
- Configurable scoring policies.
- Improved passphrase analysis.
- GUI or web-based interface.
- Configurable organizational password policies.
- Additional test cases and edge-case coverage.

Any future implementation should preserve user privacy and avoid storing plaintext passwords.

---

## Internship Context

**Program:** Prodigy InfoTech Cyber Security Internship

**Task:** Task 03 — Password Complexity Checker

**Technology:** Python

**Testing Framework:** Pytest

**Repository:** `Prodigy_InfoTech_CyberSecurity`

---

## Ethical Disclaimer

This project was developed strictly for **educational and cybersecurity learning purposes**.

The Password Complexity Checker is intended to demonstrate password-security concepts and basic defensive analysis.

It should not be used as a substitute for a professional password-security auditing system or organizational authentication policy.

---

## Author

**Anisha Prasad**

Cyber Security Internship Project — Prodigy InfoTech

---

## Summary

The Password Complexity Checker demonstrates how basic password characteristics can be evaluated programmatically.

The project combines:

```text
Password Analysis
       +
Pattern Detection
       +
Rule-Based Scoring
       +
Strength Classification
       +
Security Feedback
       +
Automated Testing
```

The key security lesson from this task is that **password complexity is only one part of authentication security**.

Strong password practices should be combined with:

- Unique passwords
- Password managers
- Multi-factor authentication
- Appropriate authentication protections
- Protection against credential reuse and credential stuffing

---

**Task 03 completed as part of the Prodigy InfoTech Cyber Security Internship.**