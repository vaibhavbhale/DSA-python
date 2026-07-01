def exist(board, word):
    rows = len(board)
    cols = len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True

        if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]):
            return False

        temp = board[r][c]
        board[r][c] = "#"   # mark visited

        found = (
            dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c + 1, i + 1) or
            dfs(r, c - 1, i + 1)
        )

        board[r][c] = temp   # restore original value
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False


# Input
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = "ABCCED"

# Function call
print(exist(board, word))


# Dry Run:

# Word = "ABCCED"

# Start searching from board[0][0] = "A"

# dfs(0,0,0)
# word[0] = "A" matches
# mark visited

# Board:
# # B C E
# S F C S
# A D E E

# Search next character "B"

# Try down → board[1][0] = "S" (not B) ❌
# Try up → out of bounds ❌
# Try right → board[0][1