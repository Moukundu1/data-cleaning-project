# 🧹 Data Cleaning Project — Employee Dataset

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-darkblue?logo=pandas)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

> A complete, beginner-friendly **Data Science project** that takes a messy, real-world style Employee Dataset and transforms it into clean, analysis-ready data — step by step.

---

## 📌 Project Overview

In the real world, data is **never perfect**. It comes with missing values, typos, duplicates, inconsistent formats, and invalid entries. Before any analysis or machine learning can be done, the data must be **cleaned and standardized**.

This project demonstrates a full **end-to-end data cleaning pipeline** on a fictional Employee Dataset with 20 records and 9 columns. Each step is carefully documented so beginners can follow along and understand the *why* behind every decision.

---

## 🎯 Objectives

- Identify and handle **missing values** using appropriate strategies
- Detect and remove **duplicate records**
- Standardize **inconsistent text** (gender labels, names, categories)
- Validate **emails** using regular expressions
- Remove and replace **outliers** in numerical columns
- Parse and fix **mixed date formats**
- Visualize the cleaned dataset with meaningful charts
- Save the final clean dataset for downstream analysis

---

## 🚨 Problems Found in the Raw Data

The raw dataset (`data/raw_data.csv`) contains the following real-world data quality issues:

| # | Problem | Example from Dataset |
|---|---------|----------------------|
| 1 | **Missing values** | Age, Salary, City left blank |
| 2 | **Duplicate rows** | Row 1 and Row 5 are identical |
| 3 | **Invalid email format** | `amitgmail.com` — missing the `@` symbol |
| 4 | **Inconsistent gender labels** | `male`, `M`, `Male`, `f`, `Female`, `F` all used |
| 5 | **Age outlier** | Age = `999` — clearly a data entry error |
| 6 | **Negative salary** | Salary = `-5000` — logically impossible |
| 7 | **Mixed date formats** | `15-03-2022` vs `2022-03-15` in same column |
| 8 | **Extra whitespace in names** | `  Meena Joshi  ` instead of `Meena Joshi` |
| 9 | **Placeholder / junk names** | `N/A` appearing as a person's name |
| 10 | **Inconsistent text case** | `AMIT KUMAR` vs `Priya Das` vs `ravi verma` |

---

## 🔧 Data Cleaning Steps (Pipeline)

Each step is implemented in both `src/data_cleaning.py` (script) and `notebooks/data_cleaning_notebook.ipynb` (interactive notebook).

### Step 1 — Load Raw Data
Read the CSV file using Pandas and get a first look at the data: shape, column types, and a summary of missing values.

### Step 2 — Remove Duplicate Rows
Use `drop_duplicates()` to identify and remove rows that are completely identical. Duplicates can skew analysis and model training.

### Step 3 — Clean Column Names
Strip extra whitespace, convert to lowercase, and replace spaces with underscores so all column names follow a consistent `snake_case` convention.

### Step 4 — Fix Text Columns
- **Name:** Strip leading/trailing spaces, apply Title Case, remove rows with placeholder values like `N/A`
- **Gender:** Map all variations (`M`, `male`, `f`, `Female`) to a standard format (`Male` / `Female`)
- **Department & City:** Strip spaces and apply consistent Title Case

### Step 5 — Validate Email Addresses
Use a **regular expression (regex)** pattern to check that every email follows the standard format (`user@domain.com`). Invalid emails (like `amitgmail.com` or `sanjay@`) are flagged and replaced with `NaN`.

### Step 6 — Handle Age Column
- Convert the column to numeric (non-numeric values become `NaN`)
- Flag values outside the realistic range of **18 to 65** as outliers
- Replace outliers and missing values with the **column median**

### Step 7 — Handle Salary Column
- Convert to numeric, forcing errors to `NaN`
- Remove logically impossible **negative salary** values
- Fill missing salaries with the **median salary within the same department** (group-wise imputation) for a smarter, context-aware fill

### Step 8 — Fix Mixed Date Formats
Write a custom parser that tries multiple date formats (`YYYY-MM-DD`, `DD-MM-YYYY`, `MM/DD/YYYY`) so that all dates are converted to a single consistent `datetime` format regardless of how they were originally entered.

### Step 9 — Handle Remaining Missing Values
- Fill any remaining missing `city` values with the **most frequent city (mode)**
- Fill missing `email` values with a standard placeholder `unknown@placeholder.com`

### Step 10 — Save Cleaned Data & Visualize
- Export the final cleaned DataFrame to `outputs/cleaned_data.csv`
- Generate 4 visualizations: Department distribution, Gender pie chart, Salary histogram, Age histogram
- Save charts to `outputs/visualization.png`

---

## 📁 Project Structure

```
data-cleaning-project/
│
├── data/
│   └── raw_data.csv                      # Original messy dataset (20 rows, 9 columns)
│
├── notebooks/
│   └── data_cleaning_notebook.ipynb      # Interactive Jupyter Notebook with explanations
│
├── src/
│   └── data_cleaning.py                  # Standalone Python script (full pipeline)
│
├── outputs/
│   ├── cleaned_data.csv                  # Final cleaned dataset
│   └── visualization.png                 # Charts generated from cleaned data
│
├── requirements.txt                      # Python dependencies
├── .gitignore                            # Files to exclude from Git
└── README.md                             # Project documentation (you are here)
```

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.10+** installed. You can check with:
```bash
python --version
```

### 1. Clone the Repository
```bash
git clone https://github.com/Moukundu1/data-cleaning-project.git
cd data-cleaning-project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Python Script
```bash
python src/data_cleaning.py
```
This will print step-by-step output to the terminal and save `cleaned_data.csv` and `visualization.png` inside the `outputs/` folder.

### 4. Or Open the Jupyter Notebook
```bash
jupyter notebook notebooks/data_cleaning_notebook.ipynb
```
The notebook walks through every step interactively with code cells and explanations — great for learning!

---

## 📊 Results Summary

| Metric | Before Cleaning | After Cleaning |
|--------|----------------|----------------|
| Total Rows | 20 | 19 |
| Duplicate Rows | 1 | 0 |
| Missing Values | 7 | 0 |
| Invalid Emails | 2 | 0 |
| Age Outliers | 1 (age=999) | 0 |
| Negative Salaries | 1 | 0 |
| Inconsistent Gender Labels | 5 formats | 2 (Male/Female) |
| Mixed Date Formats | 2 formats | 1 (datetime) |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.10+** | Core programming language |
| **Pandas** | Data loading, manipulation, and cleaning |
| **NumPy** | Numerical operations and NaN handling |
| **Matplotlib** | Data visualization and chart generation |
| **Seaborn** | Enhanced statistical visualizations |
| **Jupyter Notebook** | Interactive, step-by-step exploration |
| **re (Regex)** | Email validation using pattern matching |

---

## 💡 Key Concepts Covered

- `df.drop_duplicates()` — removing duplicate rows
- `df.isnull().sum()` — finding missing values
- `df.fillna()` and `groupby().transform()` — smart imputation
- `pd.to_numeric(errors='coerce')` — safe type conversion
- Regular expressions for data validation
- Outlier detection and treatment
- Multi-format date parsing with `strptime`
- Data visualization with Matplotlib

---

## 📚 Who Is This For?

This project is ideal for:
- 🎓 Students learning Data Science or Python
- 💼 Beginners building their first GitHub portfolio
- 👩‍💻 Anyone preparing for data analyst / data scientist roles
- 📖 Those who want to understand data cleaning before jumping into ML

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

## 🙋 Author

Made with ❤️ for learning Data Science.  


---

⭐ **If this project helped you, please give it a star!** ⭐
