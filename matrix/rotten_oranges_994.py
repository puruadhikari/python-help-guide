"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

from collections import deque


def rotten_oragnes(grid):
    m = len(grid)
    n = len(grid[0])
    fresh_count = 0
    queue = deque()
    timer = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_count += 1

    if fresh_count == 0:
        return 0

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1:
                    queue.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh_count -= 1

        print(queue)
        if len(queue) > 0:
            timer += 1

    return timer if fresh_count == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

print(rotten_oragnes(grid))