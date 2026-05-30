import math
import torch

def sinusoidal_positional_encoding(seq_len: int, d_model: int) -> torch.Tensor:
    position = torch.arange(seq_len).unsqueeze(1)          
    i = torch.arange(0, d_model, 2)                        
    div_term = torch.exp(i * (-math.log(10000.0) / d_model))
    
    angles = position * div_term                            
    
    pe = torch.zeros(seq_len, d_model)
    pe[:, 0::2] = torch.sin(angles)                        
    pe[:, 1::2] = torch.cos(angles)                        
    
    return pe