"""
Christian Thomas
Complete
This program reads in the provided text.txt and determines the following:
1. The number of uppercase letters in the file
2. The number of lowercase letters in the file
3. The number of digits in the file
4. The number of whitespace characters in the file

example output: 
Uppercase letters: 20
Lowercase letters: 310
Digits: 4
Spaces: 82
"""

def main():
    try:
        with open("text.txt", "r") as infile:
            text = infile.read()

            lower_chars = 0
            upper_chars = 0
            digits = 0
            spaces = 0
            for char in text:
                # have to check for spaces or numbers first, otherwise the upper/lower check will return true for nums & spaces.
                if char.isspace():
                    spaces += 1
                elif char.isdigit():
                    digits += 1
                elif char.isupper():
                    upper_chars += 1
                elif char.islower():
                    lower_chars += 1
    except IOError:
        print("An IOError occurred.")

    
    print(f"Uppercase characters: {upper_chars}\nLowercase characters: {lower_chars}\nDigits: {digits}\nSpaces: {spaces}")

if __name__ == "__main__":
    main()