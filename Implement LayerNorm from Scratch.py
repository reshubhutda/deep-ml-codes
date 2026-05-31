import torch

def layer_norm(x, gamma, beta, eps=1e-5):
    # TODO: normalize over the last dim, then affine-transform with gamma and beta
    mean_ = x.mean(dim=-1, keepdim=True)
    var_ = x.var(dim=-1, keepdim=True, unbiased = False)
    x_hat = (x-mean_)/torch.sqrt(var_ + eps)
    return gamma*x_hat + beta
