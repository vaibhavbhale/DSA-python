def combinationSum(candidates, target):
    res = []

    def backtracking(i, cur):
        if sum(cur) == target:
            res.append(cur.copy())   # found valid combination
            return

        if i >= len(candidates) or sum(cur) > target:
            return

        for j in range(i, len(candidates)):
            cur.append(candidates[j])   # choose
            backtracking(j, cur)        # can reuse same element
            cur.pop()                   # backtrack

    backtracking(0, [])
    return res


# Input
candidates = [2, 3, 6, 7]
target = 7

# Function call
print(combinationSum(candidates, target))


# Dry Run:

# Initial:
# candidates = [2,3,6,7]
# target = 7
# res = []

# backtracking(0, [])

# j = 0 → choose 2
# cur = [2]
# sum = 2

#   j = 0 → choose 2
#   cur = [2,2]
#   sum = 4

#       j = 0 → choose 2
#       cur = [2,2,2]
#       sum = 6

#           j = 0 → choose 2
#           cur = [2,2,2,2]
#           sum = 8 > 7 → return
#           pop → [2,2,2]

#           j = 1 → choose 3
#           cur = [2,2,2,3]
#           sum = 9 > 7 → return
#           pop → [2,2,2]

#       pop → [2,2]

#       j = 1 → choose 3
#       cur = [2,2,3]
#       sum = 7 → valid
#       add [2,2,3] to res

#       pop → [2,2]

#   pop → [2]

#   j = 1 → choose 3
#   cur = [2,3]
#   sum = 5

#       j = 1 → choose 3
#       cur = [2,3,3]
#       sum = 8 > 7 → return
#       pop → [2,3]

#       j = 2 → choose 6
#       cur = [2,3,6]
#       sum = 11 > 7 → return
#       pop → [2,3]

#   pop → [2]

# pop → []

# j = 1 → choose 3
# cur = [3]
# sum = 3

#   j = 1 → choose 3
#   cur = [3,3]
#   sum = 6

#       j = 1 → choose 3
#       cur = [3,3,3]
#       sum = 9 > 7 → return
#       pop → [3,3]

#   pop → [3]

# pop → []

# j = 2 → choose 6
# cur = [6]
# sum = 6

#   j = 2 → choose 6
#   cur = [6,6]
#   sum = 12 > 7 → return
#   pop → [6]

# pop → []

# j = 3 → choose 7
# cur = [7]
# sum = 7 → valid
# add [7] to res

# Final res:
# [[2,2,3], [7]]