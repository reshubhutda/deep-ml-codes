import torch

def linear_forward(x: torch.Tensor, W: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    # y = x W^T + b

    if x.shape[1] != W.shape[1]:
        return -1

    y = x @ W.T + b

    return y