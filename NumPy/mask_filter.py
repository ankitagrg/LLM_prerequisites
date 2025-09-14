import numpy as np

arr = np.array([10, 15, 20, 25, 30])
mask = arr > 18
print("Mask:", mask)
print("Filtered elements:", arr[mask])

# Negative masking
print("Elements <= 20:", arr[arr <= 20])
