"""
Christian Thomas
Complete
This program writes a series of random numbers to a file. Each number is in the range of 1 through 500.
The application lets the user specify how many numbers to write to the file.
"""

import random

def main():
    # get number of random numbers to write
    while True:
        try:
            num = int(input("How many random numbers do you want to write to the file? "))
            if num <= 0:
                raise ValueError("The number must be greater than 0.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")
    # open file for writing
    try:
        with open("random_numbers.txt", "w") as infile:
            for _ in range(num):
                # generate random number
                rand_num = random.randint(1, 500)
                # write to file
                infile.write(f"{rand_num}\n")
        print(f"{num} random numbers have been written to 'random_numbers.txt'.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    main()