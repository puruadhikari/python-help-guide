"""
You are creating Flippy, an AI that plans to take over the world by solving games involving flipping things.
First, the AI must master a one-dimensional game called Reversi.

Rules:
There are two players: 'X' (the AI player) and 'O'.
The goal is to place a new 'X' in a blank space ('') on the board to capture the 'O' tokens between two 'X' tokens, with no spaces in between.
A move can capture tokens to the left or to the right, but not both at the same time.
The optimal move is the one that captures the most 'O' tokens. In the case of a tie, return any valid move that captures the maximum tokens.
Input:
board: A 1D list of characters representing the board. The board contains 'X', 'O', and blank spaces ('').
Output:
Return a tuple (index, captures), where:
index: The position of the optimal move.
captures: The number of 'O' tokens captured by this move.
If no valid move is possible, return None or null.
"""


def reversi(board):
    result = []
    n = len(board)

    for i in range(n):
        if board[i] == '':  # Consider blank spaces for potential moves
            # Check left capture
            left = i - 1
            captured_left = 0
            while left >= 0 and board[left] == 'O':
                captured_left += 1
                left -= 1
            if left >= 0 and board[left] == 'X' and captured_left > 0:
                result.append((i, captured_left))

            # Check right capture
            right = i + 1
            captured_right = 0
            while right < n and board[right] == 'O':
                captured_right += 1
                right += 1
            if right < n and board[right] == 'X' and captured_right > 0:
                # Accumulate valid right captures
                if i < n:
                    result.append((i, captured_right))

    # If no valid moves, return None
    if not result:
        return None

    # Sort by the number of captured tokens in descending order and return the best move
    result.sort(key=lambda x: x[1], reverse=True)
    print(result)
    return result[0]


# Test the function
board1 = ['X', 'O', 'O', 'O', '', 'O', 'O', '', 'X', '', 'O', 'X', 'O', '', 'X']
board2 = ['X', '', 'O', '', '', 'O', '', 'X', 'O', '', 'O', '', '', 'X', 'O', '']

print(reversi(board1))  # Expected Output: (4, 3)
print(reversi(board2))  # Expected Output: (12, 2)

