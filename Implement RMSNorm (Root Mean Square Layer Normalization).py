import numpy as np

def rmsnorm(x: np.ndarray, g: np.ndarray, eps: float = 1e-5) -> np.ndarray:
    """
    Apply RMSNorm to the input array.
    
    Parameters:
        x   : np.ndarray of shape (batch_size, features)
        g   : np.ndarray of shape (features,) - gain parameter
        eps : float - small constant for numerical stability
    
    Returns:
        np.ndarray of same shape as x
    """
    sq_x = x ** 2
    mean_x = np.mean(sq_x, axis = -1, keepdims = True)
    mean_x_eps = mean_x + eps
    sqrt_x = np.sqrt(mean_x_eps)
    x = x/sqrt_x
    return x * g
