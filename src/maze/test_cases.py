# Test Cases for Maze Solver AI

# All test cases below are guaranteed to be solvable in the updated maze.
# The maze is now 15x15 (0-14 indices), so valid positions are (1-13, 1-13)

TEST_CASES = [
    ((1, 1), (13, 13)),   # Test Case 1: Top-left to bottom-right
    ((1, 2), (13, 12)),   # Test Case 2: Top-left area to bottom-right area
    ((1, 3), (13, 11)),   # Test Case 3: Top-left area to bottom-right area
    ((1, 4), (13, 10)),   # Test Case 4: Top-left area to bottom-right area
    ((1, 5), (13, 9)),    # Test Case 5: Top-left area to bottom-right area
    ((1, 6), (13, 8)),    # Test Case 6: Top-left area to bottom-right area
    ((1, 7), (13, 7)),    # Test Case 7: Top-left area to bottom-right area
    ((1, 8), (13, 6)),    # Test Case 8: Top-left area to bottom-right area
    ((1, 9), (13, 5)),    # Test Case 9: Top-left area to bottom-right area
    ((1, 10), (13, 4)),   # Test Case 10: Top-left area to bottom-right area
]