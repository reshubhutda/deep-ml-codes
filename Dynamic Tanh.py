import numpy as np

def dynamic_tanh(x: np.ndarray, alpha: float, gamma: float, beta: float) -> list[float]:
    # Your code here
    sinh = np.exp(alpha*x) - np.exp(alpha*-x)
    cosh = np.exp(alpha*x) + np.exp(alpha*-x)
    tanh = (sinh/cosh)
    return gamma*tanh+beta