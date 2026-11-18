
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/car data.csv")

# Basic information
print("DATASET SHAPE:", df.shape)

print("\nDATA TYPES:")
print(df.dtypes)

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

print("\nSTATISTICAL SUMMARY:")
print(df.describe())

# Set visualization style
sns.set_style("whitegrid")

# 1. Selling price distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Selling_Price"], kde=True)
plt.title("Distribution of Car Selling Prices")
plt.xlabel("Selling Price (Lakhs)")
plt.show()

# 2. Year vs Selling Price
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Year", y="Selling_Price")
plt.title("Manufacturing Year vs Selling Price")
plt.show()

# 3. Present Price vs Selling Price
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Present_Price",
                y="Selling_Price")
plt.title("Present Price vs Selling Price")
plt.show()

# 4. Fuel Type vs Selling Price
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Fuel_Type",
            y="Selling_Price")
plt.title("Fuel Type vs Selling Price")
plt.show()

# 5. Transmission vs Selling Price
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Transmission",
            y="Selling_Price")
plt.title("Transmission vs Selling Price")
plt.show()

# 6. Correlation heatmap
numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(),
            annot=True, cmap="coolwarm",
            fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

print("\nEDA COMPLETED SUCCESSFULLY!")
