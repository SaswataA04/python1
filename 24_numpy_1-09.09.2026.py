import numpy as np
from scipy import linalg

# Create a 4x4 matrix
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

print("Original Matrix A (4x4):")
print(A)
print(f"\nShape of A: {A.shape}")

# 1. Transpose of the matrix
A_transpose = A.T
print("\n1. Transpose of Matrix A (Aᵀ):")
print(A_transpose)

# 2. Rank of the matrix
rank_A = np.linalg.matrix_rank(A)
print(f"\n2. Rank of Matrix A: {rank_A}")