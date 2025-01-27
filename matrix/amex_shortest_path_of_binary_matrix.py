"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell
(i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an
edge or a corner).
The length of a clear path is the number of visited cells of this path.

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
"""
from collections import deque

grid1 = [[0,0,0],[1,1,0],[1,1,0]]


def shortest_path_binary_grid(grid):
    n = len(grid)
    row_col = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    queue = deque()
    queue.append((0, 0, 1))
    grid[0][0] = 1

    while queue:
        row, col, path = queue.popleft()
        print(row,col,path)
        if row == n - 1 and col == n-1:
            return path

        for dw, dc in row_col:
            r = row + dw
            c = col + dc

            if r >= 0 and r < n  and c >= 0 and c < n  and grid[r][c] == 0:
                queue.append((r, c, path + 1))
                grid[r][c] = 1

    return path


print(shortest_path_binary_grid(grid1))
