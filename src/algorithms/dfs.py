def dfs(maze, start, goal):
    stack = [start]
    visited = set([start])
    parent = {start: None}
    path_found = False
    rows, cols = len(maze), len(maze[0])

    while stack:
        current = stack.pop()
        
        if current == goal:
            path_found = True
            break
            
        x, y = current
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (x + dx, y + dy)
            nx, ny = neighbor
            
            if (0 <= nx < rows and
                0 <= ny < cols and
                maze[nx][ny] == '.' and
                neighbor not in visited):
                
                stack.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    path = []
    if path_found:
        node = goal
        while node is not None:
            path.append(node)
            node = parent.get(node)
        path.reverse()
        
    return path, path_found, len(visited)

