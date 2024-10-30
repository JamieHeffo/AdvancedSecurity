def letterFrequencyAttack(text):
    # Remove spaces and convert text to uppercase
    cleanedText = text.replace(" ", "").upper()

    # Calculate frequency for each letter
    frequencyDict = {}
    totalElements = len(cleanedText)

    # English language letter frequencies for substitution
    freq = {
        "E": 12.7,
        "T": 9.1,
        "A": 8.2,
        "O": 7.5,
        "I": 7.0,
        "N": 6.7,
        "S": 6.3,
        "R": 6.0,
        "H": 5.8,
        "D": 4.3,
        "L": 4.0,
        "U": 2.8,
        "C": 2.8,
        "M": 2.4,
        "W": 2.4,
        "F": 2.2,
        "G": 2.0,
        "Y": 2.0,
        "P": 1.9,
        "B": 1.5,
        "V": 1.0,
        "K": 0.8,
        "J": 0.2,
        "X": 0.2,
        "Q": 0.1,
        "Z": 0.1
    }

    # Initialize empty list to store frequencies from cipher
    cipherFreq = {}

    # Iterate through each character in the cleaned text
    for char in cleanedText:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Update the frequency count for the current letter
            if char in frequencyDict:
                frequencyDict[char] += 1
            else:
                frequencyDict[char] = 1

    # Sort the letters based on their frequency in descending order
    sortedLetters = sorted(frequencyDict.items(),
                           key=lambda x: x[1], reverse=True)

    # Create a mapping of original letters to their corresponding decrypted letters
    substitutionMapping = {}
    for originalChar, _ in sortedLetters:
        decryptedChar = max(freq, key=lambda x: freq[x])
        freq[decryptedChar] = 0  # Mark the decrypted character as used
        substitutionMapping[originalChar] = decryptedChar

    # Substitute the decrypted letters into the original text
    decryptedText = "".join(
        substitutionMapping.get(char, char) for char in text)

    # Display letters and their frequencies in order of likelihood
    print("Cipher Text Frequencies")
    for char, count in sortedLetters:
        frequency = (count / totalElements) * 100

        # store the letter and its frequency in the new list
        cipherFreq[char] = frequency

        # Print the letter, its frequency, and the decrypted text
        print(f"Letter: {char}, Frequency: {frequency:.2f}%")

    print(f"\nOriginal Text : {text}")
    print(f"Decrypted Text: {decryptedText}")


# Example usage
inputText = "UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZ\
VUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZ\
WPFUPZHMDJUDTMOHMQ"
letterFrequencyAttack(inputText)
