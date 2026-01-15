import random
import argparse
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def calculate_exact_probability(num_dice=10, target_sum=32):
    # Step 3.1: Initialize our DP table
    # dp[s] = number of ways to achieve sum 's'
    max_sum = num_dice * 6  # Maximum possible sum (all 6s)
    
    # Start with 0 dice: only way to get sum 0 is one way (do nothing)
    prev_dp = [0] * (max_sum + 1)
    prev_dp[0] = 1
    
    print(f"\n=== Exact Calculation (Dynamic Programming) ===")
    print(f"Calculating ways to get sum {target_sum} with {num_dice} dice...")
    
    # Step 3.2: Add dice one by one
    for die_num in range(1, num_dice + 1):
        current_dp = [0] * (max_sum + 1)
        
        # For each possible sum
        for total in range(die_num, max_sum + 1):
            # Try each face of the die (1 through 6)
            for face in range(1, 7):
                if total - face >= 0:
                    current_dp[total] += prev_dp[total - face]
        
        prev_dp = current_dp
        print(f"  Processed die {die_num}/{num_dice}")
    
    # Step 3.3: Calculate final probability
    ways_to_target = prev_dp[target_sum]
    total_outcomes = 6 ** num_dice
    probability = ways_to_target / total_outcomes
    
    print(f"\nResults:")
    print(f"  Ways to get {target_sum}: {ways_to_target:,}")
    print(f"  Total outcomes: {total_outcomes:,}")
    print(f"  Exact probability: {probability:.10f}")
    print(f"  Percentage: {probability * 100:.6f}%")
    
    return {
        'ways': ways_to_target,
        'total_outcomes': total_outcomes,
        'probability': probability,
        'percentage': probability * 100
    }

def run_simulation(num_trials=500, num_dice=10, target_sum=32):
    """
    Simulate dice throws and estimate probability.
    
    Parameters:
    - num_trials: number of experiments to run
    - num_dice: number of dice per trial (default 10)
    - target_sum: target sum we're looking for (default 32)
    
    Returns:
    - Dictionary with simulation results
    """
    
    print(f"\n=== Simulation ({num_trials} trials) ===")
    print(f"Running simulation...")
    
    success_count = 0
    trial_results = []  # Store each trial for Excel export
    
    # Step 4.1: Run each trial
    for trial in range(num_trials):
        # Throw dice
        dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]
        trial_sum = sum(dice_rolls)
        
        # Check if we hit the target
        is_success = (trial_sum == target_sum)
        if is_success:
            success_count += 1
        
        # Store trial data
        trial_results.append({
            'trial': trial + 1,
            'dice_rolls': dice_rolls,
            'sum': trial_sum,
            'success': is_success
        })
        
        # Progress indicator every 100 trials
        if (trial + 1) % 100 == 0:
            print(f"  Completed {trial + 1}/{num_trials} trials")
    
    # Step 4.2: Calculate estimated probability
    estimated_probability = success_count / num_trials
    
    print(f"\nResults:")
    print(f"  Successful trials: {success_count}/{num_trials}")
    print(f"  Estimated probability: {estimated_probability:.10f}")
    print(f"  Percentage: {estimated_probability * 100:.6f}%")
    
    return {
        'trials': num_trials,
        'successes': success_count,
        'probability': estimated_probability,
        'percentage': estimated_probability * 100,
        'trial_data': trial_results
    }

def main():
    """
    Main function to run the program with command-line arguments.
    """
    
    # Step 5.1: Set up command-line argument parser
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
    
    print("="*60)
    print("DICE PROBABILITY CALCULATOR")
    print("="*60)
    print(f"Configuration:")
    print(f"  Number of dice: {args.dice}")
    print(f"  Target sum: {args.target}")
    print(f"  Simulation trials: {args.trials}")
    print("="*60)
    
    # Step 5.2: Run exact calculation
    exact_result = calculate_exact_probability(args.dice, args.target)
    
    # Step 5.3: Run simulation
    sim_result = run_simulation(args.trials, args.dice, args.target)
    
    # Step 5.4: Compare results
    print(f"\n=== Comparison ===")
    difference = abs(exact_result['probability'] - sim_result['probability'])
    print(f"Exact probability:     {exact_result['percentage']:.6f}%")
    print(f"Simulated probability: {sim_result['percentage']:.6f}%")
    print(f"Difference:            {difference:.10f} ({difference * 100:.6f}%)")
    
    # We'll add Excel export in the next step
    

if __name__ == "__main__":
    main()