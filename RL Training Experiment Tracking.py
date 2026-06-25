import numpy as np

def track_rl_experiment(episode_rewards: list, episode_lengths: list, window_size: int = 10) -> dict:
    """
    Summarize metrics from an RL training run.
    
    Args:
        episode_rewards: Total reward per episode
        episode_lengths: Number of timesteps per episode
        window_size: Window size for moving average and improvement calculation
    
    Returns:
        Dictionary with training summary statistics
    """
    total_episodes = len(episode_rewards)
    mean_reward = round(np.mean(episode_rewards),4)
    std_reward = round(np.std(episode_rewards),4)
    max_reward = np.max(episode_rewards)
    min_reward = np.min(episode_rewards)
    best_episode = episode_rewards.index(max_reward)
    mean_length = np.mean(episode_lengths)
    effective_window = min(window_size, total_episodes)

    first_moving_avg = round(float(np.mean(episode_rewards[:effective_window])), 4)
    final_moving_avg = round(float(np.mean(episode_rewards[-effective_window:])), 4)

    reward_improvement = round(final_moving_avg - first_moving_avg, 4)

    return {
        'total_episodes': total_episodes,
        'mean_reward': mean_reward,
        'std_reward': std_reward,
        'max_reward': max_reward,
        'min_reward': min_reward,
        'best_episode': best_episode,
        'mean_length': mean_length,
        'final_moving_avg': final_moving_avg,
        'reward_improvement': reward_improvement
    }