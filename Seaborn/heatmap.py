import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
flights = sns.load_dataset("flights")

# Create pivot table correctly
pivot_table = flights.pivot(index="month", columns="year", values="passengers")

# Heatmap
sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")

plt.title("Flight Passengers Heatmap")
plt.show()
