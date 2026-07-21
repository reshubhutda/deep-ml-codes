import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
	# Your code here
	dot_1 = x @ w1
	dot_1_relu = [max(0, i) for i in dot_1]
	dot_2 = w2 @ dot_1_relu
	dot_2_shortcut = dot_2 + x
	dot_2_relu = [max(0,i) for i in dot_2_shortcut]
	return dot_2_relu