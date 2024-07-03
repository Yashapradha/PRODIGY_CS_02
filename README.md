ncryption and Decryption Tool

## Overview

This project involves the development of an image encryption and decryption tool using pixel manipulation techniques. The tool is implemented in Python and uses the PIL (Pillow) library along with numpy to perform secure and reversible transformations on images.

## Features

- **Encrypt Images:** Alter pixel values using a combination of XOR operations and key-based transformations to secure the image.
- **Decrypt Images:** Restore the encrypted image to its original state using the same key used for encryption.
- **Simple Command Line Interface:** Easy-to-use command line interface to encrypt and decrypt images.

## How It Works

1. **Encryption:**
   - Load the image.
   - Convert the image to a numpy array.
   - Apply XOR operation with a key to each pixel value.
   - Shift the pixel values by adding the key and ensure the values stay within the valid range using modulo operation.
   - Convert the modified array back to an image and save it.

2. **Decryption:**
   - Load the encrypted image.
   - Convert the image to a numpy array.
   - Reverse the shifting by subtracting the key and ensure the values stay within the valid range using modulo operation.
   - Apply XOR operation with the same key to each pixel value to restore the original image.
   - Convert the restored array back to an image and save it.

## Requirements

- Python 3.x
- Pillow
- numpy

## Installation

1. Clone the repository or download the code.
   ```bash
   git clone https://github.com/yourusername/image-encryption-tool.git
   ```
2. Navigate to the project directory.
   ```bash
   cd image-encryption-tool
   ```
3. Install the required libraries.
   ```bash
   pip install Pillow numpy
   ```

## Usage

1. Save the provided code in a Python file, e.g., `image_encryption.py`.
2. Run the script using Python.
   ```bash
   python image_encryption.py
   ```
3. Follow the prompts to either encrypt or decrypt an image:
   - Enter 'e' to encrypt an image or 'd' to decrypt an image.
   - Provide the path to the image file.
   - Enter an integer key for the encryption/decryption process.

### Example

To encrypt an image:
```bash
Enter 'e' to encrypt or 'd' to decrypt: e
Enter the image path: flower.jpeg
Enter the key (an integer value): 123
```

To decrypt an image:
```bash
Enter 'e' to encrypt or 'd' to decrypt: d
Enter the image path: encrypted_image.png
Enter the key (an integer value): 123
```
