"""Generate the sample student dataset used in Lab Sheet-01.

Run once:  python scripts/generate_dataset.py
Creates:   datasets/students.csv  (with a few missing values and duplicates
           on purpose, so the cleaning experiments have something to do).
"""
from pathlib import Path

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 120

cities = ["Roorkee", "Dehradun", "Haridwar", "Delhi", "Meerut", "Saharanpur"]
courses = ["BCA", "MCA", "B.Tech", "BSc IT"]

df = pd.DataFrame(
    {
        "student_id": np.arange(1001, 1001 + n),
        "name": [f"Student_{i}" for i in range(1, n + 1)],
        "age": rng.integers(19, 27, n),
        "gender": rng.choice(["Male", "Female"], n),
        "city": rng.choice(cities, n),
        "course": rng.choice(courses, n),
        "attendance": rng.normal(80, 10, n).clip(40, 100).round(1),
        "study_hours": rng.normal(5, 1.8, n).clip(0.5, 12).round(1),
        "marks_python": rng.normal(68, 12, n).clip(20, 100).round(0),
        "marks_ml": rng.normal(65, 13, n).clip(20, 100).round(0),
    }
)
# Overall score depends on the other columns (gives a nice correlation heatmap)
df["final_score"] = (
    0.35 * df["marks_python"]
    + 0.35 * df["marks_ml"]
    + 0.15 * df["attendance"]
    + 2.0 * df["study_hours"]
    + rng.normal(0, 3, n)
).clip(0, 100).round(1)

# Introduce missing values
for col, k in [("attendance", 6), ("study_hours", 5), ("marks_ml", 4), ("city", 3)]:
    df.loc[rng.choice(n, k, replace=False), col] = np.nan

# Introduce duplicate rows
df = pd.concat([df, df.sample(5, random_state=1)], ignore_index=True)

out = Path(__file__).resolve().parent.parent / "datasets" / "students.csv"
out.parent.mkdir(exist_ok=True)
df.to_csv(out, index=False)
print(f"Saved {out}  shape={df.shape}")
