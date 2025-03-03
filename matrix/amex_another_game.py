"""
You are developing a solitaire game where players can select tiles on a grid to remove them.
When a player selects a tile, the tile disappears along with any tiles of the same value that are connected
to it (directly up, down, left, or right). The connections continue recursively for tiles with the same value.
Tiles are not connected diagonally.

Write a function, disappear(grid, row, col), that takes in:

A grid of integers representing the tiles.
The row and col of the selected tile.
The function should return the total number of tiles that disappear when the player selects the tile at (row, col).
grid1 = [
    [4, 4, 4, 4],
    [5, 5, 5, 4],
    [2, 5, 7, 5]
]
disappear(grid1, 0, 0)  # Expected Output: 5
disappear(grid1, 1, 1)  # Expected Output: 4
disappear(grid1, 1, 0)  # Expected Output: 4

grid2 = [
    [0, 3, 3, 3, 3, 3, 3],
    [0, 1, 1, 1, 1, 1, 3],
    [0, 2, 2, 0, 2, 1, 4],
    [0, 1, 2, 2, 2, 1, 3],
    [0, 1, 1, 1, 1, 1, 3],
    [0, 0, 0, 0, 0, 0, 0]
]
disappear(grid2, 0, 1)  # Expected Output: ?
disappear(grid2, 4, 4)  # Expected Output: ?

"""

grid1 = [
    [4, 4, 4, 4],
    [5, 5, 5, 4],
    [2, 5, 7, 5]
]

grid2 = [
    [0, 3, 3, 3, 3, 3, 3],
    [0, 1, 1, 1, 1, 1, 3],
    [0, 2, 2, 0, 2, 1, 4],
    [0, 1, 2, 2, 2, 1, 3],
    [0, 1, 1, 1, 1, 1, 3],
    [0, 0, 0, 0, 0, 0, 0]
]
counter = 0
visited = set()
from collections import deque

def another_game_bfs(matrix, target):
    queue = deque()
    visited_bfs = set()
    m = len(matrix)
    n = len(matrix[0])

    result = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == target:
                queue.append((i, j))
                visited_bfs.add((i, j))
                break

    while queue:
        row, col = queue.popleft()
        result.append((row, col))

        # left,top,right,down
        for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            nr, nc = row + dr, col + dc
            if nr >= 0 and nr < m and nc >= 0 and nc < n and (nr, nc) not in visited_bfs and matrix[nr][nc] == target:
                queue.append((nr, nc))
                visited_bfs.add((nr, nc))
    return result

def dfs(grd, r, c, num,visited,result=[]):
    m = len(grd)
    n = len(grd[0])
    if r < 0 or r >= m or c < 0 or c >= n or grd[r][c] != num or (r,c) in visited:
        return

    visited.add((r,c))
    if grd[r][c] == num:
        result.append((r,c))

    dfs(grd, r, c - 1, num,visited)
    dfs(grd, r - 1, c, num,visited)
    dfs(grd, r, c + 1, num,visited)
    dfs(grd, r + 1, c, num,visited)

    return result

def disappear(grid, row,col):

    number = grid[row][col]
    if grid[row][col] == number and (row,col) not in visited:
        res = dfs(grid, row, col, number,visited)

    return res


print(disappear(grid2, 1,1))
print(another_game_bfs(grid2,1))