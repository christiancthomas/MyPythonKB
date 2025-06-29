"""
Given the  following list, for each of the  following, determine  the  
contents  of the  list at  the end of the code fragment.

num_list = [0] * 8

for i in range(len(num_list)):
num_list[i] = i
  for i in range(len(num_list)):
num_list[i] = num_list[i] // 3
"""

# first loop
num_list = [0, 1, 2, 3, 4, 5, 6, 7]

# second loop
num_list = [0, 0, 0, 1, 1, 1, 2, 2]