def analyze_results(results):
    """
    Analyzes the results of the maze solving algorithms and prints a formatted table.

    Parameters:
        results (list): A list of dictionaries containing the results of each test case.
                        Each dictionary should have the keys: 'path_found', 'steps_taken',
                        'time_taken', and 'memory_usage'.
    """
    print(f"{'Test Case':<10} {'Path Found':<12} {'Steps Taken':<12} {'Time Taken (s)':<15} {'Memory Usage (MB)':<15}")
    print("=" * 70)

    for index, result in enumerate(results):
        path_found = result['path_found']
        steps_taken = result['steps_taken']
        time_taken = result['time_taken']
        memory_usage = result['memory_usage']
        
        print(f"{index + 1:<10} {path_found:<12} {steps_taken:<12} {time_taken:<15.4f} {memory_usage:<15.4f}")