import numpy as np
def collect_rollouts(seeds: list[int], grid_size: int) -> list[int]:
	"""
	Collect optimal episode returns across procedurally generated gridworlds.

	Args:
		seeds: list of integer seeds, each defining one procedural environment.
		grid_size: side length of the square grid.

	Returns:
		A list of episode returns (one per seed).
	"""
	result = []
	for i in seeds:
		start = (0,0)
		gx = i % grid_size
		gy = (i // grid_size) % grid_size
		print(gx)
		print(gy)
		goal = (gx, gy)
		if gx == 0 and gy == 0:
			gx = grid_size - 1
			gy = grid_size - 1
			answer = 10 - (gx + gy)
			result.append(answer)
		else:
			distance = 10 - np.sum(np.abs(np.array(start) - np.array(goal)))
			result.append(distance)
	return result


