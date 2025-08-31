# maze-solver-ai/src/main.py

import time
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar
from algorithms.greedy import greedy
from algorithms.annealing import simulated_annealing
from maze.maze_map import MAZE
from maze.test_cases import TEST_CASES
from utils.display import display_maze
from utils.analysis import analyze_results

def main_menu():
    print("Maze Solver AI")
    print("Select a search algorithm:")
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    print("3. A* Search")
    print("4. Greedy Best-First Search")
    print("5. Simulated Annealing")
    print("6. Run Comprehensive Analysis")
    print("0. Exit")

def algorithm_menu(algorithm_name):
    print(f"\nRunning {algorithm_name}. Select a test case:")
    for i, (start, goal) in enumerate(TEST_CASES):
        print(f"{i + 1}. Start: {start}, Goal: {goal}")
    print("0. Back to Main Menu")

def get_memory_stats():
    """Get detailed memory statistics using tracemalloc"""
    import tracemalloc
    
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    
    print("\nTop 3 memory allocations:")
    for stat in top_stats[:3]:
        print(f"  {stat.count} blocks: {stat.size / 1024:.1f} KiB")
        print(f"    {stat.traceback.format()}")
    
    return snapshot

def run_algorithm(algorithm, start, goal):
    import tracemalloc
    import gc
    
    # Force garbage collection before measurement
    gc.collect()
    
    # Start memory tracking
    tracemalloc.start()
    
    start_time = time.time()
    result = algorithm(MAZE, start, goal)
    end_time = time.time()
    time_taken = end_time - start_time
    
    # Get memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Calculate memory usage based on algorithm-specific data structures
    if algorithm.__name__ == "greedy":
        path = result
        steps = len(path) - 1 if path else 0
    elif isinstance(result, tuple):
        # BFS returns: path, steps
        if len(result) == 2 and algorithm.__name__ == "bfs":
            path, steps = result
        # DFS returns: path, path_found, visited_count
        elif len(result) == 3 and algorithm.__name__ == "dfs":
            path, path_found, visited_count = result
            steps = len(path) - 1 if path else 0
        # Annealing returns: best_path, path_length
        elif len(result) == 2 and algorithm.__name__ == "simulated_annealing":
            path, steps = result
        # A* returns only path
        elif len(result) == 1:
            path = result[0]
            steps = len(path) - 1 if path else 0
        else:
            path, steps = result
    else:
        path = result
        steps = len(path) - 1 if path else 0

    return path, steps, time_taken, current, peak

def main():
    import os
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        main_menu()
        choice = input("Enter your choice: ")
        
        if choice == '0':
            break
        
        algorithm_map = {
            '1': (bfs, "Breadth-First Search"),
            '2': (dfs, "Depth-First Search"),
            '3': (astar, "A* Search"),
            '4': (greedy, "Greedy Best-First Search"),
            '5': (simulated_annealing, "Simulated Annealing"),
        }
        
        if choice == '6':
            # Run comprehensive analysis
            print("\nRunning comprehensive analysis...")
            try:
                from utils.analysis import analyze_results
                analyzer, results, metrics = analyze_results()
                print("\nAnalysis complete! Check the generated files:")
                print("- performance_analysis_comparison.png")
                print("- performance_analysis_test_cases.png")
                print("- algorithm_analysis_report.txt")
                input("\nPress Enter to continue...")
            except Exception as e:
                print(f"Error running analysis: {e}")
                print("Please ensure all dependencies are installed:")
                print("pip install numpy pandas matplotlib seaborn")
                input("\nPress Enter to continue...")
        elif choice in algorithm_map:
            algorithm, name = algorithm_map[choice]
            while True:
                algorithm_menu(name)
                test_case_choice = input("Enter your choice: ")
                
                if test_case_choice == '0':
                    break
                
                if test_case_choice.isdigit() and 1 <= int(test_case_choice) <= len(TEST_CASES):
                    start, goal = TEST_CASES[int(test_case_choice) - 1]
                    path, steps, time_taken, current_memory, peak_memory = run_algorithm(algorithm, start, goal)

                    if path:
                        print(f"\nPath Found: {path}")
                        print(f"Steps Taken: {steps}")
                        print(f"Time Taken: {time_taken:.4f} seconds")
                        print(f"Current Memory: {current_memory:,} bytes")
                        print(f"Peak Memory: {peak_memory:,} bytes")
                        display_maze(MAZE, path, start, goal)
                    else:
                        print("\nNo path found!")
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()