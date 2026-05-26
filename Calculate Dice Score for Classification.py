
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	TP = sum((y_true==1) & (y_pred==1))
	FP = sum((y_true==0) & (y_pred==1))
	FN = sum((y_true==1) & (y_pred==0))
	if TP==0:
		return 0.0
	res = (2*TP)/(2*TP + FP + FN)
	return round(res, 3)
