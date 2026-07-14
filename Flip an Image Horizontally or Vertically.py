import numpy as np

def flip_image(image, direction):
    """
    Flip an image horizontally or vertically.
    
    Args:
        image: 2D or 3D list/array representing a grayscale or RGB image
        direction: string, either 'horizontal' or 'vertical'
    
    Returns:
        Flipped image as a nested list, or -1 if input is invalid
    """
    # Your code here
    if direction == 'horizontal' and np.ndim(image)>=2:
        for i in image:
            i.reverse()
        return image
    elif direction == 'vertical' and np.ndim(image)>=2:
        return image[::-1]
    else:
        return -1