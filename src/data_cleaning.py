"""
=============================================================
  Data Cleaning Project - Employee Dataset
  Author: [Your Name]
  Description: Complete data cleaning pipeline with detailed steps
=============================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import os
import re
from datetime import datetime

# ─────────────────────────────────────────
# STEP 1: Load Raw Data
# ─────────────────────────────────────────
print("=" * 60)
print("  DATA CLEANING PROJECT - Employee Dataset")
print("=" * 60)

df = pd.read_csv("data/raw_data.csv")
print(f"\n✅ Data Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

print("\n📊 Missing Values (Before Cleaning):")
print(df.isnull().sum())

# ─────────────────────────────────────────
# STEP 2: Remove Duplicate Rows
# ─────────────────────────────────────────
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print(f"\n🗑️  Removed {before - after} duplicate(s). Remaining: {after}")

# ─────────────────────────────────────────
# STEP 3: Clean Column Names
# ─────────────────────────────────────────
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ─────────────────────────────────────────
# STEP 4: Fix Text Columns
# ─────────────────────────────────────────
df['name'] = df['name'].str.strip().str.title()
df = df[~df['name'].isin(['N/A', 'Na', 'None', 'Unknown'])]
df = df.dropna(subset=['name'])

gender_map = {'male': 'Male', 'm': 'Male', 'female': 'Female', 'f': 'Female'}
df['gender'] = df['gender'].str.strip().str.lower().map(
    lambda x: gender_map.get(x, x.capitalize()) if isinstance(x, str) else x
)
df['department'] = df['department'].str.strip().str.title()
df['city'] = df['city'].str.strip().str.title()
print(f"\n✅ Text columns cleaned.")

# ─────────────────────────────────────────
# STEP 5: Validate Emails
# ─────────────────────────────────────────
def is_valid_email(email):
    if pd.isna(email): return False
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', str(email).strip()))

df['email_valid'] = df['email'].apply(is_valid_email)
df.loc[~df['email_valid'], 'email'] = np.nan
df = df.drop(columns=['email_valid'])
print(f"✅ Invalid emails replaced with NaN.")

# ─────────────────────────────────────────
# STEP 6: Handle Age
# ─────────────────────────────────────────
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df.loc[(df['age'] < 18) | (df['age'] > 65), 'age'] = np.nan
df['age'] = df['age'].fillna(df['age'].median()).astype(int)
print(f"✅ Age cleaned. Range: {df['age'].min()} - {df['age'].max()}")

# ─────────────────────────────────────────
# STEP 7: Handle Salary
# ─────────────────────────────────────────
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
df.loc[df['salary'] < 0, 'salary'] = np.nan
df['salary'] = df.groupby('department')['salary'].transform(lambda x: x.fillna(x.median()))
df['salary'] = df['salary'].fillna(df['salary'].median()).astype(int)
print(f"✅ Salary cleaned. Range: {df['salary'].min()} - {df['salary'].max()}")

# ─────────────────────────────────────────
# STEP 8: Fix Dates
# ─────────────────────────────────────────
def parse_date(date_str):
    if pd.isna(date_str): return pd.NaT
    for fmt in ['%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y']:
        try: return datetime.strptime(str(date_str).strip(), fmt)
        except: continue
    return pd.NaT

df['joining_date'] = df['joining_date'].apply(parse_date)
df['joining_date'] = pd.to_datetime(df['joining_date'])
print(f"✅ Dates parsed.")

# ─────────────────────────────────────────
# STEP 9: Final Missing Values
# ─────────────────────────────────────────
df['city'] = df['city'].fillna(df['city'].mode()[0])
df['email'] = df['email'].fillna("unknown@placeholder.com")

# ─────────────────────────────────────────
# STEP 10: Save & Visualize
# ─────────────────────────────────────────
os.makedirs("outputs", exist_ok=True)
df.to_csv("outputs/cleaned_data.csv", index=False)
print(f"\n✅ Cleaned data saved! Final shape: {df.shape}")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Employee Data - Cleaned Dataset Overview', fontsize=16, fontweight='bold')

dept_counts = df['department'].value_counts()
axes[0, 0].bar(dept_counts.index, dept_counts.values, color='steelblue', edgecolor='white')
axes[0, 0].set_title('Employees by Department')
axes[0, 0].tick_params(axis='x', rotation=30)

gender_counts = df['gender'].value_counts()
axes[0, 1].pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%')
axes[0, 1].set_title('Gender Distribution')

axes[1, 0].hist(df['salary'], bins=8, color='teal', edgecolor='white')
axes[1, 0].set_title('Salary Distribution')

axes[1, 1].hist(df['age'], bins=8, color='coral', edgecolor='white')
axes[1, 1].set_title('Age Distribution')

plt.tight_layout()
plt.savefig("outputs/visualization.png", dpi=150, bbox_inches='tight')
print("✅ Visualization saved!")
print("\n🎉 DATA CLEANING COMPLETE!")
