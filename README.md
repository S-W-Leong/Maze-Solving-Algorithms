# Maze Solver AI

This project implements various search algorithms to solve maze problems. The algorithms included are Breadth-First Search (BFS), Depth-First Search (DFS), A* Search, Greedy Best-First Search, and Simulated Annealing. The application is terminal-based and allows users to select different algorithms and test cases to visualize the pathfinding process.

## Project Structure

```
maze-solver-ai
├── src
│   ├── main.py                # Entry point of the application
│   ├── algorithms             # Contains implementations of search algorithms
│   │   ├── bfs.py             # Breadth-First Search algorithm
│   │   ├── dfs.py             # Depth-First Search algorithm
│   │   ├── astar.py           # A* Search algorithm
│   │   ├── greedy.py          # Greedy Best-First Search algorithm
│   │   └── annealing.py       # Simulated Annealing algorithm
│   ├── maze                   # Contains maze definitions and test cases
│   │   ├── maze_map.py        # Defines the maze structure
│   │   └── test_cases.py      # Predefined test cases for the maze
│   ├── utils                  # Utility functions for display and analysis
│   │   ├── display.py         # Functions to display the maze and path
│   │   └── analysis.py        # Functions to analyze algorithm performance
│   └── types                  # Custom types or interfaces (if needed)
│       └── __init__.py
├── requirements.txt           # Required Python packages
├── README.md                  # Project documentation
└── .gitignore                 # Files and directories to ignore in version control
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd maze-solver-ai
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage

- Upon running the application, a main menu will be displayed with options to select different search algorithms.
- After selecting an algorithm, you can choose a test case to run, which will execute the algorithm and display the results, including the path found and a visual representation of the maze.
- You can also view the analysis of the algorithm's performance across different test cases.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.