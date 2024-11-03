def is_safe_to_visit(m_grid, r, c, visited, ROW, COL):
    # Check if the cell is within bounds, is '1', and has not been visited
    return (0 <= r < ROW) and (0 <= c < COL) and (m_grid[r][c] == '1' and not visited[r][c])


def dfs(matrix, row, column, visited, ROW, COL):
    # Define directions for 8 neighboring cells (diagonal, horizontal, vertical)
    r_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    c_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]

    # Mark the cell as visited
    visited[row][column] = True

    # Explore all 8 neighbors
    for index in range(8):
        n_row = row + r_nbr[index]
        n_column = column + c_nbr[index]

        # Check if the neighbor is safe to visit
        if is_safe_to_visit(matrix, n_row, n_column, visited, ROW, COL):
            dfs(matrix, n_row, n_column, visited, ROW, COL)


def count_islands(grid):
    # Handle edge case of empty grid
    if not grid or not grid[0]:
        return 0

    ROW = len(grid)
    COL = len(grid[0])
    count = 0
    # Initialize the visited matrix
    visited = [[False for _ in range(COL)] for _ in range(ROW)]

    # Iterate over each cell in the grid
    for r in range(ROW):
        for c in range(COL):
            # Start a DFS if we find an unvisited '1' cell
            if grid[r][c] == '1' and not visited[r][c]:
                dfs(grid, r, c, visited, ROW, COL)
                count += 1  # Increment count for each new island found
    return count


grid = [['1', '1', '0', '0', '0'],
        ['0', '1', '0', '0', '1'],
        ['1', '0', '0', '1', '1'],
        ['0', '0', '0', '0', '0'],
        ['1', '0', '1', '1', '0']]

# Test the function
print(count_islands(grid))  # Expected output: 3
