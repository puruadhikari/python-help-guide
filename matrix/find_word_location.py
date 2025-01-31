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


def dfs(grid, r, c, word, result, visited, index):
    m = len(grid)
    n = len(grid)

    if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != word[index] or (r, c) in visited:
        return False

    visited.add((r, c))
    result.append((r, c))

    if index == len(word) - 1:
        return True

    found = (dfs(grid, r + 1, c, word, result, visited, index + 1) or dfs(grid, r, c + 1, word, result, visited,
                                                                          index + 1))

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
