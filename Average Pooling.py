import numpy as np
def avg_pool_2d(input_matrix: list[list[float]], pool_size: int) -> list[list[float]]:
	"""
	Perform 2D average pooling on the input matrix.
	
	Args:
		input_matrix: 2D input array of shape (H, W)
		pool_size: Size of the square pooling window
		
	Returns: 
		2D array after average pooling of shape (H//pool_size, W//pool_size)
	"""
	# Your code here
	input_matrix = np.array(input_matrix, dtype=float)
	rows, cols = input_matrix.shape
	output_rows = rows // pool_size
	output_cols = cols // pool_size
	output_matrix = np.zeros((output_rows, output_cols))
			
	for i in range(output_rows):
		for j in range(output_cols):
			start_row = i * pool_size
			start_col = j * pool_size
			region = input_matrix[start_row:start_row + pool_size,start_col:start_col + pool_size]
			output_matrix[i][j] = np.mean(region)
	return output_matrix.tolist()