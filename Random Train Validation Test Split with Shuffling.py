import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    rows, cols = np.shape(data)
    rng = np.random.default_rng(seed).permutation(rows)
    train_end = int(rows * train_frac)
    train_data = np.array(data[rng[:train_end]])
    validation_end = train_end + int(rows*validation_frac)
    validation_data = np.array(data[rng[train_end:validation_end]])
    test_data = np.array(data[rng[validation_end:]])
    return train_data, validation_data, test_data