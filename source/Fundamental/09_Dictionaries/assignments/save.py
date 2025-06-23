"""
Saves a pickled version of the roster.
"""

import pickle

def save(roster):
    try:
        with open("roster.pkl", "wb") as outfile:
            pickle.dump(roster, outfile)
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("IOError occurred")