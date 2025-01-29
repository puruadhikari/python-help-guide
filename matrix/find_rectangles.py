"""
You are given a binary image represented by a 2D integer array board consisting of 0s and 1s.
The image contains at most one rectangle filled with 0s. Your task is to find the rectangle and return its coordinates.

You may return the coordinates of the top-left and bottom-right elements of the rectangle in the format [r1, c1, r2, c2], where:
board = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 1],
  [1, 0, 0, 1, 1],
  [1, 1, 1, 1, 1]
];

"""

def find_all_rectangle(matrix):
    rows,cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    rectangles = []
    def mark_visited(r1,r2,c1,c2):
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                visited[r][c] = True

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] ==0 and not visited[i][j]:
                r1,c1 = i,j
                r2 = r1
                c2 = c1
                while r2+1 < rows and matrix[r2+1][c1] ==0:
                    r2 += 1
                while c2+1 < cols and matrix[r1][c2+1] ==0:
                    c2 += 1
                mark_visited(r1,r2,c1,c2)
                rectangles.append([r1,c1,r2,c2])
    return rectangles

def find_one_rectangle(matrix):
    rows,cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] ==0:
                r1,c1 = i,j
                r2 = r1
                c2 = c1
                while r2+1 < rows and matrix[r2+1][c1] ==0:
                    r2 += 1
                while c2+1 < cols and matrix[r1][c2+1] ==0:
                    c2 += 1
                return [r1,c1,r2,c2]
    return []

board = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 1],
  [1, 0, 0, 1, 1],
  [1, 1, 1, 1, 1]
]

board1 = [
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0],
  [1, 1, 1, 0, 0]
]
print(find_all_rectangle(board))