import numpy as np
from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	y_true = [item[0] for item in data]
	y_pred = [item[1] for item in data]
	array = np.zeros(shape=(2,2), dtype=int)
	for x,y in zip(y_true, y_pred):
		if x==1 and y==1:
			array[0][0] +=1
		elif x==1 and y==0:
			array[0][1] +=1
		elif x==0 and y==1:
			array[1][0] +=1
		else:
			array[1][1] +=1
			
	return array
