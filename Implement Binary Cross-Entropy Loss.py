import math

def binary_cross_entropy(y_true: list[float], y_pred: list[float], epsilon: float = 1e-15) -> float:
	"""
	Compute binary cross-entropy loss.
	
	Args:
		y_true: True binary labels (0 or 1)
		y_pred: Predicted probabilities (between 0 and 1)
		epsilon: Small value for numerical stability
	
	Returns:
		Mean binary cross-entropy loss
	"""
	# Your code here
	result = []
	for i, j in zip(y_true, y_pred):
		result.append((float(i * math.log(j) + (1 - i) * math.log(1 - j))))
	return -sum(result)/len(result)