import numpy as np

def hamming_distance_kanerva(state: list, prototypes: list, threshold: int) -> tuple:
	"""
	Compute Hamming distances and find active prototypes for Kanerva coding.

	Args:
		state: Binary state vector (list of 0s and 1s).
		prototypes: List of binary prototype vectors.
		threshold: Maximum Hamming distance for a prototype to be active.

	Returns:
		Tuple of (distances, active_indices).
	"""
	mismatched = []
	result = []
	for x in prototypes:
		count = 0
		for i in range(0,len(state)):
			if state[i]!=x[i]:
				count+=1
		mismatched.append(count)
	for i,j in enumerate(mismatched):
		if j<=threshold:
			result.append(i)
	return (mismatched, result)



