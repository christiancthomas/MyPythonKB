"""
Square Display
Write a program that:
1. Asks the user for a positive integer no greater than 15 (use input
validation).
2. Asks the user for a character to use to create the square.
3. The program should display a square on the screen with the
number of rows and columns entered by the user using the
character provided by the user.
4. For example if the user enters 5 and % the output should be
%%%%%
%%%%%
%%%%%
%%%%%
%%%%%
"""

def main():
    # input validation for positive integer no greater than 15
    while True:
        try:
            size = int(input("Enter a positive integer no greater than 15: "))
            if size < 1 or size > 15:
                raise ValueError("Number must be between 1 and 15.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
    # input for character to create the square
    char = input("Enter a character to create the square: ")
    if char == "":
        print("Character cannot be empty. Using '%' as default.")
        char = '%'
    if len(char) > 1:
        print("Only the first character will be used.")
        char = char[0]
    # display the square
    for _ in range(size):
        print(char * size)
    print(len(char))

if __name__ == "__main__":
    main()