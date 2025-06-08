# ch. 3-1: designa a program that asks the user to enter a month (in numeric form), a day, and two-digit year.
# the program should check if the month times the day equals the year. If so, it should display a message saying the date is magic.
# Otherwise, it should display a message saying the date isn't magic.

def main():
    month = input("Enter a numeric month: ")
    day = input("Enter a day: ")
    year = input("Enter a 2-digit year: ")

    try:
        month = int(month)
        day = int(day)
        year = int(year)
    except:
        print("Invalid input. Please enter numeric values.")
        return

    # validate input
    if month < 1 or month > 12:
        print("Invalid month. Please enter a value between 1 and 12.")
        return
    if day < 1 or day > 31:
        print("Invalid day. Please enter a value between 1 and 31.")
        return
    if year < 0 or year > 99:
        print("Invalid year. Please enter a 2-digit year.")
        return

    # check if magic date
    if month * day == year:
        print("The date is ✨magic✨")
    else:
        print("The date isn't magic ❌")

if __name__ == "__main__":
    main()