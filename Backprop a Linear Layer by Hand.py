import torch

def linear_backward(grad_output, x, W):
    # TODO: return (grad_input, grad_W, grad_b) for y = x @ W.T + b
    # gradient wrt to input
    gi = grad_output @ W
    gW = grad_output.T @ x
    gb = grad_output.sum(dim=0)
    return gi, gW, gb
