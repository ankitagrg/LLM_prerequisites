import pandas as pd

df = pd.DataFrame({
    "Date": ["2025-01-01", "2025-02-15", "2025-03-20"],
    "Sales": [100, 200, 150]
})

df["Date"] = pd.to_datetime(df["Date"])
print("DataFrame with datetime:\n", df)

print("\nYear:\n", df["Date"].dt.year)
print("Month:\n", df["Date"].dt.month)
print("Day:\n", df["Date"].dt.day)
