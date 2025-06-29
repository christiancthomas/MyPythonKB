"""
Assume the variable dct references a dictionary.  Write code that pickles the 
dictionary and saves it to a file named mydata.dat
"""
import pickle

dct = {
    "a": 1,
    "b": 2,
    "c": 3
    }

with open("mydata.dat", "wb") as f:
    pickle.dump(dct, f)