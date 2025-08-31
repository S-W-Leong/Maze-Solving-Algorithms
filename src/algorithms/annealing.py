def simulated_annealing(maze, start, goal, max_iterations=1000, initial_temp=1000, cooling_rate=0.95):
    import random
    import math

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(position):
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for direction in directions:
            neighbor = (position[0] + direction[0], position[1] + direction[1])
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == ".":
                neighbors.append(neighbor)
        return neighbors

    current_position = start
    current_temp = initial_temp
    best_path = [start]
    best_cost = heuristic(start, goal)
    visited = set([start])

    found_goal = False
    for iteration in range(max_iterations):
        if current_position == goal:
            found_goal = True
            break

        # Exclude visited neighbors
        neighbors = [n for n in get_neighbors(current_position) if n not in visited]
        if not neighbors:
            break

        next_position = random.choice(neighbors)
        next_cost = heuristic(next_position, goal)

        if next_cost < best_cost or random.uniform(0, 1) < math.exp((best_cost - next_cost) / current_temp):
            current_position = next_position
            best_path.append(current_position)
            best_cost = next_cost
            visited.add(current_position)

        current_temp *= cooling_rate

    if found_goal:
        return best_path, len(best_path) - 1 if best_path else 0
    else:
        return [], 0