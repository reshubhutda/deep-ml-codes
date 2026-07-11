import numpy as np

def calculate_contrast(img) -> int:
	"""
	Calculate the contrast of a grayscale image.
	Args:
		img (numpy.ndarray): 2D array representing a grayscale image with pixel values between 0 and 255.
	"""
	# Your code here
	list_ = img.flatten()
	max_ = np.max(list_)
	min_ = np.min(list_)
	return max_ - min_