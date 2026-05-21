import torch

def flatten_then_reshape(x: torch.Tensor, new_shape) -> torch.Tensor:
    y = x.flatten()
    y = y.reshape(new_shape)
    return y

def transpose_last_two(x: torch.Tensor) -> torch.Tensor:
    # TODO: swap the last two dimensions of x
    return x.transpose(-1, -2)
