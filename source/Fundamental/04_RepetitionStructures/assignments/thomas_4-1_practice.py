"""
1. Add logic to the if-elif-else program to use a loop to keep asking the user the day of the week until they wish to stop.
In a second program, write a while loop that asks the user to enter 2 numbers. The numbers should be added and the sum displayed.
The loop should ask the user if they want to continue, if so, the loop should repeat, otherwise, the program should end.
"""

def get_day_of_week_if_elif_else_loop(number):
    if number == 1:
        return "Monday"
    elif number == 2:
        return "Tuesday"
    elif number == 3:
        return "Wednesday"
    elif number == 4:
        return "Thursday"
    elif number == 5:
        return "Friday"
    elif number == 6:
        return "Saturday"
    elif number == 7:
        return "Sunday"
    else:
        return "Error: Please enter a number between 1 and 7."

def num_sum_loop():
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        total = num1 + num2
        print(f"The sum of {num1} and {num2} is: {total}")

def main():
    ans = 'yes'
    while ans in ['yes', 'y']:
        try:
            day = int(input("Enter a number between 1 and 7: "))
            if day < 1 or day > 7:
                raise ValueError("Number must be between 1 and 7.")
            print(f"Using if-elif-else logic: {get_day_of_week_if_elif_else_loop(day)}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        ans = input("Do you want to continue? (yes/no): ").strip().lower()
        if ans not in ['yes', 'y', 'no', 'n']:
            print("Invalid response. Exiting the program.")
            break
    ans = 'yes'
    while ans in ['yes', 'y']:
        num_sum_loop()
        ans = input("Do you want to continue with the sum program? (yes/no): ").strip().lower()
        if ans not in ['yes', 'y', 'no', 'n']:
            print("Invalid response. Exiting the program.")
            break

if __name__ == "__main__":
    main()
