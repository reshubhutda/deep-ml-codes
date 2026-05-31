import math

def cosine_with_warmup(step: int, warmup_steps: int, total_steps: int, base_lr: float) -> float:
    # TODO: piecewise linear warmup, then half-cosine decay
    if step > total_steps or step < 0:
        return 0.0
    
    #Linear Warmup
    if step<=warmup_steps:
        if warmup_steps == 0:
            return 0.0
        return base_lr*(step/warmup_steps)
    
    #Cosine Decay
    decay_step = step - warmup_steps
    decay_total = total_steps - warmup_steps

    if decay_total == 0:
        return 0.0

    progress = decay_step / decay_total
    return base_lr * 0.5 * (1 + math.cos(math.pi * progress))
