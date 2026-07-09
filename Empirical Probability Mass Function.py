import numpy as np
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    len_ = len(samples)
    unique_ = np.unique(samples)
    result = []
    for i in unique_:
        count_ = samples.count(i)
        prob = count_/len_
        pmf = (i, prob)
        result.append(pmf)
    return result