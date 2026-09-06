# Python Collections --- Methods & Operations Cheat Sheet

> A practical reference for **List, Tuple, Set, Dictionary, and String**
> methods.
>
> **Rule:** Don't try to memorize everything at once. Understand what
> each method does, then practice the frequently used ones.

------------------------------------------------------------------------

# 1. Lists

## Definition

A **list** is an ordered and mutable collection of elements.

``` python
numbers = [10, 20, 30, 40]
```

### Important Properties

-   Ordered
-   Mutable
-   Allows duplicate values
-   Supports indexing and slicing
-   Can contain different data types

------------------------------------------------------------------------

## List Methods

### 1. `append()`

Adds **one element** to the end.

``` python
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
# [1, 2, 3, 4]
```

**Remember:** `append()` adds the object as a single element.

``` python
numbers.append([5, 6])
# [1, 2, 3, 4, [5, 6]]
```

------------------------------------------------------------------------

### 2. `extend()`

Adds elements from another iterable.

``` python
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])

print(numbers)
# [1, 2, 3, 4, 5, 6]
```

### `append()` vs `extend()`

``` python
a = [1, 2]

a.append([3, 4])
# [1, 2, [3, 4]]

b = [1, 2]

b.extend([3, 4])
# [1, 2, 3, 4]
```

> **High priority:** This is a very common interview/exam question.

------------------------------------------------------------------------

### 3. `insert()`

Inserts an element at a particular index.

``` python
numbers = [10, 20, 30]

numbers.insert(1, 99)

print(numbers)
# [10, 99, 20, 30]
```

**Syntax:**

``` python
list.insert(index, element)
```

------------------------------------------------------------------------

### 4. `remove()`

Removes the **first matching value**.

``` python
numbers = [10, 20, 20, 30]

numbers.remove(20)

print(numbers)
# [10, 20, 30]
```

> If the value does not exist, `remove()` raises `ValueError`.

------------------------------------------------------------------------

### 5. `pop()`

Removes and **returns** an element.

``` python
numbers = [10, 20, 30]

x = numbers.pop()

print(x)
# 30

print(numbers)
# [10, 20]
```

Remove by index:

``` python
numbers.pop(0)
```

> `pop()` without an argument removes the last element.

------------------------------------------------------------------------

### 6. `clear()`

Removes all elements.

``` python
numbers = [1, 2, 3]

numbers.clear()

print(numbers)
# []
```

------------------------------------------------------------------------

### 7. `index()`

Returns the index of the first matching value.

``` python
numbers = [10, 20, 30, 20]

print(numbers.index(20))
# 1
```

Optional range:

``` python
numbers.index(20, 2)
```

> If the value is absent, `ValueError` is raised.

------------------------------------------------------------------------

### 8. `count()`

Counts how many times a value occurs.

``` python
numbers = [1, 2, 2, 2, 3]

print(numbers.count(2))
# 3
```

------------------------------------------------------------------------

### 9. `sort()`

Sorts the list **in place**.

``` python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
# [10, 20, 30, 40]
```

Descending:

``` python
numbers.sort(reverse=True)
```

### Custom sorting

``` python
words = ["apple", "kiwi", "banana"]

words.sort(key=len)

print(words)
# ['kiwi', 'apple', 'banana']
```

> `sort()` modifies the original list and returns `None`.

------------------------------------------------------------------------

### 10. `reverse()`

Reverses the list **in place**.

``` python
numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers)
# [4, 3, 2, 1]
```

------------------------------------------------------------------------

### 11. `copy()`

Creates a **shallow copy** of the list.

``` python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
# [1, 2, 3]

print(b)
# [1, 2, 3, 4]
```

### Important: `=` is not copying

``` python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
# [1, 2, 3, 4]
```

Both names refer to the same list object.

------------------------------------------------------------------------

## List Built-in Functions / Operations

These are not list methods, but are very important:

``` python
len(numbers)       # number of elements
max(numbers)       # largest
min(numbers)       # smallest
sum(numbers)       # total
sorted(numbers)    # returns a new sorted list
```

### `sort()` vs `sorted()`

``` python
numbers = [3, 1, 2]

result = numbers.sort()
print(result)
# None
```

``` python
numbers = [3, 1, 2]

result = sorted(numbers)

print(result)
# [1, 2, 3]

print(numbers)
# [3, 1, 2]
```

> **Remember:** `sort()` changes the original list; `sorted()` returns a
> new sorted result.

------------------------------------------------------------------------

# 2. Tuples

## Definition

A **tuple** is an ordered and immutable collection.

``` python
data = (10, 20, 30, 20)
```

### Important Properties

-   Ordered
-   Immutable
-   Allows duplicates
-   Supports indexing and slicing
-   Usually used for fixed collections of values

------------------------------------------------------------------------

## Tuple Methods

Tuples have only **two main methods**.

### 1. `count()`

Counts occurrences of a value.

``` python
data = (10, 20, 20, 30)

print(data.count(20))
# 2
```

------------------------------------------------------------------------

### 2. `index()`

Returns the index of the first occurrence.

``` python
data = (10, 20, 30, 20)

print(data.index(20))
# 1
```

Optional starting position:

``` python
data.index(20, 2)
```

------------------------------------------------------------------------

## Tuple Operations

``` python
a = (1, 2)
b = (3, 4)

print(a + b)
# (1, 2, 3, 4)
```

Repetition:

``` python
print(a * 3)
# (1, 2, 1, 2, 1, 2)
```

Membership:

``` python
print(2 in a)
# True
```

Built-in functions:

``` python
len(a)
max(a)
min(a)
sum(a)
```

------------------------------------------------------------------------

## Important Tuple Trick

### Single-element tuple

``` python
a = (10,)   # tuple
b = (10)    # int
```

The **comma** is what makes it a one-element tuple.

------------------------------------------------------------------------

# 3. Sets

## Definition

A **set** is an unordered collection of unique elements.

``` python
numbers = {1, 2, 3, 4}
```

### Important Properties

-   Unique elements
-   No normal positional indexing
-   Mutable as a collection
-   Very useful for membership testing and set operations
-   Elements must be hashable

------------------------------------------------------------------------

## Set Methods

### 1. `add()`

Adds one element.

``` python
s = {1, 2, 3}

s.add(4)

print(s)
```

------------------------------------------------------------------------

### 2. `update()`

Adds elements from one or more iterables.

``` python
s = {1, 2}

s.update([3, 4, 5])

print(s)
```

Multiple iterables:

``` python
s.update([6, 7], {8, 9})
```

------------------------------------------------------------------------

### 3. `remove()`

Removes an element.

``` python
s = {1, 2, 3}

s.remove(2)
```

> Raises `KeyError` if the element does not exist.

------------------------------------------------------------------------

### 4. `discard()`

Removes an element if it exists.

``` python
s = {1, 2, 3}

s.discard(5)
```

No error if `5` is absent.

### `remove()` vs `discard()`

  Method        Element exists   Element absent
  ------------- ---------------- -------------------
  `remove()`    Removes it       Raises `KeyError`
  `discard()`   Removes it       Does nothing

------------------------------------------------------------------------

### 5. `pop()`

Removes and returns an **arbitrary** element.

``` python
s = {10, 20, 30}

x = s.pop()
print(x)
```

> Do **not** assume that `pop()` removes the first or last element in a
> set.

------------------------------------------------------------------------

### 6. `clear()`

Removes all elements.

``` python
s = {1, 2, 3}

s.clear()

print(s)
# set()
```

------------------------------------------------------------------------

### 7. `copy()`

Returns a shallow copy.

``` python
a = {1, 2, 3}
b = a.copy()
```

------------------------------------------------------------------------

# 4. Set Mathematical Operations

Suppose:

``` python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

## 1. `union()`

Returns all unique elements from both sets.

``` python
print(A.union(B))
# {1, 2, 3, 4, 5, 6}
```

Operator:

``` python
A | B
```

------------------------------------------------------------------------

## 2. `intersection()`

Returns elements common to both.

``` python
print(A.intersection(B))
# {3, 4}
```

Operator:

``` python
A & B
```

------------------------------------------------------------------------

## 3. `difference()`

Returns elements present in the first set but not the second.

``` python
print(A.difference(B))
# {1, 2}
```

Operator:

``` python
A - B
```

------------------------------------------------------------------------

## 4. `symmetric_difference()`

Returns elements that are in either set, but not in both.

``` python
print(A.symmetric_difference(B))
# {1, 2, 5, 6}
```

Operator:

``` python
A ^ B
```

------------------------------------------------------------------------

# 5. Set Relationship Methods

## `issubset()`

Checks whether every element of one set is present in another.

``` python
A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))
# True
```

Operator:

``` python
A <= B
```

------------------------------------------------------------------------

## `issuperset()`

Checks whether a set contains all elements of another set.

``` python
print(B.issuperset(A))
# True
```

Operator:

``` python
B >= A
```

------------------------------------------------------------------------

## `isdisjoint()`

Checks whether two sets have no elements in common.

``` python
A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))
# True
```

------------------------------------------------------------------------

# 6. `frozenset`

A `frozenset` is an **immutable set**.

``` python
fs = frozenset([1, 2, 3])
```

You cannot use methods such as:

``` python
fs.add(4)   # AttributeError
```

But set-like operations are available:

``` python
A = frozenset([1, 2])
B = frozenset([2, 3])

print(A | B)
```

> A `frozenset` can be used where a hashable set-like object is
> required, such as as a dictionary key.

------------------------------------------------------------------------

# 7. Dictionaries

## Definition

A **dictionary** stores data as **key-value pairs**.

``` python
student = {
    "name": "Rahul",
    "age": 18,
    "course": "CSE"
}
```

### Important Properties

-   Mutable
-   Keys are unique
-   Keys must be hashable
-   Values can be any suitable Python object
-   Preserves insertion order in modern Python

------------------------------------------------------------------------

# Dictionary Methods

## 1. `get()`

Returns the value for a key.

``` python
student = {"name": "Rahul", "age": 18}

print(student.get("name"))
# Rahul
```

If key is missing:

``` python
print(student.get("city"))
# None
```

You can provide a default:

``` python
print(student.get("city", "Not Available"))
# Not Available
```

### `[]` vs `get()`

``` python
student["city"]
```

Raises `KeyError` if the key does not exist.

``` python
student.get("city")
```

Returns `None` by default if the key does not exist.

------------------------------------------------------------------------

## 2. `keys()`

Returns a view of dictionary keys.

``` python
student = {"name": "Rahul", "age": 18}

print(student.keys())
```

Loop:

``` python
for key in student.keys():
    print(key)
```

------------------------------------------------------------------------

## 3. `values()`

Returns a view of values.

``` python
for value in student.values():
    print(value)
```

------------------------------------------------------------------------

## 4. `items()`

Returns key-value pairs.

``` python
for key, value in student.items():
    print(key, value)
```

> **Most useful for dictionary loops.**

------------------------------------------------------------------------

## 5. `update()`

Adds or updates key-value pairs.

``` python
student = {"name": "Rahul", "age": 18}

student.update({"age": 19, "city": "Panipat"})

print(student)
```

You can also use keyword arguments where valid:

``` python
student.update(course="CSE")
```

------------------------------------------------------------------------

## 6. `pop()`

Removes a specified key and returns its value.

``` python
student = {"name": "Rahul", "age": 18}

age = student.pop("age")

print(age)
# 18
```

Optional default:

``` python
student.pop("city", "Not Found")
```

------------------------------------------------------------------------

## 7. `popitem()`

Removes and returns the **last inserted key-value pair**.

``` python
student = {
    "name": "Rahul",
    "age": 18
}

item = student.popitem()

print(item)
# ('age', 18)
```

------------------------------------------------------------------------

## 8. `setdefault()`

Returns the value of a key.

If the key does not exist, it inserts the key with the provided default
value.

``` python
student = {"name": "Rahul"}

age = student.setdefault("age", 18)

print(student)
# {'name': 'Rahul', 'age': 18}
```

If the key already exists, its value is not replaced:

``` python
student = {"age": 20}

student.setdefault("age", 18)

print(student["age"])
# 20
```

------------------------------------------------------------------------

## 9. `clear()`

Removes all key-value pairs.

``` python
student.clear()

print(student)
# {}
```

------------------------------------------------------------------------

## 10. `copy()`

Creates a shallow copy.

``` python
a = {"name": "Rahul"}
b = a.copy()
```

------------------------------------------------------------------------

## 11. `fromkeys()`

Creates a new dictionary using specified keys and a common initial
value.

``` python
keys = ["name", "age", "city"]

student = dict.fromkeys(keys)

print(student)
# {'name': None, 'age': None, 'city': None}
```

With a value:

``` python
student = dict.fromkeys(keys, "Unknown")
```

> `fromkeys()` is a **class method** of `dict`, commonly used as
> `dict.fromkeys(...)`.

------------------------------------------------------------------------

# 8. Dictionary Quick Reference

  Method              Purpose
  ------------------- -----------------------------
  `get()`             Safely get a value
  `keys()`            Get keys
  `values()`          Get values
  `items()`           Get key-value pairs
  `update()`          Add/update pairs
  `pop()`             Remove a specified key
  `popitem()`         Remove last inserted pair
  `setdefault()`      Get value or insert default
  `clear()`           Remove everything
  `copy()`            Create shallow copy
  `dict.fromkeys()`   Create dictionary from keys

------------------------------------------------------------------------

# 9. Strings

Strings are also an important Python sequence type.

``` python
text = "Hello Python"
```

### Important Properties

-   Ordered
-   Immutable
-   Supports indexing and slicing
-   Can be iterated over
-   Has many useful methods

------------------------------------------------------------------------

# String Methods

## 1. `lower()`

Converts to lowercase.

``` python
text = "Hello PYTHON"

print(text.lower())
# hello python
```

------------------------------------------------------------------------

## 2. `upper()`

Converts to uppercase.

``` python
print(text.upper())
# HELLO PYTHON
```

------------------------------------------------------------------------

## 3. `capitalize()`

Capitalizes the first character and lowercases the remaining characters.

``` python
print("hello WORLD".capitalize())
# Hello world
```

------------------------------------------------------------------------

## 4. `title()`

Capitalizes the first character of each word.

``` python
print("hello python world".title())
# Hello Python World
```

------------------------------------------------------------------------

## 5. `swapcase()`

Swaps uppercase and lowercase characters.

``` python
print("Hello".swapcase())
# hELLO
```

------------------------------------------------------------------------

## 6. `strip()`

Removes leading and trailing whitespace by default.

``` python
text = "  Hello  "

print(text.strip())
# Hello
```

Related:

``` python
text.lstrip()  # left side
text.rstrip()  # right side
```

------------------------------------------------------------------------

## 7. `replace()`

Replaces part of a string.

``` python
text = "I like Java"

print(text.replace("Java", "Python"))
# I like Python
```

Optional count:

``` python
"banana".replace("a", "X", 2)
```

------------------------------------------------------------------------

## 8. `split()`

Splits a string into a list.

``` python
text = "Python is easy"

words = text.split()

print(words)
# ['Python', 'is', 'easy']
```

Using a separator:

``` python
"a,b,c".split(",")
# ['a', 'b', 'c']
```

------------------------------------------------------------------------

## 9. `join()`

Joins elements into a string.

``` python
words = ["Python", "is", "easy"]

result = " ".join(words)

print(result)
# Python is easy
```

### `split()` + `join()`

``` python
text = "Python is powerful"

words = text.split()
result = "-".join(words)

print(result)
# Python-is-powerful
```

> **Remember:** `split()` generally converts **string → list**, while
> `join()` combines **iterable of strings → string**.

------------------------------------------------------------------------

## 10. `find()`

Returns the first index of a substring.

``` python
text = "Python Programming"

print(text.find("Pro"))
# 7
```

If not found:

``` python
print(text.find("Java"))
# -1
```

------------------------------------------------------------------------

## 11. `index()`

Similar to `find()`, but raises an error if the substring is absent.

``` python
text.index("Pro")
```

### `find()` vs `index()`

  Method      Not found
  ----------- ---------------------
  `find()`    Returns `-1`
  `index()`   Raises `ValueError`

------------------------------------------------------------------------

## 12. `count()`

Counts occurrences.

``` python
print("banana".count("a"))
# 3
```

------------------------------------------------------------------------

## 13. `startswith()`

Checks whether a string starts with a value.

``` python
text = "Python Programming"

print(text.startswith("Python"))
# True
```

------------------------------------------------------------------------

## 14. `endswith()`

Checks whether a string ends with a value.

``` python
print(text.endswith("Programming"))
# True
```

------------------------------------------------------------------------

## 15. `isalpha()`

Checks whether all characters are alphabetic and the string is
non-empty.

``` python
print("Python".isalpha())
# True

print("Python123".isalpha())
# False
```

------------------------------------------------------------------------

## 16. `isdigit()`

Checks whether all characters are digits.

``` python
print("12345".isdigit())
# True
```

------------------------------------------------------------------------

## 17. `isalnum()`

Checks whether all characters are alphanumeric.

``` python
print("Python123".isalnum())
# True
```

------------------------------------------------------------------------

## 18. `isspace()`

Checks whether all characters are whitespace.

``` python
print("   ".isspace())
# True
```

------------------------------------------------------------------------

## 19. `islower()` / `isupper()`

``` python
print("hello".islower())
# True

print("HELLO".isupper())
# True
```

------------------------------------------------------------------------

# 10. String Formatting

## f-strings

The most convenient modern approach:

``` python
name = "Rahul"
age = 18

print(f"My name is {name} and I am {age} years old.")
```

You can include expressions:

``` python
a = 10
b = 20

print(f"Sum = {a + b}")
```

------------------------------------------------------------------------

# 11. Methods vs Built-in Functions

This distinction is important.

### Method

Called using an object:

``` python
numbers.append(5)
text.upper()
student.get("name")
```

### Built-in Function

Called directly:

``` python
len(numbers)
type(numbers)
max(numbers)
sum(numbers)
sorted(numbers)
```

> **Rule of thumb:** `object.method()` is a method; `function(object)`
> is a function.

------------------------------------------------------------------------

# 12. Mutable vs Immutable Cheat Sheet

  Type      Mutable?   Ordered?               Duplicates?
  --------- ---------- ---------------------- -------------
  `list`    Yes        Yes                    Yes
  `tuple`   No         Yes                    Yes
  `set`     Yes        No positional order    No
  `dict`    Yes        Yes, insertion order   Keys: No
  `str`     No         Yes                    Yes

------------------------------------------------------------------------

# 13. High-Priority Comparisons

## List

``` text
append  → add one item
extend  → add multiple items
insert  → add at an index
remove  → remove by value
pop     → remove by index and return item
clear   → remove everything
```

## Set

``` text
add       → add one item
update    → add multiple items
remove    → remove item, error if absent
discard   → remove item, no error if absent
pop       → remove arbitrary item
```

## Dictionary

``` text
get        → safely retrieve value
update     → add/update pairs
pop        → remove specified key
popitem    → remove last inserted pair
setdefault → retrieve or insert default
```

## String

``` text
lower/upper       → change case
strip             → remove surrounding whitespace
replace           → replace text
split             → string → list
join              → iterable of strings → string
find              → search, -1 if absent
index             → search, error if absent
startswith        → check beginning
endswith          → check ending
```

------------------------------------------------------------------------

# 14. Methods That Modify the Original Object

## Usually modify the object

``` python
list.append()
list.extend()
list.insert()
list.remove()
list.pop()
list.clear()
list.sort()
list.reverse()

set.add()
set.update()
set.remove()
set.discard()
set.pop()
set.clear()

dict.update()
dict.pop()
dict.popitem()
dict.setdefault()
dict.clear()
```

## Strings do NOT change in place

Because strings are immutable:

``` python
text = "hello"

text.upper()

print(text)
# hello
```

You must assign the returned string:

``` python
text = text.upper()

print(text)
# HELLO
```

------------------------------------------------------------------------

# 15. Common Mistakes

## Mistake 1 --- Confusing `append()` and `extend()`

``` python
a = [1, 2]
a.append([3, 4])

# [1, 2, [3, 4]]
```

vs.

``` python
a = [1, 2]
a.extend([3, 4])

# [1, 2, 3, 4]
```

------------------------------------------------------------------------

## Mistake 2 --- Expecting `sort()` to return the sorted list

``` python
numbers = [3, 1, 2]

result = numbers.sort()

print(result)
# None
```

Use:

``` python
numbers.sort()
```

or:

``` python
result = sorted(numbers)
```

------------------------------------------------------------------------

## Mistake 3 --- Assuming `set.pop()` removes the last element

It does not guarantee a particular positional element.

``` python
s = {10, 20, 30}

s.pop()
```

The removed element is arbitrary.

------------------------------------------------------------------------

## Mistake 4 --- Trying to modify a string

``` python
text = "hello"

# text[0] = "H"   # TypeError
```

Instead:

``` python
text = "H" + text[1:]
```

------------------------------------------------------------------------

## Mistake 5 --- Using `{}` for an empty set

``` python
x = {}
print(type(x))
# <class 'dict'>
```

Correct:

``` python
x = set()
```

------------------------------------------------------------------------

# 16. One-Page Method Map

``` text
LIST
│
├── Add
│   ├── append()
│   ├── extend()
│   └── insert()
│
├── Remove
│   ├── remove()
│   ├── pop()
│   └── clear()
│
├── Search
│   ├── index()
│   └── count()
│
├── Rearrange
│   ├── sort()
│   └── reverse()
│
└── Copy
    └── copy()


TUPLE
│
├── Search
│   ├── index()
│   └── count()
│
└── Mostly uses built-in functions
    ├── len()
    ├── min()
    ├── max()
    └── sum()


SET
│
├── Add
│   ├── add()
│   └── update()
│
├── Remove
│   ├── remove()
│   ├── discard()
│   ├── pop()
│   └── clear()
│
├── Set Operations
│   ├── union()
│   ├── intersection()
│   ├── difference()
│   └── symmetric_difference()
│
└── Relationships
    ├── issubset()
    ├── issuperset()
    └── isdisjoint()


DICTIONARY
│
├── Access
│   ├── get()
│   ├── keys()
│   ├── values()
│   └── items()
│
├── Add / Update
│   ├── update()
│   └── setdefault()
│
├── Remove
│   ├── pop()
│   ├── popitem()
│   └── clear()
│
└── Copy / Create
    ├── copy()
    └── fromkeys()


STRING
│
├── Case
│   ├── lower()
│   ├── upper()
│   ├── capitalize()
│   ├── title()
│   └── swapcase()
│
├── Clean / Replace
│   ├── strip()
│   ├── lstrip()
│   ├── rstrip()
│   └── replace()
│
├── Split / Join
│   ├── split()
│   └── join()
│
├── Search
│   ├── find()
│   ├── index()
│   └── count()
│
└── Check
    ├── startswith()
    ├── endswith()
    ├── isalpha()
    ├── isdigit()
    ├── isalnum()
    ├── isspace()
    ├── islower()
    └── isupper()
```

------------------------------------------------------------------------

# 17. What to Memorize First

Don't try to memorize every method equally.

## Tier 1 --- Must Know

### List

``` python
append()
extend()
insert()
remove()
pop()
sort()
reverse()
index()
count()
```

### Tuple

``` python
count()
index()
```

### Set

``` python
add()
update()
remove()
discard()
union()
intersection()
difference()
```

### Dictionary

``` python
get()
keys()
values()
items()
update()
pop()
popitem()
setdefault()
```

### String

``` python
lower()
upper()
strip()
replace()
split()
join()
find()
count()
startswith()
endswith()
```

## Tier 2 --- Learn Soon

``` python
list.copy()
set.copy()
dict.copy()
set.symmetric_difference()
set.issubset()
set.issuperset()
set.isdisjoint()
str.capitalize()
str.title()
str.isalpha()
str.isdigit()
str.isalnum()
```

## Tier 3 --- Learn When Needed

Methods such as `dict.fromkeys()` and less frequently used string
predicates can be learned as you encounter them in projects.

------------------------------------------------------------------------

# 18. Final Mental Model

When you see a Python collection, ask:

``` text
What type is it?
      ↓
Can I modify it?
      ↓
How do I access its elements?
      ↓
How do I add elements?
      ↓
How do I remove elements?
      ↓
How do I search?
      ↓
How do I transform it?
```

### The most important distinction

``` text
LIST       → ordered + mutable + duplicates
TUPLE      → ordered + immutable + duplicates
SET        → unique elements + set operations
DICTIONARY → key → value
STRING     → immutable sequence of characters
```

> **Best way to learn these:** write small programs using each method.
> Reading the method list repeatedly will create familiarity, but
> actually using the methods is what builds recall.
