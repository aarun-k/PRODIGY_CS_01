# caesar-cipher-python
The Caesar Cipher is one of the simplest and most well-known encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions down the alphabet. For example, with a shift of 3, 'A' would be encrypted to 'D', 'B' to 'E', and so on. When reaching the end of the alphabet, the cipher wraps around, so 'X' would become 'A', 'Y' would become 'B', and 'Z' would become 'C'.

Here's how the Caesar Cipher algorithm works:

1. Encryption: Each letter in the plaintext is shifted by a fixed number of positions down the alphabet. If the shift takes the letter beyond 'Z' in the case of uppercase letters or 'z' in the case of lowercase letters, the alphabet wraps around. Non-alphabetic characters remain unchanged.

2. Decryption: To decrypt the ciphertext, the process is reversed. Each letter in the ciphertext is shifted back by the same number of positions to recover the original plaintext.
