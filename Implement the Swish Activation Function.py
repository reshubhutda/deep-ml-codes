import numpy as np
def swish(x: float) -> float:
	"""
	Implements the Swish activation function.

	Args:
		x: Input value

	Returns:
		The Swish activation value
	"""
	# Your code here
	sigma = 1/(1 + np.exp(-x))
	val = x * sigma
	return round(val,4)import numpy as np
def swish(x: float) -> float:
	"""
	Implements the Swish activation function.

	Args:
		x: Input value

	Returns:
		The Swish activation value
	"""
	# Your code here
	sigma = 1/(1 + np.exp(-x))
	val = x * sigma
	return round(val,4)