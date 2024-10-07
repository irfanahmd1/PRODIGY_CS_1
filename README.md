Caesar Cipher - Simple Text Encryption and Decryption

Introduction
This project implements the Caesar Cipher, one of the oldest known encryption techniques. It allows users to encrypt and decrypt messages by shifting letters in the alphabet by a user-defined shift value. This program provides a hands-on experience with basic cryptography and can be a starting point for learning more advanced techniques.

How the Caesar Cipher Works

The Caesar Cipher shifts each letter in the message by a fixed number of positions in the alphabet. For example, with a shift value of 3, the letter 'A' becomes 'D', 'B' becomes 'E', and so on. Non-alphabetic characters (e.g., spaces, punctuation) remain unchanged.

For decryption, the shift is reversed to recover the original message.

Features
Encrypt Messages: The user can input a message and a shift value to encrypt it.
Decrypt Messages: Encrypted messages can be decrypted by reversing the shift value.
Supports both uppercase and lowercase letters.
Non-alphabetic characters (like punctuation and spaces) are preserved.
Usage
To use this program:
Clone the repository:
git clone https://github.com/irfanahmd1/PRODIGY_CS_1.git

Navigate to the project directory:
cd caesar-cipher

Run the program:
python3 caesar_cipher.py
Follow the instructions in the terminal:

Choose whether to encrypt or decrypt.
Enter your message and a shift value.
The program will output the encrypted or decrypted message
