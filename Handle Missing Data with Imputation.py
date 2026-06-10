import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    # Your code here
    rows, cols = data.shape
    for j in range(cols):
        if strategy == 'mean':
            mean_val = np.nanmean(data[:, j])
            data[:, j] = np.where(np.isnan(data[:, j]), mean_val, data[:, j])
        elif strategy == 'median':
            median_val = np.nanmedian(data[:, j])
            data[:, j] = np.where(np.isnan(data[:, j]), median_val, data[:, j])
        else:
            col = data[:, j]
            non_missing = col[~np.isnan(col)]
            if len(non_missing) == 0:                
                continue
            values, counts = np.unique(non_missing, return_counts=True)
            mode_val = values[np.argmax(counts)]     
            data[:, j] = np.where(np.isnan(col), mode_val, col)
    return data 