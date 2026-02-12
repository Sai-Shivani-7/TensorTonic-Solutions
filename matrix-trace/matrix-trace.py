import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    sums=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i==j:
                sums+=A[i][j]
    return sums
    
