"""
This module calculates the total and average cost of a hamburger, fries, and shake.
"""
# comment
# create function
# concept of input, output, processing
# math operations
# return statements
# recognize the main function
# variables (important)
# float: convert a string to float
# input: get input from user
# understand assignment
# understand how to call a function
# print
# fstring

def calculate_costs(hamburger, fries, shake):
    """
    Calculate the total and average cost of a hamburger, fries, and shake.

    :param hamburger: Cost of the hamburger
    :param fries: Cost of the fries
    :param shake: Cost of the shake
    :return: A tuple containing the total cost and the average cost
    """
    total = hamburger + fries + shake
    average = total / 3
    return total, average

if __name__ == "__main__":
    # Input statements to get the costs of the items
    hamburger_cost = float(input("Enter the cost of the hamburger: "))
    fries_cost = float(input("Enter the cost of the fries: "))
    shake_cost = float(input("Enter the cost of the shake: "))

    # Calculate the total and average cost
    total_cost, average_cost = calculate_costs(hamburger_cost, fries_cost, shake_cost)
    print("I am going to do the fstring {}")
    print(f"The cost is: ${total_cost}")
    print(f"The average cost is: ${average_cost}")