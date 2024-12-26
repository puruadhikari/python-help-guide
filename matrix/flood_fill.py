"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel,
either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if
it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.



Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]
"""

image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2


def flood_fill(grid, sr, sc, color):
    def dfs(grid, r, c, original_color):
        m = len(grid)
        n = len(grid[0])

        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == color or grid[r][c]==0:
            return

        grid[r][c] = color

        dfs(grid, r, c - 1,2)  # left
        dfs(grid, r - 1, c,2)  # top
        dfs(grid, r, c + 1,2)  # right
        dfs(grid, r + 1, c,2)  # bottom

    dfs(grid, 1, 1, 1)

    return grid


print(flood_fill(image, sr, sc, color))
