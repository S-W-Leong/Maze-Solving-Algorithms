def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) # Finds the distance between start and goal (absolute difference)
# value of a = (row, col)

def greedy(maze, start, goal):
    from queue import PriorityQueue

    open_set = PriorityQueue()
    open_set.put((heuristic(start, goal), start))
    came_from = {}
    visited = set()

    while not open_set.empty():
        current = open_set.get()[1]
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        visited.add(current)
        neighbors = [(current[0] + dx, current[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        for neighbor in neighbors:
            if (
                0 <= neighbor[0] < len(maze)
                and 0 <= neighbor[1] < len(maze[0])
                and maze[neighbor[0]][neighbor[1]] == "."
                and neighbor not in visited
            ):
                came_from[neighbor] = current
                open_set.put((heuristic(neighbor, goal), neighbor))

    return None  # Return None if no path is found