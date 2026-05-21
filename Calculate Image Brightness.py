
def calculate_brightness(img):
	if not img:
		return -1
	flat_list = []
	for row in img:
		if len(row)!=len(img):
			return -1
		for i in row:
			if (i<0 or i>=255):
				return -1
		flat_list.extend(row)
	result = sum(flat_list)/len(flat_list)
	return result
