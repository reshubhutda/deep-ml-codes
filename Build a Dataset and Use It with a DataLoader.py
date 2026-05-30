import torch
from torch.utils.data import Dataset

class TensorPairDataset(Dataset):
    def __init__(self, X: torch.Tensor, y: torch.Tensor):
        # TODO: store X and y on the instance
        self.X = X
        self.y = y

    def __len__(self):
        # TODO: return the number of samples
        count = 0
        for i in self.y:
            count +=1
        return count

    def __getitem__(self, idx):
        # TODO: return the (x, y) pair at idx
        return (self.X[idx], self.y[idx])
