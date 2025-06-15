"""
This program asks the user to enter a distance in kilometers and converts it to miles.
The conversion factor is 1 kilometer = 0.6214 miles.
"""

CONVERSION_FACTOR = 0.6214

def convert_km_to_mi(km):
    return km * CONVERSION_FACTOR

def main():
    km = float(input("Enter distance in kilometers: "))
    miles = convert_km_to_mi(km)
    print(f"{km} kilometers is equal to {miles:,.2f} miles.")

if __name__ == "__main__":
    main()