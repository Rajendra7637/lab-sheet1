# MCA III Sem - Lab Sheet-01 (Data Science & ML Environment)

COER University, Roorkee | Session 2026-2027

All 35 programs: environment setup, library installation, Jupyter, and dataset loading/exploration with Pandas, Matplotlib, Seaborn and Scikit-learn.

## Structure
- `lab_sheet_01_all_programs.py` - all programs, one `# %%` cell each (VS Code)
- `notebooks/lab_sheet_01.ipynb` - same programs as a Jupyter notebook
- `datasets/students.csv` - sample dataset (with missing values and duplicates)
- `scripts/generate_dataset.py` - regenerates the dataset
- `outputs/` - saved plots
- `requirements.txt`

## Run
```bash
python -m venv venv
venv\Scripts\activate          # Windows  (Linux/macOS: source venv/bin/activate)
pip install -r requirements.txt
python lab_sheet_01_all_programs.py
```
In VS Code: install the Python + Jupyter extensions, open the `.py` file, and click **Run Cell** on any block.
