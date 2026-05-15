import numpy as np
def relu(z: float) -> float:
	if (z < 0.0 or z == 0.0):
		return 0.0
	else:
		value = max(0,z)
		return value
