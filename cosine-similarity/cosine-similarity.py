import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    if np.dot(a,b)==0:
        return 0
    ans = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return ans