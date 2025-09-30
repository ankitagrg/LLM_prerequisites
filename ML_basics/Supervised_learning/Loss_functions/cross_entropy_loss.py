import numpy as np

# True labels (one-hot encoded)
y_true = np.array([[1, 0, 0], [0, 1, 0]])
# Predicted probabilities
y_pred = np.array([[0.7, 0.2, 0.1], [0.1, 0.8, 0.1]])

loss = -np.sum(y_true * np.log(y_pred)) / y_true.shape[0]
print("Cross-Entropy Loss:", loss)
