"""
Description
You are starving and you want to eat food as quickly as possible.
You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location
if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell.
If there is no path for you to reach food, return -1
"""

grid = [
    ["X", "X", "X", "X", "X", "X"],
    ["X", "*", "O", "O", "O", "X"],
    ["X", "O", "O", "#", "O", "X"],
    ["X", "X", "X", "X", "X", "X"]]

from collections import deque


def find_steps(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "*":
                start = (row, col)
                break

    queue = deque([(start[0], start[1], 0)])
    
    visited = set()
    visited.add((row, col))

    while queue:

        current_row, current_col, steps = queue.popleft()

        if grid[current_row][current_col] == "#":
            return steps

            # left
        nr, nc = current_row, current_col - 1

        if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] != "X" and (nr, nc) not in visited:
            queue.append((nr, nc, steps + 1))
            visited.add((nr, nc))
        # up
        nr, nc = current_row - 1, current_col
        if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] != "X" and (nr, nc) not in visited:
            queue.append((nr, nc, steps + 1))
            visited.add((nr, nc))
        # right
        nr, nc = current_row, current_col + 1
        if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] != "X" and (nr, nc) not in visited:
            queue.append((nr, nc, steps + 1))
            visited.add((nr, nc))
        # down
        nr, nc = current_row + 1, current_col
        if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] != "X" and (nr, nc) not in visited:
            queue.append((nr, nc, steps + 1))
            visited.add((nr, nc))
    return -1


print(find_steps(grid))
