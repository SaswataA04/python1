import numpy as np
from scipy import linalg

# Coefficient matrix A
A = np.array([[2, 3],
              [4, 5]])

# Constant vector B
B = np.array([8, 14])

# Solve the system
X = linalg.solve(A, B)

print("Solution:")
print(f"x = {X[0]}")
print(f"y = {X[1]}")