import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    labels,freq = np.unique(y_train,return_counts=True)
    maxi = np.argmax(freq)
    req = labels[maxi]
    return [req]*len(X_test)