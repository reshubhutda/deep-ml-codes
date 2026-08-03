import numpy as np

def momentum_optimizer(parameter, grad, velocity, learning_rate=0.01, momentum=0.9):
    """
    Update parameters using the momentum optimizer.
    Uses momentum to accelerate learning in relevant directions and dampen oscillations.
    Args:
        parameter: Current parameter value
        grad: Current gradient
        velocity: Current velocity/momentum term
        learning_rate: Learning rate (default=0.01)
        momentum: Momentum coefficient (default=0.9)
    Returns:
        tuple: (updated_parameter, updated_velocity)
    """
    parameter = np.array(parameter, dtype=float, ndmin=1)
    grad = np.array(grad, dtype=float, ndmin=1)
    velocity = np.array(velocity, dtype=float, ndmin=1)
    for i in range(parameter.size):
        velocity[i] = momentum * velocity[i] + learning_rate * grad[i]
        parameter[i] = parameter[i] - velocity[i]
    return np.round(parameter, 5), np.round(velocity, 5)