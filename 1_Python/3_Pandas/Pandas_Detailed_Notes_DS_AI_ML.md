# Pandas — Detailed Notes for Data Science, AI & ML

> A practical, comprehensive Pandas reference for learning Data Science, AI, and Machine Learning.

---

## Table of Contents

1. [What is Pandas?](#1-what-is-pandas)
2. [Why Pandas is Important](#2-why-pandas-is-important)
3. [Installation and Import](#3-installation-and-import)
4. [Core Data Structures](#4-core-data-structures)
5. [Series](#5-series)
6. [DataFrame](#6-dataframe)
7. [DataFrame Attributes](#7-dataframe-attributes)
8. [Inspecting Data](#8-inspecting-data)
9. [Selecting Columns](#9-selecting-columns)
10. [Selecting Rows — loc and iloc](#10-selecting-rows--loc-and-iloc)
11. [Filtering Data](#11-filtering-data)
12. [Adding and Modifying Columns](#12-adding-and-modifying-columns)
13. [Deleting Rows and Columns](#13-deleting-rows-and-columns)
14. [Missing Values](#14-missing-values)
15. [Handling Duplicates](#15-handling-duplicates)
16. [Data Types](#16-data-types)
17. [Type Conversion](#17-type-conversion)
18. [Sorting](#18-sorting)
19. [String Operations](#19-string-operations)
20. [Applying Functions](#20-applying-functions)
21. [GroupBy and Aggregation](#21-groupby-and-aggregation)
22. [Combining DataFrames](#22-combining-dataframes)
23. [Reading and Writing Files](#23-reading-and-writing-files)
24. [Working with Dates and Times](#24-working-with-dates-and-times)
25. [Renaming](#25-renaming)
26. [Indexes](#26-indexes)
27. [Useful Data Operations](#27-useful-data-operations)
28. [Pandas and NumPy](#28-pandas-and-numpy)
29. [Pandas in Machine Learning](#29-pandas-in-machine-learning)
30. [Common Data Cleaning Workflow](#30-common-data-cleaning-workflow)
31. [Important Functions Cheat Sheet](#31-important-functions-cheat-sheet)
32. [Common Mistakes](#32-common-mistakes)
33. [What to Learn First](#33-what-to-learn-first)

---

# 1. What is Pandas?

**Pandas** is an open-source Python library used for:

- Data manipulation
- Data analysis
- Data cleaning
- Data exploration
- Data transformation
- Working with tabular/structured data
- Preparing datasets for Machine Learning

Pandas is built on top of **NumPy**, so NumPy knowledge is useful when learning Pandas.

```python
import pandas as pd
```

`pd` is the conventional alias used for Pandas.

---

# 2. Why Pandas is Important

In Data Science and Machine Learning, the dataset you receive is rarely ready to use.

A real dataset may contain:

```text
Name     Age    Salary    City
Rahul    19     50000     Delhi
Aman     NaN    45000     Delhi
Priya    20     60000     NaN
```

Before using this data for ML, you may need to:

```text
Load data
    ↓
Inspect data
    ↓
Clean data
    ↓
Handle missing values
    ↓
Remove duplicates
    ↓
Fix data types
    ↓
Filter data
    ↓
Transform features
    ↓
Analyze data
    ↓
Prepare data for ML
```

Pandas provides tools for almost every step before the actual model training.

---

# 3. Installation and Import

## Install

Using pip:

```bash
pip install pandas
```

In Jupyter Notebook or Google Colab:

```python
!pip install pandas
```

## Import

```python
import pandas as pd
```

## Check version

```python
print(pd.__version__)
```

---

# 4. Core Data Structures

Pandas mainly provides two important data structures:

```text
Pandas
│
├── Series
│
└── DataFrame
```

## Series

A **Series** is a one-dimensional labeled array.

You can think of it as a single column.

```text
Index    Value
0        10
1        20
2        30
3        40
```

## DataFrame

A **DataFrame** is a two-dimensional labeled data structure.

You can think of it as a table.

```text
       Name    Age    Marks
0      Rahul   19     85
1      Aman    20     92
2      Priya   19     78
```

A DataFrame is essentially a collection of Series sharing the same index.

---

# 5. Series

## 5.1 Creating a Series

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s)
```

Output:

```text
0    10
1    20
2    30
3    40
dtype: int64
```

The left side is the index and the right side contains the values.

---

## 5.2 Creating a Series with a Custom Index

```python
s = pd.Series(
    [85, 92, 78],
    index=["Rahul", "Aman", "Priya"]
)

print(s)
```

Output:

```text
Rahul    85
Aman     92
Priya    78
dtype: int64
```

Now the labels are names instead of `0, 1, 2`.

---

## 5.3 Series from a Dictionary

```python
marks = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78
}

s = pd.Series(marks)

print(s)
```

Dictionary keys become indexes.

---

## 5.4 Accessing Series Values

```python
s = pd.Series([10, 20, 30, 40])

print(s[0])
```

Output:

```text
10
```

Using labels:

```python
s = pd.Series(
    [85, 92, 78],
    index=["Rahul", "Aman", "Priya"]
)

print(s["Rahul"])
```

Output:

```text
85
```

---

## 5.5 Series Slicing

```python
s = pd.Series([10, 20, 30, 40, 50])

print(s[1:4])
```

Output:

```text
1    20
2    30
3    40
dtype: int64
```

---

## 5.6 Series Operations

Pandas supports vectorized operations similar to NumPy.

```python
s = pd.Series([10, 20, 30, 40])

print(s + 5)
```

Output:

```text
0    15
1    25
2    35
3    45
dtype: int64
```

```python
print(s * 2)
```

```python
print(s / 10)
```

```python
print(s ** 2)
```

---

## 5.7 Useful Series Methods

```python
s.sum()
s.mean()
s.median()
s.min()
s.max()
s.std()
s.var()
s.count()
```

Example:

```python
marks = pd.Series([85, 92, 78, 90])

print(marks.mean())
print(marks.max())
print(marks.min())
```

---

# 6. DataFrame

A DataFrame is the most important Pandas object for Data Science.

## 6.1 Creating a DataFrame from a Dictionary

```python
data = {
    "Name": ["Rahul", "Aman", "Priya"],
    "Age": [19, 20, 19],
    "Marks": [85, 92, 78]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    Name  Age  Marks
0  Rahul   19     85
1   Aman   20     92
2  Priya   19     78
```

---

## 6.2 Creating a DataFrame from a List of Dictionaries

```python
data = [
    {"Name": "Rahul", "Age": 19, "Marks": 85},
    {"Name": "Aman", "Age": 20, "Marks": 92},
    {"Name": "Priya", "Age": 19, "Marks": 78}
]

df = pd.DataFrame(data)
```

---

## 6.3 Creating a DataFrame from a List

```python
data = [
    ["Rahul", 19, 85],
    ["Aman", 20, 92],
    ["Priya", 19, 78]
]

df = pd.DataFrame(
    data,
    columns=["Name", "Age", "Marks"]
)
```

---

## 6.4 Understanding a DataFrame

```text
              DataFrame
        ┌────────┬─────┬───────┐
        │ Name   │ Age │ Marks │
        ├────────┼─────┼───────┤
index 0 │ Rahul  │ 19  │  85   │
index 1 │ Aman   │ 20  │  92   │
index 2 │ Priya  │ 19  │  78   │
        └────────┴─────┴───────┘
```

- `df` → DataFrame
- `Name`, `Age`, `Marks` → columns
- `0`, `1`, `2` → index
- Each column is a Series

---

# 7. DataFrame Attributes

Attributes provide information about a DataFrame.

## 7.1 `shape`

Returns:

```text
(rows, columns)
```

```python
print(df.shape)
```

Example:

```text
(3, 3)
```

This means:

- 3 rows
- 3 columns

---

## 7.2 `columns`

```python
print(df.columns)
```

Returns the column labels.

---

## 7.3 `index`

```python
print(df.index)
```

Returns the row index.

---

## 7.4 `dtypes`

```python
print(df.dtypes)
```

Shows the data type of each column.

Example:

```text
Name     object
Age       int64
Marks     int64
dtype: object
```

---

## 7.5 `size`

```python
print(df.size)
```

Returns the total number of elements.

For a `3 × 3` DataFrame:

```text
9
```

---

## 7.6 `ndim`

```python
print(df.ndim)
```

A DataFrame is 2-dimensional:

```text
2
```

A Series is 1-dimensional:

```text
1
```

---

# 8. Inspecting Data

Before cleaning or analyzing a dataset, inspect it.

This is one of the most important habits in Data Science.

---

## 8.1 `head()`

Shows the first 5 rows by default.

```python
df.head()
```

Show first 10:

```python
df.head(10)
```

---

## 8.2 `tail()`

Shows the last 5 rows.

```python
df.tail()
```

Show last 10:

```python
df.tail(10)
```

---

## 8.3 `info()`

Provides important structural information.

```python
df.info()
```

It shows:

- Number of rows
- Columns
- Non-null values
- Data types
- Memory usage

This should be one of the first commands you run on an unfamiliar dataset.

---

## 8.4 `describe()`

Provides statistical information about numerical columns.

```python
df.describe()
```

Typically includes:

- count
- mean
- standard deviation
- minimum
- 25th percentile
- median / 50th percentile
- 75th percentile
- maximum

Example:

```python
print(df["Marks"].describe())
```

---

## 8.5 `describe(include="all")`

```python
df.describe(include="all")
```

Useful when you also want information about non-numerical columns.

---

## 8.6 `sample()`

Returns random rows.

```python
df.sample()
```

Multiple rows:

```python
df.sample(5)
```

Useful when quickly checking a large dataset.

---

## 8.7 Checking Number of Rows

```python
len(df)
```

Or:

```python
df.shape[0]
```

---

## 8.8 Checking Number of Columns

```python
df.shape[1]
```

---

# 9. Selecting Columns

Suppose:

```python
df = pd.DataFrame({
    "Name": ["Rahul", "Aman", "Priya"],
    "Age": [19, 20, 19],
    "Marks": [85, 92, 78]
})
```

## 9.1 Select One Column

```python
df["Name"]
```

Returns a Series.

---

## 9.2 Select Multiple Columns

```python
df[["Name", "Marks"]]
```

Important:

```python
df["Name"]       # Series
df[["Name"]]     # DataFrame
```

---

## 9.3 Dot Notation

You can sometimes use:

```python
df.Name
```

instead of:

```python
df["Name"]
```

But prefer:

```python
df["Name"]
```

because dot notation can fail when:

- column names contain spaces
- column names conflict with DataFrame methods
- column names are not valid Python identifiers

---

# 10. Selecting Rows — `loc` and `iloc`

This distinction is extremely important.

---

## 10.1 `loc`

`loc` selects data using **labels**.

```python
df.loc[0]
```

Select rows:

```python
df.loc[0:1]
```

Select specific columns:

```python
df.loc[0:1, ["Name", "Marks"]]
```

---

## 10.2 `iloc`

`iloc` selects data using **integer positions**.

```python
df.iloc[0]
```

First row:

```python
df.iloc[0]
```

First two rows:

```python
df.iloc[0:2]
```

First row, second column:

```python
df.iloc[0, 1]
```

Rows 0–1 and columns 0–1:

```python
df.iloc[0:2, 0:2]
```

---

## 10.3 `loc` vs `iloc`

| Feature | `loc` | `iloc` |
|---|---|---|
| Selection | Labels | Integer positions |
| Example | `df.loc[2]` | `df.iloc[2]` |
| Columns | Labels | Positions |
| Useful for | Named/index-based selection | Positional selection |

Remember:

```text
loc  → labels
iloc → integer positions
```

---

# 11. Filtering Data

Filtering is one of the most important Pandas skills for Data Science.

Suppose:

```python
df = pd.DataFrame({
    "Name": ["Rahul", "Aman", "Priya", "Rohan"],
    "Age": [19, 20, 19, 21],
    "Marks": [85, 92, 78, 65]
})
```

---

## 11.1 One Condition

Students with marks greater than 80:

```python
df[df["Marks"] > 80]
```

---

## 11.2 Equality

```python
df[df["Age"] == 19]
```

---

## 11.3 Not Equal

```python
df[df["Age"] != 19]
```

---

## 11.4 Greater Than or Equal

```python
df[df["Marks"] >= 80]
```

---

## 11.5 Less Than

```python
df[df["Marks"] < 80]
```

---

## 11.6 Multiple Conditions

Use:

```text
&  → AND
|  → OR
~  → NOT
```

Example:

```python
df[(df["Age"] >= 19) & (df["Marks"] > 80)]
```

OR:

```python
df[(df["Age"] == 19) | (df["Marks"] > 90)]
```

NOT:

```python
df[~(df["Age"] == 19)]
```

### Important

Do not use Python's `and` / `or` for Series conditions.

Wrong:

```python
df[(df["Age"] > 18) and (df["Marks"] > 80)]
```

Correct:

```python
df[(df["Age"] > 18) & (df["Marks"] > 80)]
```

Use parentheses around each condition.

---

## 11.7 `isin()`

Select rows where a value belongs to a list.

```python
df[df["Age"].isin([19, 21])]
```

---

## 11.8 `between()`

```python
df[df["Marks"].between(70, 90)]
```

This selects values between 70 and 90.

---

# 12. Adding and Modifying Columns

## 12.1 Add a New Column

```python
df["Passed"] = True
```

---

## 12.2 Column Based on Existing Columns

```python
df["Bonus"] = df["Marks"] + 5
```

---

## 12.3 Conditional Column

Using `np.where()`:

```python
import numpy as np

df["Result"] = np.where(
    df["Marks"] >= 40,
    "Pass",
    "Fail"
)
```

---

## 12.4 Modify Existing Column

```python
df["Marks"] = df["Marks"] + 5
```

---

## 12.5 Rename a Column

```python
df.rename(
    columns={"Marks": "Score"},
    inplace=True
)
```

Without modifying the original DataFrame:

```python
df = df.rename(columns={"Marks": "Score"})
```

---

# 13. Deleting Rows and Columns

## 13.1 Delete a Column

```python
df.drop(columns=["Age"])
```

To modify the original:

```python
df.drop(columns=["Age"], inplace=True)
```

---

## 13.2 Delete Multiple Columns

```python
df.drop(
    columns=["Age", "Marks"],
    inplace=True
)
```

---

## 13.3 Delete a Row

By index:

```python
df.drop(index=0)
```

Multiple rows:

```python
df.drop(index=[0, 2])
```

---

## 13.4 `inplace`

Many Pandas methods return a modified copy by default.

Example:

```python
df.drop(columns=["Age"])
```

does not necessarily modify `df`.

You can assign the result:

```python
df = df.drop(columns=["Age"])
```

Or use:

```python
df.drop(columns=["Age"], inplace=True)
```

For learning and production code, explicitly assigning the result is often easier to reason about.

---

# 14. Missing Values

Missing values are extremely common in real-world datasets.

Example:

```text
Name     Age     Marks
Rahul    19      85
Aman     NaN     92
Priya    20      NaN
```

Pandas commonly represents missing numeric data using `NaN`.

---

## 14.1 Detect Missing Values

```python
df.isna()
```

Returns `True` where a value is missing.

---

## 14.2 Count Missing Values

```python
df.isna().sum()
```

This is extremely useful.

Example:

```text
Name     0
Age      1
Marks    1
dtype: int64
```

---

## 14.3 `isnull()`

```python
df.isnull()
```

`isnull()` and `isna()` are equivalent in normal usage.

---

## 14.4 Select Rows Containing Missing Values

```python
df[df["Age"].isna()]
```

---

## 14.5 Drop Rows with Missing Values

```python
df.dropna()
```

This removes rows containing missing values.

---

## 14.6 Drop Columns with Missing Values

```python
df.dropna(axis=1)
```

`axis=0` means rows.

`axis=1` means columns.

---

## 14.7 Fill Missing Values

```python
df["Age"] = df["Age"].fillna(0)
```

---

## 14.8 Fill with Mean

For numerical data:

```python
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)
```

---

## 14.9 Fill with Median

```python
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

Median can be more robust when the data contains extreme outliers.

---

## 14.10 Fill with Mode

For categorical data:

```python
df["City"] = df["City"].fillna(
    df["City"].mode()[0]
)
```

---

## Important ML Warning

Do not blindly fill missing values using the entire dataset before splitting into training and testing data.

That can cause **data leakage**.

For ML workflows, preprocessing should generally be fitted using training data and then applied to validation/test data.

---

# 15. Handling Duplicates

## 15.1 Find Duplicates

```python
df.duplicated()
```

---

## 15.2 Count Duplicates

```python
df.duplicated().sum()
```

---

## 15.3 Remove Duplicates

```python
df.drop_duplicates()
```

Or:

```python
df.drop_duplicates(inplace=True)
```

---

## 15.4 Duplicate Based on Specific Columns

```python
df.drop_duplicates(subset=["Name"])
```

---

# 16. Data Types

Every column has a data type.

Check:

```python
df.dtypes
```

Common types include:

| Pandas dtype | Meaning |
|---|---|
| `int64` | Integer |
| `float64` | Decimal number |
| `object` | Often text/mixed data |
| `string` | String data |
| `bool` | Boolean |
| `datetime64[ns]` | Date/time |
| `category` | Categorical data |

Modern Pandas also has nullable extension types such as:

```text
Int64
Float64
boolean
string
```

Note the capitalized `Int64` is different from NumPy-style `int64`.

---

# 17. Type Conversion

## 17.1 `astype()`

```python
df["Age"] = df["Age"].astype(int)
```

Convert to float:

```python
df["Age"] = df["Age"].astype(float)
```

Convert to string:

```python
df["Age"] = df["Age"].astype(str)
```

---

## 17.2 `pd.to_numeric()`

Useful when numbers are stored as strings.

```python
df["Salary"] = pd.to_numeric(
    df["Salary"],
    errors="coerce"
)
```

`errors="coerce"` converts invalid values to `NaN`.

---

## 17.3 `pd.to_datetime()`

```python
df["Date"] = pd.to_datetime(df["Date"])
```

For invalid dates:

```python
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)
```

---

# 18. Sorting

## 18.1 Sort by One Column

```python
df.sort_values("Marks")
```

Descending:

```python
df.sort_values(
    "Marks",
    ascending=False
)
```

---

## 18.2 Sort by Multiple Columns

```python
df.sort_values(
    ["Age", "Marks"],
    ascending=[True, False]
)
```

This means:

1. Sort Age ascending
2. For equal ages, sort Marks descending

---

## 18.3 Sort by Index

```python
df.sort_index()
```

Descending:

```python
df.sort_index(ascending=False)
```

---

# 19. String Operations

Pandas provides the `.str` accessor for vectorized string operations.

Suppose:

```python
df["Name"]
```

contains names.

---

## 19.1 Lowercase

```python
df["Name"].str.lower()
```

---

## 19.2 Uppercase

```python
df["Name"].str.upper()
```

---

## 19.3 Capitalize

```python
df["Name"].str.capitalize()
```

---

## 19.4 Length

```python
df["Name"].str.len()
```

---

## 19.5 Contains

```python
df[df["Name"].str.contains("Rahul")]
```

Case-insensitive:

```python
df[
    df["Name"].str.contains(
        "rahul",
        case=False,
        na=False
    )
]
```

---

## 19.6 Strip Whitespace

Very useful for cleaning real datasets:

```python
df["Name"] = df["Name"].str.strip()
```

---

## 19.7 Replace Text

```python
df["City"] = df["City"].str.replace(
    "Delhi",
    "New Delhi",
    regex=False
)
```

---

# 20. Applying Functions

## 20.1 `apply()`

`apply()` allows you to apply a function to values.

Example:

```python
def square(x):
    return x ** 2

df["Marks"].apply(square)
```

Using lambda:

```python
df["Marks"].apply(lambda x: x + 5)
```

---

## 20.2 Applying a Function to a Column

```python
df["Name"] = df["Name"].apply(
    lambda x: x.upper()
)
```

For simple string operations, however, prefer:

```python
df["Name"] = df["Name"].str.upper()
```

---

## 20.3 Applying Across Rows

You can use:

```python
df.apply(function, axis=1)
```

`axis=1` means operate row-wise.

Example:

```python
def get_total(row):
    return row["Maths"] + row["Science"]

df["Total"] = df.apply(
    get_total,
    axis=1
)
```

### Important

Don't use `apply()` for everything.

Whenever possible, use Pandas/NumPy vectorized operations because they are generally clearer and faster.

---

# 21. GroupBy and Aggregation

`groupby()` is one of the most important Pandas concepts for Data Analysis.

Suppose:

```python
df = pd.DataFrame({
    "Department": [
        "CSE", "CSE", "ECE", "ECE"
    ],
    "Marks": [80, 90, 70, 85]
})
```

---

## 21.1 Basic GroupBy

```python
df.groupby("Department")["Marks"].mean()
```

Result conceptually:

```text
Department
CSE    85
ECE    77.5
```

---

## 21.2 Sum

```python
df.groupby("Department")["Marks"].sum()
```

---

## 21.3 Count

```python
df.groupby("Department")["Marks"].count()
```

---

## 21.4 Multiple Aggregations

```python
df.groupby("Department")["Marks"].agg(
    ["mean", "min", "max", "count"]
)
```

---

## 21.5 GroupBy Multiple Columns

```python
df.groupby(
    ["Department", "Year"]
)["Marks"].mean()
```

---

## Why GroupBy Matters

It is frequently used for questions such as:

- Average salary by department
- Average sales by city
- Number of customers by category
- Maximum score by class
- Total revenue by product

It is one of the most valuable Pandas skills for exploratory data analysis.

---

# 22. Combining DataFrames

There are three important concepts:

```text
concat()
merge()
join()
```

---

# 22.1 `concat()`

Used to concatenate DataFrames along rows or columns.

Example:

```python
df1 = pd.DataFrame({
    "Name": ["Rahul", "Aman"],
    "Marks": [85, 90]
})

df2 = pd.DataFrame({
    "Name": ["Priya", "Rohan"],
    "Marks": [78, 88]
})

result = pd.concat(
    [df1, df2],
    ignore_index=True
)
```

---

## 22.2 Concatenate Columns

```python
pd.concat(
    [df1, df2],
    axis=1
)
```

---

# 22.3 `merge()`

Used to combine DataFrames based on common columns/keys.

Example:

```python
students = pd.DataFrame({
    "StudentID": [1, 2, 3],
    "Name": ["Rahul", "Aman", "Priya"]
})

marks = pd.DataFrame({
    "StudentID": [1, 2, 3],
    "Marks": [85, 92, 78]
})

result = pd.merge(
    students,
    marks,
    on="StudentID"
)
```

---

## 22.4 Merge Types

Common SQL-style joins:

```text
inner
left
right
outer
```

Example:

```python
pd.merge(
    students,
    marks,
    on="StudentID",
    how="left"
)
```

### Meaning

| Join | Meaning |
|---|---|
| `inner` | Only matching keys |
| `left` | All rows from left + matching right |
| `right` | All rows from right + matching left |
| `outer` | All rows from both |

---

# 23. Reading and Writing Files

Pandas is heavily used for loading datasets.

---

## 23.1 Read CSV

```python
df = pd.read_csv("data.csv")
```

CSV is one of the most common formats in Data Science.

---

## 23.2 Save to CSV

```python
df.to_csv("output.csv", index=False)
```

`index=False` prevents the DataFrame index from being saved as an extra column.

---

## 23.3 Read Excel

```python
df = pd.read_excel("data.xlsx")
```

---

## 23.4 Save Excel

```python
df.to_excel(
    "output.xlsx",
    index=False
)
```

---

## 23.5 Read JSON

```python
df = pd.read_json("data.json")
```

---

## 23.6 Read SQL Data

Pandas can work with SQL databases.

Typical pattern:

```python
df = pd.read_sql(
    "SELECT * FROM students",
    connection
)
```

The exact connection setup depends on the database and Python driver.

---

## 23.7 Important `read_csv()` Options

```python
pd.read_csv(
    "data.csv",
    sep=",",
    header=0
)
```

Other useful parameters include:

```python
usecols=
nrows=
skiprows=
dtype=
parse_dates=
na_values=
```

Example:

```python
df = pd.read_csv(
    "data.csv",
    usecols=["Name", "Age", "Marks"]
)
```

---

# 24. Working with Dates and Times

Dates often appear as strings when a dataset is loaded.

Example:

```python
df["Date"]
```

Convert:

```python
df["Date"] = pd.to_datetime(df["Date"])
```

Now you can extract components.

---

## 24.1 Year

```python
df["Year"] = df["Date"].dt.year
```

---

## 24.2 Month

```python
df["Month"] = df["Date"].dt.month
```

---

## 24.3 Day

```python
df["Day"] = df["Date"].dt.day
```

---

## 24.4 Day of Week

```python
df["DayOfWeek"] = df["Date"].dt.dayofweek
```

---

## 24.5 Difference Between Dates

```python
df["Days"] = (
    df["EndDate"] - df["StartDate"]
).dt.days
```

Date/time operations are particularly useful for time-series datasets and feature engineering.

---

# 25. Renaming

## Rename Columns

```python
df.rename(
    columns={
        "Marks": "Score",
        "Name": "StudentName"
    },
    inplace=True
)
```

---

## Rename Index

```python
df.rename(
    index={0: "first", 1: "second"}
)
```

---

# 26. Indexes

Every DataFrame has an index.

Example:

```text
       Name  Marks
0      Rahul   85
1      Aman    92
2      Priya   78
```

The index is:

```text
0, 1, 2
```

---

## 26.1 Set a Column as Index

```python
df = df.set_index("Name")
```

Now:

```text
       Age  Marks
Name
Rahul   19   85
Aman    20   92
Priya   19   78
```

---

## 26.2 Reset Index

```python
df = df.reset_index()
```

---

## 26.3 Set a Specific Index

```python
df.index = ["a", "b", "c"]
```

Be careful: the number of index labels must match the number of rows.

---

# 27. Useful Data Operations

## 27.1 Unique Values

```python
df["City"].unique()
```

---

## 27.2 Number of Unique Values

```python
df["City"].nunique()
```

---

## 27.3 Value Counts

```python
df["City"].value_counts()
```

Useful for categorical data.

Example:

```text
Delhi       120
Mumbai       80
Chennai      50
```

---

## 27.4 Check Whether Values Exist

```python
df["City"].isin(["Delhi", "Mumbai"])
```

---

## 27.5 Maximum Row

```python
df.loc[df["Marks"].idxmax()]
```

---

## 27.6 Minimum Row

```python
df.loc[df["Marks"].idxmin()]
```

---

## 27.7 Correlation

For numerical columns:

```python
df.corr(numeric_only=True)
```

Correlation is useful during exploratory data analysis, but remember:

> Correlation does not automatically imply causation.

---

## 27.8 Transpose

```python
df.T
```

Rows become columns and columns become rows.

---

# 28. Pandas and NumPy

Pandas and NumPy work together extensively.

```python
import pandas as pd
import numpy as np
```

Example:

```python
df["Square"] = np.square(df["Marks"])
```

---

## NumPy Array from DataFrame

```python
array = df.to_numpy()
```

Or:

```python
array = df.values
```

`to_numpy()` is generally the clearer modern choice.

---

## Series to NumPy

```python
array = df["Marks"].to_numpy()
```

---

## Why Both Matter

Think of them like this:

```text
NumPy
  ↓
Numerical arrays + mathematical operations

Pandas
  ↓
Labeled/tabular data + cleaning + analysis
```

In Data Science, you'll frequently use both.

---

# 29. Pandas in Machine Learning

A typical ML workflow looks like:

```text
Raw Dataset
     ↓
     Pandas
     ↓
Load data
     ↓
Inspect data
     ↓
Clean data
     ↓
Handle missing values
     ↓
Remove duplicates
     ↓
Transform columns
     ↓
Feature engineering
     ↓
Split features and target
     ↓
NumPy / Scikit-learn
     ↓
Train ML model
```

Example:

```python
import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
print(df.info())
print(df.isna().sum())
```

Then:

```python
X = df.drop(columns=["Passed"])
y = df["Passed"]
```

Here:

- `X` = features
- `y` = target

Then these are usually passed into a machine-learning workflow.

---

# 30. Common Data Cleaning Workflow

A practical Pandas workflow can look like this:

```python
import pandas as pd

# 1. Load
df = pd.read_csv("data.csv")

# 2. Inspect
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# 3. Check missing values
print(df.isna().sum())

# 4. Check duplicates
print(df.duplicated().sum())

# 5. Remove duplicates
df = df.drop_duplicates()

# 6. Clean column names
df.columns = df.columns.str.strip()

# 7. Fix data types
df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce"
)

# 8. Handle missing values
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

# 9. Filter
df = df[df["Age"] >= 18]

# 10. Sort
df = df.sort_values("Age")

# 11. Save
df.to_csv("cleaned_data.csv", index=False)
```

This is only an example. The correct cleaning strategy depends on the dataset.

---

# 31. Important Functions Cheat Sheet

## Creating Data

```python
pd.Series()
pd.DataFrame()
```

## Reading Data

```python
pd.read_csv()
pd.read_excel()
pd.read_json()
pd.read_sql()
```

## Writing Data

```python
df.to_csv()
df.to_excel()
df.to_json()
```

## Inspecting

```python
df.head()
df.tail()
df.info()
df.describe()
df.sample()
df.shape
df.columns
df.index
df.dtypes
```

## Selecting

```python
df["column"]
df[["col1", "col2"]]
df.loc[]
df.iloc[]
```

## Filtering

```python
df[df["Age"] > 18]

df[
    (df["Age"] > 18) &
    (df["Marks"] > 80)
]

df["City"].isin(["Delhi", "Mumbai"])
df["Marks"].between(70, 90)
```

## Missing Data

```python
df.isna()
df.isna().sum()
df.dropna()
df.fillna()
```

## Duplicates

```python
df.duplicated()
df.duplicated().sum()
df.drop_duplicates()
```

## Sorting

```python
df.sort_values()
df.sort_index()
```

## Columns

```python
df.rename()
df.drop()
df.assign()
```

## Statistics

```python
df.mean()
df.median()
df.sum()
df.min()
df.max()
df.std()
df.var()
df.count()
```

## Categorical Analysis

```python
df["column"].unique()
df["column"].nunique()
df["column"].value_counts()
```

## Grouping

```python
df.groupby()
df.groupby().sum()
df.groupby().mean()
df.groupby().agg()
```

## Combining

```python
pd.concat()
pd.merge()
df.join()
```

## Dates

```python
pd.to_datetime()
df["date"].dt.year
df["date"].dt.month
df["date"].dt.day
```

## Conversion

```python
df.astype()
pd.to_numeric()
pd.to_datetime()
```

---

# 32. Common Mistakes

## Mistake 1 — Using `and` instead of `&`

Wrong:

```python
df[(df["Age"] > 18) and (df["Marks"] > 80)]
```

Correct:

```python
df[
    (df["Age"] > 18) &
    (df["Marks"] > 80)
]
```

---

## Mistake 2 — Forgetting parentheses

Wrong:

```python
df[df["Age"] > 18 & df["Marks"] > 80]
```

Correct:

```python
df[
    (df["Age"] > 18) &
    (df["Marks"] > 80)
]
```

---

## Mistake 3 — Confusing `loc` and `iloc`

Remember:

```text
loc  → labels
iloc → integer positions
```

---

## Mistake 4 — Accidentally modifying data

Be careful with chained indexing such as:

```python
df[df["Age"] > 18]["Marks"] = 100
```

This can lead to confusing assignment behavior.

Prefer:

```python
df.loc[df["Age"] > 18, "Marks"] = 100
```

---

## Mistake 5 — Treating missing values as zero automatically

A missing value doesn't necessarily mean zero.

For example:

```text
Salary = NaN
```

does not mean:

```text
Salary = 0
```

The correct treatment depends on what the missing value represents.

---

## Mistake 6 — Using `apply()` everywhere

This:

```python
df["Marks"].apply(lambda x: x + 5)
```

may be unnecessary.

Prefer vectorized operations:

```python
df["Marks"] + 5
```

Vectorization is generally faster and cleaner.

---

## Mistake 7 — Ignoring data leakage

When preparing data for ML, don't calculate preprocessing statistics from the test set.

For example, don't blindly calculate a mean using the entire dataset before splitting.

Use an ML preprocessing pipeline when appropriate.

---

# 33. What to Learn First

You don't need to memorize every Pandas method.

For **Data Science → AI → ML**, prioritize these:

## Tier 1 — Absolutely Essential

Master these:

```python
pd.DataFrame()
pd.Series()

pd.read_csv()

df.head()
df.tail()
df.info()
df.describe()

df.shape
df.columns
df.dtypes

df["column"]
df[["col1", "col2"]]

df.loc[]
df.iloc[]

df[df["column"] > value]

df.isna()
df.isna().sum()
df.fillna()
df.dropna()

df.drop_duplicates()

df.sort_values()

df["column"].unique()
df["column"].value_counts()

df.groupby()
```

---

## Tier 2 — Very Important

Learn next:

```python
pd.to_numeric()
pd.to_datetime()

df.astype()

df.rename()
df.drop()

df.apply()

pd.concat()
pd.merge()

df.set_index()
df.reset_index()

df.str.*
df.dt.*
```

---

## Tier 3 — Learn as Needed

Don't spend excessive time memorizing these initially:

```text
Complex MultiIndex operations
Advanced reshaping
Specialized window operations
Rare IO formats
Advanced categorical features
Complex time-series operations
```

You can learn these when a project requires them.

---

# Final Mental Model

The most useful way to think about Pandas is:

```text
                  PANDAS
                    │
        ┌───────────┴───────────┐
        ↓                       ↓
     Series                 DataFrame
                                │
       ┌────────────────────────┼────────────────────────┐
       ↓                        ↓                        ↓
    Inspect                   Select                  Clean
       │                        │                        │
 head/info/describe        loc/iloc/filter       NaN/duplicates
       │                        │                        │
       └────────────────────────┼────────────────────────┘
                                ↓
                            Transform
                                │
                   ┌────────────┼────────────┐
                   ↓            ↓            ↓
                apply()      groupby()     merge()
                                │
                                ↓
                             Analyze
                                │
                                ↓
                          Feature Engineering
                                │
                                ↓
                         Machine Learning
```

### The key idea

Don't learn Pandas as:

> "There are 100 functions I need to memorize."

Learn it as:

> **Load → Inspect → Select → Filter → Clean → Transform → Group → Combine → Analyze → Prepare for ML**

That's the workflow you'll repeatedly use with real datasets.
