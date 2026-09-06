# Python Notes --- Data Science & AI Masters 2026

> **Course:** Data Science & AI Masters 2026 - From Python To Gen AI\
> **Section:** Python\
> **Topics covered in the provided course screenshots:** Variables &
> Keywords, Datatypes & Operators, Lists, Tuples, Sets, Dictionary,
> Loops & Iterations, Functions, Map/Reduce/Filter, File Handling,
> Control Structures, OOPs.

------------------------------------------------------------------------

# 9. Variables & Keywords

## 1. Definition

A **variable** is a name used to refer to a value stored in memory.

A **keyword** is a reserved word in Python that has a predefined meaning
and cannot normally be used as a variable, function, or class name.

## 2. Simple Meaning

Think of a variable as a **label attached to some data**.

``` python
name = "Rahul"
age = 18
```

Here: - `name` refers to `"Rahul"` - `age` refers to `18`

Python automatically determines the data type from the assigned value.

## 3. Syntax

``` python
variable_name = value
```

## 4. Examples

``` python
name = "Rahul"
age = 18
marks = 85.5

print(name)
print(age)
print(marks)
```

### Multiple Assignment

``` python
x, y, z = 10, 20, 30
```

### Same Value to Multiple Variables

``` python
a = b = c = 100
```

## 5. Rules for Variable Names

-   Must start with a letter or `_`.
-   Cannot start with a number.
-   Can contain letters, numbers, and `_`.
-   Python is case-sensitive.
-   Cannot be a Python keyword.
-   Use meaningful names.

``` python
student_name = "Rahul"   # Good
age = 18                 # Good

# 2age = 18              # Invalid
# class = "CSE"           # Invalid: class is a keyword
```

## 6. Keywords

Examples:

``` text
if, else, elif, for, while, in, is, and, or, not,
def, return, class, try, except, finally, import,
from, as, True, False, None, break, continue, pass
```

You can see Python's keywords with:

``` python
import keyword
print(keyword.kwlist)
```

## 7. Important Things to Remember

-   `=` means **assignment**, not comparison.
-   Python variables do not require explicit type declarations.
-   Variable names are case-sensitive.
-   `age` and `Age` are different variables.
-   Avoid names such as `list`, `str`, `sum`, or `input` because they
    can hide built-in Python functionality.

------------------------------------------------------------------------

# 10. Datatypes & Operators

## 1. Definition

A **data type** defines what kind of value a variable contains and what
operations can be performed on it.

An **operator** is a symbol or keyword used to perform an operation on
values.

## 2. Main Built-in Data Types

  Data Type    Example               Meaning
  ------------ --------------------- ---------------------------------------
  `int`        `10`                  Integer
  `float`      `10.5`                Decimal number
  `complex`    `2 + 3j`              Complex number
  `bool`       `True`                Boolean value
  `str`        `"Hello"`             Text
  `list`       `[1, 2, 3]`           Ordered, mutable collection
  `tuple`      `(1, 2, 3)`           Ordered, immutable collection
  `set`        `{1, 2, 3}`           Unordered collection of unique values
  `dict`       `{"name": "Rahul"}`   Key-value collection
  `NoneType`   `None`                Absence of a value

Check a type with:

``` python
x = 10
print(type(x))
```

## 3. Type Conversion

``` python
x = "10"

print(int(x))
print(float(x))
print(str(10))
```

Common functions:

``` text
int()
float()
str()
bool()
list()
tuple()
set()
dict()
```

> **Important:** Not every conversion is valid. For example,
> `int("hello")` raises a `ValueError`.

## 4. Operators

### Arithmetic Operators

  Operator   Meaning             Example
  ---------- ------------------- ----------
  `+`        Addition            `5 + 2`
  `-`        Subtraction         `5 - 2`
  `*`        Multiplication      `5 * 2`
  `/`        Division            `5 / 2`
  `//`       Floor division      `5 // 2`
  `%`        Modulus/remainder   `5 % 2`
  `**`       Power               `5 ** 2`

``` python
a = 10
b = 3

print(a + b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

### Comparison Operators

``` text
==   !=   >   <   >=   <=
```

They return `True` or `False`.

``` python
print(10 > 5)     # True
print(10 == 10)   # True
print(10 != 5)    # True
```

### Logical Operators

``` text
and
or
not
```

``` python
age = 20
print(age > 18 and age < 30)
```

### Assignment Operators

``` text
=   +=   -=   *=   /=   //=   %=   **=
```

``` python
x = 10
x += 5
print(x)  # 15
```

### Membership Operators

``` text
in
not in
```

``` python
print("a" in "data")       # True
print(5 not in [1, 2, 3])  # True
```

### Identity Operators

``` text
is
is not
```

They check whether two references point to the **same object**, not
merely whether their values are equal.

``` python
a = [1, 2]
b = a

print(a is b)   # True
```

> **Remember:** `==` checks equality of values; `is` checks object
> identity.

------------------------------------------------------------------------

# 11. Lists

## 1. Definition

A **list** is an ordered, mutable collection that can store multiple
values.

## 2. Simple Meaning

A list is like a container where you can keep multiple items and later
change, add, or remove them.

## 3. Syntax

``` python
my_list = [item1, item2, item3]
```

## 4. Example

``` python
fruits = ["apple", "banana", "mango"]

print(fruits)
print(fruits[0])
```

Python uses **zero-based indexing**.

``` text
apple   -> index 0
banana  -> index 1
mango   -> index 2
```

Negative indexing:

``` python
print(fruits[-1])  # mango
```

## 5. Lists Are Mutable

``` python
fruits[1] = "orange"
print(fruits)
```

## 6. Important List Methods

### `append()`

Adds one item at the end.

``` python
numbers = [1, 2, 3]
numbers.append(4)
```

### `extend()`

Adds multiple items.

``` python
numbers.extend([5, 6])
```

### `insert()`

Adds an item at a specific position.

``` python
numbers.insert(1, 100)
```

### `remove()`

Removes the first matching value.

``` python
numbers.remove(100)
```

### `pop()`

Removes and returns an item.

``` python
x = numbers.pop()
```

### `sort()`

Sorts the list in place.

``` python
numbers.sort()
```

### `reverse()`

Reverses the list in place.

``` python
numbers.reverse()
```

### `len()`

Returns the number of items.

``` python
print(len(numbers))
```

## 7. Slicing

``` python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
```

General form:

``` python
list[start:stop:step]
```

> `stop` is excluded.

## 8. Important Things to Remember

-   Lists are ordered.
-   Lists are mutable.
-   Duplicate values are allowed.
-   Lists can contain different data types.
-   Indexing starts from `0`.
-   `append()` adds one object; `extend()` adds elements from an
    iterable.

------------------------------------------------------------------------

# 12. Tuples

## 1. Definition

A **tuple** is an ordered, immutable collection of values.

## 2. Simple Meaning

A tuple is similar to a list, but once created, its elements cannot
normally be changed.

## 3. Syntax

``` python
my_tuple = (10, 20, 30)
```

Example:

``` python
coordinates = (10, 20)

print(coordinates[0])
```

## 4. Single-Element Tuple

This is important:

``` python
x = (10,)   # tuple
y = (10)    # integer
```

The comma creates the single-element tuple.

## 5. Tuple Unpacking

``` python
person = ("Rahul", 18)

name, age = person

print(name)
print(age)
```

## 6. Important Things to Remember

-   Tuples are ordered.
-   Tuples are immutable.
-   Duplicates are allowed.
-   Indexing and slicing work similarly to lists.
-   Tuples are useful for fixed collections of values.

> **Why use a tuple?** When the collection should not be changed
> accidentally.

------------------------------------------------------------------------

# 13. Sets

## 1. Definition

A **set** is an unordered collection of unique elements.

## 2. Simple Meaning

A set automatically removes duplicate values.

``` python
numbers = {1, 2, 2, 3, 3}
print(numbers)
```

The result contains only unique values.

## 3. Syntax

``` python
my_set = {1, 2, 3}
```

## 4. Creating an Empty Set

``` python
s = set()
```

> `{}` creates an empty dictionary, not an empty set.

## 5. Common Operations

### Add

``` python
s.add(10)
```

### Remove

``` python
s.remove(10)
```

`remove()` raises an error if the item does not exist.

### Discard

``` python
s.discard(10)
```

`discard()` does not raise an error if the item is absent.

### Union

``` python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

### Intersection

``` python
print(a & b)
```

### Difference

``` python
print(a - b)
```

### Symmetric Difference

``` python
print(a ^ b)
```

## 6. Important Things to Remember

-   Sets contain unique elements.
-   Sets do not support normal positional indexing.
-   Sets are useful for membership testing and removing duplicates.
-   Set elements must be hashable.

------------------------------------------------------------------------

# 14. Dictionary

## 1. Definition

A **dictionary** is a mutable collection that stores data as **key-value
pairs**.

## 2. Simple Meaning

Think of a dictionary like a real dictionary:

``` text
key -> value
```

Example:

``` python
student = {
    "name": "Rahul",
    "age": 18,
    "course": "CSE"
}
```

## 3. Accessing Values

``` python
print(student["name"])
```

Using `get()`:

``` python
print(student.get("name"))
```

`get()` is useful when the key may not exist.

## 4. Adding / Updating Values

``` python
student["age"] = 19
student["city"] = "Panipat"
```

## 5. Removing Values

``` python
student.pop("city")
```

Other useful methods:

``` python
student.keys()
student.values()
student.items()
```

## 6. Looping Through a Dictionary

``` python
for key, value in student.items():
    print(key, value)
```

## 7. Important Things to Remember

-   Dictionaries store key-value pairs.
-   Keys must be hashable.
-   Keys are unique.
-   Values can be duplicated.
-   Dictionaries are mutable.
-   Use `get()` when you want safer access to possibly missing keys.

------------------------------------------------------------------------

# 15. Loops & Iterations

## 1. Definition

A **loop** repeatedly executes a block of code.

Python mainly provides:

-   `for`
-   `while`

## 2. `for` Loop

Use a `for` loop to iterate over an iterable.

### Syntax

``` python
for variable in iterable:
    # code
```

### Example

``` python
for i in [1, 2, 3]:
    print(i)
```

### Using `range()`

``` python
for i in range(5):
    print(i)
```

Output:

``` text
0
1
2
3
4
```

`range(start, stop, step)`:

``` python
for i in range(1, 10, 2):
    print(i)
```

## 3. `while` Loop

Repeats while a condition is `True`.

### Syntax

``` python
while condition:
    # code
```

Example:

``` python
i = 1

while i <= 5:
    print(i)
    i += 1
```

> Always make sure the condition can eventually become false, otherwise
> you may create an infinite loop.

## 4. `break`

Stops the loop immediately.

``` python
for i in range(10):
    if i == 5:
        break
    print(i)
```

## 5. `continue`

Skips the current iteration.

``` python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

## 6. `pass`

Does nothing; it is used as a placeholder.

``` python
if True:
    pass
```

## 7. Important Things to Remember

-   `for` is commonly used for iterating over sequences/iterables.
-   `while` is condition-based.
-   `break` exits the loop.
-   `continue` skips the current iteration.
-   `pass` does nothing.
-   Python blocks are defined by indentation.

------------------------------------------------------------------------

# 16. Functions

## 1. Definition

A **function** is a reusable block of code designed to perform a
particular task.

## 2. Simple Meaning

Instead of writing the same code repeatedly, put it inside a function
and call it whenever needed.

## 3. Syntax

``` python
def function_name(parameters):
    # function body
    return result
```

## 4. Basic Example

``` python
def greet():
    print("Hello!")

greet()
```

## 5. Parameters and Arguments

``` python
def greet(name):
    print("Hello", name)

greet("Rahul")
```

Here: - `name` is a **parameter**. - `"Rahul"` is an **argument**.

## 6. Return Value

``` python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

`return` sends a value back to the caller.

## 7. Default Arguments

``` python
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Rahul")
```

## 8. Keyword Arguments

``` python
def student(name, age):
    print(name, age)

student(age=18, name="Rahul")
```

## 9. Variable-Length Arguments

### `*args`

Used for multiple positional arguments.

``` python
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))
```

### `**kwargs`

Used for multiple keyword arguments.

``` python
def show(**data):
    print(data)

show(name="Rahul", age=18)
```

## 10. Lambda Functions

A lambda is a small anonymous function.

``` python
square = lambda x: x * x

print(square(5))
```

## 11. Scope

### Local Variable

Created inside a function.

``` python
def test():
    x = 10
```

### Global Variable

Created outside functions.

``` python
x = 10

def test():
    print(x)
```

> Prefer clear function inputs/outputs over relying heavily on global
> variables.

## 12. Important Things to Remember

-   Define functions with `def`.
-   A function runs when it is called.
-   `return` sends a value back.
-   Parameters receive arguments.
-   Functions reduce repetition and improve code organization.
-   Keep functions focused on one logical responsibility.

------------------------------------------------------------------------

# 17. Map, Reduce & Filter

These are commonly used functional programming tools in Python.

## 1. `map()`

### Definition

`map()` applies a function to every item in an iterable.

### Syntax

``` python
map(function, iterable)
```

### Example

``` python
numbers = [1, 2, 3, 4]

squares = map(lambda x: x * x, numbers)

print(list(squares))
```

Output:

``` text
[1, 4, 9, 16]
```

> In Python 3, `map()` returns an iterator, so `list()` is commonly used
> when you want to display all results immediately.

------------------------------------------------------------------------

## 2. `filter()`

### Definition

`filter()` keeps only the elements for which a function returns `True`.

### Syntax

``` python
filter(function, iterable)
```

### Example

``` python
numbers = [1, 2, 3, 4, 5, 6]

even = filter(lambda x: x % 2 == 0, numbers)

print(list(even))
```

Output:

``` text
[2, 4, 6]
```

------------------------------------------------------------------------

## 3. `reduce()`

### Definition

`reduce()` repeatedly combines elements to produce a single result.

It is available through `functools`.

### Syntax

``` python
from functools import reduce

reduce(function, iterable)
```

### Example

``` python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)
```

Output:

``` text
10
```

The operation is conceptually:

``` text
(((1 + 2) + 3) + 4)
```

## 4. Quick Comparison

  Function     Purpose                         Result
  ------------ ------------------------------- --------------
  `map()`      Transform every item            Iterator
  `filter()`   Select matching items           Iterator
  `reduce()`   Combine items into one result   Single value

## 5. Important Things to Remember

-   `map()` → **transform**
-   `filter()` → **select**
-   `reduce()` → **combine**
-   `reduce()` comes from `functools`.
-   List comprehensions are often more readable than `map()`/`filter()`
    for simple transformations.

------------------------------------------------------------------------

# 18. File Handling

## 1. Definition

**File handling** means reading from and writing data to files using
Python.

## 2. Simple Meaning

Python can open a file, read its contents, write new data, and close it.

## 3. Opening a File

``` python
file = open("data.txt", "r")
```

Common modes:

  Mode   Meaning
  ------ ------------------------------------
  `r`    Read
  `w`    Write; overwrites existing content
  `a`    Append
  `x`    Create a new file
  `b`    Binary mode
  `t`    Text mode

## 4. Reading

``` python
file = open("data.txt", "r")

content = file.read()
print(content)

file.close()
```

Other methods:

``` python
file.readline()
file.readlines()
```

## 5. Writing

``` python
file = open("data.txt", "w")
file.write("Hello Python")
file.close()
```

> **Warning:** `w` mode can overwrite existing file contents.

## 6. Appending

``` python
file = open("data.txt", "a")
file.write("\nNew line")
file.close()
```

## 7. Best Practice: `with`

Use a context manager so the file is automatically closed.

``` python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

Writing:

``` python
with open("data.txt", "w") as file:
    file.write("Hello")
```

## 8. Important Things to Remember

-   Always handle files carefully.
-   Prefer `with open(...)` over manually calling `close()`.
-   `r` reads.
-   `w` overwrites.
-   `a` appends.
-   File paths can be relative or absolute.
-   File encoding matters when working with text; for example:

``` python
with open("data.txt", "r", encoding="utf-8") as file:
    text = file.read()
```

------------------------------------------------------------------------

# 19. Control Structures

## 1. Definition

**Control structures** control the order in which statements are
executed.

The major types are:

1.  Sequential execution
2.  Conditional execution
3.  Iteration/repetition

## 2. Sequential

Statements normally execute from top to bottom.

``` python
x = 10
y = 20
z = x + y

print(z)
```

## 3. Conditional Statements

### `if`

``` python
age = 20

if age >= 18:
    print("Adult")
```

### `if-else`

``` python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### `if-elif-else`

``` python
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
else:
    grade = "C"

print(grade)
```

## 4. Nested Conditions

``` python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
```

Avoid excessive nesting when a simpler condition is possible.

## 5. Conditional Expression

Python supports a one-line conditional expression:

``` python
age = 20
status = "Adult" if age >= 18 else "Minor"
```

## 6. Important Things to Remember

-   Conditions evaluate to truthy/falsy values.
-   Indentation is part of Python syntax.
-   `elif` means "else if".
-   Only the appropriate branch of an `if/elif/else` chain executes.
-   Loops are also control structures because they control repetition.

------------------------------------------------------------------------

# 20. OOPs --- Object-Oriented Programming

## 1. Definition

**Object-Oriented Programming (OOP)** is a programming paradigm that
organizes code around **objects**, which combine data and behavior.

## 2. Simple Meaning

Instead of thinking only about functions and data separately, we can
create objects that contain:

-   **Attributes** → data/state
-   **Methods** → behavior/actions

## 3. Class

A **class** is a blueprint for creating objects.

### Syntax

``` python
class ClassName:
    # attributes and methods
    pass
```

## 4. Object

An **object** is an instance of a class.

``` python
class Student:
    pass

student1 = Student()
student2 = Student()
```

Here `student1` and `student2` are objects of the `Student` class.

## 5. Constructor: `__init__()`

`__init__()` is commonly used to initialize object attributes when an
object is created.

``` python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Rahul", 18)

print(student.name)
print(student.age)
```

## 6. What is `self`?

`self` refers to the current object instance.

``` python
self.name = name
```

It means the object's `name` attribute receives the value of the
parameter `name`.

## 7. Methods

Methods are functions defined inside a class.

``` python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)

student = Student("Rahul")
student.introduce()
```

## 8. Four Important OOP Concepts

### 1. Encapsulation

Bundling data and methods together and controlling how internal state is
accessed.

### 2. Inheritance

A class can derive from another class.

``` python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()
```

### 3. Polymorphism

Different objects can provide the same interface with different
behavior.

``` python
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

for animal in [Dog(), Cat()]:
    animal.speak()
```

### 4. Abstraction

Showing the necessary interface while hiding unnecessary implementation
details.

Python can implement formal abstraction using the `abc` module.

## 9. Class Variable vs Instance Variable

``` python
class Student:
    university = "Geeta University"  # class variable

    def __init__(self, name):
        self.name = name              # instance variable
```

-   Class variable is associated with the class.
-   Instance variable is associated with a particular object.

## 10. Important Things to Remember

-   Class = blueprint.
-   Object = instance of a class.
-   Attributes represent state/data.
-   Methods represent behavior.
-   `self` refers to the current instance.
-   `__init__()` is commonly used for initialization.
-   Inheritance enables code reuse and specialization.
-   Polymorphism allows a common interface with different
    implementations.
-   Abstraction focuses on what an object does rather than unnecessary
    implementation details.

------------------------------------------------------------------------

# Python Quick Revision Cheat Sheet

  Concept        Remember
  -------------- --------------------------------
  Variable       Name referring to a value
  Keyword        Reserved Python word
  `=`            Assignment
  `==`           Equality comparison
  `is`           Object identity
  List           Ordered + mutable
  Tuple          Ordered + immutable
  Set            Unique elements
  Dictionary     Key-value pairs
  `for`          Iterate over an iterable
  `while`        Repeat while condition is true
  `break`        Exit loop
  `continue`     Skip current iteration
  `pass`         Do nothing / placeholder
  Function       Reusable block of code
  `map()`        Transform
  `filter()`     Select
  `reduce()`     Combine
  `r`            Read file
  `w`            Write/overwrite
  `a`            Append
  Class          Blueprint
  Object         Instance
  `self`         Current instance
  `__init__()`   Object initialization

------------------------------------------------------------------------

# High-Priority Things to Remember

1.  **Python is dynamically typed** --- you do not normally declare a
    variable's type before assigning a value.
2.  **Lists are mutable; tuples are immutable.**
3.  **Sets remove duplicates and do not provide normal positional
    indexing.**
4.  **Dictionary keys must be hashable and unique.**
5.  **`==` and `is` are not interchangeable.**
6.  **`append()` and `extend()` behave differently.**
7.  **`w` mode can destroy existing file contents.**
8.  **Use `with open(...)` for safer file handling.**
9.  **`map()` transforms, `filter()` selects, and `reduce()` combines.**
10. **Indentation defines code blocks in Python.**
11. **Functions help reduce repetition and organize programs.**
12. **OOP organizes data and behavior around objects.**

------------------------------------------------------------------------

# Practice Questions

## Beginner

1.  What is a variable in Python?
2.  What is the difference between `=` and `==`?
3.  Name five Python data types.
4.  Why does Python use zero-based indexing?
5.  What is the difference between a list and a tuple?
6.  How does a set handle duplicate values?
7.  What is a dictionary?
8.  What is the purpose of a `for` loop?
9.  What is the difference between `break` and `continue`?
10. What is a function?

## Coding Practice

1.  Create a list of five numbers and find its maximum value.
2.  Remove duplicate values from a list using a set.
3.  Create a dictionary containing a student's name, age, and marks.
4.  Write a function that returns the square of a number.
5.  Use `filter()` to select even numbers.
6.  Use `map()` to calculate the squares of numbers.
7.  Use `reduce()` to calculate the product of a list of numbers.
8.  Write a program that reads a text file and prints its contents.
9.  Write an `if-elif-else` program to assign grades.
10. Create a `Student` class with `name`, `age`, and an `introduce()`
    method.

------------------------------------------------------------------------

# Final Mental Model

``` text
Python Basics
│
├── Variables & Keywords
│
├── Data Types
│   ├── Numbers
│   ├── Strings
│   ├── Lists
│   ├── Tuples
│   ├── Sets
│   └── Dictionaries
│
├── Operators
│
├── Control Flow
│   ├── if / elif / else
│   ├── for
│   ├── while
│   ├── break
│   └── continue
│
├── Functions
│   ├── Parameters
│   ├── Arguments
│   ├── return
│   └── lambda
│
├── Functional Tools
│   ├── map()
│   ├── filter()
│   └── reduce()
│
├── File Handling
│   ├── Read
│   ├── Write
│   └── Append
│
└── OOP
    ├── Class
    ├── Object
    ├── Attributes
    ├── Methods
    ├── Inheritance
    ├── Polymorphism
    ├── Encapsulation
    └── Abstraction
```

> **Note:** These are foundational notes based on the topic list visible
> in your screenshots. They are not a verbatim summary of the
> instructor's lectures. For future daily notes, send me what the
> instructor actually covered and I can make the notes match the course
> exactly, while adding missing explanations and correcting
> misconceptions.
