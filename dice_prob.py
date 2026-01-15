import random
import argparse

def count_ways_to_sum(num_dice, target_sum):
    """
    Count the number of ways to get a target sum with num_dice dice.
    Uses dynamic programming approach.
    
    Returns the count of combinations that sum to target_sum.
    """
    # dp[i][s] = number of ways to get sum s using i dice
    # We'll use rolling array to save space
    
    max_sum = num_dice * 6
    
    # Initialize: with 0 dice, only sum 0 is possible (1 way)
    dp = [0] * (max_sum + 1)
    dp[0] = 1
    
    # Add dice one by one
    for dice in range(1, num_dice + 1):
        new_dp = [0] * (max_sum + 1)
        
        # For each possible sum
        for s in range(dice, min(dice * 6, max_sum) + 1):
            # Try each face value (1-6)
            for face in range(1, 7):
                if s - face >= 0:
                    new_dp[s] += dp[s - face]
        
        dp = new_dp
    
    return dp[target_sum]

def calculate_exact_probability(num_dice, target_sum):
    """
    Calculate the exact probability of getting target_sum with num_dice dice.
    """
    ways = count_ways_to_sum(num_dice, target_sum)
    total_outcomes = 6 ** num_dice
    probability = ways / total_outcomes
    
    return ways, total_outcomes, probability

def simulate_dice_throws(num_dice, target_sum, num_trials):
    """
    Simulate throwing num_dice dice for num_trials trials.
    Count how many times the sum equals target_sum.
    """
    success_count = 0
    
    for trial in range(num_trials):
        # Throw the dice
        dice_sum = sum(random.randint(1, 6) for _ in range(num_dice))
        
        # Check if we hit the target
        if dice_sum == target_sum:
            success_count += 1
    
    estimated_probability = success_count / num_trials
    
    return success_count, num_trials, estimated_probability

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Calculate and simulate dice probability'
    )
    parser.add_argument(
        '--trials',
        type=int,
        default=500,
        help='Number of simulation trials (default: 500)'
    )
    parser.add_argument(
        '--dice',
        type=int,
        default=10,
        help='Number of dice to throw (default: 10)'
    )
    parser.add_argument(
        '--target',
        type=int,
        default=32,
        help='Target sum (default: 32)'
    )
    
    args = parser.parse_args()
    
    # Problem parameters from arguments
    num_dice = args.dice
    target_sum = args.target
    num_trials = args.trials
    
    print("=" * 60)
    print("DICE PROBABILITY PROBLEM")
    print("=" * 60)
    print(f"Problem: What is the probability that {num_dice} dice sum to {target_sum}?")
    print(f"Simulation trials: {num_trials}")
    print()
    
    # Part 1: Exact calculation
    print("Part 1: EXACT CALCULATION")
    print("-" * 60)
    ways, total_outcomes, exact_prob = calculate_exact_probability(num_dice, target_sum)
    print(f"Number of ways to get sum {target_sum}: {ways:,}")
    print(f"Total possible outcomes: {total_outcomes:,}")
    print(f"Exact probability: {exact_prob:.10f}")
    print(f"Exact probability(%): {exact_prob * 100:.8f}%")
    print()
    
    # Part 2: Simulation
    print("Part 2: SIMULATION")
    print("-" * 60)
    print(f"Running {num_trials} trials...")
    successes, trials, sim_prob = simulate_dice_throws(num_dice, target_sum, num_trials)
    print(f"Successful trials (sum = {target_sum}): {successes}/{trials}")
    print(f"Estimated probability: {sim_prob:.10f}")
    print(f"Estimated probability(%): {sim_prob * 100:.8f}%")
    print()
    
    # Comparison
    print("COMPARISON")
    print("-" * 60)
    difference = abs(exact_prob - sim_prob)
    print(f"Exact probability:      {exact_prob * 100:.8f}%")
    print(f"Simulated probability:  {sim_prob * 100:.8f}%")
    print(f"Absolute difference:    {difference * 100:.8f}%")
    print("=" * 60)

if __name__ == "__main__":
    main()
