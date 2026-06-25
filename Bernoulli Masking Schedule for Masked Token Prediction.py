import numpy as np

def bernoulli_mask_schedule(seq_len: int, t: float, schedule: str, seed: int) -> list:
	"""
	Generate a Bernoulli mask whose probability is set by a schedule.

	Args:
		seq_len: length of the token sequence
		t: schedule parameter in [0, 1]
		schedule: 'linear' or 'cosine'
		seed: random seed

	Returns:
		A list of 0/1 integers of length seq_len (1 = masked).
	"""
	np.random.seed(seed)
	seq = np.random.rand(seq_len)
	if schedule == 'linear':
		p = t
		mask_seq = np.zeros(seq_len)
		mask_seq = np.where(np.array(seq) < p, 1.0, 0.0)
	else:
		p = 1 - np.cos((np.pi*t)/2)
		mask_seq = np.zeros(seq_len)
		mask_seq = np.where(np.array(seq) < p, 1.0, 0.0)
	return mask_seq