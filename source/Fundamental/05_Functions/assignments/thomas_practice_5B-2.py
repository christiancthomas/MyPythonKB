"""
This Program calculates the area of a square based on a randomly
generated integer to be used as the side length of the square.
"""

import random
import square as s

def side():
    return random.randint(1, 100)



def main():
    length = side()
    area = s.square_area(length)
    perimeter = s.square_perimeter(length)

    print(f"Side Length: {length}")
    print(f"Area: {area:,.0f}")
    print(f"Perimeter: {perimeter}")

    return side, area, perimeter

if __name__ == "__main__":
    main()