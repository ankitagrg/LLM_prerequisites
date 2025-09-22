import sympy as sp

x = sp.Symbol('x')
f = x**2 + 3*x + 2

# Derivative
df = sp.diff(f, x)
print("Function:", f)
print("Derivative:", df)
