import matplotlib.pyplot as plt

# Bar chart
categories = ["A", "B", "C", "D"]
values = [3, 7, 5, 2]

plt.bar(categories, values, color="skyblue")
plt.title("Bar Chart Example")
plt.show()

# Pie chart
plt.pie(values, labels=categories, autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart Example")
plt.show()
