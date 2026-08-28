import numpy as np

def clip_gradients_by_value(gradients: np.ndarray, clip_value: float) -> np.ndarray:
    """
    Clip gradient values to be within [-clip_value, clip_value].
    
    Args:
        gradients: A numpy array representing gradients (any shape)
        clip_value: The maximum absolute value for any gradient element (non-negative)
    
    Returns:
        Clipped gradients with same shape as input
    """
    gradients = gradients.flatten()
    lower_range_clip = - clip_value
    upper_range_clip = clip_value
    for i in range(len(gradients)):
        if gradients[i] > upper_range_clip:
            gradients[i] = upper_range_clip
        elif gradients[i] < lower_range_clip:
            gradients[i] = lower_range_clip
        else:
            continue
    return gradients