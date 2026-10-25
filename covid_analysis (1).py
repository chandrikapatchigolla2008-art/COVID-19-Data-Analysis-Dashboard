# ============================================================
# COVID-19 DATA ANALYSIS
# COMPLETE CODE
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. UPLOAD DATASET
# ============================================================

from google.colab import files

uploaded = files.upload()

# Automatically get uploaded filename
filename = next(iter(uploaded))

print("\nDataset file selected:", filename)


# ============================================================
# 2. LOAD DATASET
# ============================================================

df = pd.read_csv(filename)

print("\n================================================")
print("       DATASET LOADED SUCCESSFULLY")
print("================================================")

print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())


# ============================================================
# 3. DATA PREPROCESSING
# ============================================================

print("\n================================================")
print("             DATA PREPROCESSING")
print("================================================")


# Missing values before preprocessing
print("\nMissing values before preprocessing:")
print(df.isnull().sum())


# Convert Date column
df["Date_reported"] = pd.to_datetime(
    df["Date_reported"],
    errors="coerce"
)

print("\nDate column converted successfully.")


# Check duplicate records
duplicate_count = df.duplicated().sum()

print("\nDuplicate records:", duplicate_count)


# Remove duplicate records
df = df.drop_duplicates()

print("Duplicate records removed.")


# Identify numerical columns
numeric_cols = df.select_dtypes(
    include=["int64", "float64"]
).columns

print("\nNumerical columns:")
print(list(numeric_cols))


# Handle missing numerical values
df[numeric_cols] = df[numeric_cols].fillna(0)

print("\nMissing numerical values replaced with 0.")


# Check missing values after preprocessing
print("\nMissing values after preprocessing:")
print(df.isnull().sum())


# Check data types
print("\nData types:")
print(df.dtypes)


# ============================================================
# 4. PREPROCESSING RESULT
# ============================================================

print("\n================================================")
print("          PREPROCESSING COMPLETED")
print("================================================")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Countries:", df["Country"].nunique())


# ============================================================
# 5. MEAN
# ============================================================

print("\n================================================")
print("                    MEAN")
print("================================================")

mean_cases = df["New_cases"].mean()
mean_deaths = df["New_deaths"].mean()

print("Mean of New Cases:", mean_cases)
print("Mean of New Deaths:", mean_deaths)


# ============================================================
# 6. MEDIAN
# ============================================================

print("\n================================================")
print("                   MEDIAN")
print("================================================")

median_cases = df["New_cases"].median()
median_deaths = df["New_deaths"].median()

print("Median of New Cases:", median_cases)
print("Median of New Deaths:", median_deaths)


# ============================================================
# 7. DESCRIPTIVE STATISTICS
# ============================================================

print("\n================================================")
print("          DESCRIPTIVE STATISTICS")
print("================================================")

print(
    df[
        [
            "New_cases",
            "Cumulative_cases",
            "New_deaths",
            "Cumulative_deaths"
        ]
    ].describe()
)


# ============================================================
# 8. COUNTRY-WISE ANALYSIS
# ============================================================

country_cases = (
    df.groupby("Country")["Cumulative_cases"]
    .max()
    .sort_values(ascending=False)
)

print("\n================================================")
print("       TOP 10 COUNTRIES BY CASES")
print("================================================")

print(country_cases.head(10))


# ============================================================
# 9. BAR GRAPH - TOP 10 COUNTRIES
# ============================================================

top10 = country_cases.head(10)

plt.figure(figsize=(12, 6))

plt.bar(
    top10.index,
    top10.values
)

plt.title("Top 10 Countries by COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Cumulative Cases")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================================
# 10. LINE GRAPH - CASES TREND
# ============================================================

daily_cases = (
    df.groupby("Date_reported")["New_cases"]
    .sum()
)

plt.figure(figsize=(12, 6))

plt.plot(
    daily_cases.index,
    daily_cases.values
)

plt.title("COVID-19 Cases Trend Over Time")
plt.xlabel("Date")
plt.ylabel("New Cases")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================================
# 11. LINE GRAPH - DEATHS TREND
# ============================================================

daily_deaths = (
    df.groupby("Date_reported")["New_deaths"]
    .sum()
)

plt.figure(figsize=(12, 6))

plt.plot(
    daily_deaths.index,
    daily_deaths.values
)

plt.title("COVID-19 Deaths Trend Over Time")
plt.xlabel("Date")
plt.ylabel("New Deaths")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================================
# 12. PIE CHART - CASES VS DEATHS
# ============================================================

total_cases = df["New_cases"].sum()
total_deaths = df["New_deaths"].sum()

plt.figure(figsize=(7, 7))

plt.pie(
    [total_cases, total_deaths],
    labels=["Cases", "Deaths"],
    autopct="%1.1f%%"
)

plt.title("COVID-19 Cases vs Deaths")

plt.show()


# ============================================================
# 13. BAR GRAPH - CASES VS DEATHS
# ============================================================

plt.figure(figsize=(7, 5))

plt.bar(
    ["Cases", "Deaths"],
    [total_cases, total_deaths]
)

plt.title("COVID-19 Cases vs Deaths")
plt.xlabel("Category")
plt.ylabel("Count")

plt.show()


# ============================================================
# 14. FINAL RESULTS
# ============================================================

print("\n================================================")
print("              FINAL RESULTS")
print("================================================")

print("Total New Cases:", total_cases)
print("Total New Deaths:", total_deaths)
print("Number of Countries:", df["Country"].nunique())

print("\nMean New Cases:", mean_cases)
print("Median New Cases:", median_cases)

print("\nMean New Deaths:", mean_deaths)
print("Median New Deaths:", median_deaths)

print("\nMissing Values:", df.isnull().sum().sum())
print("Duplicate Rows:", df.duplicated().sum())

print("\n================================================")
print("       COVID-19 ANALYSIS COMPLETED")
print("================================================")
