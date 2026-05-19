import numpy as np

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
	log_proportion = np.log(sigma_q/sigma_p)
	mean_difference = (mu_p - mu_q)**2
	temp_ = (sigma_p**2 + mean_difference)/(2*sigma_q**2)
	return (log_proportion + temp_ - 0.5)