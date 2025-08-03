def astar(maze, start, goal):
    from queue import PriorityQueue

    # Initialize the open and closed sets
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    
    # Initialize g_score and f_score dictionaries
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while not open_set.empty():
        current = open_set.get()[1]

        # Check if we reached the goal
        if current == goal:
            return reconstruct_path(came_from, current)

        # Explore neighbors
        for neighbor in get_neighbors(maze, current):
            tentative_g_score = g_score[current] + 1  # Assuming cost between nodes is 1

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                # This path to neighbor is better than any previous one
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                if neighbor not in [i[1] for i in open_set.queue]:
                    open_set.put((f_score[neighbor], neighbor))

    return None  # Return None if no path is found


def heuristic(a, b):
    # Using Manhattan distance as heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(maze, node):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for direction in directions:
        neighbor = (node[0] + direction[0], node[1] + direction[1])
        if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == ".":
            neighbors.append(neighbor)
    return neighbors


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()  # Reverse the path to get it from start to goal
    return total_path