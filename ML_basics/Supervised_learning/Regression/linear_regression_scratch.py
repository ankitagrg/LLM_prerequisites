import numpy as np

# Generate dummy data
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])  

# Initialize weights
m, b = 0, 0  
learning_rate = 0.01
epochs = 1000

for _ in range(epochs):
    y_pred = m * X + b
    error = y - y_pred
    m_grad = -(2/len(X)) * sum(X * error)
    b_grad = -(2/len(X)) * sum(error)
    m -= learning_rate * m_grad
    b -= learning_rate * b_grad

print(f"Final model: y = {m:.2f}x + {b:.2f}")
