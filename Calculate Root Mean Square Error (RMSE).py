
import numpy as np

def rmse(y_true, y_pred):
    y_true = np.array(y_true.flatten())
    y_pred = np.array(y_pred.flatten())
    difference = y_true - y_pred
    squared = np.sum(difference ** 2)
    rmse_res = np.sqrt(squared / len(y_true))
    return round(rmse_res, 3)

