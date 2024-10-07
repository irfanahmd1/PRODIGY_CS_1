def encrypt(message, shift_value):
    encrypted_message = ""
    for character in message:
        if character.isupper():
            new_char = chr((ord(character) - ord('A') + shift_value) % 26 + ord('A'))
            encrypted_message += new_char
        elif character.islower():
            new_char = chr((ord(character) - ord('a') + shift_value) % 26 + ord('a'))
            encrypted_message += new_char
        else:
            encrypted_message += character
    return encrypted_message


def decrypt(message, shift_value):
    return encrypt(message, -shift_value)


def main():
    print("Welcome to Caesar Cipher!")
    operation = input("Do you want to encrypt or decrypt? ").lower()
    message = input("Enter your message: ")
    shift_value = int(input("Enter shift value: "))

    if operation == "encrypt":
        print(f"Encrypted Message: {encrypt(message, shift_value)}")
    elif operation == "decrypt":
        print(f"Decrypted Message: {decrypt(message, shift_value)}")
    else:
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    main()