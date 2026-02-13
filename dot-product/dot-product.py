import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    ans = 0.0
    if(len(x)!=len(y)):
        raise ValueError("Lengths should be same") 
    for i in range(len(x)):
        ans += x[i] * y[i]
    return ans