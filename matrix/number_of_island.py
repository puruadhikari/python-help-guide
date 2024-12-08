grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

visited = set()


def number_of_island(grid1):
    number_island = 0

    for row_val in range(len(grid1)):
        for col_val in range(len(grid1[0])):
            if grid1[row_val][col_val] == "1" and (row_val, col_val) not in visited:
                dfs(row_val, col_val, grid1, visited)
                number_island += 1

    return number_island


def dfs(row, col, matrix, visited):
    m = len(matrix)
    n = len(matrix[0])
    if row < 0 or row >= m or n < 0 or col >= n or (row, col) in visited or matrix[row][col] == "0":
        return

    visited.add((row, col))

    dfs(row, col - 1, matrix, visited)  # left
    dfs(row - 1, col, matrix, visited)  # top
    dfs(row, col + 1, matrix, visited)  # right
    dfs(row + 1, col, matrix, visited)  # down


print("Number of island are : ", number_of_island(grid))