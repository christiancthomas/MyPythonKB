## Chapter 4: Repetition Structures

So far, you've learned how to make programs take input, process it, display output, and make decisions. But what if you
need to perform an action multiple times? Typing out the same lines of code over and over is inefficient and prone to
errors. This is where **repetition structures**, or **loops**, come into play. Loops are fundamental to programming,
allowing you to automate repetitive tasks and process collections of data efficiently.

### 1\. The `while` Loop

**Loops** are control structures that allow a block of code to be executed repeatedly. They are crucial for tasks that
involve processing lists of items, waiting for user input, or running simulations.

The **`while` loop** repeatedly executes a block of code as long as a specified condition remains true. It's often used
when you don't know in advance how many times the loop needs to run.

```python
# Syntax of a while loop
# while condition:
#     # Code to be executed repeatedly as long as condition is true
#     # (Remember to update something related to the condition inside the loop!)

count = 1
while count <= 5:
    print(f"Count is: {count}")
    count = count + 1  # Increment count to eventually make the condition false

print("Loop finished!")
```

In this example, the `print` statement and the `count = count + 1` line will execute as long as `count` is less than or
equal to 5. Once `count` becomes 6, the condition `count <= 5` becomes `False`, and the loop terminates.

### 2\. The `for` Loop

The **`for` loop** is used to iterate over a sequence (like a list, tuple, string, or range) or other iterable objects.
It's ideal when you know in advance how many times you want to iterate or when you need to process each item in a
collection.

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for char in "Python":
    print(char)
```

The `range()` function is commonly used with `for` loops to generate a sequence of numbers:

* `range(stop)`: Generates numbers from 0 up to (but not including) `stop`.
  ```python
  for i in range(5): # Generates 0, 1, 2, 3, 4
      print(i)
  ```
* `range(start, stop)`: Generates numbers from `start` up to (but not including) `stop`.
  ```python
  for i in range(1, 6): # Generates 1, 2, 3, 4, 5
      print(i)
  ```
* `range(start, stop, step)`: Generates numbers from `start` up to (but not including) `stop`, incrementing by `step`
  each time.
  ```python
  for i in range(2, 11, 2): # Generates 2, 4, 6, 8, 10
      print(i)
  ```

### 3\. Nested Loops

Just like `if` statements, loops can be **nested** inside other loops. This means an inner loop completes all its
iterations for each single iteration of the outer loop. Nested loops are useful for tasks like processing
two-dimensional data (e.g., rows and columns in a grid), generating patterns, or comparing all pairs of items in a
collection.

```python
# Printing a multiplication table excerpt
for i in range(1, 4):  # Outer loop for rows
    for j in range(1, 4):  # Inner loop for columns
        print(f"{i} * {j} = {i * j}", end="\t")  # \t adds a tab space
    print()  # Move to the next line after each row
```

The output of the above would look like:

```
1 * 1 = 1    1 * 2 = 2    1 * 3 = 3
2 * 1 = 2    2 * 2 = 4    2 * 3 = 6
3 * 1 = 3    3 * 2 = 6    3 * 3 = 9
```

### 4\. Loop Control Statements

Sometimes, you need more precise control over how a loop executes. Python provides special statements for this:

* **`break`**: This statement immediately terminates the current loop and transfers control to the statement immediately
  following the loop. It's often used when a certain condition is met and no further iterations are needed.

```python
for number in range(1, 10):
    if number == 5:
        print("Found 5, breaking loop.")
        break  # Exit the loop immediately
    print(number)
print("Loop finished by break or completion.")
```

* **`continue`**: This statement immediately skips the rest of the current iteration of the loop and proceeds to the
  next iteration. It's useful when you want to skip processing for a particular case but continue with the rest of the
  loop.

  ```python
  for i in range(1, 6):
      if i == 3:
          print("Skipping 3...")
          continue # Skip the rest of this iteration
      print(i)
  ```

**Understanding infinite loops and how to avoid them**: An **infinite loop** is a loop that never terminates because its
controlling condition never becomes false. This can cause your program to freeze or consume excessive resources.

```python
# Example of an infinite loop (DO NOT RUN THIS IN PRODUCTION!)
# while True:
#     print("This will print forever!")

# How to avoid them:
# 1. Ensure the loop condition will eventually become False.
# 2. For while loops, make sure a variable in the condition is modified within the loop.
# 3. For user input loops, ensure there's a way to break out (e.g., specific input).
```

### 5\. Calculating Running Totals

Loops are excellent for performing calculations that accumulate values over multiple iterations, such as summing numbers
or counting occurrences.

A **running total** (or accumulator) is a variable that is initialized to zero before a loop and then has numbers added
to it during each iteration of the loop.

```python
# Calculating the sum of numbers from 1 to 10
total_sum = 0  # Initialize the accumulator
for num in range(1, 11):
    total_sum = total_sum + num  # Add each number to the total
print(f"The sum of numbers from 1 to 10 is: {total_sum}")

# Implementing counters in loops
# Counting even numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0  # Initialize the counter
for number in numbers:
    if number % 2 == 0:  # Check if the number is even
        even_count = even_count + 1  # Increment the counter
print(f"There are {even_count} even numbers in the list.")
```