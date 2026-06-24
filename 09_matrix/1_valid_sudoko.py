from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, grid = set(), set(), set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    r_k = (i, board[i][j])
                    c_k = (j, board[i][j])
                    g_k = (i // 3, j // 3, board[i][j])

                    if r_k in row or c_k in col or g_k in grid:
                        return False

                    row.add(r_k)
                    col.add(c_k)
                    grid.add(g_k)

        return True


# Given Input
board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

sol = Solution()
print(sol.isValidSudoku(board))

# Initially:
# row = {}
# col = {}
# grid = {}

# i = 0, j = 0 → value = "5"
# r_k = (0,"5")
# c_k = (0,"5")
# g_k = (0,0,"5")
# Not present → add to all sets

# i = 0, j = 1 → value = "3"
# r_k = (0,"3")
# c_k = (1,"3")
# g_k = (0,0,"3")
# Not present → add

# i = 0, j = 4 → value = "7"
# r_k = (0,"7")
# c_k = (4,"7")
# g_k = (0,1,"7")
# Not present → add

# i = 1, j = 0 → value = "6"
# r_k = (1,"6")
# c_k = (0,"6")
# g_k = (0,0,"6")
# Not present → add

# i = 1, j = 3 → value = "1"
# r_k = (1,"1")
# c_k = (3,"1")
# g_k = (0,1,"1")
# Not present → add

# i = 1, j = 4 → value = "9"
# r_k = (1,"9")
# c_k = (4,"9")
# g_k = (0,1,"9")
# Not present → add

# i = 1, j = 5 → value = "5"
# r_k = (1,"5")
# c_k = (5,"5")
# g_k = (0,1,"5")
# Not present → add

# i = 2, j = 1 → value = "9"
# r_k = (2,"9")
# c_k = (1,"9")
# g_k = (0,0,"9")
# Not present → add

# i = 2, j = 2 → value = "8"
# r_k = (2,"8")
# c_k = (2,"8")
# g_k = (0,0,"8")
# Not present → add

# Continue same process for all filled cells.

# At every step:
# Check if number already exists in same row, column, or 3x3 grid.
# If yes → return False
# In this given board → no duplicates found anywhere.

# After checking all 81 cells:
# No conflict detected.

# Final Output:
# True