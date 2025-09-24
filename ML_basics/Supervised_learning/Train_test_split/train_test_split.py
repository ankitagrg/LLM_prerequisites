from sklearn.model_selection import train_test_split
import numpy as np

X = np.arange(10).reshape((5, 2))
y = np.array([1, 2, 3, 4, 5])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

print("X_train:\n", X_train)
print("X_test:\n", X_test)
print("y_train:", y_train)
print("y_test:", y_test)
