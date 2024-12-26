#board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEP"


def dfs(grid, visited, tracker, row_val, col_val, word, char_index):
    m = len(grid)
    n = len(grid[0])

    if (row_val < 0 or row_val >= m or
            col_val < 0 or col_val >= n or
            (row_val, col_val) in visited or
            word[char_index] != grid[row_val][col_val] ):
        return False

    visited.add((row_val, col_val))

    if char_index == len(word)-1:
        return True

    found = (dfs(grid, visited, tracker, row_val, col_val - 1, word, char_index+1) or
             dfs(grid, visited, tracker, row_val - 1, col_val, word, char_index+1) or
             dfs(grid, visited, tracker, row_val, col_val + 1, word, char_index + 1) or
             dfs(grid, visited, tracker, row_val + 1, col_val, word, char_index + 1))

    if not found:
        visited.remove((row_val,col_val))

    return found


def is_word_found(board, word):
    row = len(board)
    col = len(board[0])
    visited = set()
    tracker = []
    index = 0
    can_be_formed = False
    for r in range(row):
        for c in range(col):
            if board[r][c] == word[index]:
                if dfs(board, visited, tracker, r, c, word, 0):
                    print(f"visited: {visited}")
                    can_be_formed= True

    return can_be_formed


print(is_word_found(board,word))

