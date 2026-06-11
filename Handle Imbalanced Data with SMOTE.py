import numpy as np

def smote(X_minority, n_synthetic, k=5, random_seed=42):
    np.random.seed(random_seed)

    n_samples = X_minority.shape[0]
    synthetic_samples = []

    if n_synthetic == 0:
        return np.empty((0, X_minority.shape[1]))

    for i in range(n_synthetic):
        idx = np.random.randint(n_samples)
        sample = X_minority[idx]
        distances = np.linalg.norm(X_minority - sample, axis=1)
        neighbor_indices = np.argsort(distances)[1:k+1]
        neighbor_idx = np.random.choice(neighbor_indices)
        neighbor = X_minority[neighbor_idx]
        gap = np.random.random()
        synthetic = sample + gap * (neighbor - sample)

        synthetic_samples.append(synthetic)
    return np.array(synthetic_samples)