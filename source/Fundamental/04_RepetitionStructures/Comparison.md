When it comes to repetitive tasks in Python, you have three primary tools at your disposal: **`while` loops**, **`for`
loops**, and **recursion**. While they can sometimes be used interchangeably, each has its own distinct advantages and
is best suited for different scenarios.

A **`for` loop** is the most common choice for iterating over a sequence of items. If you have a list, string, or any
other iterable object and you want to do something for each element in it, a `for` loop is generally the most
straightforward and readable option.

A **`while` loop**, on the other hand, is ideal when you need to repeat a block of code as long as a certain condition
is true. The number of iterations doesn't have to be known beforehand. Think of it as a loop that continues until a
specific goal is met.

**Recursion** is a more advanced concept where a function calls itself. It's particularly elegant for problems that can
be broken down into smaller, self-similar sub-problems. A classic example is calculating factorials or traversing
complex data structures like trees.

---

## At a Glance: `for` vs. `while` vs. Recursion

| Feature                | `for` Loop                                                          | `while` Loop                                                   | Recursion                                                             |
|------------------------|---------------------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------------|
| **Best For**           | Iterating over a known sequence (lists, strings, etc.)              | Looping as long as a condition is true                         | Problems that can be broken into smaller, identical sub-problems      |
| **Structure**          | `for item in iterable:`                                             | `while condition:`                                             | `def func(): ... func()`                                              |
| **Readability**        | Generally very high for sequences                                   | Can be less clear if the condition is complex                  | Can be very elegant for the right problem, but complex for others     |
| **Potential Pitfalls** | Modifying the list while iterating can lead to unexpected behavior. | Risk of an infinite loop if the condition never becomes false. | Exceeding the maximum recursion depth, leading to a `RecursionError`. |

---

## `for` Loops: The Go-To for Sequences

The `for` loop in Python is designed for definite iteration, meaning you iterate over a collection of items until you've
gone through every one.

**When to use it:**

* When you have a list, tuple, dictionary, set, or string and you want to process each element.
* When you need to execute a block of code a specific number of times using `range()`.

**Example:**

```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping a specific number of times
for i in range(3):
    print("Hello!")
```

---

## `while` Loops: For Conditional Repetition

A `while` loop is used for indefinite iteration, where the loop continues as long as a specified condition holds true.

**When to use it:**

* When the number of iterations is not known in advance.
* For tasks that need to run until a certain event occurs (e.g., user input, reaching a specific value).
* Implementing simple game loops.

**Example:**

```python
# Waiting for a condition to change
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
```

---

## Recursion: Solving Problems by Self-Reference

Recursion is a programming technique where a function calls itself to solve a problem. Each recursive call solves a
smaller instance of the same problem until it reaches a "base case," which is a condition that stops the recursion.

**When to use it:**

* For problems that have a naturally recursive structure, like tree traversals (e.g., navigating a file system) or
  mathematical concepts like factorials and the Fibonacci sequence.
* When it leads to a significantly simpler and more elegant solution compared to an iterative approach.

**Key considerations:**

* **Base Case:** A recursive function **must** have a base case to prevent it from calling itself infinitely.
* **Recursion Depth:** Python has a default limit on the number of recursive calls (typically around 1000) to prevent
  stack overflow errors. For very deep recursion, an iterative approach is often better.

**Example:**

```python
# Calculating a factorial using recursion
def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive step
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120
```

### Performance and Memory

In terms of performance, `for` and `while` loops are generally more efficient in Python than recursion. Each recursive
function call adds a new frame to the call stack, which consumes memory and can be slower. Python does not have
tail-call optimization, a feature in some other languages that can make certain recursive calls as efficient as loops.
Therefore, for performance-critical tasks that can be easily implemented with a loop, iteration is usually the better
choice.