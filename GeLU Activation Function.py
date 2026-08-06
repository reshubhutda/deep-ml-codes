import numpy as np
import math

def GeLU(x: np.ndarray) -> np.ndarray:
	# Your code here
	scores = []
	for i in x:
		scores.append(0.5 * i * (1.0 + math.erf(i / math.sqrt(2.0))))
	return scores