# %% [markdown]
# # Lab Sheet-01: Python Environment, Libraries, Jupyter & Dataset Loading
# **MCA III Semester (Session 2026-2027) - COER University, Roorkee**
#
# Each `# %%` block is one experiment (a separate cell in VS Code / Jupyter).
# In VS Code click **Run Cell** above a block, or open as a notebook
# (`notebooks/lab_sheet_01.ipynb`).
#
# Libraries: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
# Dataset: `datasets/students.csv`

# %% [markdown]
# ## Setup: imports, paths and helper

# %%
import platform
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Project folder (works in a .py script and in a notebook)
try:
    BASE_DIR = Path(__file__).resolve().parent
except NameError:
    BASE_DIR = Path.cwd()
    if BASE_DIR.name == "notebooks":
        BASE_DIR = BASE_DIR.parent

DATA_PATH = BASE_DIR / "datasets" / "students.csv"
OUT_DIR = BASE_DIR / "outputs"
OUT_DIR.mkdir(exist_ok=True)


def load_students(path=DATA_PATH):
    """Load the dataset with validation and exception handling."""
    try:
        if not Path(path).exists():
            raise FileNotFoundError(f"Dataset not found: {path}")
        data = pd.read_csv(path)
        if data.empty:
            raise ValueError("Dataset is empty")
        return data
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as err:
        print("Error while loading dataset:", err)
        raise


# %% [markdown]
# ## Program 1: Install Python and verify the installed version

# %%
# Install: download from python.org (3.11+) or install Anaconda.
# Verify in terminal:  python --version
print("Python version :", sys.version)
print("Version tuple  :", sys.version_info[:3])
print("Platform       :", platform.platform())
assert sys.version_info >= (3, 11), "Python 3.11 or above is required"

# %% [markdown]
# ## Program 2: Install Jupyter Notebook and launch the interface

# %%
# Install:  pip install notebook jupyterlab
# Launch :  jupyter notebook      (or)   jupyter lab
try:
    import notebook

    print("Jupyter Notebook installed, version:", notebook.__version__)
except ImportError:
    print("Jupyter Notebook not installed. Run: pip install notebook")

# %% [markdown]
# ## Program 3: Install NumPy using pip and verify

# %%
# Install:  pip install numpy
print("NumPy version:", np.__version__)
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr, "| Mean:", arr.mean(), "| Sum:", arr.sum())

# %% [markdown]
# ## Program 4: Install Pandas using pip and verify

# %%
# Install:  pip install pandas
print("Pandas version:", pd.__version__)
sample_df = pd.DataFrame({"Name": ["Asha", "Ravi", "Neha"], "Marks": [88, 76, 92]})
print(sample_df)

# %% [markdown]
# ## Program 5: Install Matplotlib and create a simple line plot

# %%
# Install:  pip install matplotlib
import matplotlib

print("Matplotlib version:", matplotlib.__version__)
x_values = np.arange(1, 11)
y_values = x_values ** 2
plt.figure(figsize=(7, 4))
plt.plot(x_values, y_values, marker="o", color="tab:blue")
plt.title("Simple Line Plot: y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig(OUT_DIR / "p05_line_plot.png", dpi=120, bbox_inches="tight")
plt.show()

# %% [markdown]
# ## Program 6: Install Seaborn and generate a basic statistical plot

# %%
# Install:  pip install seaborn
print("Seaborn version:", sns.__version__)
students = load_students()
plt.figure(figsize=(7, 4))
sns.boxplot(data=students, x="course", y="final_score")
plt.title("Final Score by Course (Box Plot)")
plt.savefig(OUT_DIR / "p06_seaborn_boxplot.png", dpi=120, bbox_inches="tight")
plt.show()

# %% [markdown]
# ## Program 7: Install Scikit-learn and verify its version

# %%
# Install:  pip install scikit-learn
import sklearn

print("Scikit-learn version:", sklearn.__version__)

# %% [markdown]
# ## Program 8: First Python program in Jupyter Notebook

# %%
name = "MCA Student"
print(f"Hello, {name}! Welcome to Data Science and Machine Learning.")
print("2 + 3 =", 2 + 3)

# %% [markdown]
# ## Program 9: Python script in Visual Studio Code / PyCharm

# %%
# Save as hello_script.py and run:  python hello_script.py
def add_numbers(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


if __name__ == "__main__":
    print("Sum =", add_numbers(15, 27))

# %% [markdown]
# ## Program 10: Create a virtual environment and install libraries

# %%
# Run these commands in the VS Code terminal (not in this cell):
#   python -m venv venv
#   venv\Scripts\activate            (Windows)
#   source venv/bin/activate         (Linux / macOS)
#   pip install -r requirements.txt
#   deactivate
in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
print("Running inside a virtual environment:", in_venv)
print("Python executable:", sys.executable)

# %% [markdown]
# ## Program 11: Load a CSV dataset using Pandas

# %%
students = load_students()
print("Dataset loaded successfully from:", DATA_PATH.name)

# %% [markdown]
# ## Program 12: First five records using head()

# %%
print(students.head())

# %% [markdown]
# ## Program 13: Last five records using tail()

# %%
print(students.tail())

# %% [markdown]
# ## Program 14: Total number of rows and columns

# %%
rows, cols = students.shape
print(f"Rows: {rows}, Columns: {cols}")

# %% [markdown]
# ## Program 15: Names of all columns

# %%
print(list(students.columns))

# %% [markdown]
# ## Program 16: Data types of all columns

# %%
print(students.dtypes)

# %% [markdown]
# ## Program 17: Descriptive statistics of numerical features

# %%
print(students.describe())

# %% [markdown]
# ## Program 18: Complete information using info()

# %%
students.info()

# %% [markdown]
# ## Program 19: Identify missing values

# %%
print(students.isnull().head(10))
print("\nDoes the dataset contain missing values?", students.isnull().values.any())

# %% [markdown]
# ## Program 20: Count missing values in each column

# %%
missing_counts = students.isnull().sum()
print(missing_counts)
print("\nTotal missing values:", missing_counts.sum())

# %% [markdown]
# ## Program 21: Unique values in a selected column

# %%
column_name = "city"
if column_name in students.columns:
    print(f"Unique values in '{column_name}':", students[column_name].unique())
else:
    print(f"Column '{column_name}' not found")

# %% [markdown]
# ## Program 22: Frequency of each unique value in a column

# %%
print(students["course"].value_counts())

# %% [markdown]
# ## Program 23: Rename one or more columns

# %%
renamed = students.rename(
    columns={"marks_python": "python_marks", "marks_ml": "ml_marks"}
)
print(renamed.columns.tolist())

# %% [markdown]
# ## Program 24: Select rows and columns using loc[]

# %%
# Rows 0 to 4 (label based, end inclusive) and selected columns
print(students.loc[0:4, ["name", "course", "final_score"]])

# %% [markdown]
# ## Program 25: Select rows and columns using iloc[]

# %%
# First 5 rows (end exclusive), columns at positions 1, 5 and 10
print(students.iloc[0:5, [1, 5, 10]])

# %% [markdown]
# ## Program 26: Filter records based on a condition

# %%
high_scorers = students[students["final_score"] > 75]
print("Students with final_score > 75:", len(high_scorers))
print(high_scorers[["name", "course", "final_score"]].head())

# %% [markdown]
# ## Program 27: Sort the dataset using one or more columns

# %%
sorted_df = students.sort_values(by=["course", "final_score"], ascending=[True, False])
print(sorted_df[["name", "course", "final_score"]].head(10))

# %% [markdown]
# ## Program 28: Add a new column

# %%
students_new = students.copy()
students_new["result"] = np.where(students_new["final_score"] >= 50, "Pass", "Fail")
print(students_new[["name", "final_score", "result"]].head())

# %% [markdown]
# ## Program 29: Delete an existing column

# %%
students_new = students_new.drop(columns=["result"])
print("'result' column deleted. Columns now:", students_new.columns.tolist())

# %% [markdown]
# ## Program 30: Remove duplicate records

# %%
print("Duplicate rows before:", students.duplicated().sum())
students_clean = students.drop_duplicates().reset_index(drop=True)
print("Duplicate rows after :", students_clean.duplicated().sum())
print("Shape before:", students.shape, "| after:", students_clean.shape)

# %% [markdown]
# ## Program 31: Save the modified dataset as a new CSV file

# %%
try:
    output_file = BASE_DIR / "datasets" / "students_cleaned.csv"
    students_clean.to_csv(output_file, index=False)
    print("Saved:", output_file)
except OSError as err:
    print("Could not save file:", err)

# %% [markdown]
# ## Program 32: Load a dataset directly from Scikit-learn

# %%
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
iris_df = iris.frame
print(iris_df.head())
print("Shape:", iris_df.shape)
print("Target names:", iris.target_names.tolist())

# %% [markdown]
# ## Program 33: Histogram of a numerical feature (Matplotlib)

# %%
plt.figure(figsize=(7, 4))
plt.hist(students_clean["final_score"].dropna(), bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram of Final Score")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.savefig(OUT_DIR / "p33_histogram.png", dpi=120, bbox_inches="tight")
plt.show()

# %% [markdown]
# ## Program 34: Scatter plot between two variables

# %%
plt.figure(figsize=(7, 4))
plt.scatter(students_clean["study_hours"], students_clean["final_score"], alpha=0.7, color="tab:green")
plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours (per day)")
plt.ylabel("Final Score")
plt.grid(True)
plt.savefig(OUT_DIR / "p34_scatter.png", dpi=120, bbox_inches="tight")
plt.show()

# %% [markdown]
# ## Program 35: Correlation matrix and heatmap

# %%
numeric_df = students_clean.select_dtypes(include="number").drop(columns=["student_id"])
corr_matrix = numeric_df.corr()
print(corr_matrix.round(2))

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation Heatmap")
plt.savefig(OUT_DIR / "p35_heatmap.png", dpi=120, bbox_inches="tight")
plt.show()

# %% [markdown]
# ## Conclusion
# All 35 experiments of Lab Sheet-01 were executed successfully: the Python
# environment and libraries were verified, and a CSV dataset was loaded,
# explored, cleaned, saved and visualised.
