import numpy as np

def mae(y_true, y_pred):
    """
    Calculate Mean Absolute Error between two arrays.

    Parameters:
        y_true (numpy.ndarray): Array of true values
        y_pred (numpy.ndarray): Array of predicted values

    Returns:
        float: Mean Absolute Error
    """
    # Your code here
    y_true = y_true.flatten()
    y_pred = y_pred.flatten()
    abs_difference = sum(np.abs(y_true - y_pred))
    return (abs_difference)/len(y_true)