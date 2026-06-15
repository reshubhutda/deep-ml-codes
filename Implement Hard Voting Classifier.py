import numpy as np
def hard_voting_classifier(predictions: list[list[int]]) -> list[int]:
    """
    Implement a hard voting classifier using majority vote.
    
    Args:
        predictions: 2D list where predictions[i][j] is classifier i's prediction for sample j
        
    Returns:
        List of final predictions using majority vote
    """
    predictions = np.array(predictions)
    rows, columns = np.shape(predictions)
    result = []
    for i in range(columns):
        dict_ = {}
        count = 1
        for j in range(rows):
            if predictions[j][i] in dict_:
                dict_[predictions[j][i]] +=1
            else:
                dict_[predictions[j][i]] = count
        result.append(max(dict_, key=lambda x: (dict_[x], -x)))
    return result