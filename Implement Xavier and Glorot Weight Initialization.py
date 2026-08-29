import numpy as np

def xavier_init(fan_in: int, fan_out: int, mode: str = 'uniform', seed: int = 42) -> dict:
    """
    Perform Xavier/Glorot weight initialization.

    Args:
        fan_in (int): Number of input units.
        fan_out (int): Number of output units.
        mode (str): 'uniform' or 'normal'.
        seed (int): Random seed for reproducibility.

    Returns:
        dict: Contains 'weights' (nested list), 'shape' (list), and 'param' (float).
    """
    # Your code here
    np.random.seed(seed)
    normal_XaGl = np.sqrt(2/(fan_in + fan_out))
    uniform_XaGl = - np.sqrt(6/(fan_in + fan_out))
    if mode == "normal":
        normal = np.random.normal(loc = 0, scale = normal_XaGl, size=(fan_in, fan_out))
        return {'weights': normal, 'shape': [fan_in, fan_out], 'param':normal_XaGl}
    elif mode == "uniform":
        uniform = np.random.uniform(low = uniform_XaGl, high = abs(uniform_XaGl), size = (fan_in, fan_out))
        return {'weights': uniform, 'shape': [fan_in, fan_out], 'param': abs(uniform_XaGl)}
    else:
        raise ValueError("mode must be 'uniform' or 'normal'")
    