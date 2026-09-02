# Task 02 — Pixel Manipulation for Image Encryption

## Overview

This project demonstrates educational image encryption using pixel-level manipulation with Python and Pillow.

The implementation applies an XOR operation to each RGB channel of every pixel using an integer encryption key from `0` to `255`.

Because XOR is reversible, applying the same transformation with the same key decrypts the image and restores the original pixel data.

This task was completed as part of my Cyber Security Internship at Prodigy InfoTech.

## Objectives

- Understand image representation at the pixel level.
- Manipulate RGB pixel values programmatically.
- Implement a reversible image transformation.
- Use Pillow for image processing.
- Validate encryption keys and input files.
- Test encryption and decryption automatically.
- Verify that the decrypted image matches the original image exactly.
- Understand the security limitations of simple XOR-based transformations.

## Project Structure

```text
02_Image_Encryption/
├── README.md
├── sample_images/
│   ├── original.png
│   ├── encrypted.png
│   └── decrypted.png
├── screenshots/
├── src/
│   ├── __init__.py
│   └── image_encryption.py
└── tests/
    └── test_image_encryption.py
```

## How It Works

An RGB image represents each pixel using three color channels:

```text
(R, G, B)
```

For each pixel, the implementation applies XOR between every color channel and the encryption key.

The transformation is:

```text
R' = R XOR key
G' = G XOR key
B' = B XOR key
```

For example, if a pixel contains:

```text
(R, G, B)
```

the encrypted pixel becomes:

```text
(R XOR key, G XOR key, B XOR key)
```

## Why XOR Is Reversible

XOR has a useful mathematical property:

```text
(A XOR K) XOR K = A
```

Therefore, applying the same XOR key twice restores the original value.

The complete process is:

```text
Original Image
      │
      ▼
XOR Pixel Transformation
      │
      ▼
Encrypted Image
      │
      ▼
XOR Transformation Using Same Key
      │
      ▼
Decrypted Image
      │
      ▼
Original Pixel Data
```

## Implementation

The main implementation is located at:

```text
src/image_encryption.py
```

The program provides:

- Pixel-level XOR transformation
- Image encryption
- Image decryption
- Encryption key validation
- Input-file validation
- Error handling
- Interactive command-line interface

### Main Functions

#### `validate_key()`

Validates that the encryption key is an integer between `0` and `255`.

#### `transform_pixel()`

Applies XOR to the RGB channels of a pixel.

#### `transform_image()`

Processes the image pixel by pixel and saves the transformed image.

#### `encrypt_image()`

Encrypts an image using the XOR transformation.

#### `decrypt_image()`

Decrypts an image using the same XOR transformation.

## Key Validation

The encryption key must:

- Be an integer.
- Be between `0` and `255`.

Examples:

```text
Valid:
0
123
255

Invalid:
-1
256
abc
```

Invalid keys are rejected before image processing begins.

## Manual Testing

A controlled `200 × 200` RGB PNG image was created for testing.

The original image was verified as:

```text
Format: PNG
Size: (200, 200)
Mode: RGB
```

### Encryption Test

The following configuration was used:

```text
Input:
02_Image_Encryption/sample_images/original.png

Output:
02_Image_Encryption/sample_images/encrypted.png

Key:
123
```

The encryption completed successfully.

The encrypted image was then compared with the original image.

Result:

```text
Images identical: False
```

This confirms that the pixel data changed after encryption.

The encrypted image was also verified:

```text
Encrypted format: PNG
Encrypted size: (200, 200)
Encrypted mode: RGB
```

### Decryption Test

The encrypted image was decrypted using the same key:

```text
123
```

Configuration:

```text
Input:
02_Image_Encryption/sample_images/encrypted.png

Output:
02_Image_Encryption/sample_images/decrypted.png
```

The decrypted image was compared against the original image.

Result:

```text
Original: (200, 200) RGB
Decrypted: (200, 200) RGB
Images identical: True
```

This confirms that the encryption/decryption transformation is reversible and that the original pixel data was restored exactly.

## Automated Testing

Automated tests were implemented using `pytest`.

Run the test suite with:

```powershell
python -m pytest .\02_Image_Encryption\tests\ -v
```

### Test Results

```text
========================= test session starts =========================
collected 6 items

test_transform_pixel PASSED
test_encrypt_and_decrypt_restore_original PASSED
test_encryption_changes_image PASSED
test_invalid_key_type PASSED
test_invalid_key_range PASSED
test_missing_input_file PASSED

========================== 6 passed in 0.15s ==========================
```

All six automated tests passed successfully.

The test suite verifies:

1. Correct XOR pixel transformation.
2. Encryption followed by decryption restores the original image.
3. Encryption changes the image pixel data.
4. Invalid key types are rejected.
5. Invalid key ranges are rejected.
6. Missing input files are handled correctly.

## Technologies Used

- Python 3.11.9
- Pillow 12.3.0
- pytest 9.1.1
- Visual Studio Code
- PowerShell
- Git
- GitHub

## Security Considerations

This implementation is intended for educational purposes.

The fixed-key XOR transformation used here demonstrates pixel manipulation and reversible encryption concepts, but it should **not** be considered secure modern image encryption.

A simple fixed-key XOR operation has significant cryptographic weaknesses and should not be used to protect sensitive or confidential images in production environments.

Real-world applications should use established cryptographic algorithms and appropriate authenticated encryption mechanisms.

## Learning Outcomes

Through this task, I practiced:

- Digital image representation.
- RGB pixel manipulation.
- XOR operations.
- Reversible transformations.
- Image processing with Pillow.
- Input validation.
- Exception handling.
- Automated testing with pytest.
- Security limitations of simple cryptographic techniques.
- Technical documentation.
- Git and GitHub workflow.

## Ethical Disclaimer

This project was created for educational and cybersecurity learning purposes.

It should only be used with images and systems for which I have permission.

The implementation should not be represented as a production-grade encryption solution.

## Author

**Anisha Prasad**

Cyber Security Intern — Prodigy InfoTech