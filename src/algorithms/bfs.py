def bfs(maze, start, goal):
    from collections import deque

    # Initialize the queue and visited set
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    # To keep track of the path
    parent = {start: None}
    
    while queue:
        current = queue.popleft()
        
        # Check if we reached the goal
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, len(path) - 1 if path else 0
        
        # Explore neighbors
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbor[0] < len(maze) and
                0 <= neighbor[1] < len(maze[0]) and
                maze[neighbor[0]][neighbor[1]] == '.' and
                neighbor not in visited):
                
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    
    # If no path is found
    return None, 0