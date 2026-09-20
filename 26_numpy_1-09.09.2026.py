#Find out the permutation mattix P , lower triangular matrix L amd upper trianglur mattix U .
# 
import numpy as np
from scipy.linalg import lu

def lu_decomposition_scipy(A):
    """
    Find P, L, U such that PA = LU
    """
    A = np.array(A, dtype=float)
    P, L, U = lu(A)
    
    print("Original Matrix A:")
    print(A)
    print("\nPermutation Matrix P:")
    print(P)
    print("\nLower Triangular Matrix L:")
    print(L)
    print("\nUpper Triangular Matrix U:")
    print(U)
    
    # Verify: PA = LU
    print("\nVerification (P @ A should equal L @ U):")
    print("P @ A =")
    print(P @ A)
    print("L @ U =")
    print(L @ U)
    
    return P, L, U


# Example usage
A = [[2, 1, 1],
     [4, -6, 0],
     [-2, 7, 2]]

P, L, U = lu_decomposition_scipy(A) 