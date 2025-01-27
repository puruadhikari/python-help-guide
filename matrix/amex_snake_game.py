"""
You are given a 2D grid representing a board for a snake game. The board consists of the following characters:

'+' represents impassable squares that snakes cannot move through.
'O' represents open squares where snakes can move freely.
A snake can enter the board from the edges (the first or last row, or the first or last column) and move in a
straight line (either horizontally or vertically). The snake's movement is blocked if it encounters a '+' square.

Write a function to find all possible starting positions from which a snake can move through the entire board
in a straight line without being blocked. Return these starting positions as a list of coordinates.
"""
board = [
          ["O","O","O","O","O","X"],
          ["O","O","O","O","O","X"],
          ["O","X","O","O","O","X"],
          ["O","O","O","O","O","O"],
          ["O","O","X","O","O","X"]
        ]

def snake_movement_path(board):
    transposed_board = []
    for i in range(len(board[0])):
        col = []
        for j in range(len(board)):
            col.append(board[j][i])
        transposed_board.append(col)
    row_access = []
    col_access = []
    for i in range(len(board)):
        row_set = set(board[i])
        if len(row_set) == 1 and "O" in row_set:
            row_access.append(i)
    for j in range(len(transposed_board)):
        col_set = set(transposed_board[j])
        if len(col_set) == 1 and "O" in col_set:
            col_access.append(j)
    return [row_access, col_access]


print(snake_movement_path(board))