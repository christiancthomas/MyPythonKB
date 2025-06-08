"""
Christian Thomas
Complete

This program should ask the user to enter the number of software packages purchased. Then, it should display the dollar amount of the discount (if any)
and the total amount of the purchase after the discount.
"""

def calculate_discount(num_licenses):
    """Calculate the discount based on the number of licenses purchased."""
    if num_licenses < 0:
        raise ValueError("Number of licenses cannot be negative.")

    base_cost = 149.00
    if num_licenses < 10:
        disc = base_cost * 0
    elif num_licenses < 50:
        disc = base_cost * 0.1
    elif num_licenses < 100:
        disc = base_cost * 0.2
    elif num_licenses < 150:
        disc = base_cost * 0.3
    else:
        disc = base_cost * 0.4
    return disc

def calculate_total(disc, num_licenses):
    """Calculate the total cost after applying the discount."""
    if num_licenses < 0:
        raise ValueError("Number of licenses cannot be negative.")
    if disc < 0:
        raise ValueError("Discount cannot be negative.")
    base_cost = 149.00
    total_cost = (base_cost - disc) * num_licenses
    return total_cost

def main():
    try:
        num_licenses = int(input("Enter the number of software packages purchased: "))
        if num_licenses < 0:
            raise ValueError("Number of licenses cannot be negative.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    else:
        discount = calculate_discount(num_licenses)
        total_cost = calculate_total(discount, num_licenses)

        print(f"Discount amount: ${discount:,.2f}")
        print(f"Total cost after discount applied: ${total_cost:,.2f}")

if __name__ == "__main__":
    main()