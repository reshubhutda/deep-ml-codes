import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	a1 = np.array(a)
	a2 = new_shape
	if(np.shape(a1)==a2):
		answer = a1
		return answer
	elif(np.shape(a1)[::-1]==a2):
		answer = a1.reshape(a2)
		answer = answer.tolist()
		return answer
	else:
		return []