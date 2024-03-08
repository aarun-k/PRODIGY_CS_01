def caesar_cipher_encrypt(plaintext: str, shift: int) -> str:
    """
    Encrypts the plaintext using the Caesar Cipher algorithm with the given shift value.

    Parameters:
        plaintext (str): The message to be encrypted.
        shift (int): The number of positions to shift each letter in the alphabet.

    Returns:
        str: The encrypted ciphertext.
    """
    ciphertext = ''
    
    for char in plaintext:
        if char.isalpha():  
            # Determine the ASCII offset based on the case (uppercase or lowercase)
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Apply the Caesar Cipher shift and wrap around if necessary
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:  
            encrypted_char = char
        ciphertext += encrypted_char
    
    return ciphertext


def caesar_cipher_decrypt(ciphertext: str, shift: int) -> str:
    """
    Decrypts the ciphertext using the Caesar Cipher algorithm with the given shift value.

    Parameters:
        ciphertext (str): The encrypted message.
        shift (int): The number of positions to shift each letter in the alphabet.

    Returns:
        str: The decrypted plaintext.
    """
    plaintext = ''
    
    for char in ciphertext:
        if char.isalpha():  
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Apply the Caesar Cipher reverse shift and wrap around if necessary
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:  
            decrypted_char = char
        plaintext += decrypted_char
    
    return plaintext


def main():
    """
    Allows the user to input a message and a shift value to perform encryption and decryption
    using the Caesar Cipher algorithm.
    """
    try:
        plaintext = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value (an integer between 1 and 25): "))

        if not 1 <= shift <= 25:
            raise ValueError("Shift value must be an integer between 1 and 25.")

        encrypted_message = caesar_cipher_encrypt(plaintext, shift)
        print("Encrypted message:", encrypted_message)

        decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
        print("Decrypted message:", decrypted_message)

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
