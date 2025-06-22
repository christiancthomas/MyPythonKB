"""
Christian Thomas
Complete
"""
def display_larger(my_list, n):
    """
    Accepts a list and integer value, n. This function compares all numbers in the list to value n, incrementally.
    If the value is greater than n, it will be stored in a second list containing only the numbers that are greater than n.

    This function prints the original list, n, and list of numbers greater than n.
    """
    big_list = [val for val in my_list if val > n]
    print(f"Original List: {my_list}\nComparative Value: {n}\nList of values larger than {n}: {big_list}")

def main():
    """
    Handles the main loop of the program. Sets variables, and gathers input from user.
    """
    LIST_LENGTH = 10
    print(f"Enter a list of {LIST_LENGTH} numbers.")
    vals = [int(input(f"Enter list value {i + 1}: ")) for i in range(LIST_LENGTH)]
    num = int(input("Enter number to compare against list: "))

    display_larger(vals, num)

if __name__ == "__main__":
    main()