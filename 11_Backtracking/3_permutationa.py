def permute(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])   # store current permutation
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]   # swap
            backtrack(start + 1)   # recursive call
            nums[start], nums[i] = nums[i], nums[start]   # backtrack (swap back)

    result = []
    backtrack(0)
    return result


# Input
nums = [1, 2, 3]

# Function call
print(permute(nums))


# Dry Run:

# Initial:
# nums = [1,2,3]
# result = []

# backtrack(0)

# start = 0
# i = 0
# swap nums[0], nums[0] → [1,2,3]
# backtrack(1)

#   start = 1
#   i = 1
#   swap nums[1], nums[1] → [1,2,3]
#   backtrack(2)

#       start = 2
#       i = 2
#       swap nums[2], nums[2] → [1,2,3]
#       backtrack(3)

#           start == len(nums)
#           add [1,2,3] to result

#       backtrack → swap back → [1,2,3]

#   i = 2
#   swap nums[1], nums[2] → [1,3,2]
#   backtrack(2)

#       i = 2
#       swap nums[2], nums[2] → [1,3,2]
#       backtrack(3)

#           add [1,3,2] to result

#       swap back → [1,3,2]

#   swap back → [1,2,3]


# i = 1
# swap nums[0], nums[1] → [2,1,3]
# backtrack(1)

#   i = 1
#   swap nums[1], nums[1] → [2,1,3]
#   add [2,1,3]

#   i = 2
#   swap nums[1], nums[2] → [2,3,1]
#   add [2,3,1]

# swap back → [1,2,3]


# i = 2
# swap nums[0], nums[2] → [3,2,1]
# backtrack(1)

#   i = 1
#   swap nums[1], nums[1] → [3,2,1]
#   add [3,2,1]

#   i = 2
#   swap nums[1], nums[2] → [3,1,2]
#   add [3,1,2]

# swap back → [1,2,3]


# Final result:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,2,1],
#   [3,1,2]
# ]