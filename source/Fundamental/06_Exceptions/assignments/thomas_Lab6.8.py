"""
Christian Thomas
Complete
This program reads the numbers from random_numbers.txt and performs the following operations:
1. Calculates the sum of the numbers contained in the file.
2. Calculates the number of random values in the file.
"""

def main():
    # Read file
    try:
        with open("random_numbers.txt", "r") as infile:
            total = 0
            count = 0

            for line in infile:
                try:
                    total += int(line.rstrip())
                    count += 1
                except ValueError:
                    print(f"invalid value: {line.rstrip()}")

            print(f"Sum of numbers in file:\t{total}")
            print(f"Count of numbers in file:\t{count}")
    # file read errors
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
    except FileNotFoundError:
        print("random_numbers.txt can't be found in the directory.")

if __name__ == "__main__":
    main()
