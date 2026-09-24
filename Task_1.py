import pandas as pd

# 1. Load the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")

# 2. Display the first 5 rows
print("\n----- FIRST 5 ROWS -----")
print(df.head())

# 3. Display number of entries and columns
print("\n----- DATASET SHAPE -----")
print("Number of Entries:", df.shape[0])
print("Number of Columns:", df.shape[1])

# 4. Display column names
print("\n----- COLUMN NAMES -----")
print(df.columns.tolist())

# 5. Display information about the dataset
print("\n----- DATASET INFORMATION -----")
df.info()

# 6. Display descriptive statistics
print("\n----- DESCRIPTIVE STATISTICS -----")
print(df.describe(include="all"))

# 7. Check missing values
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

# 8. Display data types
print("\n----- DATA TYPES -----")
print(df.dtypes)
