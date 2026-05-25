
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	mean = np.mean(y_pred)
	SSR = sum([(y - x)**2 for x,y in zip(y_pred, y_true)])
	SST = sum([(x - mean)**2 for x in y_pred])
    if SST == 0:
        return 1.0 if SSR == 0 else 0.0	
	r_squared = 1 - (SSR/SST)
	return r_squared