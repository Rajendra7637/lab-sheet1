# Lab Sheet-01: Python Setup and Dataset Exploration

**Name:** Rajendra Singh Bisht
**Roll No:** 253028065
**Course:** MCA, 3rd Semester (2026-2027)
**University:** COER University, Roorkee

## About this project

This is my work for Lab Sheet-01 of the Data Science and Machine Learning lab.
It has 35 small programs. The first ones set up Python and the libraries
(NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn). The rest load a CSV file
and explore it: look at the data, find missing values, clean it, and make
some simple graphs.

## What is in the folder

| File / Folder | What it does |
|---|---|
| `lab_sheet_01_all_programs.py` | All 35 programs in one file. Each program is its own cell. |
| `notebooks/lab_sheet_01.ipynb` | The same programs as a Jupyter notebook. |
| `datasets/students.csv` | The dataset I used. It has some missing values and duplicate rows. |
| `datasets/students_cleaned.csv` | Saved by Program 31 after removing duplicates. |
| `scripts/generate_dataset.py` | Creates `students.csv` again if it gets deleted. |
| `outputs/` | The graphs saved by the programs. |
| `requirements.txt` | The list of libraries to install. |

## Libraries used

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

Python version: 3.11 or above.

## How to run it

1. Install Python 3.11 or above.
2. Open the project folder in VS Code.
3. Open the terminal and make a virtual environment:

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   (On Linux or Mac, use `source venv/bin/activate`.)

4. Install the libraries:

   ```
   pip install -r requirements.txt
   ```

5. Run the whole file:

   ```
   python lab_sheet_01_all_programs.py
   ```

   Or open the file in VS Code and click **Run Cell** above any program
   to run one program at a time. You can also open the `.ipynb` file
   and run the cells there.

## What the programs cover

- **Programs 1-10:** Install Python, Jupyter and the libraries, check their
  versions, make a simple line plot, and create a virtual environment.
- **Programs 11-22:** Load the CSV, see the first and last rows, check the
  shape, column names, data types, missing values and unique values.
- **Programs 23-31:** Rename columns, select data with `loc` and `iloc`, filter,
  sort, add and delete columns, remove duplicates, and save a new CSV.
- **Programs 32-35:** Load a dataset from Scikit-learn, and make a histogram,
  a scatter plot and a correlation heatmap.

## Notes

- If the dataset is not found, check that you opened the main project folder
  in VS Code.
- The graphs are also saved in the `outputs/` folder.

## Conclusion

Doing this lab helped me understand how to set up a Python environment and how
to explore and clean a dataset with Pandas. I also learned to make basic graphs
with Matplotlib and Seaborn.
