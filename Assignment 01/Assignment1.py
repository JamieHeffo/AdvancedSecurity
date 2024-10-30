# Advanced Security Assignment 01
# C20483462 Jamie Heffernan

import numpy as np


def caesar(text, shift, mode=''):
    result = ""

    if mode == 'decrypt':
        # Invert the shift for decryption
        shift = -shift

    # Iterate through plaintext
    for char in text:

        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            isUpper = char.isupper()

            # Use ord() function to get unicode character of alphabet to shift
            # Add 3/shift value in mod 26 to encrypt each letter and append it to result
            # Use chr to return character of unicode after shifting
            shiftedChar = chr((ord(char) - ord('A' if isUpper else 'a') +
                               shift) % 26 + ord('A' if isUpper else 'a'))

            result += shiftedChar
        else:
            # If the character is not a letter, keep it unchanged
            result += char

    return result


def vigenere(text, key, mode=''):
    key = key.upper()
    result = ""
    key_index = 0

    # Iterate through plaintext
    for char in text:
        if char.isalpha():
            # Use ord() function to get the Unicode character of the alphabet to shift
            shift = ord(key[key_index % len(key)]) - ord('A')

            if mode == 'decrypt':
                # Invert the shift for decryption
                shift = -shift

            # Encrypt by adding shift in mod 26
            encryptedChar = chr((ord(char) + shift - ord('A' if char.isupper()
                                 else 'a')) % 26 + ord('A' if char.isupper() else 'a'))

            result += encryptedChar
            key_index += 1
        else:
            # Non-alphabetic characters like spaces are not encrypted so don't increment key index
            result += char

    return result


def hill(text, encryptionKey):

    result = ""

    # Create a 2x2 key matrix using ASCII values of key characters
    keyMatrix = np.array([[ord(encryptionKey[0]) - ord('A'), ord(encryptionKey[1]) - ord('A')],
                          [ord(encryptionKey[2]) - ord('A'), ord(encryptionKey[3]) - ord('A')]])

    # Loop through the plaintext in pairs of characters
    for i in range(0, len(text), 2):

        # Extract a pair of characters from the plaintext
        currentPair = text[i:i+2]

        # Convert characters to corresponding indices (0 to 25)
        currentPairIndices = [ord(char) - ord('A') for char in currentPair]

        # Multiply the key matrix with the pair indices in modulo 26
        encryptedPairIndices = np.dot(keyMatrix, currentPairIndices) % 26

        # Convert back to characters using ASCII values and join them
        encryptedPair = "".join([chr(index + ord('A'))
                                 for index in encryptedPairIndices])

        # Append the encrypted pair to the result
        result += encryptedPair

    return result


# Take user input and encrypt and decrypt the inputted plaintext
plaintext = input("Please enter text to encrypt/decrypt : ")
shift = 3
keyword = "Silly"
encryptionKey = 'BAKE'
hillPlaintext = 'CAKE'

caesarCipher = caesar(plaintext, shift, mode='encrypt')
caesarDecipher = caesar(caesarCipher, shift, mode='decrypt')

print('-------------------------------')
print(f"Original : {plaintext}")
print('---------Caesar Cipher---------')
print(f"Encrypted : {caesarCipher}")
print(f"Decrypted : {caesarDecipher}")

vigenereCipher = vigenere(plaintext, keyword, mode='encrypt')
vigenereDecipher = vigenere(vigenereCipher, keyword, mode='decrypt')

print('--------Vigenere Cipher--------')
print(f"Encrypted : {vigenereCipher}")
print(f"Decrypted : {vigenereDecipher}")

hillCipher = hill(hillPlaintext, encryptionKey)

print('----------Hill Cipher----------')
print(f"Original  : {hillPlaintext}")
print(f"Encrypted : {hillCipher}")
print('-------------------------------')
