grid1 = [
    ['c', 'c', 't', 'n', 'a', 'x'],
    ['c', 'c', 'a', 't', 'n', 't'],
    ['a', 'c', 'n', 'n', 't', 't'],
    ['t', 'n', 'i', 'i', 'p', 'p'],
    ['a', 'o', 'o', 'o', 'a', 'a'],
    ['s', 'a', 'a', 'a', 'o', 'o'],
    ['k', 'a', 'i', 'o', 'k', 'i']
]

# find_word_location(grid1, word1) => [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)]
word1 = "catnip"
visited = set()

from collections import deque


def find_word_bfs(matrix, word):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == word[0]:
                queue = deque()
                queue.append((i, j, [(i, j)], 0))

                while queue:
                    row, col, path, index = queue.popleft()
                    if index == len(word) - 1:
                        return path

                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nr, nc = row + dr, col + dc
                        if nr >= 0 and nr < m and nc >= 0 and nc < n and matrix[nr][nc] == word[index + 1]:
                            #NOTE path + [(nr,nc)] creates a new list with a path
                            queue.append((nr, nc, path + [(nr, nc)], index + 1))
    return []


print(find_word_bfs(grid1, word1))

def dfs(grid, r, c, word, result, visited, index):
    m = len(grid)
    n = len(grid)

    if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != word[index] or (r, c) in visited:
        return False

    visited.add((r, c))
    result.append((r, c))

    if index == len(word) - 1:
        return True

    found = (dfs(grid, r + 1, c, word, result, visited, index + 1) or
             dfs(grid, r, c + 1, word, result, visited,index + 1))

    if found:
        return True

    visited.remove((r, c))
    result.pop()

    return False


def find_word_location(grid, word):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == word[0]:
                result = []  # NOTE THIS MUST BE DEFINED HERE NOT OUTSIDE
                if dfs(grid, row, col, word, result, visited, 0):
                    return result

    return result


print(find_word_location(grid1, word1))
