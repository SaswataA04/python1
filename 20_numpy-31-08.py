import numpy as np

# Coefficient matrix
A = np.array([
    [3, -5],
    [4, -2]
])

# Constant matrix
b = np.array([10, 7])

# Solve the equations
x, y = np.linalg.solve(A, b)

print("x =", x)
print("y =", y)