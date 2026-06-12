def apply_weight_decay(parameters: list[list[float]], gradients: list[list[float]], lr: float, weight_decay: float, apply_to_all: list[bool]) -> list[list[float]]:
	"""
	Apply weight decay (L2 regularization) to parameters.
	
	Args:
		parameters: List of parameter arrays
		gradients: List of gradient arrays
		lr: Learning rate
		weight_decay: Weight decay factor
		apply_to_all: Boolean list indicating which parameter groups get weight decay
	
	Returns:
		Updated parameters
	"""
	# Your code here
	w_new = []
	for a in range(len(parameters)):
		row = []
		for i in range(len(parameters[a])):
			if apply_to_all[a]:
				decay = lr * weight_decay * parameters[a][i] 
			else:
				decay = 0
			row.append(parameters[a][i] - lr * gradients[a][i] - decay)
		w_new.append(row)
	return w_new