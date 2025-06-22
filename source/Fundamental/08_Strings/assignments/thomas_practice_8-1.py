"""
Write a program that does the following:
1. Accepts input of your first, last, and middle names into three separate strings
2. Concatenates them together to form a string called full_name
3. Counts the number of “a” or “A” letters
4. Counts the number of “e” or “E” letters
5. Counts the number of “s” or “S” letters
6. Displays each of the three counts
"""

def main():
    first = input("First name: ")
    middle = input("Middle name: ")
    last = input("Last name: ")

    full_name = f"{first} {middle} {last}"

    a_chars = 0
    e_chars = 0
    s_chars = 0
    for char in full_name.lower():
        if char == "a":
            a_chars += 1
        elif char == "e":
            e_chars += 1
        elif char == "s":
            s_chars += 1
    
    print(f"A's in name: {a_chars}\nE's in name: {e_chars}\nS's in name: {s_chars}")

if __name__ == "__main__":
    main()