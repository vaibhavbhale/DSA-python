def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    l = 0
    r = rows * cols - 1

    while l <= r:
        mid = (l + r) // 2
        i = mid // cols
        j = mid % cols

        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            r = mid - 1   # move left
        else:
            l = mid + 1   # move right

    return False


# Input
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3

# Function call
print(searchMatrix(matrix, target))


# Dry Run:

# Matrix (flattened):
# [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]

# rows = 3
# cols = 4

# Initial:
# l = 0
# r = (3 * 4) - 1 = 11

# Iteration 1:
# mid = (0 + 11) // 2 = 5
# i = 5 // 4 = 1
# j = 5 % 4 = 1

# matrix[1][1] = 11

# Check:
# 11 == 3 ? No
# 11 > 3 ? Yes

# Move left:
# r = mid - 1 = 4


# Iteration 2:
# l = 0
# r = 4
# mid = (0 + 4) // 2 = 2
# i = 2 // 4 = 0
# j = 2 % 4 = 2

# matrix[0][2] = 5

# Check:
# 5 == 3 ? No
# 5 > 3 ? Yes

# Move left:
# r = mid - 1 = 1


# Iteration 3:
# l = 0
# r = 1
# mid = (0 + 1) // 2 = 0
# i = 0 // 4 = 0
# j = 0 % 4 = 0

# matrix[0][0] = 1

# Check:
# 1 == 3 ? No
# 1 < 3 ? Yes

# Move right:
# l = mid + 1 = 1


# Iteration 4:
# l = 1
# r = 1
# mid = (1 + 1) // 2 = 1
# i = 1 // 4 = 0
# j = 1 % 4 = 1

# matrix[0][1] = 3

# Check:
# 3 == 3 ? Yes

# Return True