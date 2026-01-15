import random
import argparse
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

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

def create_convergence_plot(cumulative_probs, exact_prob, num_dice, target_sum, filename='convergence_plot.png'):
    """
    Create a plot showing probability convergence over trials.
    """
    plt.figure(figsize=(10, 6))
    trials = list(range(1, len(cumulative_probs) + 1))
    
    plt.plot(trials, cumulative_probs, 'b-', linewidth=1, alpha=0.7, label='Simulated Probability')
    plt.axhline(y=exact_prob, color='r', linestyle='--', linewidth=2, label=f'Exact Probability ({exact_prob:.6f})')
    
    plt.xlabel('Number of Trials (N)', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.title(f'Probability Convergence: {num_dice} Dice Sum to {target_sum}', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    
    return filename

def export_to_excel(num_dice, target_sum, ways, total_outcomes, exact_prob, 
                   successes, num_trials, sim_prob, trial_logs, cumulative_probs, filename=None):
    """
    Export all data to Excel workbook with multiple sheets.
    """
    if filename is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'dice_probability_results_{timestamp}.xlsx'
    
    # Create a Pandas Excel writer
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        
        # Sheet 1: Summary & Computations
        summary_data = {
            'Parameter': [
                'Number of Dice',
                'Target Sum',
                'Number of Trials',
                '',
                'EXACT CALCULATION',
                'Ways to achieve target',
                'Total possible outcomes',
                'Exact Probability',
                'Exact Probability (%)',
                '',
                'SIMULATION RESULTS',
                'Successful trials',
                'Total trials',
                'Simulated Probability',
                'Simulated Probability (%)',
                '',
                'COMPARISON',
                'Absolute Difference',
                'Difference (%)'
            ],
            'Value': [
                num_dice,
                target_sum,
                num_trials,
                '',
                '',
                ways,
                total_outcomes,
                exact_prob,
                exact_prob * 100,
                '',
                '',
                successes,
                num_trials,
                sim_prob,
                sim_prob * 100,
                '',
                '',
                abs(exact_prob - sim_prob),
                abs(exact_prob - sim_prob) * 100
            ]
        }
        df_summary = pd.DataFrame(summary_data)
        df_summary.to_excel(writer, sheet_name='Summary', index=False)
        
        # Sheet 2: Trial Logs
        df_logs = pd.DataFrame(trial_logs)
        df_logs.to_excel(writer, sheet_name='Trial Logs', index=False)
        
        # Sheet 3: Convergence Data
        convergence_data = {
            'Trial_Number': list(range(1, len(cumulative_probs) + 1)),
            'Cumulative_Probability': cumulative_probs,
            'Exact_Probability': [exact_prob] * len(cumulative_probs),
            'Difference': [abs(p - exact_prob) for p in cumulative_probs]
        }
        df_convergence = pd.DataFrame(convergence_data)
        df_convergence.to_excel(writer, sheet_name='Convergence Data', index=False)
    
    # Now add the plot to the Summary sheet
    plot_filename = 'temp_convergence_plot.png'
    create_convergence_plot(cumulative_probs, exact_prob, num_dice, target_sum, plot_filename)
    
    # Load the workbook and add image
    wb = load_workbook(filename)
    ws = wb['Summary']
    
    # Add the plot image to the right side of the summary
    img = Image(plot_filename)
    img.width = 600
    img.height = 400
    ws.add_image(img, 'E2')
    
    wb.save(filename)
    
    # Clean up temp plot file
    import os
    if os.path.exists(plot_filename):
        os.remove(plot_filename)
    
    return filename

def simulate_dice_throws(num_dice, target_sum, num_trials):
    """
    Simulate throwing num_dice dice for num_trials trials.
    Count how many times the sum equals target_sum.
    Returns detailed trial data for Excel export.
    """
    success_count = 0
    trial_logs = []
    cumulative_probs = []
    
    for trial in range(num_trials):
        # Throw the dice
        dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]
        dice_sum = sum(dice_rolls)
        
        # Check if we hit the target
        is_success = (dice_sum == target_sum)
        if is_success:
            success_count += 1
        
        # Calculate cumulative probability so far
        cumulative_prob = success_count / (trial + 1)
        
        # Store trial log
        trial_logs.append({
            'Trial': trial + 1,
            'Dice_Rolls': str(dice_rolls),
            'Sum': dice_sum,
            'Success': 'Yes' if is_success else 'No',
            'Cumulative_Successes': success_count,
            'Cumulative_Probability': cumulative_prob
        })
        
        # Store for convergence plot
        cumulative_probs.append(cumulative_prob)
    
    estimated_probability = success_count / num_trials
    
    return success_count, num_trials, estimated_probability, trial_logs, cumulative_probs

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
    successes, trials, sim_prob, trial_logs, cumulative_probs = simulate_dice_throws(num_dice, target_sum, num_trials)
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
    
    # Export to Excel
    print()
    print("Exporting results to Excel...")
    excel_filename = export_to_excel(
        num_dice, target_sum, ways, total_outcomes, exact_prob,
        successes, num_trials, sim_prob, trial_logs, cumulative_probs
    )
    print(f"✓ Excel file created: {excel_filename}")
    print(f"  - Summary sheet with computations and convergence plot")
    print(f"  - Trial Logs sheet with all {num_trials} trials")
    print(f"  - Convergence Data sheet with probability progression")
    print("=" * 60)

if __name__ == "__main__":
    main()
