"""
Look at the following statement:
mystring = ‘cookies>milk>fudge>cake>ice cream’
Write a statement that splits this string, creating the following list:
[‘cookies’, ’milk’, ’fudge’, ‘cake’, ‘ice cream’]
"""

mystring = "cookies>milk>fudge>cake>ice cream"
new_string = mystring.split(">")
print(new_string)