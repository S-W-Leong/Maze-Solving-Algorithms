# Maze-Solving Algorithms Analysis Report

## Overview
This report analyzes the performance of 5 maze-solving algorithms across 5 selected test cases, comparing theoretical predictions with actual experimental results.

## Algorithms Analyzed
1. **Breadth-First Search (BFS)**
2. **Depth-First Search (DFS)**
3. **A* Search**
4. **Greedy Best-First Search**
5. **Simulated Annealing**

## Test Cases Selected
- **Test Case 1**: (1, 1) → (13, 13) - Diagonal path across maze
- **Test Case 3**: (1, 3) → (13, 11) - Diagonal path with slight offset
- **Test Case 5**: (1, 5) → (13, 9) - Diagonal path with moderate offset
- **Test Case 7**: (1, 7) → (13, 7) - Horizontal path across maze
- **Test Case 9**: (1, 9) → (13, 5) - Diagonal path with larger offset

---

## 1. Breadth-First Search (BFS) Analysis

### Theoretical Characteristics
- **Completeness**: ✅ Complete (guaranteed to find solution if exists)
- **Cost-Optimality**: ✅ Optimal (finds shortest path)
- **Time Complexity**: O(V + E) where V = vertices, E = edges
- **Space Complexity**: O(V) - stores all nodes at current depth

### Performance Analysis Table

| Test Case | Completeness | Cost-Optimality | Time Complexity | Space Complexity | Predicted Output | Actual Output | Hypothesis |
|-----------|--------------|-----------------|-----------------|------------------|------------------|---------------|------------|
| (1,1)→(13,13) | ✅ Complete | ✅ Optimal | O(V+E) | O(V) | Success, ~24 steps, Fast | Success, 24 steps, 0.00ms | ✅ True |
| (1,3)→(13,11) | ✅ Complete | ✅ Optimal | O(V+E) | O(V) | Success, ~24 steps, Fast | Success, 24 steps, 2.22ms | ✅ True |
| (1,5)→(13,9) | ✅ Complete | ✅ Optimal | O(V+E) | O(V) | Success, ~24 steps, Fast | Success, 24 steps, 1.22ms | ✅ True |
| (1,7)→(13,7) | ✅ Complete | ✅ Optimal | O(V+E) | O(V) | Success, ~24 steps, Fast | Success, 24 steps, 0.68ms | ✅ True |
| (1,9)→(13,5) | ✅ Complete | ✅ Optimal | O(V+E) | O(V) | Success, ~24 steps, Fast | Success, 24 steps, 2.16ms | ✅ True |

### Discrepancies Discussion
**No significant discrepancies observed.** BFS performed exactly as expected:
- Consistently found optimal paths (24 steps for all cases)
- Fast execution times (0.68-2.22ms)
- Low memory usage (5.1-6.0 KB)
- 100% success rate

### Optimal Performance Case
**Test Case 7 ((1,7)→(13,7))** demonstrated optimal performance with:
- Fastest execution time (0.68ms)
- Consistent optimal path length (24 steps)
- Reasonable memory usage (6.0 KB)

**Justification**: This horizontal path across the maze is the most straightforward for BFS, requiring minimal exploration of unnecessary branches.

---

## 2. Depth-First Search (DFS) Analysis

### Theoretical Characteristics
- **Completeness**: ✅ Complete (guaranteed to find solution if exists)
- **Cost-Optimality**: ❌ Not optimal (may find suboptimal path)
- **Time Complexity**: O(V + E) where V = vertices, E = edges
- **Space Complexity**: O(V) - stores path from root to current node

### Performance Analysis Table

| Test Case | Completeness | Cost-Optimality | Time Complexity | Space Complexity | Predicted Output | Actual Output | Hypothesis |
|-----------|--------------|-----------------|-----------------|------------------|------------------|---------------|------------|
| (1,1)→(13,13) | ✅ Complete | ❌ Suboptimal | O(V+E) | O(V) | Success, >24 steps, Fast | Success, 72 steps, 0.83ms | ✅ True |
| (1,3)→(13,11) | ✅ Complete | ❌ Suboptimal | O(V+E) | O(V) | Success, >24 steps, Fast | Success, 72 steps, 2.01ms | ✅ True |
| (1,5)→(13,9) | ✅ Complete | ❌ Suboptimal | O(V+E) | O(V) | Success, >24 steps, Fast | Success, 64 steps, 2.01ms | ✅ True |
| (1,7)→(13,7) | ✅ Complete | ❌ Suboptimal | O(V+E) | O(V) | Success, >24 steps, Fast | Success, 60 steps, 0.00ms | ✅ True |
| (1,9)→(13,5) | ✅ Complete | ❌ Suboptimal | O(V+E) | O(V) | Success, >24 steps, Fast | Success, 76 steps, 2.06ms | ✅ True |

### Discrepancies Discussion
**No significant discrepancies observed.** DFS performed as expected:
- Found solutions in all cases (100% completeness)
- Consistently suboptimal paths (60-76 steps vs optimal 24)
- Fast execution times (0.00-2.06ms)
- Reasonable memory usage (4.7-5.9 KB)

### Optimal Performance Case
**Test Case 7 ((1,7)→(13,7))** demonstrated optimal performance with:
- Shortest suboptimal path (60 steps)
- Fastest execution time (0.00ms)
- Lowest memory usage (4.7 KB)

**Justification**: The horizontal path allows DFS to follow a more direct route without extensive backtracking, resulting in better performance despite still being suboptimal.

---

## 3. A* Search Analysis

### Theoretical Characteristics
- **Completeness**: ✅ Complete (guaranteed to find solution if exists)
- **Cost-Optimality**: ✅ Optimal (finds shortest path with admissible heuristic)
- **Time Complexity**: O(V log V) with priority queue
- **Space Complexity**: O(V) - stores open and closed sets

### Performance Analysis Table

| Test Case | Completeness | Cost-Optimality | Time Complexity | Space Complexity | Predicted Output | Actual Output | Hypothesis |
|-----------|--------------|-----------------|-----------------|------------------|------------------|---------------|------------|
| (1,1)→(13,13) | ✅ Complete | ✅ Optimal | O(V log V) | O(V) | Success, ~24 steps, Fast | Success, 24 steps, 44.31ms | ❌ False |
| (1,3)→(13,11) | ✅ Complete | ✅ Optimal | O(V log V) | O(V) | Success, ~24 steps, Fast | Success, 24 steps, 1.90ms | ✅ True |
| (1,5)→(13,9) | ✅ Complete | ✅ Optimal | O(V log V) | O(V) | Success, ~24 steps, Fast | Success, 24 steps, 2.77ms | ✅ True |
| (1,7)→(13,7) | ✅ Complete | ✅ Optimal | O(V log V) | O(V) | Success, ~24 steps, Fast | Success, 24 steps, 3.52ms | ✅ True |
| (1,9)→(13,5) | ✅ Complete | ✅ Optimal | O(V log V) | O(V) | Success, ~24 steps, Fast | Success, 24 steps, 0.60ms | ✅ True |

### Discrepancies Discussion
**Significant discrepancy in Test Case 1**: A* was unexpectedly slow (44.31ms vs expected fast performance).

**Why A* was slower than expected in Test Case 1:**
1. **Priority Queue Overhead**: A* uses a priority queue which has O(log n) insertion/deletion costs
2. **Heuristic Calculation**: Manhattan distance calculations add computational overhead
3. **Memory Allocation**: Higher memory usage (275.7 KB) suggests extensive data structure overhead
4. **Implementation Efficiency**: The specific implementation may have suboptimal priority queue usage

### Optimal Performance Case
**Test Case 9 ((1,9)→(13,5))** demonstrated optimal performance with:
- Fastest execution time (0.60ms)
- Optimal path length (24 steps)
- Reasonable memory usage (5.8 KB)

**Justification**: This test case likely benefited from the heuristic function providing excellent guidance, reducing the number of nodes explored and priority queue operations.

---

## 4. Greedy Best-First Search Analysis

### Theoretical Characteristics
- **Completeness**: ❌ Not complete (may get stuck in local optima)
- **Cost-Optimality**: ❌ Not optimal (prioritizes heuristic over actual cost)
- **Time Complexity**: O(V log V) with priority queue
- **Space Complexity**: O(V) - stores open set

### Performance Analysis Table

| Test Case | Completeness | Cost-Optimality | Time Complexity | Space Complexity | Predicted Output | Actual Output | Hypothesis |
|-----------|--------------|-----------------|-----------------|------------------|------------------|---------------|------------|
| (1,1)→(13,13) | ❌ Incomplete | ❌ Suboptimal | O(V log V) | O(V) | Success, ~24 steps, Fast | Success, 24 steps, 0.00ms | ❌ False |
| (1,3)→(13,11) | ❌ Incomplete | ❌ Suboptimal | O(V log V) | O(V) | Success, ~24 steps, Fast | Success, 24 steps, 0.00ms | ❌ False |
| (1,5)→(13,9) | ❌ Incomplete | ❌ Suboptimal | O(V log V) | O(V) | Success, >24 steps, Fast | Success, 32 steps, 7.66ms | ✅ True |
| (1,7)→(13,7) | ❌ Incomplete | ❌ Suboptimal | O(V log V) | O(V) | Success, >24 steps, Fast | Success, 28 steps, 2.70ms | ✅ True |
| (1,9)→(13,5) | ❌ Incomplete | ❌ Suboptimal | O(V log V) | O(V) | Success, >24 steps, Fast | Success, 28 steps, 2.90ms | ✅ True |

### Discrepancies Discussion
**Significant discrepancies in Test Cases 1 and 3**: Greedy found optimal paths when it was expected to be suboptimal.

**Why Greedy performed better than expected:**
1. **Maze Structure**: The maze layout may be particularly favorable for greedy search
2. **Heuristic Quality**: Manhattan distance heuristic works well for this grid-based maze
3. **Path Characteristics**: The diagonal paths may align well with the heuristic function
4. **Implementation**: The specific implementation may have additional optimizations

### Optimal Performance Case
**Test Cases 1 and 3 ((1,1)→(13,13) and (1,3)→(13,11))** demonstrated optimal performance with:
- Optimal path lengths (24 steps)
- Fastest execution times (0.00ms)
- Lowest memory usage (3.3-4.1 KB)

**Justification**: These diagonal paths align perfectly with the Manhattan distance heuristic, allowing greedy search to find optimal solutions efficiently.

---

## 5. Simulated Annealing Analysis

### Theoretical Characteristics
- **Completeness**: ❌ Not complete (probabilistic, may not find solution)
- **Cost-Optimality**: ❌ Not optimal (approximation algorithm)
- **Time Complexity**: O(iterations) - depends on parameters
- **Space Complexity**: O(path_length) - stores current path

### Performance Analysis Table

| Test Case | Completeness | Cost-Optimality | Time Complexity | Space Complexity | Predicted Output | Actual Output | Hypothesis |
|-----------|--------------|-----------------|-----------------|------------------|------------------|---------------|------------|
| (1,1)→(13,13) | ❌ Incomplete | ❌ Suboptimal | O(iterations) | O(path) | May fail, >24 steps, Slow | Failed, 0 steps, 17.93ms | ✅ True |
| (1,3)→(13,11) | ❌ Incomplete | ❌ Suboptimal | O(iterations) | O(path) | May fail, >24 steps, Slow | Failed, 0 steps, 0.97ms | ✅ True |
| (1,5)→(13,9) | ❌ Incomplete | ❌ Suboptimal | O(iterations) | O(path) | May fail, >24 steps, Slow | Failed, 0 steps, 0.00ms | ✅ True |
| (1,7)→(13,7) | ❌ Incomplete | ❌ Suboptimal | O(iterations) | O(path) | May fail, >24 steps, Slow | Failed, 0 steps, 0.00ms | ✅ True |
| (1,9)→(13,5) | ❌ Incomplete | ❌ Suboptimal | O(iterations) | O(path) | May fail, >24 steps, Slow | Success, 40 steps, 0.00ms | ✅ True |

### Discrepancies Discussion
**No significant discrepancies observed.** Simulated Annealing performed as expected:
- Low success rate (20% - only 1 out of 5 cases)
- Suboptimal path when successful (40 steps vs optimal 24)
- Variable execution times (0.00-17.93ms)
- Low memory usage (1.5-99.2 KB)

### Optimal Performance Case
**Test Case 9 ((1,9)→(13,5))** demonstrated optimal performance with:
- Only successful case (40 steps)
- Fast execution time (0.00ms)
- Reasonable memory usage (3.1 KB)

**Justification**: This test case may have had favorable starting conditions or the random walk happened to find a path quickly, though it was still suboptimal.

---

## Overall Algorithm Comparison

### Summary of Key Findings

| Algorithm | Completeness | Cost-Optimality | Avg Time (ms) | Avg Memory (KB) | Success Rate |
|-----------|--------------|-----------------|---------------|-----------------|--------------|
| BFS | ✅ 100% | ✅ Optimal | 1.26 | 5.7 | 100% |
| DFS | ✅ 100% | ❌ Suboptimal | 1.38 | 5.3 | 100% |
| A* | ✅ 100% | ✅ Optimal | 10.62 | 59.5 | 100% |
| Greedy | ❌ 100%* | ❌ Variable | 2.65 | 4.4 | 100% |
| Simulated Annealing | ❌ 20% | ❌ Suboptimal | 3.78 | 21.2 | 20% |

*Note: Greedy achieved 100% success rate despite theoretical incompleteness

### Recommendations

1. **For Guaranteed Solutions**: Use BFS or A* (both 100% complete)
2. **For Optimal Paths**: Use BFS or A* (both optimal)
3. **For Speed**: Use BFS (fastest overall)
4. **For Memory Efficiency**: Use Greedy (lowest memory usage)
5. **Avoid**: Simulated Annealing (low success rate, suboptimal)

### Conclusion

The experimental results largely align with theoretical expectations, with some notable exceptions:
- Greedy search performed better than expected in terms of completeness and optimality
- A* showed unexpected performance variation, particularly in Test Case 1
- BFS demonstrated the most consistent and predictable performance
- Simulated Annealing confirmed its probabilistic nature with low success rates

These findings provide valuable insights into algorithm selection for maze-solving applications based on specific requirements for completeness, optimality, speed, and memory efficiency.
