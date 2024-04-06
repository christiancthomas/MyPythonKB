"""
This module calculates the total and average income based on monthly gross income and deductions.
"""


def calculate_net_monthly_income(gross_income, deductions):
    """
   Calculate the net monthly income.

   :param gross_income: Monthly gross income
   :param deductions: Monthly paycheck deductions
   :return: Net monthly income
   """
    return gross_income - deductions


def calculate_yearly_income(monthly_income):
    """
    Calculate the yearly income based on monthly income.

    :param monthly_income: Monthly income
    :return: Yearly income
    """
    return monthly_income * 12


def main():
    """
    Main function to accept inputs, calculate and display income details.
    """
    # Step 1: Accept input of monthly gross income
    monthly_gross_income = float(input("Enter your monthly gross income: "))

    # Step 2: Accept input of monthly paycheck deductions
    monthly_deductions = float(input("Enter your monthly paycheck deductions: "))

    # Step 3: Calculate net monthly income
    net_monthly_income = calculate_net_monthly_income(monthly_gross_income, monthly_deductions)

    # Step 4: Display net monthly income with appropriate formatting
    print(f"Monthly net income is: ${net_monthly_income:,.2f}")

    # Step 5: Calculate yearly gross pay
    yearly_gross_income = calculate_yearly_income(monthly_gross_income)

    # Step 6: Calculate yearly net pay
    yearly_net_income = calculate_yearly_income(net_monthly_income)

    # Step 7: Display yearly gross pay with appropriate formatting
    print(f"Yearly gross income is: ${yearly_gross_income:,.2f}")

    # Step 8: Display yearly net pay with appropriate formatting
    print(f"Yearly net income is: ${yearly_net_income:,.2f}")


if __name__ == "__main__":
    main()
