
import numpy as np
from collections import Counter
def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	length = len(y)
	count = dict(Counter(y))
	for i in count.keys():
		count[i] = (count[i]/length)**2
	val = 1 - sum(count.values())
	return round(val,3)