#!/usr/bin/env python3
"""
Simple performance test script for maze-solving algorithms
"""

import time
import tracemalloc
import gc
from src.algorithms.bfs import bfs
from src.algorithms.dfs import dfs
from src.algorithms.astar import astar
from src.algorithms.greedy import greedy
from src.algorithms.annealing import simulated_annealing
from src.maze.maze_map import MAZE
from src.maze.test_cases import TEST_CASES

def test_algorithm(algorithm, algorithm_name, start, goal):
    """Test a single algorithm and return performance metrics"""
    gc.collect()
    tracemalloc.start()
    
    start_time = time.time()
    result = algorithm(MAZE, start, goal)
    end_time = time.time()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    time_taken = end_time - start_time
    
    # Extract path and steps based on algorithm return format
    if algorithm_name == "BFS":
        path, steps = result if result[0] else (None, 0)
    elif algorithm_name == "DFS":
        path, path_found, visited_count = result
        steps = len(path) - 1 if path else 0
    elif algorithm_name == "A*":
        path = result
        steps = len(path) - 1 if path else 0
    elif algorithm_name == "Greedy":
        path = result
        steps = len(path) - 1 if path else 0
    elif algorithm_name == "Simulated Annealing":
        path, steps = result
    
    success = path is not None and len(path) > 0
    
    return {
        'success': success,
        'steps': steps,
        'time': time_taken,
        'memory': current,
        'path_length': len(path) if path else 0
    }

def main():
    """Run performance tests on selected test cases"""
    algorithms = [
        (bfs, "BFS"),
        (dfs, "DFS"), 
        (astar, "A*"),
        (greedy, "Greedy"),
        (simulated_annealing, "Simulated Annealing")
    ]
    
    # Select 5 test cases
    selected_cases = [0, 2, 4, 6, 8]  # Test cases 1, 3, 5, 7, 9
    
    print("Performance Test Results")
    print("=" * 80)
    
    results = {}
    
    for alg_func, alg_name in algorithms:
        print(f"\n{alg_name}:")
        print("-" * 40)
        results[alg_name] = []
        
        for case_idx in selected_cases:
            start, goal = TEST_CASES[case_idx]
            result = test_algorithm(alg_func, alg_name, start, goal)
            results[alg_name].append(result)
            
            print(f"  Test Case {case_idx + 1} ({start} -> {goal}):")
            print(f"    Success: {result['success']}")
            print(f"    Steps: {result['steps']}")
            print(f"    Time: {result['time']:.6f}s")
            print(f"    Memory: {result['memory']} bytes")
            print(f"    Path Length: {result['path_length']}")
    
    # Print summary table
    print("\n" + "=" * 80)
    print("SUMMARY TABLE")
    print("=" * 80)
    
    print(f"{'Algorithm':<20} {'Test Case':<10} {'Success':<8} {'Steps':<8} {'Time (ms)':<10} {'Memory (KB)':<12}")
    print("-" * 80)
    
    for alg_name in [alg[1] for alg in algorithms]:
        for i, case_idx in enumerate(selected_cases):
            result = results[alg_name][i]
            start, goal = TEST_CASES[case_idx]
            print(f"{alg_name:<20} {f'{start}->{goal}':<10} {str(result['success']):<8} {result['steps']:<8} {result['time']*1000:<10.2f} {result['memory']/1024:<12.1f}")

if __name__ == "__main__":
    main()
