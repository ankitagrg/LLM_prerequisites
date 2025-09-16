import numpy as np

N = 100000
points = np.random.rand(N, 2)
inside_circle = points[:,0]**2 + points[:,1]**2 <= 1
pi_estimate = 4 * np.sum(inside_circle) / N
print("Estimated Pi:", pi_estimate)
