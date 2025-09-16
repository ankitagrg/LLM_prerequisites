import pandas as pd

# Create a DataFrame from a dictionary
data = {
    "Name": ["Rajesh", "Suresh", "Hari", "Gita"],
    "Age": [25, 32, 30, 28],
    
    "City": ["Kathmandu", "Lalitpur", "Bhaktapur", "Pokhara"]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)
print("\nFirst 2 rows:\n", df.head(2))
print("\nInfo:\n")
print(df.info())
print("\nDescription:\n", df.describe())
