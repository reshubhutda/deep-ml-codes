def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
	if z<0:
		result = abs(alpha)*z
		return result
	else:
		return z
