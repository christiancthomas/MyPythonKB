## Chapter 3: Decision Structures and Boolean Logic

Programs are not just about performing calculations; they also need to make decisions. Imagine a program that gives a
discount only if a customer spends over a certain amount, or a game that responds differently based on user input. This
chapter will introduce you to the fundamental concepts of decision-making in Python, allowing your programs to behave
intelligently based on varying conditions.

### 1\. The `if` Statement

In programming, **decision-making** is the ability of a program to choose different paths of execution based on certain
conditions. The simplest form of a decision structure is the `if` statement.

The `if` statement allows a block of code to be executed *only if* a specified condition is true.

```python
# Syntax of an if statement
# if condition:
#     # Code to be executed if condition is true
#     # (Indented block)

age = 18
if age >= 18:
    print("You are eligible to vote.")
```

In this example, the `print()` statement will only execute because the condition `age >= 18` is `True`. If `age` were
`17`, the condition would be `False`, and the `print()` statement would be skipped.

### 2\. The `if-else` Statement

Often, you want your program to do one thing if a condition is true, and something *different* if the condition is
false. This is where the `if-else` statement comes in handy.

```python
# Syntax of an if-else statement
# if condition:
#     # Code for true condition
# else:
#     # Code for false condition

temperature = 28

if temperature > 30:
    print("It's a hot day!")
else:
    print("It's not too hot today.")

# Example with user input
score = int(input("Enter your test score: "))
if score >= 60:
    print("Congratulations! You passed.")
else:
    print("Keep practicing. You did not pass.")
```

Here, if `temperature` is greater than 30, the first `print()` executes. Otherwise (if `temperature` is 30 or less), the
`print()` statement in the `else` block executes.

### 3\. Nested Decision Structures

You can place `if` or `if-else` statements inside other `if` or `else` blocks. This is called **nesting**, and it allows
for more complex decision-making scenarios where a decision depends on a previous decision.

```python
# Example of a nested if-else structure
is_logged_in = True
has_admin_rights = False

if is_logged_in:
    print("Welcome, user!")
    if has_admin_rights:
        print("You have administrator access.")
    else:
        print("You have regular user access.")
else:
    print("Please log in to access the system.")
```

**The importance of indentation in Python**: Python uses **indentation** (whitespace at the beginning of a line) to
define code blocks. Unlike many other languages that use curly braces `{}` or keywords like `END IF`, Python relies on
consistent indentation. A standard indentation is four spaces. Incorrect indentation will lead to syntax errors.

```python
# Correct indentation
if True:
    print("This line is part of the if block.")
    print("So is this one.")
else:
    print("This is part of the else block.")

# Incorrect indentation (will cause an error)
# if True:
# print("This line is not indented correctly.")
```

### 4\. The `if-elif-else` Statement

When you have more than two possible outcomes or multiple conditions to check sequentially, `if-elif-else` provides a
cleaner and more efficient solution than multiple nested `if-else` statements. `elif` is short for "else if".

The program checks conditions in order from top to bottom. As soon as a condition evaluates to `True`, its corresponding
block of code is executed, and the rest of the `elif` and `else` blocks are skipped. If none of the `if` or `elif`
conditions are true, the `else` block (if present) is executed.

```python
# Grading example using if-elif-else
grade = int(input("Enter your numerical grade: "))

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

This structure is much more readable and maintainable than deeply nested `if-else` statements for this kind of scenario.

### 5\. Boolean Expressions and Logical Operators

Conditions in `if`, `elif`, and `else` statements are evaluated as **Boolean expressions**. A Boolean expression is an
expression that evaluates to either `True` or `False`. These are the two fundamental Boolean values.

```python
is_raining = True  # Boolean variable
is_sunny = False  # Another Boolean variable

print(is_raining)  # Output: True
print(5 > 3)  # Output: True
print(10 == 20)  # Output: False
```

You can combine multiple Boolean expressions using **logical operators**:

* **`and`**: Returns `True` if *both* operands are `True`. Otherwise, returns `False`.
  ```python
  age = 20
  has_ticket = True
  if age >= 18 and has_ticket:
      print("You can enter the concert.")
  ```
* **`or`**: Returns `True` if *at least one* of the operands is `True`. Returns `False` only if both are `False`.
  ```python
  is_weekend = False
  is_holiday = True
  if is_weekend or is_holiday:
      print("Enjoy your day off!")
  ```
* **`not`**: Reverses the Boolean value of its operand. If an expression is `True`, `not` makes it `False`, and
  vice-versa.
  ```python
  is_locked = False
  if not is_locked:
      print("The door is unlocked.")
  ```

### 6\. Comparison Operators

Boolean expressions are often formed using **comparison operators** (also known as relational operators), which compare
two values and return a `True` or `False` result.

* `==` (Equal to)
    * `x == y` is `True` if `x` has the same value as `y`.
* `!=` (Not equal to)
    * `x != y` is `True` if `x` does not have the same value as `y`.
* `>` (Greater than)
    * `x > y` is `True` if `x` is greater than `y`.
* `<` (Less than)
    * `x < y` is `True` if `x` is less than `y`.
* `>=` (Greater than or equal to)
    * `x >= y` is `True` if `x` is greater than or equal to `y`.
* `<=` (Less than or equal to)
    * `x <= y` is `True` if `x` is less than or equal to `y`.

<!-- end list -->

```python
num1 = 10
num2 = 20
string1 = "apple"
string2 = "banana"

print(num1 == num2)  # False
print(num1 != num2)  # True
print(num1 < num2)  # True
print(string1 > string2)  # False (lexicographical comparison)
print(num1 <= 10)  # True
```