# Utility function to display all test cases before solving
def display_all_test_cases(test_cases, maze):
    """
    Displays all test cases with the maze, marking 'S' (start) and 'G' (goal) for each case.
    test_cases: iterable of dicts or tuples with 'start' and 'goal' keys/values
    maze: the maze map (2D list)
    """
    for idx, case in enumerate(test_cases):
        # Support both dict and tuple formats
        if isinstance(case, dict):
            start = case.get('start')
            goal = case.get('goal')
        elif isinstance(case, tuple) and len(case) == 2:
            start, goal = case
        else:
            print(f"Test case {idx+1} format not recognized.")
            continue
        print(f"Test Case {idx+1}: Start={start}, Goal={goal}")
        display_maze(maze, path=None, start=start, goal=goal)
        print("-"*40)

def display_maze(maze, path=None, start=None, goal=None):
    """
    Displays the maze with the path marked and start/goal points highlighted.
    
    Parameters:
    maze (list of list of str): The maze represented as a 2D list.
    path (list of tuple, optional): The path found from start to goal, represented as a list of (row, col) tuples. If None, no path will be marked.
    start (tuple): The starting position as (row, col).
    goal (tuple): The goal position as (row, col).
    """
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    
    # Create a copy of the maze to mark the path
    maze_with_path = [row[:] for row in maze]
    
    # Mark the start point with "S"
    if start is not None:
        start_row, start_col = start
        maze_with_path[start_row][start_col] = 'S'
    
    # Mark the goal point with "G"
    if goal is not None:
        goal_row, goal_col = goal
        maze_with_path[goal_row][goal_col] = 'G'
    
    # Mark the path in the maze if path is a non-empty iterable
    if path:
        try:
            for (row, col) in path:
                # Don't overwrite start and goal markers
                if maze_with_path[row][col] not in ['S', 'G']:
                    maze_with_path[row][col] = '*'
        except TypeError:
            print("Invalid path format! Path should be a list of (row, col) tuples.")
    else:
        print("No path found!")
    
    # Print the maze with the path and colors
    for row in maze_with_path:
        for cell in row:
            if cell == '*':
                print(f"{RED}{cell}{RESET}", end=' ')
            elif cell == 'S':
                print(f"{GREEN}{cell}{RESET}", end=' ')
            elif cell == 'G':
                print(f"{BLUE}{cell}{RESET}", end=' ')
            else:
                print(f"{cell}", end=' ')
        print()  # New line after each row

