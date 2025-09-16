import pandas as pd

df = pd.DataFrame({
    "Date": pd.to_datetime(["2025-01-01", "2025-01-15", "2025-02-10", "2025-02-20"]),
    "Product": ["A", "B", "A", "C"],
    "Sales": [100, 200, 150, 250]
})

print("Sales by product:\n", df.groupby("Product")["Sales"].sum())


df["Month"] = df["Date"].dt.month
print("\nSales per month:\n", df.groupby("Month")["Sales"].sum())
