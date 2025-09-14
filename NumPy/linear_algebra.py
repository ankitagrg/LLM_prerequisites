import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

# Matrix multiplication
print("Dot Product:\n", np.dot(A,B))

# Transpose
print("Transpose A:\n", A.T)

# Determinant
print("Determinant A:", np.linalg.det(A))

# Inverse
print("Inverse A:\n", np.linalg.inv(A))
