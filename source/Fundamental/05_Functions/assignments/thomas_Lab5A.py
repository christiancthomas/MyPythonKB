"""
Christian Thomas
Complete

This program calculates the average restaurant rating and number of stars.
main accepts 5 numeric ratings from the user, using a loop. It then calculates the average score
for that restaurant.

Uses determine_stars to calculate the number of stars based on the average rating:
- Greater than 9.0: 5 stars
- Between 8.0 and 9.0: 4 stars
- Between 7.0 and 8.0: 3 stars
- Between 6.0 and 7.0: 2 stars
- Between 5.0 and 6.0: 1 star
- Less than 5.0: 0 stars
"""

def main():
    """
    Main function to calculate average restaurant rating and number of stars.
    It prompts the user for 5 ratings, calculates the average, and determines the number of stars.
    """
    total = 0
    count = 0

    for i in range(5):
        try:
            rating = float(input(f"Enter critic {i + 1}'s score (0-10): "))
            if 0 <= rating <= 10:
                total += rating
                count += 1
            else:
                print("Rating must be between 0 and 10. Please try again.")
                i -= 1  # Decrement to repeat this iteration
        except ValueError:
            print("Invalid input. Please enter a numeric value between 0 and 10.")
            i -= 1

    average = total / count
    stars = determine_stars(average)
    print(f"The average rating is: {average:.2f}")
    print(f"Your average of {average:.2f} gives you", "⭐️" * stars)

def determine_stars(average):
    """
    Determines the number of stars based on average rating.
    """
    if average > 9.0:
        return 5
    elif average >= 8.0:
        return 4
    elif average >= 7.0:
        return 3
    elif average >= 6.0:
        return 2
    elif average >= 5.0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()
