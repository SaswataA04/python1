import numpy as np

# Define two 3x3 matrices
A = np.array([[2, 1, 3],
              [1, 4, 2],
              [3, 2, 5]])

B = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 10]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

# 1. Find the inverse of matrix A
try:
    A_inverse = np.linalg.inv(A)
    print("\n1. Inverse of Matrix A:")
    print(A_inverse)
except np.linalg.LinAlgError:
    print("\n1. Matrix A is singular (not invertible)")

# 2. Find the determinant of matrix B
det_B = np.linalg.det(B)
print(f"\n2. Determinant of Matrix B: {det_B:.4f}")

# 3. Print the result of A · A⁻¹ (should be identity matrix)
if 'A_inverse' in locals():
    result = np.dot(A, A_inverse)
    print("\n3. Result of A · A⁻¹:")
    print(result)
    print("\n(Note: This should be the identity matrix, with values very close to 1 on the diagonal and 0 elsewhere)")