# Maze-Solving Algorithms Analysis

This project now includes comprehensive analysis capabilities for evaluating maze-solving algorithms with multiple performance metrics and visualizations.

## Analysis Features

### Evaluation Metrics

The analysis evaluates each algorithm using four key metrics:

1. **Completeness** - Whether the algorithm successfully finds a path (success rate)
2. **Cost Optimality** - Number of steps taken to reach the goal
3. **Time Complexity** - Execution time in milliseconds
4. **Space Complexity** - Memory usage in kilobytes

### Generated Visualizations

The analysis generates two main visualization files:

1. **`performance_analysis_comparison.png`** - Algorithm performance comparison
   - Bar charts showing each algorithm's performance across all metrics
   - X-axis: Algorithms (BFS, DFS, A*, Greedy, Simulated Annealing)
   - Y-axis: Performance metrics (success rate, steps, time, memory)

2. **`performance_analysis_test_cases.png`** - Performance across test cases
   - Line plots showing how each algorithm performs across the 10 test cases
   - X-axis: Test cases (1-10)
   - Y-axis: Performance metrics
   - Includes a success rate heatmap

### Detailed Report

The analysis also generates `algorithm_analysis_report.txt` containing:
- Comprehensive metrics summary
- Statistical analysis (mean, standard deviation, min, max)
- Detailed results for each test case
- Performance rankings

## How to Run the Analysis

### Option 1: Using the Main Menu
1. Run the main program: `python src/main.py`
2. Select option `6. Run Comprehensive Analysis`
3. Wait for the analysis to complete
4. Check the generated files in the project directory

### Option 2: Using the Dedicated Analysis Script
1. Run the analysis script directly: `python src/run_analysis.py`
2. This will run the complete analysis and display a summary

### Option 3: Using Python Interactive Mode
```python
from src.utils.analysis import analyze_results

# Run the complete analysis
analyzer, results, metrics = analyze_results()

# Access specific metrics
print(f"BFS success rate: {metrics['completeness']['BFS']['mean']*100:.1f}%")
print(f"A* average steps: {metrics['cost_optimality']['A*']['mean']:.1f}")
```

## Dependencies

Make sure you have the required packages installed:

```bash
pip install numpy pandas matplotlib seaborn
```

## Test Cases

The analysis uses 10 different test cases with varying start and goal positions:
- Test Case 1: (1,1) → (13,13) - Top-left to bottom-right
- Test Case 2: (1,2) → (13,12) - Top-left area to bottom-right area
- Test Case 3: (1,3) → (13,11) - Top-left area to bottom-right area
- ... and so on

## Algorithms Analyzed

1. **Breadth-First Search (BFS)**
   - Guaranteed to find shortest path
   - Complete and optimal
   - Higher memory usage

2. **Depth-First Search (DFS)**
   - May not find shortest path
   - Complete but not optimal
   - Lower memory usage

3. **A* Search**
   - Uses heuristic function
   - Complete and optimal (with admissible heuristic)
   - Generally efficient

4. **Greedy Best-First Search**
   - Uses heuristic function
   - Complete but not optimal
   - Fast but may take longer paths

5. **Simulated Annealing**
   - Metaheuristic approach
   - May not always find path
   - Good for complex optimization

## Understanding the Results

### Success Rate (Completeness)
- Higher percentage = more reliable path finding
- 100% means the algorithm found a path in all test cases

### Average Steps (Cost Optimality)
- Lower number = more efficient path
- BFS and A* typically have the lowest values

### Execution Time (Time Complexity)
- Lower time = faster algorithm
- Measured in milliseconds
- May vary based on system performance

### Memory Usage (Space Complexity)
- Lower memory = more memory efficient
- Measured in kilobytes
- BFS typically uses more memory due to queue structure

## Customization

You can modify the analysis by:

1. **Adding new algorithms**: Update the `algorithms` dictionary in `AlgorithmAnalyzer.__init__()`
2. **Adding new test cases**: Modify `TEST_CASES` in `src/maze/test_cases.py`
3. **Changing metrics**: Modify the `calculate_metrics()` method
4. **Customizing visualizations**: Modify the chart creation methods

## Example Output

After running the analysis, you'll see output like:

```
ANALYSIS COMPLETE!

Generated Files:
1. performance_analysis_comparison.png - Algorithm performance comparison
2. performance_analysis_test_cases.png - Performance across test cases
3. algorithm_analysis_report.txt - Detailed text report

Key Findings Summary:
• Most Complete: BFS (100.0% success rate)
• Most Cost-Optimal: A* (24.5 avg steps)
• Fastest: Greedy (0.15 ms avg)
• Most Memory-Efficient: DFS (12.3 KB avg)
```

This analysis provides comprehensive insights into the performance characteristics of different maze-solving algorithms, helping you understand their trade-offs and choose the most appropriate algorithm for your specific use case.
