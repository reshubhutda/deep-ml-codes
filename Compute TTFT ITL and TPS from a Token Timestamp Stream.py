import numpy as np
def compute_inference_metrics(timestamps):
	timestamps = np.array(timestamps)

	TTFT = float(timestamps[1] - timestamps[0])

	if len(timestamps) <= 2:
		ITL = 0.0
	else:
		ITL_diff = [timestamps[i] - timestamps[i - 1] for i in range(2, len(timestamps))]
		ITL = float(sum(ITL_diff) / len(ITL_diff))

	TPS = (len(timestamps) - 1) / (timestamps[-1] - timestamps[0])

	return {'ttft': TTFT, 'tps': TPS, 'itl': ITL}