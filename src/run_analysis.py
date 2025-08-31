#!/usr/bin/env python3
"""
Maze-Solving Algorithms Comprehensive Analysis Script

This script runs a comprehensive analysis of all maze-solving algorithms
with the following evaluation metrics:
1. Completeness (path found?)
2. Cost-optimality (steps taken)
3. Time complexity (time taken)
4. Space complexity (memory usage)

It generates:
1. Performance comparison charts (Algorithm vs Performance)
2. Performance across test cases charts (Test Case vs Performance)
3. Detailed analysis report
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.analysis import analyze_results

def main():
    """Main function to run the comprehensive analysis"""
    print("=" * 80)
    print("MAZE-SOLVING ALGORITHMS COMPREHENSIVE ANALYSIS")
    print("=" * 80)
    print()
    print("This analysis will evaluate the following algorithms:")
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    print("3. A* Search")
    print("4. Greedy Best-First Search")
    print("5. Simulated Annealing")
    print()
    print("Evaluation Metrics:")
    print("- Completeness: Path finding success rate")
    print("- Cost Optimality: Average steps taken")
    print("- Time Complexity: Average execution time")
    print("- Space Complexity: Average memory usage")
    print()
    print("Test Cases: 10 different start-goal pairs")
    print()
    
    try:
        # Run the comprehensive analysis
        analyzer, results, metrics = analyze_results()
        
        print("\n" + "=" * 80)
        print("ANALYSIS COMPLETE!")
        print("=" * 80)
        print()
        print("Generated Files:")
        print("1. performance_analysis_comparison.png - Algorithm performance comparison")
        print("2. performance_analysis_test_cases.png - Performance across test cases")
        print("3. algorithm_analysis_report.txt - Detailed text report")
        print()
        print("Key Findings Summary:")
        print("-" * 40)
        
        # Print summary of key findings
        best_completeness = max(metrics['completeness'].keys(), 
                              key=lambda x: metrics['completeness'][x]['mean'])
        best_cost = min(metrics['cost_optimality'].keys(), 
                       key=lambda x: metrics['cost_optimality'][x]['mean'])
        best_time = min(metrics['time_complexity'].keys(), 
                       key=lambda x: metrics['time_complexity'][x]['mean'])
        best_memory = min(metrics['space_complexity'].keys(), 
                         key=lambda x: metrics['space_complexity'][x]['mean'])
        
        print(f"• Most Complete: {best_completeness} ({metrics['completeness'][best_completeness]['mean']*100:.1f}% success rate)")
        print(f"• Most Cost-Optimal: {best_cost} ({metrics['cost_optimality'][best_cost]['mean']:.1f} avg steps)")
        print(f"• Fastest: {best_time} ({metrics['time_complexity'][best_time]['mean']*1000:.2f} ms avg)")
        print(f"• Most Memory-Efficient: {best_memory} ({metrics['space_complexity'][best_memory]['mean']/1024:.1f} KB avg)")
        
        print()
        print("Check the generated files for detailed analysis and visualizations!")
        
    except Exception as e:
        print(f"Error during analysis: {e}")
        print("Please ensure all dependencies are installed:")
        print("pip install numpy pandas matplotlib seaborn")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
