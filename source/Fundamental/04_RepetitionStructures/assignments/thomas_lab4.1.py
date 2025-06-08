"""
Christian Thomas
Complete
This program asks the user to enter their monthly budget. Then, it asks the user to enter
expenses and keep a running total. When the user cancels the loop (by entering 0), the program will
displa the budget, total spent, and how much they're over or under budget.
"""

def main():
    try:
        budget = float(input("Enter your monthly budget: $"))
        if budget < 0:
            raise ValueError("Budget cannot be negative.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    total_expenses = 0.0
    while True:
        try:
            expense = float(input("Enter an expense amount (or 0 to finish): $"))
            if expense < 0:
                raise ValueError("Expense cannot be negative.")
            if expense == 0:
                break
            total_expenses += expense
        except ValueError as e:
            print(f"Invalid input: {e}")
    print(f"Monthly budget: ${budget:,.2f}")
    print(f"Total expenses: ${total_expenses:,.2f}")
    if total_expenses > budget:
        print(f"You are over budget by ${total_expenses - budget:,.2f}. YIKES 😬")
    elif total_expenses < budget:
        print(f"You are under budget by ${budget - total_expenses:,.2f}. Nice job! 👍")
    else:
        print("You are exactly on budget. Great job!")
if __name__ == "__main__":
    main()
