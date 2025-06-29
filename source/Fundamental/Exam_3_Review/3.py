"""
Create  a list called rand_list which consists of 20 random  numbers  between 0 thru 100.
"""
import random

rand_list = []
for _ in range(20):
    rand_list.append(random.randint(0,100))

print(rand_list)