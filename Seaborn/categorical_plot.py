import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Bar plot
sns.barplot(x="day", y="total_bill", data=tips)

plt.title("Average Total Bill per Day")
plt.show()

# Box plot
sns.boxplot(x="day", y="total_bill", data=tips, hue="sex")

plt.title("Boxplot of Total Bill by Day and Gender")
plt.show()
