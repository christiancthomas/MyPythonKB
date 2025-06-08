"""
Practice Assignment 2-1 & 2-2
Ask user to enter the costs for the following items: Hamburger, Fries,
Shake.
3. Calculate the total cost and display with appropriate message (Example: The cost is: $45)
4. Calculate the average cost and display with appropriate message (Example: The average cost is: $15)
5. Note: Don’t worry about displaying cents to 2 decimals.
6. Turn in your program to the practice assignment link in course content.
"""

def meal_cost():
    hamburger_cost = float(input('What is the cost of the hamburger? '))
    fries_cost = float(input('What is the cost of the fries? '))
    shake_cost = float(input('What is the cost of the shake? '))

    total_cost = hamburger_cost + fries_cost + shake_cost
    average_cost = total_cost / 3

    print(f'The cost is: ${total_cost}')
    print(f'The average cost is: ${average_cost}')

if __name__ == '__main__':
    meal_cost()