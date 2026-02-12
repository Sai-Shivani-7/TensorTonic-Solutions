import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    transpose = [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
    return np.array(transpose)