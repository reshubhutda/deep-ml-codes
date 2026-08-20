import math

def tanh(x: float) -> float:
	"""
	Implements the Tanh (hyperbolic tangent) activation function.

	Args:
		x (float): Input value

	Returns:
		float: The tanh of the input, rounded to 4 decimal places
	"""
	# Your code here
	pos_exponential_of_x = math.exp(x)
	neg_exponential_of_x = math.exp(-x)
	return (pos_exponential_of_x - neg_exponential_of_x)/(pos_exponential_of_x + neg_exponential_of_x)
	