import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Histogram + KDE
sns.histplot(tips["total_bill"], kde=True)

plt.title("Distribution of Total Bill")
plt.show()

# KDE plot only
sns.kdeplot(tips["tip"], shade=True)

plt.title("KDE Plot of Tips")
plt.show()
