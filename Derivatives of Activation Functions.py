import numpy as np
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	# Your code here
	derivative = {}
	derivative_sigmoid = ((1)/(1+np.exp(-x)))*(1-(1)/(1+np.exp(-x)))
	derivative_relu = (1.0 if x>=1 else 0.0)
	derivative_tanh = 1 - ((np.exp(x)-np.exp(-x))/((np.exp(x) + np.exp(-x))))**2
	derivative.update({'sigmoid':derivative_sigmoid, 'tanh': derivative_tanh, 'relu': derivative_relu})
	return derivative