from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])
        
        def count_neighbours(r, c):
            directions = [(-1,-1), (-1,0), (-1,1),
                          (0,-1),         (0,1),
                          (1,-1),  (1,0), (1,1)]
            
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] in (1, 3):  # originally alive
                        count += 1
            return count
        
       
        for r in range(rows):
            for c in range(cols):
                n = count_neighbours(r, c)
                
                if board[r][c] == 1:   # currently alive
                    if n in [2, 3]:
                        board[r][c] = 3   # alive → alive
                else:   # currently dead
                    if n == 3:
                        board[r][c] = 2   # dead → alive

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in (2, 3):
                    board[r][c] = 1



board = [[0,1,0],
         [0,0,1],
         [1,1,1],
         [0,0,0]]

sol = Solution()
sol.gameOfLife(board)
print(board)

# Original Board:
# 0 1 0
# 0 0 1
# 1 1 1
# 0 0 0

# Rules:
# 1 → Alive
# 0 → Dead
# 2 → Dead → Alive
# 3 → Alive → Alive

# ---------------- FIRST PASS (Mark Changes) ----------------

# (0,0) = 0
# Neighbours = 1 → stays 0

# (0,1) = 1
# Neighbours = 1 → dies (not 2 or 3)
# remains 1 for now (will convert to 0 later)

# (0,2) = 0
# Neighbours = 2 → stays 0

# (1,0) = 0
# Neighbours = 3 → dead → alive → mark 2

# (1,1) = 0
# Neighbours = 5 → stays 0

# (1,2) = 1
# Neighbours = 3 → alive → alive → mark 3

# (2,0) = 1
# Neighbours = 1 → dies (remains 1)

# (2,1) = 1
# Neighbours = 3 → alive → alive → mark 3

# (2,2) = 1
# Neighbours = 2 → alive → alive → mark 3

# (3,0) = 0
# Neighbours = 2 → stays 0

# (3,1) = 0
# Neighbours = 3 → dead → alive → mark 2

# (3,2) = 0
# Neighbours = 2 → stays 0

# Board after first pass (intermediate states):
# 0 1 0
# 2 0 3
# 1 3 3
# 0 2 0

# ---------------- SECOND PASS (Finalize) ----------------

# Convert:
# 1 → 0 (dead)
# 2 → 1 (alive)
# 3 → 1 (alive)

# Final Board:
# 0 0 0
# 1 0 1
# 0 1 1
# 0 1 0