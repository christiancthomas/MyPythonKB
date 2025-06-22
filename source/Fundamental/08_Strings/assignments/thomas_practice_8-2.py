"""
1. Flip case: Write a program to do the following:
2. Accept the input of a sentence from the user that contains lowercase, uppercase,
and special characters.
3. Make a new sentence in which the lowercase characters are changed to
uppercase and the uppercase are changed to lower case. All other characters will
retain their original value.
4. Print the original sentence and the new sentence.
5. Turn in your program to the practice assignment link in course
content.
"""

def main():
    sentence = input("Enter a sentence with a mix of upper and lowercase characters: ")
    flipped_sentence = ""
    for char in sentence:
        if char.lower() == char:
            flipped_sentence += char.upper()
        else:
            flipped_sentence += char.lower()
    
    print(f"Original sentence: {sentence}\nfLIPPED SENTENCE: {flipped_sentence}")

if __name__ == "__main__":
    main()