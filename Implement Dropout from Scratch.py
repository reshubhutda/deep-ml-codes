import torch

def dropout(x: torch.Tensor, p: float, training: bool) -> torch.Tensor:
    # TODO: implement inverted dropout
    if p == 0.0 or training == False:
        return x
    mask = (torch.rand(x.shape) > p).float()
    for i in range(0,len(x)):
        if mask[i] == 0:
            x[i] = 0
        else:
            x[i] = 1/(1.0-p)
    return x
