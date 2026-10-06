def analyze_memory_fragmentation(block_status: list) -> dict:
	"""
	Analyze memory fragmentation in a block-based memory pool.

	Args:
		block_status: List of ints where 1 = allocated block, 0 = free block

	Returns:
		dict with keys:
			'utilization': float, fraction of allocated blocks
			'num_free_fragments': int, count of contiguous free regions
			'largest_free_fragment': int, size of largest contiguous free region
			'fragmentation_ratio': float, measure of free memory scatter
	"""
	len_ = len(block_status)
	if len_ == 0:
		return {
		'utilization': 0.0,
		'num_free_fragments': 0,
		'largest_free_fragment': 0,
		'fragmentation_ratio': 0.0
		}
	else:
		zeros = block_status.count(0)
		ones = block_status.count(1)
		utilization = round(ones / len_, 4)
		if zeros == len(block_status):
			return {
			'utilization': 0.0,
			'num_free_fragments': 1,
			'largest_free_fragment': len_,
			'fragmentation_ratio': 0.0
			}
		elif ones == len(block_status):
			return {
			'utilization': 1.0,
			'num_free_fragments': 0,
			'largest_free_fragment': 0,
			'fragmentation_ratio': 0.0
			}
		else:
			len_free_segment = []
			count = 0
			for i in block_status:
				if i == 0:
					count = count + 1
				else:
					if count > 0:
						len_free_segment.append(count)
						count = 0
			if count>0:
				len_free_segment.append(count)
			
			return {'utilization': utilization, 'num_free_fragments': len(len_free_segment), 'largest_free_fragment': max(len_free_segment), 'fragmentation_ratio': round(1.0 - (max(len_free_segment)) / block_status.count(0), 4)}