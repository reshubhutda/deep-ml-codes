def rejection_sampling_best_of_k(candidates, scores):
    """
    Select the highest-scoring candidate per prompt.

    Args:
        candidates: list of N lists, each containing K candidate outputs.
        scores: list of N lists, each containing K reward scores.

    Returns:
        List of N selected candidates.
    """
    result = []
    for i, j in zip(candidates, scores):
        result.append(i[j.index(max(j))])
    
    return result