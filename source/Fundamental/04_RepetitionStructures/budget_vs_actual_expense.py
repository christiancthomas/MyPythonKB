"""
LAB 4:

Budgeted vs. Actual Expenses - Pseudocode

START Program

    // Declare Variables
    DECLARE budget AS REAL
    DECLARE total_spent AS REAL = 0.0
    DECLARE expense AS REAL

    // Input: Get Budget Amount
    PROMPT "Enter amount budgeted for the month: "
    GET budget

    // Process: Loop to get expenses and calculate total spent
    LOOP
        PROMPT "Enter an amount spent (0 to quit): "
        GET expense

        IF expense IS LESS THAN 0 THEN
            DISPLAY "Expense cannot be negative. Please enter a valid amount."
            CONTINUE LOOP // Go to the next iteration
        END IF

        IF expense IS EQUAL TO 0 THEN
            BREAK LOOP // Exit the loop
        END IF

        ADD expense TO total_spent
    END LOOP

    // Output: Display results
    DISPLAY "Budgeted: $" FORMATTED TO 2 DECIMAL PLACES (budget)
    DISPLAY "Spent: $" FORMATTED TO 2 DECIMAL PLACES (total_spent)

    IF total_spent IS GREATER THAN budget THEN
        DECLARE over_budget AS REAL = total_spent - budget
        DISPLAY "You are $" FORMATTED TO 2 DECIMAL PLACES (over_budget) " over budget. PLAN BETTER NEXT TIME!"
    ELSE IF total_spent IS LESS THAN budget THEN
        DECLARE under_budget AS REAL = budget - total_spent
        DISPLAY "You are $" FORMATTED TO 2 DECIMAL PLACES (under_budget) " under budget. Good job!"
    ELSE // total_spent IS EQUAL TO budget
        DISPLAY "You are exactly on budget."
    END IF

END Program

"""


# Name: Truc Huynh
# Program Status: Complete
# Description: This program calculates the difference between budgeted and actual expenses
#              for a month, indicating if the user is over or under budget.

def main():
    # Input
    budget = float(input("Enter amount budgeted for the month: "))

    total_spent = 0.0

    # Process
    while True:
        expense = float(input("Enter an amount spent(0 to quit): "))
        if expense == 0:
            break
        total_spent += expense

    # Output
    print(f"\nBudgeted: $ {budget:,.2f}")
    print(f"Spent: $ {total_spent:,.2f}")

    if total_spent > budget:
        over_budget = total_spent - budget
        print(f"You are $ {over_budget:,.2f} over budget. PLAN BETTER NEXT TIME!")
    elif total_spent < budget:
        under_budget = budget - total_spent
        print(f"You are $ {under_budget:,.2f} under budget. Good job!")
    else:
        print("You are exactly on budget.")


if __name__ == "__main__":
    main()
