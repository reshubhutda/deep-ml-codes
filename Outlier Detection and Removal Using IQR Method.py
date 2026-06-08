import numpy as np

def detect_outliers_iqr(data: list[float], k: float = 1.5) -> dict:
	"""
	Detect and remove outliers using the IQR method.
	
	Args:
		data: List of numerical values
		k: IQR multiplier for determining outlier bounds (default 1.5)
	
	Returns:
		Dictionary with 'cleaned_data', 'outlier_indices', 'lower_bound', 'upper_bound'
	"""
	# Your code here
	# 1+ (N-1)xP
	length_ = len(data)
	if length_<=0:
		return {
			'cleaned_data': [],
			'outlier_indices': [],
			'lower_bound': None,
			'upper_bound': None
		}
	outliers = []
	final = []
	median = np.median(data)
	sorted_data = sorted(data)
    Q1 = np.percentile(sorted_data, 25)
    Q3 = np.percentile(sorted_data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - k * IQR
    upper_bound = Q3 + k * IQR
	for i in range(0, length_):
		if data[i]<lower_bound or data[i]>upper_bound:
			outliers.append(i)
		else:
			final.append(data[i])	
	
	return {'cleaned_data': final, 'outlier_indices': outliers, 'lower_bound': lower_bound, 'upper_bound': upper_bound}
	