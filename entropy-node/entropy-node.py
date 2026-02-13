import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    sums = 0.0
    label,freq=np.unique(y,return_counts=True);
    for i in range(len(label)):
        p = freq[i]/len(y)
        sums += p*np.log2(p)
    return -(sums)