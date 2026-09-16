import math

def compute_visual_tokens(image_height: int, image_width: int, patch_size: int,
                          max_resolution: int = None, add_cls_token: bool = True,
                          padding_strategy: str = 'pad') -> dict:
    """
    Compute the number of visual tokens a VLM produces for a given image.

    Args:
        image_height: Original image height in pixels.
        image_width: Original image width in pixels.
        patch_size: Side length of each square patch in pixels.
        max_resolution: If set, resize so longest side equals this value.
        add_cls_token: Whether a [CLS] token is prepended.
        padding_strategy: 'pad' to pad to patch multiple, 'truncate' to drop remainders.

    Returns:
        Dictionary with effective_height, effective_width, patches_h,
        patches_w, num_patches, total_tokens.
    """
    h = image_height
    w = image_width
    if max_resolution is not None and max(image_height, image_width)>max_resolution:
        scale = max_resolution/max(image_height, image_width)
        h = round(image_height * scale)
        w = round(image_width * scale)

    if padding_strategy == 'pad':
        patches_h = math.ceil(h/patch_size)
        patches_w = math.ceil(w/patch_size)
        effective_height = patches_h * patch_size
        effective_width = patches_w * patch_size
    else:
        patches_h = h//patch_size
        patches_w = w//patch_size
        effective_height = patches_h * patch_size
        effective_width = patches_w * patch_size
    num_patches = patches_h * patches_w
    
    if add_cls_token:
        total_tokens = num_patches + 1
    else:
        total_tokens = num_patches
    return {
        "effective_height": effective_height,
        "effective_width": effective_width,
        "patches_h": patches_h,
        "patches_w": patches_w,
        "num_patches": num_patches,
        "total_tokens": total_tokens,
    }
