import numpy as np
from math import factorial

def taylor_approximation(func_name: str, x: float, n_terms: int) -> float:
    """
    Compute Taylor series approximation for common functions.
    
    Args:
        func_name: Name of function ('exp', 'sin', 'cos')
        x: Point at which to evaluate
        n_terms: Number of terms in the series
    
    Returns:
        Taylor series approximation rounded to 6 decimal places
    """
    result = []
    for i in range(n_terms):
        match func_name:
            case 'exp':
                result.append((x**i)/factorial(i))
            case 'sin':
                result.append((((-1)**i)*x**(2*i+1))/factorial(2*i+1))
            case 'cos':
                result.append((((-1)**i)*x**(2*i))/factorial(2*i))            
    return sum(result)