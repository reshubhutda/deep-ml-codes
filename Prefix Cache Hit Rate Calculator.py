import numpy as np

def prefix_cache_hit_rate(prompts: list, cache: list) -> dict:
    """
    Calculate the prefix cache hit rate for a batch of tokenized prompts.

    Args:
        prompts: List of tokenized prompts (list of list of ints).
        cache: List of cached prefixes (list of list of ints).

    Returns:
        Dictionary with 'hit_rate', 'cached_tokens', and 'total_tokens'.
    """
    # Your code here
    pass
    total_prompt_tokens = sum(len(prompt) for prompt in prompts)
    if total_prompt_tokens == 0:
        return {
        'hit_rate': 0.0,
        'cached_tokens': 0,
        'total_tokens': 0
                }
    total = 0
    for prompt in prompts:
        longest = 0
        for cache_entry in cache:
            if prompt[:len(cache_entry)] == cache_entry:
                longest = max(longest,len(cache_entry))
        total = total + longest
    return {'hit_rate': round(float(total/total_prompt_tokens),4), 'cached_tokens': total, 'total_tokens': total_prompt_tokens}

