#!/usr/bin/env python3
"""
Test script to verify the improved visualizations work correctly
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_visualizations():
    """Test the visualization functions with sample data"""
    try:
        from utils.analysis import AlgorithmAnalyzer
        
        # Create analyzer instance
        analyzer = AlgorithmAnalyzer()
        
        # Create sample results for testing
        analyzer.results = {
            'Test Case 1': {
                'BFS': {
                    'path_found': True,
                    'steps': 24,
                    'time_taken': 0.001,
                    'peak_memory': 20480
                },
                'DFS': {
                    'path_found': True,
                    'steps': 66,
                    'time_taken': 0.0002,
                    'peak_memory': 11264
                },
                'A*': {
                    'path_found': True,
                    'steps': 24,
                    'time_taken': 0.003,
                    'peak_memory': 16384
                },
                'Greedy': {
                    'path_found': True,
                    'steps': 28,
                    'time_taken': 0.002,
                    'peak_memory': 12288
                },
                'Simulated Annealing': {
                    'path_found': False,
                    'steps': 0,
                    'time_taken': 0.001,
                    'peak_memory': 5120
                }
            },
            'Test Case 2': {
                'BFS': {
                    'path_found': True,
                    'steps': 22,
                    'time_taken': 0.001,
                    'peak_memory': 20480
                },
                'DFS': {
                    'path_found': True,
                    'steps': 65,
                    'time_taken': 0.0002,
                    'peak_memory': 11264
                },
                'A*': {
                    'path_found': True,
                    'steps': 22,
                    'time_taken': 0.003,
                    'peak_memory': 16384
                },
                'Greedy': {
                    'path_found': True,
                    'steps': 26,
                    'time_taken': 0.002,
                    'peak_memory': 12288
                },
                'Simulated Annealing': {
                    'path_found': False,
                    'steps': 0,
                    'time_taken': 0.001,
                    'peak_memory': 5120
                }
            }
        }
        
        print("Testing visualization functions...")
        
        # Test metrics calculation
        metrics = analyzer.calculate_metrics()
        print("✓ Metrics calculation completed")
        
        # Test comparison charts
        print("Generating comparison charts...")
        analyzer.create_performance_comparison_charts("test_visualization")
        print("✓ Comparison charts generated successfully")
        
        print("\nVisualization test completed successfully!")
        print("Check the generated files:")
        print("- test_visualization_comparison.png")
        print("- test_visualization_test_cases.png")
        
        return True
        
    except Exception as e:
        print(f"✗ Visualization test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run the visualization test"""
    print("Testing Improved Visualizations")
    print("=" * 40)
    
    if test_visualizations():
        print("\n✓ All visualization tests passed!")
        print("The improved charts should now have:")
        print("- Better text spacing and no overlap")
        print("- Rotated x-axis labels for better readability")
        print("- Larger figure sizes for more space")
        print("- Proper legend positioning")
        print("- Consistent font sizes")
    else:
        print("\n✗ Visualization tests failed!")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
