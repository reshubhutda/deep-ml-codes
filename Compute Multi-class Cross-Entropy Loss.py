import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    # Your code here
    predicted_probs = predicted_probs.flatten()
    true_labels = true_labels.flatten()
    index = np.where(true_labels == 1)[0]
    prob = []
    for i in index:
        prob.append(predicted_probs[i])
    prob = np.clip(prob, epsilon, 1.0)
    return -np.mean(np.log(prob))