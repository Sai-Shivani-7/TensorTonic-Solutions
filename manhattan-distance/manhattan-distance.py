import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    if(len(x)!=len(y)):
        raise ValueError("Lengths should be same")
    sums=0
    for i in range(len(x)):
        sums+=(max(x[i],y[i])-min(x[i],y[i]))
    return sums