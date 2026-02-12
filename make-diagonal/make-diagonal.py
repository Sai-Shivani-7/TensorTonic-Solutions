import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    ans = np.zeros((len(v),len(v)))
    for i in range(len(v)):
        ans[i][i] = v[i]
    return ans
