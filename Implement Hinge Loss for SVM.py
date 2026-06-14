import numpy as np

def hinge_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Compute the average hinge loss for SVM classification.
    
    Args:
        y_true: Array of true labels (-1 or +1)
        y_pred: Array of predicted scores (raw SVM scores)
    
    Returns:
        Average hinge loss rounded to 4 decimal places
    """
    hinge_loss = [max(0,1-y_true[x]*y_pred[x]) for x in range(len(y_true))]
    return sum(hinge_loss)/len(hinge_loss)
