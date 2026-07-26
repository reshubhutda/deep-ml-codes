import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
    result = []

    if x.ndim == 3:
        x = np.reshape(
            x,
            (x.shape[0] * x.shape[1], x.shape[2])
        )

        for i in range(x.shape[1]): 
            total = 0
            for j in range(x.shape[0]):
                total += x[j][i]
            average = total / x.shape[0]
            result.append(average)
    return np.array(result)