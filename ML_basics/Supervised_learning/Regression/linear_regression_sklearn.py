from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Print the model parameters
print("Coefficient (slope):", model.coef_[0])
print("Intercept:", model.intercept_)
print("Prediction for x=6:", model.predict([[6]])[0])
