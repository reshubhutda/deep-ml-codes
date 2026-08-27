import numpy as np

def he_initialization(n_in: int, n_out: int, mode: str = 'fan_in', distribution: str = 'normal', seed: int = None) -> np.ndarray:
    """
    Implement He (Kaiming) weight initialization.
    
    Parameters:
    n_in: number of input units
    n_out: number of output units
    mode: 'fan_in' or 'fan_out'
    distribution: 'normal' or 'uniform'
    seed: random seed for reproducibility
    
    Returns:
    numpy array of shape (n_in, n_out) with He-initialized weights
    """
    np.random.seed(seed)
    normal_fan_in = np.sqrt(2/n_in)
    normal_fan_out = np.sqrt(2/n_out)
    uniform_fan_in = np.sqrt(6/n_in)
    uniform_fan_out = np.sqrt(6/n_out) 
    if mode  == 'fan_in':
        if distribution == 'normal':
            return np.random.normal(loc = 0, scale = normal_fan_in, size = (n_in, n_out))
        else:
            return np.random.uniform(low = -uniform_fan_in, high = uniform_fan_in, size = (n_in, n_out))
    else:
        if distribution == 'normal':
            return np.random.normal(loc = 0, scale = normal_fan_out, size = (n_in, n_out))
        else:
            return np.random.uniform(low = -uniform_fan_out, high = uniform_fan_out, size = (n_in, n_out))