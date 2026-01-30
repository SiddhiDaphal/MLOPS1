import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:\\Users\\USER\\ML1\\data\\cleaned_sales.csv")

# Show first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Shape
print("\nRows & Columns:", df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Column names
print("\nColumn Names:")
print(df.columns)

# ----------------------------
# BASIC ANALYSIS
# ----------------------------

# If you have a 'Sales' column
if 'Sales' in df.columns:
    print("\nTotal Sales:", df['Sales'].sum())
    print("Average Sales:", df['Sales'].mean())
    print("Maximum Sales:", df['Sales'].max())
    print("Minimum Sales:", df['Sales'].min())

# Group by Category (if exists)
if 'Category' in df.columns:
    category_sales = df.groupby('Category')['Sales'].sum()
    print("\nSales by Category:")
    print(category_sales)

# Group by Region (if exists)
if 'Region' in df.columns:
    region_sales = df.groupby('Region')['Sales'].sum()
    print("\nSales by Region:")
    print(region_sales)

# ----------------------------
# SIMPLE VISUALIZATION
# ----------------------------

if 'Sales' in df.columns:
    plt.figure()
    df['Sales'].plot(kind='hist')
    plt.title("Sales Distribution")
    plt.show()

# Save cleaned data (optional)
df.to_csv("cleaned_sales.csv", index=False)

print("\nAnalysis Completed!")
