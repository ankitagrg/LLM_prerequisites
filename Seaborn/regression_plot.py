import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Linear regression
sns.lmplot(x="total_bill", y="tip", data=tips)
plt.title("Linear Regression Plot")
plt.show()

# Polynomial regression (order=2)
sns.lmplot(x="total_bill", y="tip", data=tips, order=2)
plt.title("Polynomial Regression Plot")
plt.show()

# Multiple regression with hue
sns.lmplot(x="total_bill", y="tip", data=tips, hue="smoker", markers=["o","x"])
plt.title("Regression by Smoker Status")
plt.show()
