#!/usr/bin/env python3
"""
Test script to verify the analysis module works correctly
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that all required modules can be imported"""
    try:
        from utils.analysis import AlgorithmAnalyzer
        print("✓ Analysis module imported successfully")
        
        from algorithms.bfs import bfs
        from algorithms.dfs import dfs
        from algorithms.astar import astar
        from algorithms.greedy import greedy
        from algorithms.annealing import simulated_annealing
        print("✓ All algorithms imported successfully")
        
        from maze.maze_map import MAZE
        from maze.test_cases import TEST_CASES
        print("✓ Maze and test cases imported successfully")
        
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_single_algorithm():
    """Test running a single algorithm"""
    try:
        from utils.analysis import AlgorithmAnalyzer
        from maze.maze_map import MAZE
        from maze.test_cases import TEST_CASES
        
        analyzer = AlgorithmAnalyzer()
        start, goal = TEST_CASES[0]  # Use first test case
        
        # Test BFS
        result = analyzer.run_single_algorithm('BFS', analyzer.algorithms['BFS'], start, goal)
        
        print(f"✓ BFS test completed:")
        print(f"  - Path found: {result['path_found']}")
        print(f"  - Steps: {result['steps']}")
        print(f"  - Time: {result['time_taken']*1000:.2f} ms")
        print(f"  - Memory: {result['peak_memory']/1024:.1f} KB")
        
        return True
    except Exception as e:
        print(f"✗ Single algorithm test failed: {e}")
        return False

def test_metrics_calculation():
    """Test metrics calculation with sample data"""
    try:
        from utils.analysis import AlgorithmAnalyzer
        
        analyzer = AlgorithmAnalyzer()
        
        # Create sample results
        analyzer.results = {
            'Test Case 1': {
                'BFS': {
                    'path_found': True,
                    'steps': 10,
                    'time_taken': 0.001,
                    'peak_memory': 1024
                },
                'DFS': {
                    'path_found': True,
                    'steps': 15,
                    'time_taken': 0.002,
                    'peak_memory': 512
                }
            }
        }
        
        metrics = analyzer.calculate_metrics()
        
        print("✓ Metrics calculation test completed:")
        print(f"  - BFS completeness: {metrics['completeness']['BFS']['mean']*100:.1f}%")
        print(f"  - BFS avg steps: {metrics['cost_optimality']['BFS']['mean']:.1f}")
        print(f"  - DFS avg steps: {metrics['cost_optimality']['DFS']['mean']:.1f}")
        
        return True
    except Exception as e:
        print(f"✗ Metrics calculation test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing Maze-Solving Algorithms Analysis Module")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Single Algorithm Test", test_single_algorithm),
        ("Metrics Calculation Test", test_metrics_calculation)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nRunning {test_name}...")
        if test_func():
            passed += 1
            print(f"✓ {test_name} PASSED")
        else:
            print(f"✗ {test_name} FAILED")
    
    print(f"\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All tests passed! The analysis module is ready to use.")
        print("\nYou can now run the full analysis using:")
        print("  python src/run_analysis.py")
        print("  or")
        print("  python src/main.py (and select option 6)")
    else:
        print("✗ Some tests failed. Please check the error messages above.")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
