import numpy as np

def convert_range(values, c, d):
    values_array = np.array(values, dtype=float)
    shape_ = values_array.shape

    values = values_array.flatten()
    a = np.min(values)
    b = np.max(values)

    result = np.array(
        [c + ((d - c) / (b - a)) * (i - a) for i in values],
        dtype=float
    )

    result = result.reshape(shape_)
    return result