def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	frequency = {}
	length_ = len(apples)
	for item in apples:
		if item in frequency:
			frequency[item] += 1
		else:
			frequency[item] = 1	
	for i,j in frequency.items():
		frequency[i] = j/length_
	gini = 1 - sum([i**2 for i in frequency.values()])
	return gini