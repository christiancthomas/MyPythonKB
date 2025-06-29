"""
Write a loop that counts and displays the number of lowercase letters 
that appear in the string my_string. 
"""

my_string = "Example string"
sum = 0
for i in my_string:
    if i.islower():
        sum += 1

print(f"Number of lowercase letters in {my_string}: {sum}")