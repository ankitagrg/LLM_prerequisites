import numpy as np

# Creating Arrays
arr = np.array([1, 2, 3, 4])
matrix = np.array([[1, 2], [3, 4]])
zeros = np.zeros((2, 3))
ones = np.ones((3, 3))

print("Array:", arr)
print("Matrix:\n", matrix)

# Indexing and Slicing
print("First element:", arr[0])
print("Slice:", arr[1:3])

# Vectorized Operations
print("Array * 2:", arr * 2)
print("Array + 10:", arr + 10)

# Boolean Indexing
print("Elements > 2:", arr[arr > 2])

# Reshape and Linear Algebra
reshaped = np.arange(1, 10).reshape(3, 3)
print("3x3 Matrix:\n", reshaped)
print("Transpose:\n", reshaped.T)
print("Matrix * Matrix:\n", np.dot(reshaped, reshaped))
