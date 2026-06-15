import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	magnitude = np.array(gradient)
	magnitude = np.sqrt(sum(magnitude**2))
	if magnitude == 0.0:
		return {'magnitude': magnitude, 'direction': gradient}	
	direction = [i/magnitude for i in gradient]
	descent_direction = [-i for i in direction]
	return {'magnitude': magnitude, 'direction': direction, 'descent_direction': descent_direction}
