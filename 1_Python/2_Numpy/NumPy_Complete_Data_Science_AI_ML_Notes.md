# NumPy --- Complete Data Science, AI & Machine Learning Notes

> A practical NumPy reference for Data Science, Machine Learning, Deep
> Learning and AI.
>
> **Core idea:** NumPy is mainly about efficient numerical computation
> with multidimensional arrays.

------------------------------------------------------------------------

# 1. What is NumPy?

## Definition

**NumPy (Numerical Python)** is a Python library for fast numerical and
scientific computing. Its central data structure is the **NumPy array
(`ndarray`)**.

## Simple Meaning

Python lists are general-purpose containers. NumPy arrays are designed
specifically for numerical data and allow efficient operations on entire
arrays.

``` python
import numpy as np

arr = np.array([10, 20, 30])
print(arr)
```

## Why NumPy Matters

NumPy is a foundation for the Python data-science ecosystem:

``` text
Python → NumPy → Pandas / Matplotlib / SciPy → ML → AI / Deep Learning
```

Many data-science and ML libraries work with NumPy arrays or NumPy-like
array concepts.

------------------------------------------------------------------------

# 2. Installation and Import

``` bash
pip install numpy
```

Standard import:

``` python
import numpy as np
```

`np` is only an alias.

------------------------------------------------------------------------

# 3. NumPy `ndarray`

## Definition

`ndarray` means **N-dimensional array** and is NumPy's primary array
object.

``` python
arr = np.array([1, 2, 3, 4])

print(type(arr))
# <class 'numpy.ndarray'>
```

## Dimensions

``` text
0D → scalar
1D → vector
2D → matrix/table
3D → collection of matrices
4D+ → higher-dimensional data
```

Examples:

``` python
np.array(10)                         # 0D
np.array([1, 2, 3])                  # 1D
np.array([[1, 2], [3, 4]])           # 2D
np.array([[[1, 2]], [[3, 4]]])       # 3D
```

------------------------------------------------------------------------

# 4. Creating Arrays

## From a List

``` python
arr = np.array([1, 2, 3, 4])
```

## From a Tuple

``` python
arr = np.array((1, 2, 3, 4))
```

## 2D Array

``` python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

## Specify `dtype`

``` python
arr = np.array([1, 2, 3], dtype=np.float32)
```

------------------------------------------------------------------------

# 5. Important Array Attributes

``` python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

  Attribute    Meaning                      Example
  ------------ ---------------------------- ------------------
  `ndim`       Number of dimensions         `2`
  `shape`      Size of each dimension       `(2, 3)`
  `size`       Total elements               `6`
  `dtype`      Element data type            `int64` etc.
  `itemsize`   Bytes per element            depends on dtype
  `nbytes`     Bytes used by element data   depends on array

``` python
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.itemsize)
print(arr.nbytes)
```

## Most Important Distinction

``` text
ndim  → How many dimensions?
shape → How large is each dimension?
size  → How many elements in total?
dtype → What type are the elements?
```

------------------------------------------------------------------------

# 6. Python List vs NumPy Array

Python list:

``` python
a = [1, 2, 3]
print(a * 2)
# [1, 2, 3, 1, 2, 3]
```

NumPy array:

``` python
a = np.array([1, 2, 3])
print(a * 2)
# [2 4 6]
```

NumPy is optimized for numerical, array-oriented workloads and can
execute many operations in efficient compiled code.

> NumPy is not automatically faster for every possible task. Its
> advantage is strongest for suitable numerical workloads.

------------------------------------------------------------------------

# 7. NumPy Data Types

Common NumPy dtypes include:

``` text
int8, int16, int32, int64
uint8, uint16, ...
float16, float32, float64
complex64, complex128
bool
```

Example:

``` python
arr = np.array([1, 2, 3], dtype=np.float32)

print(arr.dtype)
```

## Why `dtype` Matters in ML

It affects:

-   memory usage,
-   precision,
-   computation,
-   compatibility,
-   sometimes model performance.

`float32` is very common in ML/deep-learning workloads.

------------------------------------------------------------------------

# 8. Type Conversion with `astype()`

``` python
arr = np.array([1, 2, 3])

float_arr = arr.astype(np.float64)

print(float_arr)
print(float_arr.dtype)
```

Example:

``` python
arr = np.array([1.2, 2.8, 3.9])
int_arr = arr.astype(int)

print(int_arr)
```

> Converting floats to integers removes the fractional part; it does not
> perform normal rounding.

------------------------------------------------------------------------

# 9. Array Creation Functions

## `np.zeros()`

``` python
np.zeros(5)
np.zeros((2, 3))
```

## `np.ones()`

``` python
np.ones(5)
np.ones((2, 3))
```

## `np.full()`

``` python
np.full((2, 3), 7)
```

## `np.empty()`

``` python
arr = np.empty((2, 3))
```

> `empty()` does not initialize elements to zero. Use `zeros()` when you
> need zeros.

## Identity Matrix

``` python
np.eye(3)
np.identity(3)
```

## `np.arange()`

``` python
np.arange(0, 10)
# 0 through 9

np.arange(0, 10, 2)
# 0, 2, 4, 6, 8
```

> The stop value is normally excluded.

## `np.linspace()`

``` python
np.linspace(0, 10, 5)
# [0. , 2.5, 5. , 7.5, 10.]
```

### `arange()` vs `linspace()`

``` text
arange()   → control the step
linspace() → control the number of points
```

For floating-point ranges where an exact number of samples is required,
`linspace()` is often preferable.

## `np.logspace()`

``` python
np.logspace(0, 3, 4)
```

Conceptually creates values based on:

``` text
10^0, 10^1, 10^2, 10^3
```

------------------------------------------------------------------------

# 10. Random Numbers

Modern NumPy code should generally use a random `Generator`.

``` python
rng = np.random.default_rng(42)
```

The seed makes results reproducible.

## Random Floats

``` python
rng.random(5)
rng.random((2, 3))
```

Values are in `[0, 1)`.

## Random Integers

``` python
rng.integers(1, 10, size=5)
```

`1` is inclusive and `10` is exclusive.

## Normal Distribution

``` python
rng.normal(loc=0, scale=1, size=5)
```

## Choice

``` python
rng.choice([10, 20, 30], size=5)
```

Without replacement:

``` python
rng.choice([10, 20, 30], size=2, replace=False)
```

## Shuffle

``` python
arr = np.array([1, 2, 3, 4, 5])
rng.shuffle(arr)
```

`shuffle()` changes the supplied array.

## Permutation

``` python
arr = np.array([1, 2, 3, 4, 5])
shuffled = rng.permutation(arr)
```

`permutation()` returns a permuted result.

> Reproducible randomness is important when debugging ML experiments and
> comparing results.

------------------------------------------------------------------------

# 11. Indexing

``` python
arr = np.array([10, 20, 30, 40])

arr[0]     # 10
arr[-1]    # 40
```

NumPy uses zero-based indexing.

## 2D Indexing

``` python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 1])
# 20
```

The standard mental model is:

``` python
arr[row, column]
```

------------------------------------------------------------------------

# 12. Slicing

General form:

``` python
array[start:stop:step]
```

Example:

``` python
arr = np.array([10, 20, 30, 40, 50])

arr[1:4]
# [20 30 40]

arr[:3]
# [10 20 30]

arr[2:]
# [30 40 50]

arr[::-1]
# reversed
```

## 2D Slicing

``` python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```

First two rows:

``` python
arr[:2]
```

First two columns:

``` python
arr[:, :2]
```

Rows 1 onward, columns 1 onward:

``` python
arr[1:, 1:]
```

Specific row:

``` python
arr[1, :]
```

Specific column:

``` python
arr[:, 1]
```

------------------------------------------------------------------------

# 13. Views vs Copies

This is **very important** in NumPy.

Basic slicing often creates a **view**.

``` python
arr = np.array([1, 2, 3, 4])

view = arr[1:3]
view[0] = 99

print(arr)
# [1, 99, 3, 4]
```

The original changed.

For an independent array:

``` python
copy_arr = arr[1:3].copy()
```

Then modifying `copy_arr` does not modify `arr`.

> Always think about whether you are working with the original data, a
> view, or a copy.

------------------------------------------------------------------------

# 14. Reshaping

## `reshape()`

Changes the shape while keeping the same number of elements.

``` python
arr = np.arange(6)

new_arr = arr.reshape(2, 3)

print(new_arr)
# [[0 1 2]
#  [3 4 5]]
```

The total number of elements must remain unchanged.

``` text
6 = 2 × 3 = 1 × 6 = 3 × 2
```

## Using `-1`

``` python
arr = np.arange(12)

arr.reshape(3, -1)
# shape → (3, 4)
```

NumPy infers the missing dimension.

Only one dimension can be inferred with `-1`.

------------------------------------------------------------------------

# 15. Flattening

## `flatten()`

Returns a flattened copy.

``` python
arr = np.array([
    [1, 2],
    [3, 4]
])

flat = arr.flatten()
```

## `ravel()`

Returns a flattened array and may return a view when possible.

``` python
flat = arr.ravel()
```

### Difference

``` text
flatten() → always copy
ravel()   → view when possible, otherwise copy
```

------------------------------------------------------------------------

# 16. Transpose

For a 2D array:

``` python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.T)
```

Result:

``` text
[[1 4]
 [2 5]
 [3 6]]
```

Also:

``` python
np.transpose(arr)
```

> For higher-dimensional arrays, transposition involves axis ordering;
> `.T` reverses the axes rather than simply swapping rows and columns.

------------------------------------------------------------------------

# 17. Adding and Removing Dimensions

## `np.newaxis`

``` python
arr = np.array([1, 2, 3])

row = arr[np.newaxis, :]
column = arr[:, np.newaxis]

print(row.shape)
# (1, 3)

print(column.shape)
# (3, 1)
```

## `expand_dims()`

``` python
np.expand_dims(arr, axis=0)
```

## `squeeze()`

Removes axes whose length is 1.

``` python
arr = np.array([[1, 2, 3]])

print(arr.shape)
# (1, 3)

print(np.squeeze(arr).shape)
# (3,)
```

These operations are extremely useful when matching ML input shapes.

------------------------------------------------------------------------

# 18. Concatenation and Stacking

## `np.concatenate()`

``` python
a = np.array([1, 2])
b = np.array([3, 4])

np.concatenate((a, b))
# [1 2 3 4]
```

For 2D arrays, `axis` controls the direction.

## `vstack()`

``` python
a = np.array([1, 2])
b = np.array([3, 4])

np.vstack((a, b))
```

Conceptually:

``` text
[[1 2]
 [3 4]]
```

## `hstack()`

``` python
np.hstack((a, b))
```

Conceptually:

``` text
[1 2 3 4]
```

## `column_stack()`

Useful for creating feature columns:

``` python
age = np.array([18, 19, 20])
marks = np.array([80, 90, 85])

X = np.column_stack((age, marks))
```

------------------------------------------------------------------------

# 19. Splitting

## `np.split()`

``` python
arr = np.array([1, 2, 3, 4])

parts = np.split(arr, 2)
```

## `np.array_split()`

Can handle uneven splits.

``` python
arr = np.array([1, 2, 3, 4, 5])

parts = np.array_split(arr, 2)
```

------------------------------------------------------------------------

# 20. Element-wise Arithmetic

``` python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

a + b
a - b
a * b
a / b
a ** 2
```

NumPy performs these element by element when shapes are compatible.

## Scalar Operations

``` python
arr = np.array([1, 2, 3])

arr + 10
arr * 2
arr ** 2
```

This is vectorized computation.

------------------------------------------------------------------------

# 21. Comparison Operations

``` python
arr = np.array([10, 20, 30, 40])

arr > 20
```

Result:

``` text
[False False True True]
```

Other comparisons:

``` python
arr == 20
arr != 20
arr >= 20
arr < 30
```

These produce Boolean arrays.

------------------------------------------------------------------------

# 22. Boolean Masking

One of the most important NumPy techniques for Data Science.

``` python
arr = np.array([10, 20, 30, 40, 50])

mask = arr > 25

print(arr[mask])
# [30 40 50]
```

Short form:

``` python
arr[arr > 25]
```

This is commonly used for filtering numerical data.

------------------------------------------------------------------------

# 23. Multiple Conditions

For element-wise conditions use:

``` text
& → AND
| → OR
~ → NOT
```

Example:

``` python
arr = np.array([10, 20, 30, 40, 50])

result = arr[(arr > 20) & (arr < 50)]

print(result)
# [30 40]
```

Use parentheses:

``` python
(arr > 20) & (arr < 50)
```

Do not use Python's `and`/`or` for element-wise NumPy array conditions.

------------------------------------------------------------------------

# 24. `where()`

Returns indices satisfying a condition:

``` python
arr = np.array([10, 20, 30, 40])

np.where(arr > 20)
```

It can also choose between two values:

``` python
result = np.where(arr > 20, "High", "Low")
```

This is useful for data transformation and feature engineering.

------------------------------------------------------------------------

# 25. `any()` and `all()`

## `any()`

True if at least one condition is true.

``` python
arr = np.array([1, 2, 3])

np.any(arr > 2)
# True
```

## `all()`

True if all conditions are true.

``` python
np.all(arr > 0)
# True
```

`axis` can be used with multidimensional arrays.

------------------------------------------------------------------------

# 26. Aggregation Functions

``` python
arr = np.array([10, 20, 30, 40, 50])

np.sum(arr)
np.mean(arr)
np.median(arr)
np.min(arr)
np.max(arr)
np.std(arr)
np.var(arr)
np.prod(arr)
```

Useful index functions:

``` python
np.argmax(arr)
np.argmin(arr)
```

  Function     Meaning
  ------------ --------------------
  `sum()`      Sum
  `mean()`     Average
  `median()`   Median
  `min()`      Minimum
  `max()`      Maximum
  `std()`      Standard deviation
  `var()`      Variance
  `prod()`     Product
  `argmin()`   Index of minimum
  `argmax()`   Index of maximum

------------------------------------------------------------------------

# 27. `axis` --- Critical Concept

Consider:

``` python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

Shape:

``` text
(2, 3)
```

## `axis=0`

Reduce along rows → one result for each column.

``` python
arr.sum(axis=0)
# [5 7 9]
```

## `axis=1`

Reduce along columns → one result for each row.

``` python
arr.sum(axis=1)
# [6 15]
```

### Better Mental Model

Instead of memorizing "axis 0 = rows", think:

> **The specified axis is the dimension being reduced/operated along.**

For a 2D array:

``` text
axis=0 → collapse row dimension → one result per column
axis=1 → collapse column dimension → one result per row
```

------------------------------------------------------------------------

# 28. `keepdims=True`

Preserves the reduced dimension as size `1`.

``` python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

mean = arr.mean(axis=1, keepdims=True)

print(mean.shape)
# (2, 1)
```

This is useful for broadcasting results back against the original array.

------------------------------------------------------------------------

# 29. Cumulative Operations

## `cumsum()`

``` python
arr = np.array([1, 2, 3, 4])

np.cumsum(arr)
# [1 3 6 10]
```

## `cumprod()`

``` python
np.cumprod(arr)
# [1 2 6 24]
```

------------------------------------------------------------------------

# 30. Broadcasting

## Definition

**Broadcasting** is NumPy's mechanism for performing operations between
arrays with compatible shapes.

Simple example:

``` python
arr = np.array([1, 2, 3])

arr + 10
```

The scalar is applied to every element.

## 2D Example

``` python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

row = np.array([10, 20, 30])

print(arr + row)
```

Result:

``` text
[[11 22 33]
 [14 25 36]]
```

------------------------------------------------------------------------

# 31. Broadcasting Rules

Compare shapes from **right to left**.

Dimensions are compatible if:

1.  They are equal, OR
2.  One dimension is `1`.

Example:

``` text
(2, 3)
(3,)
```

Treat the second as:

``` text
(1, 3)
```

Compatible.

Another example:

``` text
(3, 1)
(1, 4)
```

Compatible → result:

``` text
(3, 4)
```

But:

``` text
(2, 3)
(2, 2)
```

are incompatible.

> Broadcasting is fundamental to feature scaling, normalization, batch
> operations and many ML calculations.

------------------------------------------------------------------------

# 32. Universal Functions (`ufunc`)

NumPy provides vectorized mathematical functions.

``` python
np.sqrt(arr)
np.exp(arr)
np.log(arr)
np.sin(arr)
np.cos(arr)
np.abs(arr)
np.round(arr)
np.floor(arr)
np.ceil(arr)
```

Example:

``` python
arr = np.array([1, 4, 9])

np.sqrt(arr)
# [1. 2. 3.]
```

------------------------------------------------------------------------

# 33. Rounding and Mathematical Functions

``` python
arr = np.array([1.234, 2.678, 3.456])

np.round(arr, 2)
np.floor(arr)
np.ceil(arr)
np.trunc(arr)
```

Remember:

``` text
round → round to specified decimals
floor → greatest integer <= value
ceil  → smallest integer >= value
trunc → remove fractional part toward zero
```

Other useful functions:

``` python
np.power()
np.square()
np.log10()
```

------------------------------------------------------------------------

# 34. Sorting

## `np.sort()`

Returns a sorted result.

``` python
arr = np.array([30, 10, 20])

result = np.sort(arr)

print(result)
# [10 20 30]

print(arr)
# [30 10 20]
```

## `arr.sort()`

Sorts in place.

``` python
arr.sort()
```

### Difference

``` text
np.sort(arr) → returns sorted result
arr.sort()   → modifies original array
```

## `argsort()`

Returns indices that would sort the array.

``` python
arr = np.array([30, 10, 20])

np.argsort(arr)
# [1 2 0]
```

------------------------------------------------------------------------

# 35. Unique Values

``` python
arr = np.array([1, 2, 2, 3, 3, 3])

np.unique(arr)
# [1 2 3]
```

Get frequencies:

``` python
values, counts = np.unique(arr, return_counts=True)
```

Useful in exploratory data analysis and categorical inspection.

------------------------------------------------------------------------

# 36. Missing Values with `np.nan`

``` python
arr = np.array([1.0, 2.0, np.nan, 4.0])

np.isnan(arr)
```

NaN-aware functions:

``` python
np.nanmean(arr)
np.nanmedian(arr)
np.nansum(arr)
np.nanmin(arr)
np.nanmax(arr)
np.nanstd(arr)
```

> Missing-data handling in real projects is often more conveniently
> managed with Pandas or dedicated preprocessing tools.

------------------------------------------------------------------------

# 37. Linear Algebra

NumPy provides important linear-algebra tools.

## Dot Product

``` python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.dot(a, b)
# 32
```

Because:

``` text
1×4 + 2×5 + 3×6 = 32
```

------------------------------------------------------------------------

# 38. Matrix Multiplication

Use `@`:

``` python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

C = A @ B
```

Also:

``` python
np.matmul(A, B)
```

### Critical Difference

``` text
A * B → element-wise multiplication
A @ B → matrix multiplication
```

------------------------------------------------------------------------

# 39. Determinant and Inverse

``` python
A = np.array([
    [1, 2],
    [3, 4]
])

np.linalg.det(A)
```

Inverse:

``` python
np.linalg.inv(A)
```

A regular inverse requires a square, non-singular matrix.

## Better Way to Solve `Ax = b`

Instead of explicitly calculating an inverse:

``` python
x = np.linalg.inv(A) @ b
```

prefer:

``` python
x = np.linalg.solve(A, b)
```

This is generally more appropriate numerically and computationally.

------------------------------------------------------------------------

# 40. Eigenvalues and Eigenvectors

``` python
A = np.array([
    [2, 0],
    [0, 3]
])

values, vectors = np.linalg.eig(A)
```

Important for:

-   PCA,
-   dimensionality reduction,
-   linear algebra,
-   scientific computing.

------------------------------------------------------------------------

# 41. Norm

A norm measures vector magnitude.

``` python
v = np.array([3, 4])

np.linalg.norm(v)
# 5.0
```

Because:

``` text
sqrt(3² + 4²) = 5
```

Norms are used in:

-   distance calculations,
-   normalization,
-   optimization,
-   ML. 

------------------------------------------------------------------------

# 42. Solving a Linear System

System:

``` text
2x + y = 5
x + 3y = 6
```

Represent:

``` python
A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([5, 6])

x = np.linalg.solve(A, b)
```

This pattern is useful for understanding the linear algebra behind ML.

------------------------------------------------------------------------

# 43. NumPy Shapes in Machine Learning

A common ML dataset is represented as:

``` text
X.shape = (n_samples, n_features)
```

Example:

``` python
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

print(X.shape)
# (4, 3)
```

Interpretation:

``` text
4 samples
3 features
```

Target vector may have:

``` python
y.shape
# (4,)
```

## Important Shape Difference

``` python
x = np.array([1, 2, 3])
x.shape
# (3,)
```

versus:

``` python
x.reshape(1, -1).shape
# (1, 3)
```

and:

``` python
x.reshape(-1, 1).shape
# (3, 1)
```

These are three different shapes and can behave differently during
matrix operations and broadcasting.

------------------------------------------------------------------------

# 44. Feature Scaling Example

``` python
X = np.array([
    [10, 100],
    [20, 200],
    [30, 300]
], dtype=float)

mean = X.mean(axis=0)
std = X.std(axis=0)

X_scaled = (X - mean) / std
```

This combines:

``` text
axis
mean
std
broadcasting
vectorized arithmetic
```

In actual ML projects, use a proper preprocessing pipeline and calculate
scaling parameters using training data only to prevent data leakage.

------------------------------------------------------------------------

# 45. Distance Between Vectors

``` python
a = np.array([1, 2, 3])
b = np.array([4, 6, 3])

distance = np.linalg.norm(a - b)
```

Euclidean distance is important in:

-   KNN,
-   clustering,
-   similarity search,
-   recommendation systems,
-   embedding applications.

------------------------------------------------------------------------

# 46. Dot Product in Machine Learning

A simple linear model:

``` python
x = np.array([2, 3, 4])
w = np.array([0.5, 1.0, 2.0])
b = 1

y = x @ w + b
```

Mathematically:

``` text
y = x₁w₁ + x₂w₂ + x₃w₃ + b
```

This basic operation appears throughout machine learning.

------------------------------------------------------------------------

# 47. Saving and Loading Arrays

## `.npy`

``` python
arr = np.array([1, 2, 3])

np.save("data.npy", arr)

loaded = np.load("data.npy")
```

## `.npz`

Store multiple arrays:

``` python
np.savez(
    "data.npz",
    x=np.array([1, 2]),
    y=np.array([3, 4])
)
```

Load:

``` python
data = np.load("data.npz")

print(data["x"])
print(data["y"])
```

> Be cautious when loading files from untrusted sources and use safe
> loading practices.

------------------------------------------------------------------------

# 48. Vectorization

Instead of:

``` python
numbers = np.array([1, 2, 3, 4])

result = []

for x in numbers:
    result.append(x * 2)
```

Prefer:

``` python
result = numbers * 2
```

This is **vectorized computation**.

Benefits:

-   cleaner code,
-   often faster for numerical workloads,
-   fewer explicit Python loops,
-   naturally works with broadcasting.

------------------------------------------------------------------------

# 49. Useful Data-Transformation Functions

## `clip()`

Restrict values to a range.

``` python
arr = np.array([10, 20, 30, 40, 50])

np.clip(arr, 20, 40)
# [20 20 30 40 40]
```

## `diff()`

Differences between consecutive values:

``` python
arr = np.array([10, 15, 23, 30])

np.diff(arr)
# [5 8 7]
```

## `gradient()`

Numerical gradient:

``` python
np.gradient(arr)
```

These are useful in numerical and time-series work.

------------------------------------------------------------------------

# 50. Iterating Through Arrays

``` python
arr = np.array([10, 20, 30])

for x in arr:
    print(x)
```

2D:

``` python
arr = np.array([
    [1, 2],
    [3, 4]
])

for row in arr:
    print(row)
```

For element-wise iteration:

``` python
for x in np.nditer(arr):
    print(x)
```

> Prefer vectorized operations when a direct NumPy expression can
> perform the task.

------------------------------------------------------------------------

# 51. Common NumPy Mistakes

## 1. Using `and` / `or` with arrays

Wrong:

``` python
arr[(arr > 10) and (arr < 50)]
```

Correct:

``` python
arr[(arr > 10) & (arr < 50)]
```

------------------------------------------------------------------------

## 2. Forgetting parentheses

Wrong:

``` python
arr > 10 & arr < 50
```

Correct:

``` python
(arr > 10) & (arr < 50)
```

------------------------------------------------------------------------

## 3. Confusing `*` and `@`

``` text
* → element-wise multiplication
@ → matrix multiplication
```

------------------------------------------------------------------------

## 4. Confusing `shape` and `size`

``` text
shape → dimensions
size  → total elements
```

------------------------------------------------------------------------

## 5. Forgetting views

A slice can share data with the original array.

Use:

``` python
arr.copy()
```

when an independent copy is needed.

------------------------------------------------------------------------

## 6. Assuming `np.empty()` gives zeros

It does not.

Use:

``` python
np.zeros(...)
```

------------------------------------------------------------------------

## 7. Misunderstanding `axis`

For:

``` python
arr.shape == (2, 3)
```

remember:

``` text
axis=0 → result per column
axis=1 → result per row
```

------------------------------------------------------------------------

## 8. Confusing `(3,)`, `(1,3)` and `(3,1)`

``` text
(3,)   → 1D
(1,3)  → 2D row
(3,1)  → 2D column
```

Shape differences are a major source of ML errors.

------------------------------------------------------------------------

# 52. NumPy vs Pandas

Use NumPy when you mainly need:

-   numerical arrays,
-   mathematical operations,
-   matrix/linear-algebra operations,
-   vectorized calculations,
-   multidimensional numerical data.

Use Pandas when you mainly need:

-   tabular data,
-   column names,
-   row labels,
-   mixed data types,
-   missing-data workflows,
-   CSV/Excel-style data analysis.

They work together constantly in Data Science.

------------------------------------------------------------------------

# 53. NumPy in the ML Pipeline

A typical workflow:

``` text
Raw Data
   ↓
Load / Clean
   ↓
NumPy / Pandas
   ↓
Inspect shape + dtype
   ↓
Filter / Transform
   ↓
Feature Matrix X
   ↓
Scaling / Encoding
   ↓
Train / Validation / Test
   ↓
ML Model
```

NumPy knowledge is especially useful for understanding what happens to
data between these steps.

------------------------------------------------------------------------

# 54. NumPy and Deep Learning

Deep-learning systems work with multidimensional numerical tensors.

Conceptually:

``` text
1D → vector
2D → matrix
3D → volume / sequence-like structure
4D → batch of structured data
```

For example, image data may be represented using a shape such as:

``` text
(batch, height, width, channels)
```

or another layout depending on the framework.

> Never assume tensor layout. Inspect the actual shape.

------------------------------------------------------------------------

# 55. Core NumPy Function Cheat Sheet

## Array Creation

``` python
np.array()
np.zeros()
np.ones()
np.full()
np.empty()
np.eye()
np.identity()
np.arange()
np.linspace()
np.logspace()
```

## Inspection

``` python
arr.ndim
arr.shape
arr.size
arr.dtype
arr.itemsize
arr.nbytes
```

## Reshaping

``` python
arr.reshape()
arr.flatten()
arr.ravel()
arr.T
np.transpose()
np.expand_dims()
np.squeeze()
```

## Combining

``` python
np.concatenate()
np.vstack()
np.hstack()
np.column_stack()
np.stack()
np.split()
np.array_split()
```

## Filtering / Searching

``` python
np.where()
np.unique()
np.argmax()
np.argmin()
np.argsort()
np.any()
np.all()
```

## Statistics

``` python
np.sum()
np.mean()
np.median()
np.min()
np.max()
np.std()
np.var()
np.prod()
```

## Math

``` python
np.sqrt()
np.exp()
np.log()
np.log10()
np.abs()
np.power()
np.square()
np.round()
np.floor()
np.ceil()
```

## Random

``` python
np.random.default_rng()
rng.random()
rng.integers()
rng.normal()
rng.choice()
rng.shuffle()
rng.permutation()
```

## Linear Algebra

``` python
np.dot()
np.matmul()
np.linalg.solve()
np.linalg.inv()
np.linalg.det()
np.linalg.eig()
np.linalg.norm()
```

------------------------------------------------------------------------

# 56. What to Master for Data Science / AI / ML

## Tier 1 --- Must Master

``` text
ndarray
shape
ndim
size
dtype
indexing
slicing
reshape()
axis
vectorization
Boolean masking
broadcasting
mean()
sum()
min()
max()
std()
where()
```

## Tier 2 --- Very Important

``` text
astype()
concatenate()
stacking
flatten()
ravel()
transpose
copy vs view
unique()
argsort()
argmax()
argmin()
NaN handling
random Generator
```

## Tier 3 --- ML Mathematics

``` text
dot product
matrix multiplication (@)
norm
solve()
eigenvalues/eigenvectors
```

## Tier 4 --- Learn as Needed

``` text
logspace()
gradient()
diff()
specialized array manipulation
specialized linear algebra
```

------------------------------------------------------------------------

# 57. Interview / Viva Questions

## Fundamentals

1.  What is NumPy?
2.  What is an `ndarray`?
3.  Why is NumPy generally faster than Python lists for numerical
    workloads?
4.  What is the difference between `shape`, `size`, and `ndim`?
5.  What is `dtype`?
6.  What is vectorization?
7.  What is broadcasting?
8.  What is the difference between a view and a copy?
9.  What is the difference between `reshape()` and `flatten()`?
10. What does `axis` mean?

## Comparisons

11. `arange()` vs `linspace()`
12. `np.sort()` vs `arr.sort()`
13. `flatten()` vs `ravel()`
14. `*` vs `@`
15. assignment vs `.copy()`
16. `np.where()` vs Boolean masking

## ML-Oriented

17. What does `X.shape = (1000, 20)` mean?
18. Why is broadcasting useful in feature scaling?
19. How do you select values greater than a threshold?
20. How do you calculate the mean of every feature?
21. How do you calculate Euclidean distance?
22. How do you multiply two matrices?
23. Why can `(3,)`, `(1,3)` and `(3,1)` behave differently?
24. Why should scaling parameters be learned from training data only?

------------------------------------------------------------------------

# 58. Practice Problems

## Beginner

### 1.

Create a NumPy array containing numbers from 1 to 10.

### 2.

Create a `3 × 4` array of zeros.

### 3.

Create a `4 × 4` identity matrix.

### 4.

Print the shape, size, dimensions and dtype of an array.

### 5.

Convert an integer array to `float32`.

## Intermediate

### 6.

Create an array from 1 to 20 and select only even numbers.

### 7.

Create a `4 × 5` matrix and extract:

-   first row,
-   last column,
-   first two rows,
-   a middle section.

### 8.

Reshape numbers from 1 to 12 into:

``` text
(3, 4)
(4, 3)
(2, 6)
```

### 9.

Find the mean of every column.

### 10.

Find the maximum value and its index.

## Data Science

### 11.

Create a dataset containing:

``` text
Age
Height
Weight
```

Calculate mean, minimum, maximum and standard deviation for every
feature.

### 12.

Use Boolean masking to find people whose age is greater than 18.

### 13.

Standardize a feature matrix using:

``` text
(X - mean) / std
```

### 14.

Calculate Euclidean distance between two feature vectors.

### 15.

Perform matrix multiplication using `@`.

### 16.

Create a feature matrix and use `np.where()` to assign a label based on
a threshold.

------------------------------------------------------------------------

# 59. Final Mental Model

The most important NumPy chain is:

``` text
ARRAY
  ↓
Shape + dtype
  ↓
Indexing / Slicing
  ↓
Vectorized Operations
  ↓
Broadcasting
  ↓
Boolean Masking
  ↓
Aggregation + axis
  ↓
Reshaping
  ↓
Matrix Operations
  ↓
Machine Learning
```

When you get an array, ask:

``` text
1. What is its type?
2. What is its shape?
3. What is its dtype?
4. How many dimensions does it have?
5. Do I need indexing or slicing?
6. Am I creating a view or a copy?
7. What axis am I operating on?
8. Are the shapes broadcast-compatible?
```

> **Golden Rule:** Before performing an important operation, check
> **shape + dtype + axis**. These three explain a huge percentage of
> NumPy and ML bugs.

------------------------------------------------------------------------

# 60. Final Summary

If you master these concepts, you have the NumPy foundation needed for
most Data Science and ML work:

``` text
✓ ndarray
✓ dimensions
✓ shape
✓ dtype
✓ indexing
✓ slicing
✓ views / copies
✓ reshape
✓ transpose
✓ broadcasting
✓ vectorization
✓ Boolean masking
✓ axis
✓ aggregation
✓ sorting
✓ unique values
✓ NaN handling
✓ random numbers
✓ concatenation
✓ matrix multiplication
✓ dot products
✓ norms
✓ linear algebra
✓ ML data shapes
```

Do not try to memorize NumPy as a list of hundreds of functions.

**Understand arrays first.**

Once you understand:

``` text
shape → axis → broadcasting → vectorization → masking
```

the rest of NumPy becomes significantly easier.
