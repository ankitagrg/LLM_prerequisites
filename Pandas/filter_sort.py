import pandas as pd

df = pd.DataFrame({
    "Name": ["Sita", "Som", "Ram", "Gita"],
    "Age": [25, 32, 30, 28],
    "City": ["Kathmandu", "Lalitpur", "Chitwan", "Pokhara"]
})

# Selecting columns
print("Names column:\n", df["Name"])

# Selecting rows
print("\nSecond row (iloc):\n", df.iloc[1])

# Filtering
print("\nAge > 28:\n", df[df["Age"] > 28])

# Sorting
print("\nSorted by Age:\n", df.sort_values(by="Age", ascending=False))
