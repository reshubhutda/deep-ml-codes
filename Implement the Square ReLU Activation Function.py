import numpy as np

def square_relu(x: np.ndarray) -> dict:
	"""
	Apply the Square ReLU activation function and compute its derivative.
	
	Args:
		x: Input numpy array of any shape
	
	Returns:
		Dictionary with 'output' and 'derivative' as numpy arrays
	"""
	relu_activation = np.round((np.maximum(0, x))**2, 12)
	relu_activation_derivative = np.round(2 * np.maximum(0, x), 12)
	return {'output': relu_activation, 'derivative': relu_activation_derivative}