"""
4-2: write a program that asks the user to enter two numbers, a low and high number.
1. in the first loop, the low number will be the starting point for the loop and the
high will be the ending point. The loop should display the iterator number and
that number x 10 on the same line, separated by a tab. See example on p. 177.
2. The second loop should accumulate all the numbers between the starting point
and ending point. You will need to create and initialize an accumulator such as
total before you start the loop.
"""

def main():
    # First loop: Display numbers and their multiples of 10
    low = int(input("Low number: "))
    high = int(input("High number: "))
    print("Number\tTimes 10")
    for i in range(low, high + 1):
        print(f"{i}\t{i * 10}")

    # Second loop: Accumulate numbers between low and high
    total = 0
    for i in range(low, high + 1):
        total += i
    print(f"Total of numbers between {low} and {high}: {total:,.0f}")

if __name__ == "__main__":
    main()