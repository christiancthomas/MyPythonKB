"""
In Python, write a program to generate a random floating point number between 1
and 100 which will be used as the radius of a circle.

In a separate function, calculate the area of a circle based on the radius
your program just generated and return it to the main function.

In the main function, display the radius and the area.
"""

import random
import math

def rand_radius():
    return random.uniform(1, 100)

def calc_area(radius):
    return math.pi * (radius ** 2)

def main():
    radius = rand_radius()
    area = calc_area(radius)
    print(f"math.pi: {math.pi}")
    print(f"Radius: {radius:,.2f}")
    print(f"Area: {area:,.2f}")

if __name__ == "__main__":
    main()