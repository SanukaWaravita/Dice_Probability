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

calculate_exact_probability()