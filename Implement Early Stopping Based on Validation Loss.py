import math

class EarlyStopping:
    def __init__(self, patience, mode='min'):
        self.patience = patience
        self.mode = mode
        self.bad_steps = 0

        if mode == 'min':
            self.best = math.inf
        else:
            self.best = -math.inf

    def step(self, metric):
        if self.mode == 'min':
            if metric < self.best:
                self.best = metric
                self.bad_steps = 0
                return False

        if self.mode == 'max':
            if metric > self.best:
                self.best = metric
                self.bad_steps = 0
                return False

        self.bad_steps += 1
        return self.bad_steps >= self.patience
