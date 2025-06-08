"""
Instructions

1. Accept input of monthly gross income from the user.
2. Accept input of monthly paycheck deductions (one number) from the user.
3. Calculate net monthly income.
4. Display the monthly net income with an appropriate label (Ex. Monthly net
income is: ) followed by the result formatted in to 2 decimal places preceded
by a dollar sign and comma separators ($nn,nnn.nn). Don’t forget to
suppress the extra spaces.
5. Calculate yearly gross pay and display with appropriate label and formatting.
6. Calculate yearly net pay and display with appropriate label and formatting.
7. Run your program and make any corrections. Turn in your program and IPO
chart to the practice assignment link in course content.
"""


gross_income = float(input("Enter your monthly gross income: "))
deductions = float(input("Enter your monthly paycheck deductions: "))
net_income = gross_income - deductions
print(f"Monthly net income is: ${net_income:,.2f}")
yearly_gross_pay = gross_income * 12
print(f"Yearly gross pay is: ${yearly_gross_pay:,.2f}")
yearly_net_pay = net_income * 12
print(f"Yearly net pay is: ${yearly_net_pay:,.2f}")