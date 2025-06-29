"""
Write code that retrieves and unpickles the dictionary that you pickled 
in the previous problem.
"""

import pickle

dct = {
    "a": 1,
    "b": 2,
    "c": 3
    }

with open("mydata.dat", "wb") as f:
    pickle.dump(dct, f)

# Unpickling for question 20

with open("mydata.dat", "rb") as f:
    data = pickle.load(f)
