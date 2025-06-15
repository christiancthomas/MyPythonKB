"""
"""

import distance as d

def main():
    """
    Main function to calculate and display the distance an object falls under the influence of gravity.
    It calculates the distance for each second from 1 to 10 seconds.
    main prints the time in seconds and the corresponding distance in meters.
    """

    for i in range(1, 11):
        time = i
        dist = d.falling_distance(time)
        print(f"{time} seconds: \t{dist:,.2f} m")

if __name__ == "__main__":
    main()