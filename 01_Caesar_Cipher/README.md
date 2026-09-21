# Task 01 — Caesar Cipher

## Overview

This project implements a Caesar Cipher encryption and decryption tool using Python.

The Caesar Cipher is a classical substitution cipher in which each letter in the plaintext is shifted by a fixed number of positions in the alphabet. The same shift value can be used in reverse to decrypt the message.

This task was completed as part of my Cyber Security Internship at Prodigy InfoTech.

## Objectives

- Understand the basic concept of substitution ciphers.
- Implement text encryption using the Caesar Cipher.
- Implement text decryption using the reverse shift.
- Preserve uppercase and lowercase characters.
- Preserve spaces, punctuation, and numbers.
- Handle shift values outside the standard 0–25 range.
- Validate user input.
- Implement automated tests using pytest.
- Document the implementation and testing process.

## Project Structure

```text
01_Caesar_Cipher/
├── README.md
├── screenshots/
│   ├── 01_basic_encryption.png
│   ├── 02_basic_decryption.png
│   ├── 03_edge_cases.png
│   └── 04_automated_tests.png
├── src/
│   └── caesar_cipher.py
└── tests/
    └── test_caesar_cipher.py
```

## How the Caesar Cipher Works

The Caesar Cipher shifts each alphabetic character by a specified number of positions.

For example, with a shift of `3`:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

Example:

```text
Plaintext:
HELLO WORLD

Shift:
3

Ciphertext:
KHOOR ZRUOG
```

For decryption, the shift is reversed:

```text
Ciphertext:
KHOOR ZRUOG

Shift:
3

Plaintext:
HELLO WORLD
```

## Implementation

The main implementation is located at:

```text
src/caesar_cipher.py
```

The program provides:

- Caesar Cipher encryption
- Caesar Cipher decryption
- Uppercase and lowercase support
- Preservation of spaces
- Preservation of punctuation
- Preservation of numbers
- Support for large shift values
- Input validation
- Interactive command-line interface

## Character Handling

Only alphabetic characters are shifted.

For example:

```text
Input:
Hello, World! 123

Shift:
5

Output:
Mjqqt, Btwqi! 123
```

The following characters remain unchanged:

- Spaces
- Numbers
- Punctuation
- Special characters

## Shift Handling

The implementation supports shift values beyond the normal `0–25` range by using alphabetic wrap-around.

For example:

```text
Shift:
29
```

is equivalent to:

```text
29 % 26 = 3
```

Therefore:

```text
HELLO
```

becomes:

```text
KHOOR
```

## Input Validation

The program validates the shift value before performing encryption or decryption.

Example of invalid input:

```text
abc
```

Result:

```text
Invalid shift. Please enter an integer.
```

## Manual Testing

The following manual test cases were performed successfully.

### Test 1 — Basic Encryption

```text
Input:
HELLO WORLD

Shift:
3

Expected:
KHOOR ZRUOG
```

Result:

```text
PASS
```

### Test 2 — Basic Decryption

```text
Input:
KHOOR ZRUOG

Shift:
3

Expected:
HELLO WORLD
```

Result:

```text
PASS
```

### Test 3 — Alphabet Wrap-Around

```text
Input:
xyz

Shift:
3

Expected:
abc
```

Result:

```text
PASS
```

### Test 4 — Mixed Characters

```text
Input:
Hello, World! 123

Shift:
5

Expected:
Mjqqt, Btwqi! 123
```

Result:

```text
PASS
```

### Test 5 — Large Shift

```text
Input:
HELLO

Shift:
29

Expected:
KHOOR
```

Result:

```text
PASS
```

### Test 6 — Number Input

```text
Input:
3

Shift:
3

Expected:
3
```

Result:

```text
PASS
```

### Test 7 — Invalid Shift

```text
Input:
HELLO

Shift:
abc

Expected:
Invalid shift. Please enter an integer.
```

Result:

```text
PASS
```

## Automated Testing

Automated tests were implemented using pytest.

Run the complete test suite with:

```powershell
python -m pytest .\01_Caesar_Cipher\tests\ -v
```

### Test Results

```text
12 passed
```

All automated tests passed successfully.

The test suite covers:

- Basic encryption
- Basic decryption
- Uppercase characters
- Lowercase characters
- Alphabet wrap-around
- Large shift values
- Zero shift
- Negative shift handling
- Spaces
- Punctuation
- Numbers
- Invalid shift input

## Technologies Used

- Python 3.11.9
- pytest 9.1.1
- Visual Studio Code
- PowerShell
- Git
- GitHub

## Security Considerations

The Caesar Cipher is a classical cryptographic technique and is not secure for protecting sensitive information.

There are only 26 possible shift positions in the standard English alphabet, making the cipher vulnerable to brute-force attacks and frequency analysis.

This implementation is intended for:

- Educational purposes
- Understanding cryptography concepts
- Learning encryption and decryption
- Practicing Python programming and testing

It should not be used to protect real-world confidential data.

## Learning Outcomes

Through this task, I practiced:

- Classical cryptography concepts
- Substitution cipher implementation
- Encryption and decryption logic
- Alphabet wrap-around
- Input validation
- Exception handling
- Automated testing with pytest
- Command-line application development
- Git and GitHub workflow
- Technical documentation

## Ethical Disclaimer

This project was created for educational and cybersecurity learning purposes.

Cryptographic tools should only be used for legitimate and authorized purposes.

## Author

**Anisha Prasad**

Cyber Security Intern — Prodigy InfoTech