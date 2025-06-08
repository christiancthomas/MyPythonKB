"""
Christian Thomas
Complete
This application assumes the ocean’s level is currently rising at about 1.8 millimeters per year and
displays the number of millimeters that the ocean will have risen each year for the next 25 years in tabular format.
years
"""

def main():
    RISING_RATE = 1.8  # in millimeters per year
    print("Year\tRise (in millimeters)")
    print("─" * 30)
    for year in range(1, 26):
        millimeters = RISING_RATE * year
        print(f"{year}\t{millimeters:.2f}")
        year += 1

if __name__ == "__main__":
    main()