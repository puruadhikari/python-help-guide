matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

from collections import deque


def bfs_traversal(matrix, row, col):
    m = len(matrix)
    n = len(matrix[0])

    queue = deque()
    visited = set()
    result = []

    visited.add((row, col))
    queue.append((row, col))
    result.append(matrix[row][col])

    while queue:
        r, c = queue.popleft()
        # left,up,right,down
        for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            nr, nc = r + dr, c + dc

            if nr >= 0 and nr < m and nc >= 0 and nc < n and (nr, nc) not in visited:
                queue.append((nr, nc))
                visited.add((nr, nc))
                result.append(matrix[nr][nc])
    print(visited)
    return result

def dfs_traversal(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = []
    visited = set()

    def dfs(r,c):
        if r < 0 or r >= m or c < 0 or c >= n or (r,c) in visited:
            return

        result.append(matrix[r][c])
        visited.add((r,c))
        #left,up,right,down
        dfs(r,c-1)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r+1,c)

    dfs(0,0)
    return result

#print(bfs_traversal(matrix, 0, 0))
print(dfs_traversal(matrix))