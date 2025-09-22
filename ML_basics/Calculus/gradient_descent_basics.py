import numpy as np

# Simple function: f(x) = x^2
def f(x):
    return x**2

def grad_f(x):
    return 2*x

# Gradient descent
x = 10.0
learning_rate = 0.1

for i in range(10):
    grad = grad_f(x)
    x = x - learning_rate * grad
    print(f"Iteration {i+1}: x = {x:.4f}, f(x) = {f(x):.4f}")
