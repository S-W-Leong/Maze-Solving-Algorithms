import time
import tracemalloc
import gc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Any
import seaborn as sns
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar
from algorithms.greedy import greedy
from algorithms.annealing import simulated_annealing
from maze.maze_map import MAZE
from maze.test_cases import TEST_CASES

class AlgorithmAnalyzer:
    def __init__(self):
        self.algorithms = {
            'BFS': bfs,
            'DFS': dfs,
            'A*': astar,
            'Greedy': greedy,
            'Simulated Annealing': simulated_annealing
        }
        self.results = {}
        
    def run_single_algorithm(self, algorithm_name: str, algorithm_func, start: Tuple[int, int], goal: Tuple[int, int]) -> Dict[str, Any]:
        """Run a single algorithm and collect performance metrics"""
        # Force garbage collection before measurement
        gc.collect()
        
        # Start memory tracking
        tracemalloc.start()
        
        # Time the algorithm execution
        start_time = time.time()
        result = algorithm_func(MAZE, start, goal)
        end_time = time.time()
        time_taken = end_time - start_time
        
        # Get memory usage
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Parse results based on algorithm return format
        path = None
        steps = 0
        visited_count = 0
        path_found = False
        
        if algorithm_name == 'BFS':
            if result and result[0]:
                path, steps = result
                path_found = True
        elif algorithm_name == 'DFS':
            if result and result[0]:
                path, path_found, visited_count = result
                steps = len(path) - 1 if path else 0
        elif algorithm_name == 'A*':
            if result:
                path = result
                steps = len(path) - 1 if path else 0
                path_found = True
        elif algorithm_name == 'Greedy':
            if result:
                path = result
                steps = len(path) - 1 if path else 0
                path_found = True
        elif algorithm_name == 'Simulated Annealing':
            if result and result[0]:
                path, steps = result
                path_found = True
        
        return {
            'algorithm': algorithm_name,
            'start': start,
            'goal': goal,
            'path_found': path_found,
            'path': path,
            'steps': steps,
            'time_taken': time_taken,
            'current_memory': current_memory,
            'peak_memory': peak_memory,
            'visited_count': visited_count
        }
    
    def run_all_algorithms_on_test_case(self, test_case_idx: int) -> Dict[str, Dict[str, Any]]:
        """Run all algorithms on a specific test case"""
        start, goal = TEST_CASES[test_case_idx]
        results = {}
        
        for algorithm_name, algorithm_func in self.algorithms.items():
            try:
                result = self.run_single_algorithm(algorithm_name, algorithm_func, start, goal)
                results[algorithm_name] = result
            except Exception as e:
                print(f"Error running {algorithm_name} on test case {test_case_idx + 1}: {e}")
                results[algorithm_name] = {
                    'algorithm': algorithm_name,
                    'start': start,
                    'goal': goal,
                    'path_found': False,
                    'path': None,
                    'steps': 0,
                    'time_taken': 0,
                    'current_memory': 0,
                    'peak_memory': 0,
                    'visited_count': 0,
                    'error': str(e)
                }
        
        return results
    
    def run_comprehensive_analysis(self) -> Dict[str, Any]:
        """Run all algorithms on all test cases"""
        all_results = {}
        
        for test_case_idx in range(len(TEST_CASES)):
            test_case_results = self.run_all_algorithms_on_test_case(test_case_idx)
            all_results[f'Test Case {test_case_idx + 1}'] = test_case_results
        
        self.results = all_results
        return all_results
    
    def calculate_metrics(self) -> Dict[str, Any]:
        """Calculate comprehensive metrics for all algorithms"""
        if not self.results:
            raise ValueError("No results available. Run comprehensive_analysis first.")
        
        metrics = {
            'completeness': {},
            'cost_optimality': {},
            'time_complexity': {},
            'space_complexity': {},
            'overall_performance': {}
        }
        
        # Initialize metrics for each algorithm
        for algorithm_name in self.algorithms.keys():
            metrics['completeness'][algorithm_name] = []
            metrics['cost_optimality'][algorithm_name] = []
            metrics['time_complexity'][algorithm_name] = []
            metrics['space_complexity'][algorithm_name] = []
        
        # Collect data from all test cases
        for test_case_name, test_case_results in self.results.items():
            for algorithm_name, result in test_case_results.items():
                # Completeness (path found?)
                metrics['completeness'][algorithm_name].append(1 if result['path_found'] else 0)
                
                # Cost optimality (steps taken)
                metrics['cost_optimality'][algorithm_name].append(result['steps'])
                
                # Time complexity (time taken)
                metrics['time_complexity'][algorithm_name].append(result['time_taken'])
                
                # Space complexity (memory usage)
                metrics['space_complexity'][algorithm_name].append(result['peak_memory'])
        
        # Calculate averages and statistics
        for metric_type in metrics:
            if metric_type != 'overall_performance':
                for algorithm_name in metrics[metric_type]:
                    values = metrics[metric_type][algorithm_name]
                    metrics[metric_type][algorithm_name] = {
                        'values': values,
                        'mean': np.mean(values),
                        'std': np.std(values),
                        'min': np.min(values),
                        'max': np.max(values)
                    }
        
        return metrics
    
    def create_performance_comparison_charts(self, save_path: str = "performance_analysis"):
        """Create comprehensive performance comparison charts"""
        if not self.results:
            raise ValueError("No results available. Run comprehensive_analysis first.")
        
        metrics = self.calculate_metrics()
        
        # Set up the plotting style
        try:
            plt.style.use('seaborn-v0_8')
        except:
            plt.style.use('seaborn')
        sns.set_palette("husl")
        
        # Create a figure with multiple subplots - increased figure size for better spacing
        fig, axes = plt.subplots(2, 2, figsize=(18, 14))
        fig.suptitle('Maze-Solving Algorithms Performance Analysis', fontsize=18, fontweight='bold', y=0.98)
        
        # 1. Completeness Comparison (Algorithm vs Success Rate)
        completeness_data = [metrics['completeness'][alg]['mean'] * 100 for alg in self.algorithms.keys()]
        bars1 = axes[0, 0].bar(self.algorithms.keys(), completeness_data, color='skyblue', alpha=0.7)
        axes[0, 0].set_title('Completeness: Path Finding Success Rate', fontweight='bold', fontsize=14, pad=20)
        axes[0, 0].set_ylabel('Success Rate (%)', fontsize=12)
        axes[0, 0].set_ylim(0, 110)  # Increased y-limit to accommodate text
        axes[0, 0].tick_params(axis='x', rotation=45, labelsize=11)  # Rotate x-axis labels
        axes[0, 0].tick_params(axis='y', labelsize=11)
        
        # Add value labels on bars with better positioning
        for i, (bar, v) in enumerate(zip(bars1, completeness_data)):
            height = bar.get_height()
            axes[0, 0].text(bar.get_x() + bar.get_width()/2., height + 2,
                           f'{v:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        # 2. Cost Optimality Comparison (Algorithm vs Average Steps)
        cost_data = [metrics['cost_optimality'][alg]['mean'] for alg in self.algorithms.keys()]
        bars2 = axes[0, 1].bar(self.algorithms.keys(), cost_data, color='lightcoral', alpha=0.7)
        axes[0, 1].set_title('Cost Optimality: Average Steps Taken', fontweight='bold', fontsize=14, pad=20)
        axes[0, 1].set_ylabel('Average Steps', fontsize=12)
        axes[0, 1].tick_params(axis='x', rotation=45, labelsize=11)
        axes[0, 1].tick_params(axis='y', labelsize=11)
        
        # Add value labels on bars
        for i, (bar, v) in enumerate(zip(bars2, cost_data)):
            height = bar.get_height()
            axes[0, 1].text(bar.get_x() + bar.get_width()/2., height + 1,
                           f'{v:.1f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        # 3. Time Complexity Comparison (Algorithm vs Average Time)
        time_data = [metrics['time_complexity'][alg]['mean'] * 1000 for alg in self.algorithms.keys()]  # Convert to ms
        bars3 = axes[1, 0].bar(self.algorithms.keys(), time_data, color='lightgreen', alpha=0.7)
        axes[1, 0].set_title('Time Complexity: Average Execution Time', fontweight='bold', fontsize=14, pad=20)
        axes[1, 0].set_ylabel('Time (milliseconds)', fontsize=12)
        axes[1, 0].tick_params(axis='x', rotation=45, labelsize=11)
        axes[1, 0].tick_params(axis='y', labelsize=11)
        
        # Add value labels on bars
        for i, (bar, v) in enumerate(zip(bars3, time_data)):
            height = bar.get_height()
            axes[1, 0].text(bar.get_x() + bar.get_width()/2., height + 0.05,
                           f'{v:.2f}ms', ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        # 4. Space Complexity Comparison (Algorithm vs Average Memory)
        memory_data = [metrics['space_complexity'][alg]['mean'] / 1024 for alg in self.algorithms.keys()]  # Convert to KB
        bars4 = axes[1, 1].bar(self.algorithms.keys(), memory_data, color='gold', alpha=0.7)
        axes[1, 1].set_title('Space Complexity: Average Memory Usage', fontweight='bold', fontsize=14, pad=20)
        axes[1, 1].set_ylabel('Memory (KB)', fontsize=12)
        axes[1, 1].tick_params(axis='x', rotation=45, labelsize=11)
        axes[1, 1].tick_params(axis='y', labelsize=11)
        
        # Add value labels on bars
        for i, (bar, v) in enumerate(zip(bars4, memory_data)):
            height = bar.get_height()
            axes[1, 1].text(bar.get_x() + bar.get_width()/2., height + 0.2,
                           f'{v:.1f}KB', ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        # Adjust layout with more padding
        plt.tight_layout(pad=3.0)
        plt.savefig(f'{save_path}_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Create performance across test cases chart
        self.create_test_case_performance_chart(save_path)
        
        return metrics
    
    def create_test_case_performance_chart(self, save_path: str):
        """Create chart showing performance of each algorithm across all test cases"""
        if not self.results:
            raise ValueError("No results available. Run comprehensive_analysis first.")
        
        # Prepare data for plotting
        test_cases = list(self.results.keys())
        algorithms = list(self.algorithms.keys())
        
        # Set up the plotting style
        try:
            plt.style.use('seaborn-v0_8')
        except:
            plt.style.use('seaborn')
        sns.set_palette("husl")
        
        # Create subplots for different metrics - increased figure size
        fig, axes = plt.subplots(2, 2, figsize=(20, 15))
        fig.suptitle('Algorithm Performance Across Test Cases', fontsize=18, fontweight='bold', y=0.98)
        
        # 1. Steps taken across test cases
        for alg in algorithms:
            steps_data = []
            for test_case in test_cases:
                steps_data.append(self.results[test_case][alg]['steps'])
            axes[0, 0].plot(range(1, len(test_cases) + 1), steps_data, marker='o', label=alg, linewidth=2, markersize=6)
        
        axes[0, 0].set_title('Steps Taken Across Test Cases', fontweight='bold', fontsize=14, pad=20)
        axes[0, 0].set_xlabel('Test Case', fontsize=12)
        axes[0, 0].set_ylabel('Steps', fontsize=12)
        axes[0, 0].legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=11)
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].tick_params(labelsize=11)
        
        # 2. Time taken across test cases
        for alg in algorithms:
            time_data = []
            for test_case in test_cases:
                time_data.append(self.results[test_case][alg]['time_taken'] * 1000)  # Convert to ms
            axes[0, 1].plot(range(1, len(test_cases) + 1), time_data, marker='s', label=alg, linewidth=2, markersize=6)
        
        axes[0, 1].set_title('Execution Time Across Test Cases', fontweight='bold', fontsize=14, pad=20)
        axes[0, 1].set_xlabel('Test Case', fontsize=12)
        axes[0, 1].set_ylabel('Time (milliseconds)', fontsize=12)
        axes[0, 1].legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=11)
        axes[0, 1].grid(True, alpha=0.3)
        axes[0, 1].tick_params(labelsize=11)
        
        # 3. Memory usage across test cases
        for alg in algorithms:
            memory_data = []
            for test_case in test_cases:
                memory_data.append(self.results[test_case][alg]['peak_memory'] / 1024)  # Convert to KB
            axes[1, 0].plot(range(1, len(test_cases) + 1), memory_data, marker='^', label=alg, linewidth=2, markersize=6)
        
        axes[1, 0].set_title('Memory Usage Across Test Cases', fontweight='bold', fontsize=14, pad=20)
        axes[1, 0].set_xlabel('Test Case', fontsize=12)
        axes[1, 0].set_ylabel('Memory (KB)', fontsize=12)
        axes[1, 0].legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=11)
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].tick_params(labelsize=11)
        
        # 4. Success rate heatmap
        success_matrix = []
        for alg in algorithms:
            row = []
            for test_case in test_cases:
                row.append(1 if self.results[test_case][alg]['path_found'] else 0)
            success_matrix.append(row)
        
        im = axes[1, 1].imshow(success_matrix, cmap='RdYlGn', aspect='auto')
        axes[1, 1].set_title('Path Finding Success Heatmap', fontweight='bold', fontsize=14, pad=20)
        axes[1, 1].set_xlabel('Test Case', fontsize=12)
        axes[1, 1].set_ylabel('Algorithm', fontsize=12)
        axes[1, 1].set_xticks(range(len(test_cases)))
        axes[1, 1].set_xticklabels([f'TC{i+1}' for i in range(len(test_cases))], fontsize=11)
        axes[1, 1].set_yticks(range(len(algorithms)))
        axes[1, 1].set_yticklabels(algorithms, fontsize=11)
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=axes[1, 1])
        cbar.set_label('Success (1) / Failure (0)', fontsize=12)
        cbar.ax.tick_params(labelsize=11)
        
        # Adjust layout with more padding and space for legends
        plt.tight_layout(pad=3.0)
        plt.savefig(f'{save_path}_test_cases.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def generate_detailed_report(self, save_path: str = "algorithm_analysis_report.txt"):
        """Generate a detailed text report of the analysis"""
        if not self.results:
            raise ValueError("No results available. Run comprehensive_analysis first.")
        
        metrics = self.calculate_metrics()
        
        with open(save_path, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write("MAZE-SOLVING ALGORITHMS COMPREHENSIVE ANALYSIS REPORT\n")
            f.write("=" * 80 + "\n\n")
            
            f.write("EVALUATION METRICS SUMMARY:\n")
            f.write("-" * 40 + "\n\n")
            
            # Completeness Analysis
            f.write("1. COMPLETENESS ANALYSIS (Path Finding Success Rate):\n")
            f.write("-" * 50 + "\n")
            for alg in self.algorithms.keys():
                success_rate = metrics['completeness'][alg]['mean'] * 100
                f.write(f"{alg:20}: {success_rate:6.1f}% success rate\n")
            f.write("\n")
            
            # Cost Optimality Analysis
            f.write("2. COST OPTIMALITY ANALYSIS (Average Steps Taken):\n")
            f.write("-" * 50 + "\n")
            for alg in self.algorithms.keys():
                avg_steps = metrics['cost_optimality'][alg]['mean']
                std_steps = metrics['cost_optimality'][alg]['std']
                f.write(f"{alg:20}: {avg_steps:6.1f} ± {std_steps:.1f} steps\n")
            f.write("\n")
            
            # Time Complexity Analysis
            f.write("3. TIME COMPLEXITY ANALYSIS (Average Execution Time):\n")
            f.write("-" * 50 + "\n")
            for alg in self.algorithms.keys():
                avg_time = metrics['time_complexity'][alg]['mean'] * 1000  # Convert to ms
                std_time = metrics['time_complexity'][alg]['std'] * 1000
                f.write(f"{alg:20}: {avg_time:6.2f} ± {std_time:.2f} ms\n")
            f.write("\n")
            
            # Space Complexity Analysis
            f.write("4. SPACE COMPLEXITY ANALYSIS (Average Memory Usage):\n")
            f.write("-" * 50 + "\n")
            for alg in self.algorithms.keys():
                avg_memory = metrics['space_complexity'][alg]['mean'] / 1024  # Convert to KB
                std_memory = metrics['space_complexity'][alg]['std'] / 1024
                f.write(f"{alg:20}: {avg_memory:6.1f} ± {std_memory:.1f} KB\n")
            f.write("\n")
            
            # Detailed Results for Each Test Case
            f.write("DETAILED RESULTS BY TEST CASE:\n")
            f.write("=" * 50 + "\n\n")
            
            for test_case_name, test_case_results in self.results.items():
                f.write(f"{test_case_name}:\n")
                f.write("-" * 30 + "\n")
                for alg_name, result in test_case_results.items():
                    f.write(f"  {alg_name:18}: ")
                    if result['path_found']:
                        f.write(f"✓ Path found ({result['steps']} steps, ")
                        f.write(f"{result['time_taken']*1000:.2f}ms, ")
                        f.write(f"{result['peak_memory']/1024:.1f}KB)\n")
                    else:
                        f.write("✗ No path found\n")
                f.write("\n")
        
        print(f"Detailed report saved to: {save_path}")

def analyze_results():
    """Main function to run the complete analysis"""
    print("Starting comprehensive algorithm analysis...")
    print("This may take a few moments as we test all algorithms on all test cases...")
    
    analyzer = AlgorithmAnalyzer()
    
    # Run comprehensive analysis
    results = analyzer.run_comprehensive_analysis()
    
    # Generate charts and metrics
    metrics = analyzer.create_performance_comparison_charts()
    
    # Generate detailed report
    analyzer.generate_detailed_report()
    
    print("\nAnalysis complete! Generated files:")
    print("- performance_analysis_comparison.png")
    print("- performance_analysis_test_cases.png")
    print("- algorithm_analysis_report.txt")
    
    return analyzer, results, metrics
