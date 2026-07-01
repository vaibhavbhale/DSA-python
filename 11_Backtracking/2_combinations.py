def combine(n, k):
    res = []
    comb = []

    def backtrack(start):
        if len(comb) == k:
            res.append(comb[:])   # store copy of current combination
            return

        for num in range(start, n + 1):
            comb.append(num)      # choose
            backtrack(num + 1)    # explore
            comb.pop()            # backtrack (remove last)

    backtrack(1)
    return res


# Input
n = 4
k = 2

# Function call
print(combine(n, k))


# Dry Run:

# Initial:
# n = 4, k = 2
# res = []
# comb = []

# Call backtrack(1)

# start = 1
# Loop num = 1
# comb = [1]
# Call backtrack(2)

#   start = 2
#   Loop num = 2
#   comb = [1,2]
#   len(comb) == k → add [1,2] to res
#   res = [[1,2]]
#   pop → comb = [1]

#   Loop num = 3
#   comb = [1,3]
#   add [1,3]
#   res = [[1,2],[1,3]]
#   pop → comb = [1]

#   Loop num = 4
#   comb = [1,4]
#   add [1,4]
#   res = [[1,2],[1,3],[1,4]]
#   pop → comb = [1]

# pop → comb = []

# Loop num = 2
# comb = [2]
# Call backtrack(3)

#   Loop num = 3
#   comb = [2,3]
#   add [2,3]
#   res = [[1,2],[1,3],[1,4],[2,3]]
#   pop → comb = [2]

#   Loop num = 4
#   comb = [2,4]
#   add [2,4]
#   res = [[1,2],[1,3],[1,4],[2,3],[2,4]]
#   pop → comb = [2]

# pop → comb = []

# Loop num = 3
# comb = [3]
# Call backtrack(4)

#   Loop num = 4
#   comb = [3,4]
#   add [3,4]
#   res = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
#   pop → comb = [3]

# pop → comb = []

# Loop num = 4
# comb = [4]
# Call backtrack(5)
# no more elements, return

# Final res:
# [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]