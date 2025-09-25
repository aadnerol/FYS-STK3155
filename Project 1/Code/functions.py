import numpy as np

def polynomial_features(x, p, intercept=False):
    n = len(x)
    # Condition on intercept:
    if intercept==True:
        X = np.zeros((n, p + 1))
        for i in range(p+1):
            X[:, i] = x ** i
            # First column becomes ones because for all x, x**i = 1 when i=0.
    else: 
        X = np.zeros((n, p))
        for i in range(p):
            X[:, i] = x ** (i+1)
    
    return X 



def Ridge_parameters(X, y, lam = 1.0):
    # Assumes X is scaled and has no intercept column
    p = X.shape[1]
    return np.linalg.pinv((X.T @ X)+ lam*np.eye(p)) @ X.T @ y
