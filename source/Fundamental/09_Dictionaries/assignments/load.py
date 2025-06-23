"""
Loads the roster into the program.
"""

import pickle

def load(filename):
    try:
        with open(filename, "rb") as infile:
            roster = pickle.load(infile)
            return roster
    except FileNotFoundError:
        print("File not found - returning empty roster.")
        return {}
    except IOError:
        print("IOError occurred - returning empty roster.")
        return {}
    except pickle.UnpicklingError:
        print("Error unpickling file - returning empty roster.")
        return {}
