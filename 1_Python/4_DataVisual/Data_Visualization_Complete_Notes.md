# Data Visualization --- Complete Notes for Data Science, AI & ML

> Practical notes for Python Data Visualization with **Matplotlib,
> Seaborn and Pandas plotting**. The goal is not to memorize plotting
> commands, but to learn how to choose, create and correctly interpret
> visualizations for EDA and ML.

## 1. What is Data Visualization?

**Definition:** Data Visualization is the graphical representation of
data using charts, plots and graphs so that patterns, trends,
distributions, relationships, comparisons and anomalies can be
understood more easily.

**Simple meaning:** Instead of reading thousands of numbers, we turn
them into a visual form that makes useful patterns easier to see.

### Why do we need it?

-   Understand datasets quickly
-   Perform Exploratory Data Analysis (EDA)
-   Find trends and relationships
-   Detect potential outliers
-   Compare categories
-   Understand distributions
-   Detect data-quality issues
-   Communicate findings
-   Understand features before ML
-   Diagnose model performance after ML

## 2. Data Visualization in the Data Science Workflow

``` text
Raw Data → Cleaning → EDA → Visualization → Feature Engineering → ML → Evaluation
```

Visualization is heavily used during EDA, but it is also useful for
model diagnostics and communicating results.

A useful EDA flow is:

``` text
Load → Inspect → Clean → Analyze distributions → Analyze relationships
→ Investigate outliers → Find patterns → Prepare for ML
```

## 3. Main Python Libraries

  Library           Main role
  ----------------- --------------------------------------------------
  Matplotlib        Fundamental plotting and detailed control
  Seaborn           Statistical and DataFrame-oriented visualization
  Pandas plotting   Quick plots directly from DataFrames
  Plotly            Interactive visualization

For a core Data Science course, learn **Matplotlib + Seaborn** first.

------------------------------------------------------------------------

# Part A --- Matplotlib

## 4. Matplotlib

**Definition:** Matplotlib is a Python library for creating static,
animated and interactive visualizations.

Import it as:

``` python
import matplotlib.pyplot as plt
```

Basic example:

``` python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()
```

## 5. Figure and Axes

A **Figure** is the complete drawing area. An **Axes** is an individual
plotting area inside the Figure.

Object-oriented style:

``` python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [2, 4, 6])
plt.show()
```

Think:

``` text
Figure
└── Axes
    ├── x-axis
    ├── y-axis
    └── plotted data
```

`plt.plot()` is convenient for simple work; `fig, ax = plt.subplots()`
is often clearer for multi-plot and reusable code.

## 6. Basic Plot Components

A professional plot commonly has:

-   Title
-   X-axis label
-   Y-axis label
-   Legend when multiple series exist
-   Appropriate ticks
-   Grid when useful
-   Clear units
-   Meaningful annotations when needed

Example:

``` python
plt.plot(x, y, label="Sales")
plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()
```

## 7. Line Plot

### Definition

A line plot connects observations and is especially useful for trends
across an ordered variable, particularly time.

``` python
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 150, 140, 180]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
```

Useful parameters:

``` python
plt.plot(
    x, y,
    color="blue",
    linestyle="--",
    marker="o",
    linewidth=2,
    label="Sales"
)
```

Common uses:

-   Time series
-   Stock prices
-   Temperature over time
-   Monthly sales
-   Training/validation loss
-   Model metrics across epochs

## 8. Multiple Lines

``` python
plt.plot(months, sales_2025, label="2025")
plt.plot(months, sales_2026, label="2026")
plt.legend()
plt.show()
```

Use a legend whenever viewers need to distinguish multiple series.

## 9. Scatter Plot

A scatter plot shows individual observations as points and is commonly
used to examine relationships between numerical variables.

``` python
hours = [1, 2, 3, 4, 5, 6]
scores = [40, 45, 52, 60, 68, 75]

plt.scatter(hours, scores, alpha=0.7)
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.title("Study Hours vs Score")
plt.show()
```

It can reveal:

-   Positive/negative association
-   Weak/strong association
-   Clusters
-   Outliers
-   Non-linear patterns

**Important:** association/correlation does not prove causation.

## 10. Bar Chart

A bar chart compares values across discrete categories.

``` python
subjects = ["Python", "NumPy", "Pandas", "ML"]
hours = [20, 12, 15, 25]

plt.bar(subjects, hours)
plt.xlabel("Subject")
plt.ylabel("Hours")
plt.title("Learning Hours")
plt.show()
```

Horizontal:

``` python
plt.barh(subjects, hours)
```

Typical uses: sales by product, students by department, customers by
city.

### Bar chart vs Histogram

  Bar chart                   Histogram
  --------------------------- -------------------------------
  Usually categorical         Numerical distribution
  Bars represent categories   Bars represent numerical bins
  Categories are discrete     Bins cover intervals

## 11. Histogram

A histogram shows the distribution of a numerical variable by dividing
its range into **bins**.

``` python
import numpy as np

data = np.random.default_rng(42).normal(50, 10, 500)
plt.hist(data, bins=20)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution")
plt.show()
```

Histograms help inspect:

-   Center
-   Spread
-   Skewness
-   Multiple peaks
-   Potential outliers

`bins` controls how the range is divided. Too few bins can hide
structure; too many can create noise.

## 12. Box Plot

A box plot summarizes a numerical distribution using quartiles and can
highlight potential outliers.

``` python
data = [10, 12, 13, 14, 15, 16, 18, 20, 50]
plt.boxplot(data)
plt.ylabel("Value")
plt.title("Box Plot")
plt.show()
```

Important concepts:

-   Q1 = first quartile
-   Median = Q2
-   Q3 = third quartile
-   IQR = Q3 - Q1

A common rule marks observations below `Q1 - 1.5 × IQR` or above
`Q3 + 1.5 × IQR` as potential outliers.

**Important:** a flagged point is not automatically an error.
Investigate it.

## 13. Pie Chart

A pie chart shows parts of a whole.

``` python
labels = ["Python", "Pandas", "NumPy", "ML"]
values = [30, 20, 20, 30]

plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Learning Distribution")
plt.show()
```

Use it only when there are relatively few categories and part-to-whole
is the main question. For precise comparisons, a bar chart is usually
easier to read.

## 14. Area Plot

``` python
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 40]

plt.plot(x, y)
plt.fill_between(x, y)
plt.show()
```

Useful for trends and some cumulative/compositional displays.

## 15. Subplots

Multiple plots can share one Figure.

``` python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot([1, 2, 3], [2, 4, 6])
axes[0, 1].bar(["A", "B", "C"], [10, 20, 15])
axes[1, 0].scatter([1, 2, 3], [3, 5, 4])
axes[1, 1].hist([1, 2, 2, 3, 3, 3, 4])

plt.tight_layout()
plt.show()
```

`figsize=(width, height)` controls the Figure size. `tight_layout()`
helps prevent labels from overlapping.

## 16. Save a Plot

``` python
plt.plot(x, y)
plt.savefig("plot.png", dpi=300, bbox_inches="tight")
plt.show()
```

-   `dpi` controls resolution.
-   `bbox_inches="tight"` reduces unnecessary whitespace.

## 17. Common Matplotlib Functions

``` python
plt.plot()
plt.scatter()
plt.bar()
plt.barh()
plt.hist()
plt.boxplot()
plt.pie()
plt.fill_between()

plt.title()
plt.xlabel()
plt.ylabel()
plt.legend()
plt.grid()
plt.xlim()
plt.ylim()
plt.xticks()
plt.yticks()

plt.figure()
plt.subplots()
plt.tight_layout()
plt.savefig()
plt.show()
```

------------------------------------------------------------------------

# Part B --- Seaborn

## 18. Seaborn

**Definition:** Seaborn is a statistical visualization library built on
top of Matplotlib. It provides higher-level functions, strong DataFrame
integration and convenient statistical plots.

``` python
import seaborn as sns
import matplotlib.pyplot as plt
```

## 19. Load a Sample Dataset

``` python
df = sns.load_dataset("tips")
print(df.head())
```

Sample datasets are useful for learning, but real projects normally use
your own CSV, database or other data source.

## 20. Scatter Plot

``` python
sns.scatterplot(data=df, x="total_bill", y="tip")
plt.show()
```

Color by category:

``` python
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="day"
)
plt.show()
```

`hue` maps a variable to color/group.

## 21. Line Plot

``` python
sns.lineplot(data=df, x="size", y="tip")
plt.show()
```

For time-series data, make sure the time variable is correctly typed,
ordered and appropriately aggregated.

## 22. Bar Plot

``` python
sns.barplot(data=df, x="day", y="total_bill")
plt.show()
```

**Important:** `barplot` is generally an estimation plot. It aggregates
y values by x category and displays an estimate plus uncertainty.

If you want the number of observations in each category, use
`countplot()`.

## 23. Count Plot

``` python
sns.countplot(data=df, x="day")
plt.show()
```

It displays the number of observations in each category.

## 24. Histogram

``` python
sns.histplot(data=df, x="total_bill", bins=20)
plt.show()
```

## 25. KDE Plot

KDE (Kernel Density Estimation) gives a smooth estimate of a numerical
distribution.

``` python
sns.kdeplot(data=df, x="total_bill")
plt.show()
```

KDE is an estimate affected by smoothing/bandwidth, so do not treat
every curve as exact ground truth.

## 26. Box Plot

``` python
sns.boxplot(data=df, x="day", y="total_bill")
plt.show()
```

Excellent for comparing numerical distributions across categories.

## 27. Violin Plot

A violin plot combines box-plot-like summary information with a density
shape.

``` python
sns.violinplot(data=df, x="day", y="total_bill")
plt.show()
```

Useful when distribution shape matters in addition to quartiles/median.

## 28. Pair Plot

A pair plot displays pairwise relationships among several numerical
variables.

``` python
sns.pairplot(df)
plt.show()
```

With categories:

``` python
sns.pairplot(df, hue="sex")
plt.show()
```

It is powerful for small-to-medium datasets, but can become expensive
and cluttered with many rows or columns.

## 29. Heatmap

A heatmap represents values with color intensity. A common EDA use is a
correlation matrix.

``` python
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.show()
```

`annot=True` writes values into cells.

## 30. Correlation Heatmap

``` python
corr = df.select_dtypes(include="number").corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Matrix")
plt.show()
```

Correlation describes association according to a particular correlation
measure; Pearson correlation mainly captures linear association.
**Correlation does not prove causation.**

## 31. Important Seaborn Functions

``` python
sns.scatterplot()
sns.lineplot()
sns.barplot()
sns.countplot()
sns.histplot()
sns.kdeplot()
sns.boxplot()
sns.violinplot()
sns.pairplot()
sns.heatmap()
sns.set_theme()
```

Useful parameters:

``` text
data, x, y, hue, style, size, palette, alpha, bins
```

Example:

``` python
sns.scatterplot(
    data=df,
    x="Age",
    y="Salary",
    hue="Department",
    size="Experience"
)
```

Do not add so many encodings that the chart becomes unreadable.

------------------------------------------------------------------------

# Part C --- Pandas Plotting

## 32. Plotting Directly from a DataFrame

``` python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
df["Sales"].plot()
plt.show()
```

Or:

``` python
df.plot(x="Month", y="Sales", kind="line")
plt.show()
```

Common `kind` values:

``` text
line
bar
barh
hist
box
area
pie
scatter
hexbin
```

Pandas plotting is excellent for quick EDA and uses Matplotlib
underneath.

------------------------------------------------------------------------

# Part D --- Choosing the Correct Visualization

## 33. Numerical vs Categorical Variables

### Numerical

Examples:

``` text
Age, Salary, Height, Temperature, Sales
```

Useful plots:

-   Histogram
-   KDE
-   Box plot
-   Violin plot
-   Scatter plot
-   Line plot

### Categorical

Examples:

``` text
City, Department, Product, Day, Gender
```

Useful plots:

-   Bar plot
-   Count plot
-   Box/violin plot with category on x-axis

## 34. Univariate, Bivariate and Multivariate Analysis

### Univariate

One variable.

``` python
sns.histplot(data=df, x="Age")
```

Ask: What is its distribution? Where is it centered? Is it skewed? Are
there potential outliers?

### Bivariate

Two variables.

``` python
sns.scatterplot(data=df, x="Age", y="Salary")
```

Ask: Are they associated? Is there a trend? Are there clusters or
outliers?

### Multivariate

Three or more variables.

``` python
sns.scatterplot(
    data=df,
    x="Age",
    y="Salary",
    hue="Department",
    size="Experience"
)
```

## 35. Plot Selection Cheat Sheet

  Goal                                           Useful visualization
  ---------------------------------------------- -----------------------
  Trend over time                                Line
  Relationship between two numerical variables   Scatter
  Numerical distribution                         Histogram / KDE
  Potential outliers                             Box plot
  Compare categories                             Bar plot
  Count observations by category                 Count plot
  Compare distributions by category              Box / Violin
  Pairwise relationships                         Pair plot
  Correlation matrix                             Heatmap
  Part-to-whole with few categories              Pie, when appropriate
  Multiple views in one figure                   Subplots

### Mental decision tree

``` text
What do I want to know?
        |
  ┌─────┼──────────────┐
  |     |              |
Trend  Distribution  Relationship
  |     |              |
Line  Histogram      Scatter
      KDE
      Box/Violin

Comparison → Bar / Box / Violin
Frequency  → Count plot
Correlation → Heatmap
```

------------------------------------------------------------------------

# Part E --- Visualization for EDA

## 36. Practical EDA Workflow

``` python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("employees.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
```

Then visualize distributions:

``` python
sns.histplot(data=df, x="Age", bins=20)
plt.show()
```

Potential outliers:

``` python
sns.boxplot(data=df, x="Salary")
plt.show()
```

Relationships:

``` python
sns.scatterplot(data=df, x="Experience", y="Salary")
plt.show()
```

Category comparison:

``` python
sns.boxplot(data=df, x="Department", y="Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

Correlation:

``` python
corr = df.select_dtypes(include="number").corr()
sns.heatmap(corr, annot=True)
plt.show()
```

## 37. Aggregation Before Plotting

Large datasets often need aggregation first.

``` python
monthly_sales = (
    df.groupby("Month")["Sales"]
      .sum()
      .reset_index()
)

sns.barplot(data=monthly_sales, x="Month", y="Sales")
plt.show()
```

The key idea is: **plot the statistic that answers the question**,
rather than automatically plotting every raw observation.

## 38. Date/Time Visualization

Convert date columns properly:

``` python
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

plt.plot(df["Date"], df["Sales"])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

Good practices:

-   Use datetime dtype
-   Sort chronologically
-   Aggregate when necessary
-   Avoid overcrowded labels

------------------------------------------------------------------------

# Part F --- Visualization + Machine Learning

## 39. Before ML

Use visualization to investigate:

-   Feature distributions
-   Outliers
-   Missing-data patterns
-   Feature relationships
-   Class imbalance
-   Potentially redundant features

Visualization does not replace statistical tests or domain knowledge.

## 40. Class Imbalance

``` python
print(df["target"].value_counts())

sns.countplot(data=df, x="target")
plt.show()
```

If one class dominates, accuracy alone may not adequately describe
classifier performance.

## 41. Residual Plot

For regression:

``` text
Residual = Actual - Predicted
```

Example:

``` python
residuals = y_actual - y_pred

sns.scatterplot(x=y_pred, y=residuals)
plt.axhline(0)
plt.xlabel("Predicted")
plt.ylabel("Residual")
plt.show()
```

Patterns in residuals can reveal non-linearity, changing variance, or
other model/data issues.

## 42. Confusion Matrix Heatmap

``` python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_true, y_pred)

sns.heatmap(cm, annot=True, fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
```

A confusion matrix summarizes counts of true positives, true negatives,
false positives and false negatives.

## 43. Training Curves

In ML/DL, line plots are commonly used for:

-   Training loss
-   Validation loss
-   Training accuracy
-   Validation accuracy
-   Other metrics across epochs

Example:

``` python
plt.plot(history["loss"], label="Training")
plt.plot(history["val_loss"], label="Validation")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.show()
```

These curves can help identify patterns such as overfitting, although
diagnosis should consider the full training setup.

------------------------------------------------------------------------

# Part G --- Customization and Professional Charts

## 44. Figure Size

``` python
plt.figure(figsize=(10, 6))
```

## 45. Axis Limits

``` python
plt.xlim(0, 100)
plt.ylim(0, 200)
```

Use limits carefully; poor limits can hide information or exaggerate
visual differences.

## 46. Ticks

``` python
plt.xticks(rotation=45)
```

You can also specify tick positions and labels:

``` python
plt.xticks([1, 2, 3], ["Python", "Pandas", "ML"])
```

## 47. Transparency (`alpha`)

``` python
plt.scatter(x, y, alpha=0.3)
```

Useful when many points overlap.

## 48. Log Scale

``` python
plt.yscale("log")
```

Useful when values span several orders of magnitude. Always make the
scale clear to the reader.

## 49. Annotations

``` python
plt.annotate(
    "Important Point",
    xy=(3, 6),
    xytext=(4, 8),
    arrowprops={"arrowstyle": "->"}
)
```

Use annotations only when they add useful context.

## 50. Styling

``` python
sns.set_theme(style="whitegrid")
```

Good visualization is about clarity, not decoration. Avoid unnecessary
3D effects, excessive colors and clutter.

------------------------------------------------------------------------

# Part H --- Common Mistakes

## 51. Wrong Chart

Do not use a pie chart for dozens of categories. Use a chart suited to
the question.

## 52. Confusing Bar Chart and Histogram

Bar = categorical comparison.

Histogram = numerical distribution.

## 53. Misleading Axes

Especially for bar charts, unusual axis limits can exaggerate
differences.

## 54. Too Much Decoration

A beautiful chart that is difficult to interpret is not a good chart.

## 55. Ignoring Missing Values

Missing data can affect both calculations and visual interpretation.

## 56. Automatically Removing Outliers

An outlier can be:

-   A genuine rare observation
-   Measurement error
-   Data-entry error
-   A meaningful extreme case

Investigate before removing.

## 57. Correlation ≠ Causation

A visual relationship or correlation does not by itself establish a
causal relationship.

## 58. Plotting Everything

Every chart should answer a useful question. More charts do not
automatically mean better EDA.

## 59. Poor Labels

Use meaningful titles, axis labels, units and legends where needed.

## 60. Ignoring Data Types

Choose plots based on whether variables are numerical, categorical,
ordinal or temporal.

------------------------------------------------------------------------

# Part I --- Matplotlib vs Seaborn vs Pandas

  Feature                 Matplotlib   Seaborn     Pandas plotting
  ----------------------- ------------ ----------- -----------------
  Low-level control       Excellent    Good        Moderate
  Statistical plots       Basic        Excellent   Basic
  DataFrame integration   Good         Excellent   Excellent
  Quick EDA               Good         Excellent   Excellent
  Customization           Excellent    Excellent   Good
  Foundation value        Essential    Essential   Useful

A good learning order:

``` text
Matplotlib → Seaborn → Pandas plotting → Interactive tools
```

------------------------------------------------------------------------

# Part J --- End-to-End Example

``` python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data.csv")

# Basic inspection
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# Missing values
print(df.isnull().sum())

# Distribution
sns.histplot(data=df, x="Age", bins=20)
plt.title("Age Distribution")
plt.show()

# Potential outliers
sns.boxplot(data=df, x="Salary")
plt.title("Salary Distribution")
plt.show()

# Relationship
sns.scatterplot(data=df, x="Age", y="Salary")
plt.title("Age vs Salary")
plt.show()

# Category comparison
sns.boxplot(data=df, x="Department", y="Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlation
corr = df.select_dtypes(include="number").corr()
sns.heatmap(corr, annot=True)
plt.title("Correlation Matrix")
plt.show()
```

------------------------------------------------------------------------

# Part K --- What to Memorize

## Tier 1 --- Must Know

``` python
import matplotlib.pyplot as plt
import seaborn as sns

plt.plot()
plt.scatter()
plt.bar()
plt.hist()
plt.boxplot()

plt.title()
plt.xlabel()
plt.ylabel()
plt.legend()
plt.show()

sns.scatterplot()
sns.lineplot()
sns.barplot()
sns.countplot()
sns.histplot()
sns.boxplot()
sns.heatmap()
```

## Tier 2 --- Very Important

``` python
plt.subplots()
plt.tight_layout()
plt.savefig()

sns.violinplot()
sns.kdeplot()
sns.pairplot()

hue
style
size
alpha
bins
figsize
```

## Tier 3 --- Learn as Needed

-   Advanced annotations
-   Custom tick formatters
-   Advanced layouts
-   Complex styling
-   Specialized statistical plots
-   Interactive visualization libraries

Do not try to memorize every parameter. Learn the core functions, then
use documentation when you need a less-common option.

------------------------------------------------------------------------

# Part L --- Interview / Viva Questions

### 1. What is Data Visualization?

Graphical representation of data to communicate patterns, distributions,
relationships, trends and comparisons.

### 2. What is Matplotlib?

A Python visualization library that provides fundamental plotting and
detailed customization.

### 3. What is Seaborn?

A statistical visualization library built on top of Matplotlib.

### 4. Bar chart vs histogram?

A bar chart is generally used for categorical comparisons; a histogram
represents a numerical distribution using bins.

### 5. What is a scatter plot used for?

To inspect relationships/associations between two numerical variables.

### 6. What is a box plot used for?

To summarize a numerical distribution and identify potential outliers.

### 7. What is a heatmap?

A visualization in which values are represented through color intensity.

### 8. What is `hue` in Seaborn?

It maps a variable to color/grouping in a plot.

### 9. What is `figsize`?

It controls Figure dimensions.

### 10. What does `bins` do in a histogram?

It controls how the numerical range is divided into intervals.

### 11. Does correlation imply causation?

No.

### 12. What is EDA?

Exploratory Data Analysis: examining and understanding data through
statistics, visualization and analytical techniques.

------------------------------------------------------------------------

# Part M --- Practice Questions

## Beginner

1.  Plot daily temperatures with a line plot. Add labels and markers.
2.  Create a bar chart comparing four products and their sales.
3.  Generate 1,000 random numerical values and create a histogram with
    different bin counts.
4.  Create a box plot and investigate potential outliers.
5.  Create a scatter plot of study hours vs exam score.

## Intermediate

1.  Load a CSV and inspect shape, data types and missing values.
2.  Plot numerical distributions.
3.  Plot category frequencies with `countplot`.
4.  Compare a numerical variable across categories with box plots.
5.  Create a correlation heatmap.
6.  Build a 2×2 subplot figure containing four different chart types.
7.  Create a scatter plot with `hue` for a categorical feature.

## Advanced Beginner

Perform complete EDA on an ML dataset:

``` text
Dataset overview
↓
Data types
↓
Missing values
↓
Numerical distributions
↓
Categorical frequencies
↓
Outliers
↓
Relationships
↓
Correlation
↓
Insights
```

Then write down at least five observations from the visualizations and
explain which observations are descriptive versus which would require
statistical/domain validation.

------------------------------------------------------------------------

# Final Mental Model

``` text
DATA
 ↓
Understand Variables
 ↓
Ask a Question
 ↓
Choose the Right Plot
 ↓
Visualize
 ↓
Interpret
 ↓
Validate with Statistics / Domain Knowledge
 ↓
Take Action
```

The goal is **not**:

> I know 50 plotting functions.

The goal is:

> I can look at a dataset, ask the right question, choose an appropriate
> visualization, create it, and correctly interpret what it shows.

## Core Memory Map

``` text
Distribution → Histogram / KDE / Box Plot
Comparison   → Bar / Box / Violin
Relationship → Scatter
Trend        → Line
Correlation  → Heatmap
Frequency    → Count Plot
Multiple     → Subplots
```

That is the core Data Visualization foundation you need for Data
Science, EDA and the transition into Machine Learning.
