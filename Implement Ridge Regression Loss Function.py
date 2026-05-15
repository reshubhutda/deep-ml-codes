import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# calculate prediction
	prediction = [w @ X[i] for i in range(len(X))]
	# Mean square error
	error = sum([(y_true[i] - prediction[i])**2 for i in range(len(X))])/len(X)
	
	# regularization
	reg = alpha*sum(w**2)

	# result

	result = error + reg
	return result