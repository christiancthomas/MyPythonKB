"""
7. For each string testing or modification method, fill out what it does

List Method       |   What does it do? Return?
_____________________________________________________
append(item)                Appends item to the end of a list
index (item)                Gives the index position of the  item in list
insert (index, item)        Inserts item at index position in list
sort ()                     Sorts the list in ascending order
remove (item)               Removes item from list
reverse()                   Reverses the order of the list
List Built In Functions  |  What does it do?
_____________________________________________________
del                         Deletes a specific element or slice from the list.
min                         Gets min value from list
max                         Gets max value from list
len                         Gets length of list
String Testing Method       |   What does it do? Return?
_____________________________________________________
isalnum()                       True if the string is made of alphabetic characters or numeric values, otherwise False
isalpha()                       True if the string is made of alphabetic characters, otherwise False
isdigit()                       True if the entire string is made of numbers, otherwise False
islower()                       True if the string is all lowercase, otherwise False
isupper()                       True if the string is all uppercase, otherwise False
isspace()                       True if the all characters in string are whitespace, otherwise False
String Modification         |   What does it do? Return?
____________________________________________________
lower()                       Turns the string to all lowercase
lstrip()                       Strips leading whitespace from string
lstrip(char)                       Strips leading "char" characters from string
rstrip()                       Strips trailing whitespace from string
rstrip(char)                       Strips trailing "char" characters from string
strip()                       Strips all leading and trailing whitespace from string
strip(char)                       Strips all "char" characters from string
upper()                       Turns the string to all uppercase
String Search and Replace   |   What does it do? Return?
____________________________________________________
endswith(substring)             True if the string ends with substring value
find(substring)                 Returns index location of substring value in the string
replace(old,new)                Replaces old value with new value in string 
startswith(substring)           True if the string starts with substring value
split(separator)                Splits the string into one or more substrings based on instances of separator value
len()                           Returns integer value indicating the length of the string

"""

"""
8. Write  a program  that uses a two-dimensional list that has 4 rows, 
with 5 columns in each row.  The program  should do the following things:
1.  Create  or fill in the list so that it has random  numbers  between  0 and 50.
2.  Print the entire  list using a loop.
"""
import random
rows, col = 4, 5
matrix = []
for i in range(rows):
    row = []
    for j in range(col):
        row.append(random.randint(0, 50))
    matrix.append(row)

for row in matrix:
    print(row)

