from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col = False
        R = len(matrix)
        C = len(matrix[0])

    
        for i in range(R):
            if matrix[i][0] == 0:
                col = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Handle first row
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # Step 4: Handle first column
        if col:
            for i in range(R):
                matrix[i][0] = 0


matrix = [[1,1,1],
          [1,0,1],
          [1,1,1]]

sol = Solution()
sol.setZeroes(matrix)
print(matrix)

# Original Matrix:
# 1 1 1
# 1 0 1
# 1 1 1

# R = 3, C = 3
# col = False

# ---------------- STEP 1: MARK ROWS & COLUMNS ----------------

# i = 0
# matrix[0][0] = 1 → col remains False
# j = 1 → matrix[0][1] = 1 → nothing
# j = 2 → matrix[0][2] = 1 → nothing

# i = 1
# matrix[1][0] = 1 → col remains False
# j = 1 → matrix[1][1] = 0 → Found Zero!
# So mark:
# matrix[0][1] = 0   (mark column)
# matrix[1][0] = 0   (mark row)

# Matrix becomes:
# 1 0 1
# 0 0 1
# 1 1 1

# j = 2 → matrix[1][2] = 1 → nothing

# i = 2
# matrix[2][0] = 1 → col remains False
# j = 1 → matrix[2][1] = 1
# j = 2 → matrix[2][2] = 1

# After marking:
# 1 0 1
# 0 0 1
# 1 1 1

# ---------------- STEP 2: SET INNER ZEROES ----------------

# i = 1, j = 1
# matrix[1][0] == 0 OR matrix[0][1] == 0 → True
# So matrix[1][1] = 0 (already 0)

# i = 1, j = 2
# matrix[1][0] == 0 → True
# So matrix[1][2] = 0

# Matrix:
# 1 0 1
# 0 0 0
# 1 1 1

# i = 2, j = 1
# matrix[0][1] == 0 → True
# So matrix[2][1] = 0

# i = 2, j = 2
# matrix[2][0] != 0 AND matrix[0][2] != 0 → nothing

# Matrix now:
# 1 0 1
# 0 0 0
# 1 0 1

# ---------------- STEP 3: FIRST ROW ----------------

# matrix[0][0] != 0 → do nothing

# ---------------- STEP 4: FIRST COLUMN ----------------

# col == False → do nothing

# ---------------- FINAL MATRIX ----------------
# 1 0 1
# 0 0 0
# 1 0 1