# Python Foundation Refresh — Part 1: Core Syntax

**Track:** AI/ML foundations  
**Level:** Beginner refresh  
**Topics:** Types and operators, conditions, loops, strings  
**Goal:** Write small Python programs independently and understand the code you read.

---

## How to use these notes

For each section:

1. Read the definition and syntax.
2. Type and run each example yourself.
3. Change the inputs and predict the output before running the code.
4. Complete the practice questions without copying a solution.
5. Mark a topic complete only when you can explain it and solve a similar problem independently.

You do not need to memorize every method. Learn the core patterns and know how to look up details when necessary.

---

# 1. Variables, Data Types, and Type Conversion

## 1.1 Variables

**Definition:** A variable is a name that refers to a value.

```python
age = 18
name = "Rahul"
height = 1.75
```

- `age` refers to the integer `18`.
- `name` refers to the string `"Rahul"`.
- `height` refers to the floating-point number `1.75`.

The `=` symbol assigns a value; it does not mean “is equal to” as it does in a mathematical equation.

### Naming rules

- Names may contain letters, digits, and underscores.
- A name cannot start with a digit.
- Names are case-sensitive: `score` and `Score` are different.
- Do not use Python keywords such as `if`, `for`, or `class` as variable names.
- Prefer descriptive names such as `total_marks` over vague names such as `x`, except for short mathematical examples.

```python
total_marks = 275
student_count = 5
```

## 1.2 Basic data types

A **data type** describes the kind of value a variable refers to and the operations that make sense for that value.

| Type | Meaning | Examples |
|---|---|---|
| `int` | Integer (whole number) | `7`, `-3`, `0` |
| `float` | Floating-point number | `3.14`, `-0.5` |
| `str` | Text | `"Python"`, `'AI'` |
| `bool` | Truth value | `True`, `False` |
| `NoneType` | Absence of a value | `None` |

```python
count = 10
price = 99.5
language = "Python"
is_ready = True
result = None

print(type(count))      # <class 'int'>
print(type(price))      # <class 'float'>
print(type(language))   # <class 'str'>
print(type(is_ready))   # <class 'bool'>
```

Use `type(value)` to inspect a value's type.

**Important:** `True` and `False` are capitalized in Python. `"True"` is a string, not a Boolean.

## 1.3 Input and output

`print()` displays information. `input()` reads text typed by the user.

```python
name = input("Enter your name: ")
print("Hello,", name)
```

**Key rule:** `input()` returns a string, even when the user enters digits.

```python
age = input("Enter your age: ")
print(type(age))  # str
```

Convert the input when you need a number:

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height in metres: "))
```

## 1.4 Type conversion

**Definition:** Type conversion changes a value from one type to another when the conversion is valid.

```python
int("25")       # 25
float("3.5")    # 3.5
str(42)         # "42"
float(7)        # 7.0
int(3.9)        # 3 (truncates the decimal part)
```

Invalid conversions raise an error:

```python
int("hello")    # ValueError
```

Do not assume that `int()` rounds a decimal: `int(3.9)` gives `3`, not `4`.

## 1.5 Comments

A comment starts with `#` and is ignored by Python when running the program.

```python
# Calculate the total cost
price = 50
quantity = 3
total = price * quantity
print(total)
```

Use comments to explain *why* a step is needed, not to repeat every obvious line.

### Quick practice — Section 1

1. Create variables for your name, age, and current study hours. Print each value and its type.
2. Ask the user for two numbers and print their sum. Ensure the inputs are converted to numbers.
3. What is the difference between `25`, `25.0`, and `"25"`?
4. Predict the result of `int(8.9)`, `float("4")`, and `str(12)`.
5. Why does `input("Number: ") + input("Number: ")` join the entered text instead of adding the numbers?

---

# 2. Operators

An **operator** performs an operation on one or more values.

## 2.1 Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor division | `5 // 2` | `2` |
| `%` | Remainder (modulo) | `5 % 2` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

`/` produces a floating-point result in Python 3. `//` rounds the quotient down toward negative infinity, which matters for negative numbers.

```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
print(2 ** 4)   # 16
print(-7 // 2)  # -4
```

**Common AI/ML use:** `%` can test whether a number is even; `**` can square a value; `/` is used for averages and ratios.

```python
number = 14
print(number % 2 == 0)  # True
```

## 2.2 Comparison operators

Comparisons evaluate to `True` or `False`.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

```python
marks = 82
print(marks >= 40)  # True
print(marks == 100) # False
print(marks != 0)   # True
```

**Do not confuse `=` and `==`:**

- `x = 5` assigns `5` to `x`.
- `x == 5` checks whether `x` equals `5`.

## 2.3 Logical operators

Logical operators combine or invert Boolean conditions.

| Operator | Meaning | Example |
|---|---|---|
| `and` | Both conditions must be true | `age >= 18 and age <= 60` |
| `or` | At least one condition must be true | `day == "Sat" or day == "Sun"` |
| `not` | Reverses a Boolean result | `not is_valid` |

```python
age = 20
has_id = True

print(age >= 18 and has_id)  # True
print(age < 18 or has_id)    # True
print(not has_id)            # False
```

Python also supports chained comparisons:

```python
marks = 75
print(0 <= marks <= 100)  # True
```

## 2.4 Assignment operators

Assignment operators update a variable.

```python
count = 10
count += 2   # same effect as count = count + 2
count -= 1
count *= 3
count /= 2
```

Other forms include `//=`, `%=`, and `**=`. Know that they exist; you do not need to memorize every form immediately.

## 2.5 Operator precedence

Precedence determines which operations happen first. Parentheses make the intended order clear.

```python
answer = 2 + 3 * 4       # 14
answer = (2 + 3) * 4     # 20
```

For everyday code, use parentheses when an expression might be unclear. This is safer than trying to memorize an extensive precedence table.

### Quick practice — Section 2

1. Predict: `17 // 5`, `17 % 5`, `2 ** 5`, and `17 / 5`.
2. Write an expression that checks whether `n` is odd.
3. Check whether a mark is between 0 and 100, inclusive.
4. Write a condition that is true if a person is at least 18 and has an ID.
5. Predict: `10 + 2 * 3 == 16`.
6. Explain the difference between `x = x + 1` and `x == x + 1`.

---

# 3. Conditional Statements

## 3.1 What is a condition?

A **condition** is an expression that evaluates to a truth value and lets a program choose which code to execute.

Conditional statements use `if`, `elif`, and `else`.

### Syntax

```python
if condition:
    # Runs if condition is true
elif another_condition:
    # Runs if the first condition is false
    # and this condition is true
else:
    # Runs if no earlier condition is true
```

Python uses indentation to define the block of code belonging to each branch. Use consistent four-space indentation.

## 3.2 `if`

Use `if` when code should run only if a condition is true.

```python
temperature = 30

if temperature > 25:
    print("It is warm.")
```

If the condition is false, the indented statement is skipped.

## 3.3 `if-else`

Use `else` to handle the alternative case.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## 3.4 `if-elif-else`

Use multiple branches when there are several mutually exclusive cases.

```python
marks = 76

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print(grade)
```

Conditions are tested from top to bottom. Once a matching branch runs, the remaining branches are skipped. Put the most restrictive/highest threshold first in a grading example like this.

## 3.5 Nested conditions

An `if` statement can appear inside another `if` statement. Use nesting only when the second decision depends on the first.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Too young")
```

The same decision can sometimes be written more simply with `and`. Choose the version that is easiest to read.

## 3.6 Truthy and falsy values

Python conditions can use values other than explicit `True` and `False`.

Common falsy values include:

- `False`
- `None`
- Numeric zero such as `0` and `0.0`
- Empty strings and collections, such as `""`, `[]`, `{}`, and `set()`

Most other values are truthy.

```python
name = ""

if name:
    print("Name supplied")
else:
    print("Name is empty")
```

This is useful for checking whether a string or collection is empty.

## 3.7 Common mistakes

**Mistake 1: Using `=` instead of `==` in a comparison**

```python
# Incorrect:
# if marks = 50:

# Correct:
if marks == 50:
    print("Exactly 50")
```

**Mistake 2: Incorrect indentation**

The body of a conditional must be indented.

**Mistake 3: Incorrect branch order**

If `marks >= 40` comes before `marks >= 90`, a mark of 95 will match the first condition and receive the wrong grade.

**Mistake 4: Forgetting boundary cases**

If a passing mark is 40, test values such as 39, 40, and 41.

### Practice — Section 3

Write each program yourself:

1. Determine whether a number is positive, negative, or zero.
2. Determine whether a number is even or odd.
3. Find the largest of three numbers.
4. Convert marks into grades using a grading scale you define. Handle values outside 0–100.
5. Check whether a year is a leap year. A year is a leap year if it is divisible by 400, or divisible by 4 but not by 100.
6. Calculate a simple ticket price based on age using thresholds you choose.
7. Ask for a username and print a message if it is empty.
8. For each program, test a normal case and at least one boundary or invalid case.

---

# 4. Loops

## 4.1 What is a loop?

A **loop** repeats a block of code. Loops are useful when processing many values, counting, accumulating totals, and iterating over datasets.

Python has two main loop statements:

- `for`: iterates over items in an iterable, such as a list, string, or range.
- `while`: repeats as long as its condition remains true.

## 4.2 The `for` loop

### Syntax

```python
for item in iterable:
    # Do something with item
```

Example:

```python
for name in ["Aman", "Riya", "Sam"]:
    print(name)
```

The loop runs once for each item in the list.

### Using `range()`

`range()` generates a sequence of integers, commonly for counting.

```python
range(stop)          # 0 through stop - 1
range(start, stop)   # start through stop - 1
range(start, stop, step)
```

Examples:

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

for i in range(10, 0, -2):
    print(i)  # 10, 8, 6, 4, 2
```

The `stop` value is excluded. This is a very common source of off-by-one errors.

### Accumulation

An accumulator stores a running result.

```python
total = 0

for number in [2, 4, 6]:
    total += number

print(total)  # 12
```

The variable `total` must be initialized before the loop.

### Counting with a loop

```python
count = 0

for number in [3, 8, 10, 5, 12]:
    if number > 7:
        count += 1

print(count)  # 3
```

## 4.3 The `while` loop

### Syntax

```python
while condition:
    # Repeated code
    # Update state so the condition can eventually become false
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

A `while` loop is useful when the number of repetitions depends on a condition rather than a known collection.

**Warning:** If the condition never becomes false, the loop can run indefinitely.

```python
# Do not run this example:
# while True:
#     print("This never ends unless interrupted")
```

Always identify what changes inside the loop and why it will eventually stop.

## 4.4 `break` and `continue`

- `break` immediately exits the nearest loop.
- `continue` skips the rest of the current iteration and moves to the next iteration.

```python
for number in range(1, 8):
    if number == 5:
        break
    print(number)  # 1, 2, 3, 4
```

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)  # 1, 2, 4, 5
```

Use these statements when they make the logic clearer. Avoid unnecessary control-flow tricks.

## 4.5 Nested loops

A **nested loop** is a loop inside another loop. For each iteration of the outer loop, the inner loop runs through its own iterations.

```python
for row in range(3):
    for column in range(2):
        print(row, column)
```

This prints six pairs because the outer loop runs three times and the inner loop runs twice each time.

Nested loops are useful for small patterns and comparing pairs of items. They can be expensive for large datasets, so do not use them automatically when a vectorized NumPy operation would be clearer or faster.

## 4.6 Common loop patterns

### Sum of values

```python
numbers = [1, 2, 3, 4]
total = 0

for number in numbers:
    total += number

print(total)  # 10
```

### Find a maximum

```python
numbers = [4, 9, 2, 7]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)  # 9
```

This version assumes the list is not empty.

### Search for an item

```python
numbers = [4, 9, 2, 7]
target = 2
found = False

for number in numbers:
    if number == target:
        found = True
        break

print(found)  # True
```

For ordinary Python lists, `target in numbers` is shorter. The loop version is useful for learning the search pattern.

## 4.7 Common loop mistakes

- Forgetting to update the `while` loop's counter.
- Expecting `range(1, 5)` to include 5.
- Initializing a sum or counter inside the loop when it should persist across iterations.
- Using the wrong indentation.
- Assuming a list has at least one element when reading `numbers[0]`.
- Changing a loop variable without understanding which iteration it affects.

### Practice — Section 4

1. Print integers from 1 to 20.
2. Print all multiples of 3 between 1 and 60.
3. Calculate the sum of integers from 1 to `n`.
4. Calculate the factorial of a non-negative integer `n`.
5. Count the digits in a positive integer using arithmetic, not string conversion.
6. Reverse a positive integer using `%` and `//`.
7. Determine whether a number is prime.
8. Find the largest and smallest values in a list without using `max()` or `min()`.
9. Count how many values in a list are above a threshold.
10. Print a right-angled triangle of stars using nested loops.
11. Write a `while` loop that keeps asking for input until the user enters `"quit"`.
12. Trace the output of a loop containing both `break` and `continue`.

---

# 5. Strings

## 5.1 What is a string?

A **string** (`str`) is a sequence of characters used to represent text. Strings can be written with single or double quotes.

```python
language = "Python"
message = 'Hello world'
```

Triple quotes can create strings spanning multiple lines:

```python
description = """Python is widely used
for data analysis and machine learning."""
```

## 5.2 Strings are immutable

**Immutable** means that the contents of an existing string cannot be changed in place.

```python
word = "Python"
# word[0] = "J"  # TypeError
word = "J" + word[1:]  # Create a new string
print(word)  # Jython
```

Operations such as `replace()` return a new string; they do not modify the original string.

## 5.3 Indexing

Each character has an index. Positive indexing starts at zero; negative indexing starts from the end.

For `word = "Python"`:

| Character | P | y | t | h | o | n |
|---|---:|---:|---:|---:|---:|---:|
| Positive index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative index | -6 | -5 | -4 | -3 | -2 | -1 |

```python
word = "Python"

print(word[0])   # P
print(word[2])   # t
print(word[-1])  # n
```

An index outside the valid range raises `IndexError`.

## 5.4 Slicing

**Slicing** extracts part of a string.

```python
text[start:stop:step]
```

The `start` index is included, but the `stop` index is excluded.

```python
word = "Python"

print(word[0:2])   # Py
print(word[2:])    # thon
print(word[:4])    # Pyth
print(word[::2])   # Pto
print(word[::-1])  # nohtyP
```

Leaving out `start` or `stop` uses the appropriate end of the string. A negative step can traverse the string backwards.

## 5.5 Common string methods

String methods return values; many do not change the original string.

| Method | Purpose | Example |
|---|---|---|
| `.lower()` | Convert to lowercase | `"AI".lower()` → `"ai"` |
| `.upper()` | Convert to uppercase | `"ai".upper()` → `"AI"` |
| `.strip()` | Remove surrounding whitespace | `" hi ".strip()` → `"hi"` |
| `.split()` | Split into a list | `"a b".split()` → `["a", "b"]` |
| `.join(iterable)` | Join strings with a separator | `"-".join(["a", "b"])` → `"a-b"` |
| `.replace(old, new)` | Replace occurrences | `"banana".replace("a", "o")` → `"bonono"` |
| `.find(sub)` | First matching index, or `-1` | `"python".find("th")` → `2` |
| `.count(sub)` | Count non-overlapping occurrences | `"banana".count("a")` → `3` |
| `.startswith(prefix)` | Test prefix | `"python".startswith("py")` → `True` |
| `.endswith(suffix)` | Test suffix | `"file.csv".endswith(".csv")` → `True` |

Remember: `.split()` with no argument splits on runs of whitespace. `.join()` is called on the separator string, not on the list.

```python
sentence = "  Learn Python for AI  "
cleaned = sentence.strip().lower()
words = cleaned.split()
joined = "_".join(words)

print(cleaned)  # learn python for ai
print(words)    # ['learn', 'python', 'for', 'ai']
print(joined)   # learn_python_for_ai
```

## 5.6 String formatting

An **f-string** inserts values or expressions into text. Put `f` before the opening quote and place expressions inside `{}`.

```python
name = "Rahul"
score = 87

print(f"{name} scored {score} marks.")
print(f"Next score target: {score + 5}")
```

Formatting is useful for readable output, reports, and debugging.

## 5.7 Iterating over strings

A string is iterable, so a `for` loop can visit each character.

```python
word = "python"

for character in word:
    print(character)
```

This pattern is useful for counting letters, filtering characters, and checking text.

## 5.8 Useful string problem patterns

### Count vowels

```python
text = "Machine Learning"
vowels = "aeiou"
count = 0

for character in text.lower():
    if character in vowels:
        count += 1

print(count)
```

### Check a palindrome (simple version)

A palindrome reads the same forwards and backwards.

```python
word = "level"
print(word == word[::-1])  # True
```

This exact check is case-sensitive and includes spaces and punctuation. For a more realistic sentence check, normalize the text first.

### Reverse word order

```python
sentence = "Python is useful"
words = sentence.split()
reversed_sentence = " ".join(words[::-1])

print(reversed_sentence)  # useful is Python
```

### Count character frequency

```python
text = "banana"
frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

print(frequency)  # {'b': 1, 'a': 3, 'n': 2}
```

This example introduces a dictionary-based counting pattern; dictionaries are covered in the collections section of the larger study plan.

## 5.9 Common string mistakes

- Forgetting that indexing starts at zero.
- Expecting the stop index in a slice to be included.
- Trying to modify a character in place.
- Writing `text.lower` instead of calling `text.lower()`.
- Forgetting to store a returned string, e.g. `text.replace(...)` without assigning the result.
- Using `.join()` on non-string items without converting them.
- Forgetting that `"5" + "2"` produces `"52"`, not `7`.

### Practice — Section 5

1. Print the first, last, and middle character of a string, handling short strings safely.
2. Extract the first three and last three characters of a string.
3. Reverse a string using slicing.
4. Count vowels in a sentence, ignoring capitalization.
5. Count uppercase letters, lowercase letters, and digits in a string.
6. Check whether a word is a palindrome.
7. Check whether two words are anagrams, ignoring capitalization.
8. Reverse the order of words in a sentence.
9. Replace repeated spaces in a sentence with single spaces.
10. Count how many times a specified character appears.
11. Given a filename, check whether it ends with `.csv`, ignoring case.
12. Format a student's name, marks, and grade using an f-string.

---

# 6. Final Mixed Practice

Complete these after studying all four sections. Avoid copying code from the notes.

## Level 1 — Core fluency

1. Read two numbers and print their sum, difference, product, and quotient. Handle division by zero.
2. Check whether a number is divisible by both 3 and 5.
3. Print all numbers from 1 to `n` that are divisible by 2 or 7.
4. Count the digits of a positive integer.
5. Count the words in a sentence after trimming leading and trailing spaces.

## Level 2 — Combining concepts

6. Given a list of marks, count how many are passing using a threshold of 40.
7. Given a sentence, count its vowels and consonants. State how you handle spaces, digits, and punctuation.
8. Check whether a string is a palindrome after converting to lowercase and removing spaces.
9. Find the sum of the digits of a positive integer using `%` and `//`.
10. Print a multiplication table from 1 to 10 for a user-supplied number.

## Level 3 — Independent problem solving

11. Check whether a positive integer is prime.
12. Print the first `n` terms of the Fibonacci sequence.
13. Find the second-largest distinct number in a list. Handle lists with fewer than two distinct values.
14. Determine whether two strings are anagrams, ignoring spaces and capitalization.
15. Create a simple password validator using rules you define (for example, minimum length, at least one digit, and at least one uppercase letter).

For each solution, test ordinary inputs, edge cases, and invalid inputs where appropriate. Write down any issue you find and how you fixed it.

---

# 7. Completion Checklist

You are ready to move on when you can do the following without following a tutorial line by line:

- [ ] Explain `int`, `float`, `str`, `bool`, and `None`.
- [ ] Read numeric input and convert it safely for the task.
- [ ] Use arithmetic, comparison, and logical operators.
- [ ] Write `if`, `elif`, and `else` branches with correct boundaries.
- [ ] Choose between `for` and `while`.
- [ ] Use `range()` correctly and avoid off-by-one errors.
- [ ] Write loops that accumulate totals and count matching values.
- [ ] Explain and use `break` and `continue`.
- [ ] Index and slice strings.
- [ ] Use common string methods and f-strings.
- [ ] Solve at least 10 mixed exercises independently.
- [ ] Explain your solution and test at least one edge case per problem.

## What you can postpone

For this AI/ML foundation refresh, do not spend this session studying decorators, generators, metaclasses, async programming, advanced class design, or Python internals. Those topics may matter in specialized work later, but they are not prerequisites for starting data analysis and introductory machine learning.

**Next step:** Once this part is solid, study collections in depth—lists, tuples, sets, dictionaries, and comprehensions—then continue with NumPy, Pandas, and visualization practice.
