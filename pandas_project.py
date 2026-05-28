import pandas as pd

# Load Dataset
df = pd.read_csv("sample_data.csv")

print("Original Dataset")
print(df)

# Display First Rows
print("\nFirst 5 Rows")
print(df.head())

# Dataset Information
print("\nDataset Information")
print(df.info())

# Checking Missing Values
print("\nMissing Values")
print(df.isnull())

# Counting Missing Values
print("\nCount Missing Values")
print(df.isnull().sum())

# Filling Missing Values
print("\nFill Missing Values")
df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)

# Removing Missing Values
print("\nRemove Missing Values")
df.dropna(inplace=True)

print(df)

# Checking Data Types
print("\nData Types")
print(df.dtypes)

# Changing Data Types
print("\nConvert Age to Integer")
df["Age"] = df["Age"].astype(int)

print(df.dtypes)

# Checking Duplicate Rows
print("\nDuplicate Rows")
print(df.duplicated())

# Removing Duplicate Rows
print("\nRemoving Duplicates")
df.drop_duplicates(inplace=True)

print(df)

# Selecting Single Column
print("\nSelect Name Column")
print(df["Name"])

# Selecting Multiple Columns
print("\nSelect Multiple Columns")
print(df[["Name", "Age"]])

# Filtering Data
print("\nFilter Age > 25")
print(df[df["Age"] > 25])

# Sorting Data
print("\nSort by Age Ascending")
print(df.sort_values("Age"))

# Sort Descending
print("\nSort by Age Descending")
print(df.sort_values("Age", ascending=False))

# Adding New Column
print("\nAdd Salary Column")
df["Salary"] = [50000, 60000, 45000]

print(df)

# Save Cleaned Data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved successfully.")

