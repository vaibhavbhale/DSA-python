def totalNQueens(n):
    board = [[0] * n for _ in range(n)]

    row_used = [0] * n
    slash_used = [0] * (2 * n - 1)
    backslash_used = [0] * (2 * n - 1)

    solutions = 0

    def solve(col):
        nonlocal solutions

        if col == n:
            solutions += 1
            return

        for row in range(n):

            slash = row + col
            backslash = row - col + (n - 1)

            if not row_used[row] and not slash_used[slash] and not backslash_used[backslash]:

                board[row][col] = 1
                row_used[row] = slash_used[slash] = backslash_used[backslash] = 1

                solve(col + 1)

                board[row][col] = 0
                row_used[row] = slash_used[slash] = backslash_used[backslash] = 0

    solve(0)
    return solutions


# Input
n = 4

# Function call
print(totalNQueens(n))


# Dry Run:

# Initial:
# n = 4
# solutions = 0

# Column 0:
# Try row 0 → place queen at (0,0)

# Board:
# Q . . .
# . . . .
# . . . .
# . . . .

# Column 1:
# row 0 → not possible (same row)
# row 1 → not possible (diagonal)
# row 2 → place queen at (2,1)

# Board:
# Q . . .
# . . . .
# . Q . .
# . . . .

# Column 2:
# row 0 → not possible
# row 1 → not possible
# row 2 → not possible
# row 3 → not possible
# No valid move → backtrack

# Remove queen from (2,1)

# Column 1:
# Try row 3 → place queen at (3,1)

# Board:
# Q . . .
# . . . .
# . . . .
# . Q . .

# Column 2:
# row 1 → place queen at (1,2)

# Board:
# Q . . .
# . . Q .
# . . . .
# . Q . .

# Column 3:
# No valid row → backtrack

# Remove (1,2)
# Remove (3,1)
# Remove (0,0)

# Column 0:
# Try row 1 → place queen at (1,0)

# Board:
# . . . .
# Q . . .
# . . . .
# . . . .

# Column 1:
# Try row 3 → place queen at (3,1)

# Board:
# . . . .
# Q . . .
# . . . .
# . Q . .

# Column 2:
# Try row 0 → place queen at (0,2)

# Board:
# . . Q .
# Q . . .
# . . . .
# . Q . .

# Column 3:
# Try row 2 → place queen at (2,3)

# Board:
# . . Q .
# Q . . .
# . . . Q
# . Q . .

# All columns filled → Solution 1
# solutions = 1

# Backtrack...

# Another valid arrangement:

# Column 0 → row 2
# Column 1 → row 0
# Column 2 → row 3
# Column 3 → row 1

# Board:
# . Q . .
# . . . Q
# Q . . .
# . . Q .

# All columns filled → Solution 2
# solutions = 2

# Final:
# Total solutions = 2