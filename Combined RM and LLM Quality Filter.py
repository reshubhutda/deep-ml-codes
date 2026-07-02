import numpy as np
def combined_quality_filter(rm_scores, llm_scores):
    """
    Return a boolean list marking high-quality samples by combined RM and LLM criteria.
    """
    if not rm_scores or not llm_scores:
        return []
    percent = np.percentile(rm_scores, 75)
    max_ = max(llm_scores)
    result = []
    for i, j in zip(rm_scores, llm_scores):
        if i>=percent or j==max_:
            result.append(True)
        else:
            result.append(False)
    return result