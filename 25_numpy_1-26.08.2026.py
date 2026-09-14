import numpy as np
from scipy import linalg

# Create a 4x4 square matrix
A = np.array([[4, 1, 2, 0],
              [1, 3, 0, 1],
              [2, 0, 5, 2],
              [0, 1, 2, 4]])

print("Matrix A (4x4):")
print(A)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors (each column is an eigenvector):")
print(eigenvectors)