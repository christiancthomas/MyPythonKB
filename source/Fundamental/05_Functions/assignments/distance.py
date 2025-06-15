"""
Christian Thomas
Complete
This program calculates the distance an object falls under the influence of gravity.
"""

GRAVITY = 9.8  # Acceleration due to gravity in m/s^2

def falling_distance(time):
    """
    Calculate the distance an object falls under the influence of gravity.
    """

    distance = 0.5 * GRAVITY * time ** 2
    return distance

