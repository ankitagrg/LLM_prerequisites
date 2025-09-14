import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[10,20],[30,40]])

# Add scalar to matrix
print("A + 5:\n", A + 5)

# Elementwise addition
print("A + B:\n", A + B)

# Broadcasting 
row_vec = np.array([1,2])
print("A + row_vec:\n", A + row_vec)
