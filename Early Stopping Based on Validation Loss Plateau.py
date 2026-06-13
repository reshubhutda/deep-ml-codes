import numpy as np

def early_stopping(val_losses: list[float], patience: int = 5, min_delta: float = 0.0) -> list[bool]:
	"""
	Determine at each epoch whether training should stop based on validation loss.
	
	Args:
		val_losses: List of validation losses at each epoch
		patience: Number of epochs to wait for improvement before stopping
		min_delta: Minimum change in validation loss to qualify as improvement
	
	Returns:
		List of booleans indicating whether to stop at each epoch
	"""
	# Your code here
	best= float("inf")
	result = []
	counter = 0
	for i in val_losses:
		if best - i > min_delta and i < best:
			best = i
			counter = 0
			result.append(False)
		else:
			counter  = counter + 1
			if counter >= patience:
				result.append(True)
			else:
				result.append(False)
	return result