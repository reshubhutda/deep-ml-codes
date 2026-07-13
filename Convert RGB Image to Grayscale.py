import numpy as np

def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminosity method.
    
    Args:
        image: RGB image as list or numpy array of shape (H, W, 3)
               with values in range [0, 255]
    
    Returns:
        Grayscale image as 2D list with integer values,
        or -1 if input is invalid
    """
    # Write your code here
    image = np.array(image)
    result = []
    if image.ndim !=3 or np.any(image>255):
        return -1
    else:
        img_ = image.reshape(image.shape[0] * image.shape[1], image.shape[2])
        for i in img_:
            result.append(round(sum(i * [0.299, 0.587, 0.114])))
    return np.array(result).reshape(image.shape[:2]).tolist()
            