def display_maze(maze, path, start=None, goal=None):
    """
    Displays the maze with the path marked and start/goal points highlighted.
    
    Parameters:
    maze (list of list of str): The maze represented as a 2D list.
    path (list of tuple): The path found from start to goal, represented as a list of (row, col) tuples.
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
    
    # Mark the path in the maze if path exists and is not None
    if path is not None and len(path) > 0:
        for (row, col) in path:
            # Don't overwrite start and goal markers
            if maze_with_path[row][col] not in ['S', 'G']:
                maze_with_path[row][col] = '*'
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