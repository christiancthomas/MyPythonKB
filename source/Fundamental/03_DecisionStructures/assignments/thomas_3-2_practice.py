"""
1. Write a program that asks the user for a number in the range of 1-7. The program
should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday,
3 = Wednesday, etc.
2. If the user enters anything except the numbers 1-7, an error message should be
displayed.
3. Write two programs: one that uses if-else-if logic and the second uses if-elif-else
4. Turn in your program to the practice assignment link in course content.
"""

def get_day_of_week_if_elif_else(number):
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

def get_day_of_week_if_else_if(number):
    if number < 1 or number > 7:
        return "Error: Please enter a number between 1 and 7."
    if number == 1:
        return "Monday"
    else:
        if number == 2:
            return "Tuesday"
        else:
            if number == 3:
                return "Wednesday"
            else:
                if number == 4:
                    return "Thursday"
                else:
                    if number == 5:
                        return "Friday"
                    else:
                        if number == 6:
                            return "Saturday"
                        else:
                            return "Sunday"

def main():
    day = int(input("Enter a number between 1 and 7: "))
    print(f"Using if-elif-else logic: {get_day_of_week_if_elif_else(day)}")
    print(f"Using if-else-if logic: {get_day_of_week_if_else_if(day)}")

if __name__ == "__main__":
    main()

