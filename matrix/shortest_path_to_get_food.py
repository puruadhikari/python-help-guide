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
