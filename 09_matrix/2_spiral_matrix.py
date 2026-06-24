from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        total = n * m
        ans = []
        c = 0

        rowstart = 0
        colstart = 0
        rowend = n - 1
        colend = m - 1   

        while c < total:
            for i in range(colstart, colend + 1):
                ans.append(matrix[rowstart][i])
                c += 1
            rowstart += 1
            
            if c == total:
                break
            
            for i in range(rowstart, rowend + 1):
                ans.append(matrix[i][colend])
                c += 1
            colend -= 1
            
            if c == total:
                break
            
            for i in range(colend, colstart - 1, -1):
                ans.append(matrix[rowend][i])
                c += 1
            rowend -= 1
            
            if c == total:
                break
            
            for i in range(rowend, rowstart - 1, -1):
                ans.append(matrix[i][colstart])
                c += 1
            colstart += 1 
        
        return ans


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

sol = Solution()
print(sol.spiralOrder(matrix))


# n = 3, m = 3
# total = 9
# rowstart = 0, rowend = 2
# colstart = 0, colend = 2
# c = 0
# ans = []

# ---------------- FIRST LOOP ----------------

# Traverse Top Row (left → right)
# matrix[0][0] = 1 → ans = [1]
# matrix[0][1] = 2 → ans = [1,2]
# matrix[0][2] = 3 → ans = [1,2,3]
# c = 3
# rowstart = 1

# Traverse Right Column (top → bottom)
# matrix[1][2] = 6 → ans = [1,2,3,6]
# matrix[2][2] = 9 → ans = [1,2,3,6,9]
# c = 5
# colend = 1

# Traverse Bottom Row (right → left)
# matrix[2][1] = 8 → ans = [1,2,3,6,9,8]
# matrix[2][0] = 7 → ans = [1,2,3,6,9,8,7]
# c = 7
# rowend = 1

# Traverse Left Column (bottom → top)
# matrix[1][0] = 4 → ans = [1,2,3,6,9,8,7,4]
# c = 8
# colstart = 1

# ---------------- SECOND LOOP ----------------

# Traverse Top Row (left → right)
# matrix[1][1] = 5 → ans = [1,2,3,6,9,8,7,4,5]
# c = 9
# rowstart = 2

# c == total → break loop

# Final Answer:
# [1,2,3,6,9,8,7,4,5]