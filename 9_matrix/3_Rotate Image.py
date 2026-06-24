from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

sol = Solution()
sol.rotate(matrix)
print(matrix)

# Original Matrix:
# 1 2 3
# 4 5 6
# 7 8 9

# n = 3

# ---------------- STEP 1: TRANSPOSE ----------------
# (Swap matrix[i][j] with matrix[j][i])

# i = 0
# j = 1 → swap matrix[0][1] and matrix[1][0]
# 2 ↔ 4
# Matrix becomes:
# 1 4 3
# 2 5 6
# 7 8 9

# j = 2 → swap matrix[0][2] and matrix[2][0]
# 3 ↔ 7
# Matrix becomes:
# 1 4 7
# 2 5 6
# 3 8 9

# i = 1
# j = 2 → swap matrix[1][2] and matrix[2][1]
# 6 ↔ 8
# Matrix becomes:
# 1 4 7
# 2 5 8
# 3 6 9

# i = 2 → no swaps (since j starts from i+1)

# After Transpose:
# 1 4 7
# 2 5 8
# 3 6 9

# ---------------- STEP 2: REVERSE EACH ROW ----------------

# Reverse row 0: [1,4,7] → [7,4,1]
# Reverse row 1: [2,5,8] → [8,5,2]
# Reverse row 2: [3,6,9] → [9,6,3]

# Final Matrix:
# 7 4 1
# 8 5 2
# 9 6 3