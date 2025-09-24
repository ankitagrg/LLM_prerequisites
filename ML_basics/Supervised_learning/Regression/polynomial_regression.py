import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Generate non-linear data
X = np.array([1, 2, 3, 4, 5]).reshape(-1,1)
y = np.array([2, 6, 14, 28, 45])

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)

plt.scatter(X, y, color="red")
plt.plot(X, y_pred, color="blue")
plt.title("Polynomial Regression")
plt.show()
