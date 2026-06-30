import numpy as np

def top_quartile_mask(scores: list) -> list:
    """
    Return a boolean list marking scores in the top quartile (>= 75th percentile).
    """
    if not scores:
        return []
    top_percentile = np.percentile(scores, 75)
    result = []

    for i in scores:
        if i >= top_percentile:
            result.append(True)
        else:
            result.append(False)
    return result