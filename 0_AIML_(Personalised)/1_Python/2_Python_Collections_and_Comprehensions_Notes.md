# Python Collections and Comprehensions --- Study Notes

**Topics:** Lists, Tuples, Sets, Dictionaries, and Comprehensions\
**Focus:** Definitions, syntax, use cases, important methods, examples,
common mistakes, and Data Science / AI / ML connections.

## 1. Big Picture

  ------------------------------------------------------------------------------------
  Structure    Syntax              Ordered?     Mutable?    Duplicates?   Main use
  ------------ ------------------- ------------ ----------- ------------- ------------
  List         `[1, 2, 3]`         Yes          Yes         Allowed       Changeable
                                                                          sequence

  Tuple        `(1, 2, 3)`         Yes          No\*        Allowed       Fixed
                                                                          sequence /
                                                                          record

  Set          `{1, 2, 3}`         No           Yes         Not allowed   Unique
                                   positional                             values / set
                                   order                                  operations

  Dictionary   `{"name": "Ava"}`   Yes,         Yes         Keys are      Key-value
                                   insertion                unique        lookup
                                   order                                  
  ------------------------------------------------------------------------------------

\*A tuple's items cannot be reassigned, but a tuple can contain a
mutable object such as a list.

-   Need a changeable sequence? **List**
-   Need a fixed sequence? **Tuple**
-   Need unique values or set operations? **Set**
-   Need key-to-value lookup? **Dictionary**
-   Need to build a collection from an iterable compactly?
    **Comprehension**

------------------------------------------------------------------------

# 2. Lists

## Definition

A **list** is an ordered, mutable collection that can contain duplicate
values and mixed data types.

## Syntax

``` python
numbers = [10, 20, 30]
mixed = [10, "Python", 3.5, True]
empty = []
```

Lists use square brackets `[]`.

## Use cases

Use lists when order matters, duplicates are allowed, and you need to
add, remove, replace, index, or slice items. Examples include scores,
file names, predictions, and sequences of results.

## Accessing and slicing

``` python
languages = ["Python", "C++", "Java", "SQL"]

languages[0]    # 'Python'
languages[-1]   # 'SQL'
languages[1:3]  # ['C++', 'Java']
languages[:2]   # ['Python', 'C++']
languages[::-1] # reversed copy
```

Python uses **zero-based indexing**. A slice `start:stop` includes
`start` but excludes `stop`. Negative indices count from the end.

## Updating

``` python
scores = [70, 80, 90]
scores[1] = 85
# [70, 85, 90]
```

## Important methods

Assume `items = [10, 20, 30]`.

  --------------------------------------------------------------------------
  Method                  Purpose                 Example
  ----------------------- ----------------------- --------------------------
  `append(x)`             Add one object at the   `items.append(40)`
                          end                     

  `extend(iterable)`      Add each item from an   `items.extend([40, 50])`
                          iterable                

  `insert(i, x)`          Insert at index         `items.insert(1, 15)`

  `remove(x)`             Remove first matching   `items.remove(20)`
                          value                   

  `pop(i)`                Remove and return item; `last = items.pop()`
                          defaults to last        

  `clear()`               Remove all items        `items.clear()`

  `index(x)`              Index of first match    `items.index(20)`

  `count(x)`              Count occurrences       `[1, 2, 1].count(1)`

  `sort()`                Sort in place           `items.sort()`

  `reverse()`             Reverse in place        `items.reverse()`

  `copy()`                Shallow copy            `other = items.copy()`
  --------------------------------------------------------------------------

### `append()` vs `extend()`

``` python
a = [1, 2]
a.append([3, 4])
# [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])
# [1, 2, 3, 4]
```

`append()` adds its argument as one item; `extend()` adds each item from
the iterable.

### `sort()` vs `sorted()`

``` python
values = [3, 1, 2]
result = sorted(values)  # new list; original unchanged
values.sort()            # changes values in place
```

`list.sort()` returns `None`; do not assign its result back to the list.

### Useful built-ins

``` python
values = [4, 2, 8, 6]

len(values)       # 4
min(values)       # 2
max(values)       # 8
sum(values)       # 20
sorted(values)    # [2, 4, 6, 8]
any([False, True])  # True
all([True, True])   # True
```

## Membership and iteration

``` python
if "Python" in languages:
    print("Found")

for language in languages:
    print(language)
```

## Common mistakes

-   Using `append([3, 4])` when you meant to add `3` and `4`
    individually.
-   Writing `values = values.sort()`; the result becomes `None`.
-   Accessing an index that does not exist, which raises `IndexError`.

**Data Science connection:** Lists are useful for simple sequences and
collecting results. Large numerical calculations are usually better
suited to NumPy arrays.

------------------------------------------------------------------------

# 3. Tuples

## Definition

A **tuple** is an ordered collection whose item references cannot be
reassigned after creation. It allows duplicates and mixed data types.

## Syntax

``` python
point = (3, 5)
record = ("Ava", 19, "CSE")
empty = ()
single = (42,)  # comma is essential
```

`(42)` is an integer, not a tuple. A single-element tuple needs a comma.

## Use cases

Use tuples for fixed records, coordinates, returning multiple values
from functions, and as dictionary keys when all elements are hashable.

## Access and unpacking

``` python
person = ("Ava", 19, "CSE")
person[0]  # 'Ava'

name, age, branch = person

first, *middle, last = [10, 20, 30, 40]
# first=10, middle=[20, 30], last=40
```

## Methods

Tuples have two main methods:

``` python
values = (10, 20, 10, 30)
values.count(10)  # 2
values.index(20)  # 1
```

They also support indexing, slicing, concatenation, repetition, and
`len()`:

``` python
(1, 2) + (3, 4)  # (1, 2, 3, 4)
(1, 2) * 2       # (1, 2, 1, 2)
len((1, 2, 3))   # 3
```

## Important nuance: immutability

``` python
data = ([1, 2], "Python")
data[0].append(3)  # allowed: inner list changes
# data[0] = [9, 9]  # TypeError
```

The tuple cannot reassign its item, but a mutable object inside it can
still change.

**Data Science connection:** NumPy shapes are tuples, such as `(100, 5)`
for 100 rows and 5 columns.

------------------------------------------------------------------------

# 4. Sets

## Definition

A **set** is a mutable collection of unique, hashable elements. It does
not support positional indexing.

## Syntax

``` python
numbers = {1, 2, 3, 3}
empty_set = set()
empty_dict = {}  # empty dictionary, not set
```

Set elements must be hashable. Lists and dictionaries cannot be set
elements.

## Use cases

Use sets to remove duplicates, test membership, or compare groups of
unique values.

## Important methods

Assume `s = {1, 2, 3}`.

  Method               Purpose
  -------------------- ----------------------------------------
  `add(x)`             Add one element
  `update(iterable)`   Add elements from an iterable
  `remove(x)`          Remove; raises `KeyError` if absent
  `discard(x)`         Remove if present; no error if absent
  `pop()`              Remove and return an arbitrary element
  `clear()`            Remove all elements
  `copy()`             Shallow copy

``` python
s.add(4)
s.update([5, 6])
s.discard(99)  # no error
# s.remove(99) # KeyError
```

Do not rely on which element `pop()` returns.

## Set operations

``` python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A | B  # union: {1, 2, 3, 4, 5, 6}
A & B  # intersection: {3, 4}
A - B  # difference: {1, 2}
A ^ B  # symmetric difference: {1, 2, 5, 6}
```

-   **Union:** elements in either set
-   **Intersection:** elements in both sets
-   **Difference:** elements in the first but not the second
-   **Symmetric difference:** elements in exactly one of the sets

Relationships:

``` python
A = {1, 2}
B = {1, 2, 3}

A.issubset(B)         # True
B.issuperset(A)       # True
A.isdisjoint({8, 9})  # True
```

## Remove duplicates from a list

``` python
values = [1, 2, 2, 3, 1]
unique_values = set(values)
```

Set order is not guaranteed. To preserve first-occurrence order:

``` python
unique_values = list(dict.fromkeys(values))
# [1, 2, 3]
```

## Frozen sets

`frozenset` is an immutable set:

``` python
fixed = frozenset([1, 2, 3])
```

**Data Science connection:** Sets are useful for unique labels and
category comparisons. Pandas also has `unique()` and `drop_duplicates()`
for tabular data.

------------------------------------------------------------------------

# 5. Dictionaries

## Definition

A **dictionary** is a mutable mapping from unique, hashable keys to
values. Dictionaries preserve insertion order in modern Python.

## Syntax

``` python
student = {
    "name": "Ava",
    "age": 19,
    "branch": "CSE"
}

empty = {}
also_empty = dict()
```

Keys must be hashable. Values may be lists, dictionaries, or other
objects.

## Use cases

Use dictionaries for key-based lookup, configuration, structured
records, label mappings, and frequency counts.

## Access values

``` python
student = {"name": "Ava", "age": 19}

student["name"]  # 'Ava'
student.get("city")  # None
student.get("city", "Unknown")  # 'Unknown'
```

`student["missing"]` raises `KeyError`. `get()` returns a default and
does not insert the key.

## Add and update

``` python
student["city"] = "Panipat"
student["age"] = 20
student.update({"age": 21, "year": 2})
```

## Important methods

  Method                       Purpose
  ---------------------------- -----------------------------------------
  `get(key, default)`          Return value or default safely
  `keys()`                     Dynamic view of keys
  `values()`                   Dynamic view of values
  `items()`                    Dynamic view of key-value pairs
  `update(other)`              Add/update entries
  `pop(key)`                   Remove key and return value
  `popitem()`                  Remove and return last inserted pair
  `setdefault(key, default)`   Return value; insert default if missing
  `clear()`                    Remove all entries
  `copy()`                     Shallow copy
  `fromkeys(keys, value)`      Build a dictionary from keys

``` python
student.keys()
student.values()
student.items()

for key, value in student.items():
    print(key, value)
```

### `get()` vs `setdefault()`

``` python
d = {"a": 1}

d.get("b", 0)         # returns 0; d unchanged
d.setdefault("b", 0)  # returns 0; inserts "b": 0
```

### Counting with a dictionary

``` python
words = ["ai", "python", "ai", "data", "python", "ai"]
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

# {'ai': 3, 'python': 2, 'data': 1}
```

### `fromkeys()` mutable-value trap

``` python
d = dict.fromkeys(["a", "b"], [])
d["a"].append(1)
# Both d["a"] and d["b"] refer to the same list.
```

For independent lists, use:

``` python
d = {key: [] for key in ["a", "b"]}
```

**Data Science connection:** Dictionaries are useful for label-to-ID
mappings, counts, configuration, JSON-like data, and building DataFrames
from columns.

------------------------------------------------------------------------

# 6. Comprehensions

## Definition

A **comprehension** is a compact way to construct a collection from an
iterable, optionally transforming and filtering its elements.

Types: - List comprehension - Set comprehension - Dictionary
comprehension - Generator expression (lazy iterator, not an eagerly
created collection)

## Why use them?

They often make simple collection-building loops shorter and clearer.
Prefer a normal loop when the logic becomes complicated.

## List comprehension

Syntax:

``` python
[expression for item in iterable]
```

Example:

``` python
squares = [n ** 2 for n in range(1, 6)]
# [1, 4, 9, 16, 25]
```

Equivalent loop:

``` python
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
```

### With a filter

``` python
evens = [n for n in range(1, 11) if n % 2 == 0]
# [2, 4, 6, 8, 10]
```

Transform and filter:

``` python
squares_of_evens = [n ** 2 for n in range(1, 11) if n % 2 == 0]
```

## Filtering vs conditional expression

Filter: only include matching items.

``` python
[n for n in range(1, 6) if n % 2 == 0]
```

Conditional expression: include every item but choose its output value.

``` python
["even" if n % 2 == 0 else "odd" for n in range(1, 6)]
```

## Set comprehension

Syntax:

``` python
{expression for item in iterable}
```

Example:

``` python
lengths = {len(word) for word in ["AI", "data", "ML", "data"]}
# {2, 4}
```

## Dictionary comprehension

Syntax:

``` python
{key_expression: value_expression for item in iterable}
```

Example:

``` python
squares = {n: n ** 2 for n in range(1, 6)}
```

With filtering:

``` python
even_squares = {n: n ** 2 for n in range(1, 11) if n % 2 == 0}
```

From two lists:

``` python
names = ["Ava", "Ravi", "Mina"]
scores = [90, 85, 95]

score_map = {name: score for name, score in zip(names, scores)}
```

If keys repeat, later values overwrite earlier values.

## Nested comprehension

Flatten a nested list:

``` python
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [value for row in matrix for value in row]
# [1, 2, 3, 4, 5, 6]
```

This follows the same order as:

``` python
flat = []
for row in matrix:
    for value in row:
        flat.append(value)
```

## Generator expression

``` python
squares = (n ** 2 for n in range(1, 6))
```

A generator yields values as requested rather than immediately storing
them all in a list:

``` python
for value in squares:
    print(value)
```

Generators can help when processing large sequences without needing
every result in memory.

## Comprehension use cases

  Goal                   Example
  ---------------------- --------------------------------------
  Transform              `[x * 2 for x in values]`
  Filter                 `[x for x in values if x > 0]`
  Transform + filter     `[x**2 for x in values if x > 0]`
  Unique results         `{x.lower() for x in words}`
  Create mapping         `{x: x**2 for x in values}`
  Flatten nested lists   `[x for row in matrix for x in row]`

------------------------------------------------------------------------

# 7. Comparison Table

  --------------------------------------------------------------------------------
  Feature        List           Tuple          Set                Dictionary
  -------------- -------------- -------------- ------------------ ----------------
  Stores         Values         Values         Unique values      Key-value pairs

  Syntax         `[]`           `()`           `{...}` / `set()`  `{key: value}`

  Indexing       Yes            Yes            No                 By key

  Mutable        Yes            No             Yes                Yes
  container                                                       

  Duplicates     Yes            Yes            No                 Keys: no

  Insertion      Yes            Yes            No                 Yes
  order                                        positional-order   
                                               guarantee          

  Main strength  Flexible       Fixed sequence Uniqueness         Key lookup
                 sequence                                         
  --------------------------------------------------------------------------------

------------------------------------------------------------------------

# 8. Mutability and Copying

Lists, sets, and dictionaries are mutable. Tuples are immutable
containers, but may contain mutable objects. `frozenset` is immutable.

``` python
a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3] — same list object
```

Shallow copy:

``` python
a = [1, 2]
b = a.copy()
b.append(3)

print(a)  # [1, 2]
print(b)  # [1, 2, 3]
```

A shallow copy does not recursively copy nested mutable objects.

------------------------------------------------------------------------

# 9. Common Mistakes

1.  `{}` creates an empty dictionary; use `set()` for an empty set.
2.  A one-element tuple needs a comma: `(5,)`.
3.  Sets do not support positional indexing.
4.  Lists and dictionaries cannot be set elements or dictionary keys
    because they are unhashable.
5.  `append()` and `extend()` behave differently.
6.  `list.sort()` modifies the list and returns `None`.
7.  `dict[key]` raises `KeyError` if the key is absent; use `get()` if
    appropriate.
8.  `get()` does not insert a missing key; `setdefault()` can.
9.  Overly complex comprehensions are hard to maintain.
10. Tuples do not make nested mutable objects immutable.
11. `dict.fromkeys(keys, [])` shares one list among all keys.
12. Duplicate dictionary keys overwrite earlier values.

------------------------------------------------------------------------

# 10. Data Science / AI / ML Connections

### Lists

Useful for simple sequences; use NumPy arrays for large-scale numerical
operations.

### Tuples

Common for coordinates and array shapes:

``` python
import numpy as np
arr = np.zeros((100, 5))
print(arr.shape)  # (100, 5)
```

### Sets

Useful for checking labels that appear in one group but not another:

``` python
train_labels = {"cat", "dog"}
test_labels = {"cat", "bird"}
unseen = test_labels - train_labels
# {'bird'}
```

### Dictionaries

Useful for mappings:

``` python
label_to_id = {"cat": 0, "dog": 1}
```

### Comprehensions

Useful for simple filtering:

``` python
scores = [45, 72, 88, 39, 91]
passed = [score for score in scores if score >= 50]
```

For large numerical transformations, prefer vectorized NumPy/Pandas
operations where appropriate.

------------------------------------------------------------------------

# 11. Practice Questions

Try these before checking the solutions.

## Beginner

1.  Create a list of five subjects. Print the first and last.
2.  Demonstrate `append()` vs `extend()`.
3.  Sort a list without changing the original.
4.  Create a one-element tuple containing `10`.
5.  Convert `[1, 2, 2, 3, 3, 4]` to a set.
6.  Find the union and intersection of two sets.
7.  Create a student dictionary and read a value with `get()`.
8.  Count word frequencies using a dictionary.
9.  Use a list comprehension to create squares from 1 to 10.
10. Select numbers divisible by 3 from 1 to 30.

## Intermediate

11. Keep only words longer than four characters.
12. Use a set comprehension to find unique first letters.
13. Map numbers 1--5 to their cubes using a dictionary comprehension.
14. Flatten `[[1, 2], [3, 4], [5, 6]]`.
15. Combine names and marks into a dictionary using `zip()`.
16. Explain `get()` vs `setdefault()`.
17. Explain why a tuple containing a list is not deeply immutable.
18. When would you choose a set instead of a list?

## Selected solutions

``` python
# 3. Sort without modifying the original
numbers = [4, 1, 3, 2]
sorted_numbers = sorted(numbers)

# 4. Single-element tuple
single = (10,)

# 5. Remove duplicates
unique_numbers = set([1, 2, 2, 3, 3, 4])

# 6. Set operations
A = {1, 2, 3}
B = {3, 4, 5}
union = A | B
intersection = A & B

# 8. Word frequency
words = ["ai", "python", "ai", "data", "python", "ai"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

# 9. Squares
squares = [n ** 2 for n in range(1, 11)]

# 10. Multiples of 3
multiples = [n for n in range(1, 31) if n % 3 == 0]

# 11. Longer words
words = ["data", "science", "AI", "python"]
long_words = [word for word in words if len(word) > 4]

# 12. Unique first letters
first_letters = {word[0].lower() for word in words if word}

# 13. Number-to-cube mapping
cubes = {n: n ** 3 for n in range(1, 6)}

# 14. Flatten nested list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [value for row in matrix for value in row]

# 15. Names-to-marks mapping
names = ["Ava", "Ravi", "Mina"]
marks = [90, 85, 95]
mark_map = {name: mark for name, mark in zip(names, marks)}
```

------------------------------------------------------------------------

# 12. Quick Revision

-   **List:** ordered, mutable, duplicates allowed. Key methods:
    `append`, `extend`, `insert`, `remove`, `pop`, `sort`.
-   **Tuple:** ordered, immutable container. Key methods: `count`,
    `index`. Single item requires a comma.
-   **Set:** unique hashable values. Key methods: `add`, `update`,
    `discard`, `remove`; operations: `|`, `&`, `-`, `^`.
-   **Dictionary:** key-value mapping. Key methods: `get`, `items`,
    `keys`, `values`, `update`, `pop`, `setdefault`.
-   **List comprehension:**
    `[expression for item in iterable if condition]`.
-   **Set comprehension:**
    `{expression for item in iterable if condition}`.
-   **Dictionary comprehension:**
    `{key: value for item in iterable if condition}`.
-   **Generator expression:** `(expression for item in iterable)`;
    values are produced lazily.

## Final mental model

``` text
Changeable ordered sequence? → List
Fixed sequence?               → Tuple
Unique values / set math?     → Set
Key → value mapping?          → Dictionary
Compact collection building?  → Comprehension
```
