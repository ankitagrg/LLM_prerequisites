import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Basic scatter plot with regression line
sns.lmplot(x="total_bill", y="tip", data=tips)

plt.title("Scatter Plot with Regression Line")
plt.show()
