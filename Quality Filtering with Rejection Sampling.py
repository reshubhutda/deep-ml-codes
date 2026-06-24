import numpy as np

def quality_filter_rejection_sampling(scores: list, threshold: float, n_select: int = None) -> dict:
    """
    Filter generated samples using quality-based rejection sampling.
    
    Args:
        scores: list of float quality scores for generated candidate samples
        threshold: minimum quality score required for acceptance
        n_select: optional maximum number of samples to return (top by score)
    
    Returns:
        dict with 'accepted_indices', 'acceptance_rate', 'mean_quality'
    """
    scores = np.array(scores)
    indices = np.argsort(scores)[::-1]
    filtered_indices = indices[scores[indices] > threshold] 
    if n_select == None:
        if len(filtered_indices)==0:
            return {
                'accepted_indices': [],
                'acceptance_rate': 0.0,
                'mean_quality': 0.0
            }
        acceptance_rate = len(filtered_indices)/len(scores)
        mean_quality = np.mean(scores[filtered_indices])
        return {'accepted_indices': list(filtered_indices), 'acceptance_rate': acceptance_rate, 'mean_quality': round(mean_quality,1)}
    else:
        if len(filtered_indices) == 0:
            return {
                'accepted_indices': [],
                'acceptance_rate': 0.0,
                'mean_quality': 0.0
            }

        selected_indices = filtered_indices[:n_select]

        acceptance_rate = len(filtered_indices) / len(scores)
        mean_quality = np.mean(scores[selected_indices])

        return {
            'accepted_indices': list(selected_indices),
            'acceptance_rate': round(acceptance_rate, 4),
            'mean_quality': round(mean_quality, 4)
        }