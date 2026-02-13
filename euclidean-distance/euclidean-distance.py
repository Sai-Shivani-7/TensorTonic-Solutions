import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    sums = 0
    if len(x) != len(y):
        raise ValueError("Vectors must be of the same length")
    for i in range(min(len(x),len(y))):
        sums+= (x[i]-y[i])**2
    return np.sqrt(sums)
