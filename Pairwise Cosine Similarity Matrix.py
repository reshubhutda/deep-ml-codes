import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    X = np.array(X)
    numerator = np.dot(X, X.T)
    magnitude = np.linalg.norm(X, axis=1, keepdims=True)
    denominator = np.dot(magnitude, magnitude.T)
    with np.errstate(divide="ignore", invalid="ignore"):
        result = numerator/denominator
        result = np.where(denominator == 0, 0, result)
    return result