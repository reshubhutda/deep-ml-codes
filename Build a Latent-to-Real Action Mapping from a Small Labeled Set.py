import numpy as np

def map_latent_to_real(latents_labeled: np.ndarray, reals_labeled: np.ndarray, latents_query: np.ndarray) -> list:
    """Fit a linear map from latent actions to real actions using the labeled set,
    then apply it to latents_query. Return predictions as a nested list."""
    W = np.linalg.pinv(latents_labeled) @ reals_labeled
    A_hat = latents_labeled  @ W
    loss = np.sum((A_hat - reals_labeled)**2)
    A_pred = latents_query @ W 
    return A_pred