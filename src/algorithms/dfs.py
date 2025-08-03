def dfs(maze, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}
    path_found = False

    while stack:
        current = stack.pop()
        if current == goal:
            path_found = True
            break
        if current not in visited:
            visited.add(current)
            x, y = current
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (x + dx, y + dy)
                if (0 <= neighbor[0] < len(maze) and
                        0 <= neighbor[1] < len(maze[0]) and
                        maze[neighbor[0]][neighbor[1]] == '.' and
                        neighbor not in visited):
                    stack.append(neighbor)
                    parent[neighbor] = current

    path = []
    if path_found:
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()

    return path, path_found, len(visited)