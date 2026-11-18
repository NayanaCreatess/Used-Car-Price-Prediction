
import pandas as pd

# Load original dataset
df = pd.read_csv("data/car data.csv")

print("ORIGINAL DATASET")
print("Shape:", df.shape)

# 1. Check missing values
print("\nMISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# 2. Remove duplicate records
print("\nDUPLICATE ROWS:", df.duplicated().sum())

df = df.drop_duplicates()

# 3. Handle missing numerical values
numeric_columns = df.select_dtypes(include="number").columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# 4. Handle missing categorical values
categorical_columns = df.select_dtypes(include="object").columns

for col in categorical_columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

# 5. Check missing values after cleaning
print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

# 6. Check duplicate records
print("\nDUPLICATES AFTER CLEANING:")
print(df.duplicated().sum())

# 7. Display cleaned dataset
print("\nCLEANED DATASET")
print(df.head())

print("\nCLEANED DATASET SHAPE")
print(df.shape)

# 8. Save cleaned dataset
df.to_csv("data/cleaned_car_data.csv", index=False)

print("\nDATA CLEANING COMPLETED SUCCESSFULLY!")
print("Cleaned dataset saved successfully.")
