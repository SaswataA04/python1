import numpy as np
from scipy import linalg

# Create a 4x4 square matrix
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 12, 12],
              [13, 14, 15, 17]])

print("Matrix A:")
print(A)
print("=" * 60)


# 1. QR DECOMPOSITION
print("\n1. QR DECOMPOSITION")
print("-" * 60)

Q, R = linalg.qr(A)

print("Q (Orthogonal matrix):")
print(Q)
print("\nR (Upper triangular matrix):")
print(R)

# Verify: A = Q · R
print("\nVerification: Q @ R =")
print(np.round(Q @ R, 6))
print("A =")
print(A)

# 2. SVD (Singular Value Decomposition)
print("\n" + "=" * 60)
print("\n2. SVD (Singular Value Decomposition)")
print("-" * 60)

U, S, Vt = linalg.svd(A)

print("U (Left singular vectors, 4x4):")
print(U)
print("\nS (Singular values, 1D array):")
print(S)
print("\nVt (Right singular vectors transposed, 4x4):")
print(Vt)

# Reconstruct A = U · Σ · Vt
Sigma = np.zeros((4, 4))
np.fill_diagonal(Sigma, S)
A_reconstructed = U @ Sigma @ Vt

print("\nReconstructed A (U @ Σ @ Vᵀ):")
print(np.round(A_reconstructed, 6))

# 3. LEAST SQUARES (lstsq)
print("\n" + "=" * 60)
print("\n3. LEAST SQUARES (lstsq)")
print("-" * 60)

# Solve A·x = b using least squares
b = np.array([1, 2, 3, 4])

x, residuals, rank, sv = linalg.lstsq(A, b)

print("b vector:")
print(b)
print("\nSolution x (least-squares):")
print(x)
print("\nResiduals (sum of squared errors):", residuals)
print("Rank of A:", rank)
print("Singular values of A:", sv)

print("\nVerification: A @ x =")
print(np.round(A @ x, 6))
print("Original b =", b)