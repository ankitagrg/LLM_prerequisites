import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

plt.plot(x, [xi*2 for xi in x], label="y=2x")
plt.plot(x, [xi**2 for xi in x], label="y=x^2")

plt.title("Multiple Line Plots")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
