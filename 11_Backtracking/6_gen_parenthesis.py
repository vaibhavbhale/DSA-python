def generateParenthesis(n):
    result = []

    def backtrack(cur, open_cnt, close_cnt):
        if open_cnt == n and close_cnt == n:
            result.append(cur)
            return

        if open_cnt < n:
            backtrack(cur + '(', open_cnt + 1, close_cnt)

        if close_cnt < open_cnt:
            backtrack(cur + ')', open_cnt, close_cnt + 1)

    backtrack("", 0, 0)
    return result


# Input
n = 3

# Function call
print(generateParenthesis(n))


# Dry Run:

# Initial:
# n = 3
# result = []

# backtrack("",0,0)

# Step 1:
# cur = ""
# open_cnt = 0, close_cnt = 0
# Can add "("

# cur = "("
# open_cnt = 1, close_cnt = 0

# Step 2:
# Can add "(" again

# cur = "(("
# open_cnt = 2, close_cnt = 0

# Step 3:
# Can add "(" again

# cur = "((("
# open_cnt = 3, close_cnt = 0

# Step 4:
# open_cnt == n, can only add ")"

# cur = "((()"
# open_cnt = 3, close_cnt = 1

# Step 5:
# cur = "((())"
# open_cnt = 3, close_cnt = 2

# Step 6:
# cur = "((()))"
# open_cnt = 3, close_cnt = 3
# Valid → add to result

# Backtrack...

# From "(("
# Instead of third "(" choose ")"

# cur = "(()"
# open_cnt = 2, close_cnt = 1

# Add "("
# cur = "(()("
# open_cnt = 3, close_cnt = 1

# Add ")"
# cur = "(()()"
# open_cnt = 3, close_cnt = 2

# Add ")"
# cur = "(()())"
# Valid → add to result

# Backtrack...

# Another path:
# cur = "(())"
# then add "(" and ")"
# gives "(())()"
# Valid → add

# Another path:
# cur = "()("
# continue...
# gives "()(())"
# Valid → add

# Another path:
# cur = "()()()"
# Valid → add


# Final result:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]