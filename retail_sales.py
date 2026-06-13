import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("retail_sales.csv")

# Statistical Summary
print(df.describe())

# Total Sales
df["TotalSales"] = (
    df["Electronics"] +
    df["Clothing"] +
    df["Groceries"]
)

print("Total Sales:", df["TotalSales"].sum())

# Sales Trend
plt.plot(df["Month"], df["TotalSales"])
plt.title("Monthly Retail Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# Category Comparison
df[["Electronics","Clothing","Groceries"]].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.show()