def longestConsecutive(nums):
    longest = 0
    s = set(nums)

    for x in s:
        if x - 1 not in s:   # start of sequence
            current = x
            length = 1

            while current + 1 in s:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


# Input
nums = [100, 4, 200, 1, 3, 2]

# Function call
print(longestConsecutive(nums))


# Dry Run:

# Initial:
# nums = [100,4,200,1,3,2]
# s = {100,4,200,1,3,2}
# longest = 0

# Loop 1:
# x = 100
# check x-1 = 99
# 99 not in s → start new sequence
# current = 100, length = 1
# 101 not in s → stop
# longest = max(0,1) = 1

# Loop 2:
# x = 4
# check x-1 = 3
# 3 in s → not start of sequence, skip

# Loop 3:
# x = 200
# check x-1 = 199
# 199 not in s → start new sequence
# current = 200, length = 1
# 201 not in s → stop
# longest = max(1,1) = 1

# Loop 4:
# x = 1
# check x-1 = 0
# 0 not in s → start new sequence
# current = 1, length = 1

# while:
# current+1 = 2 in s
# current = 2, length = 2

# current+1 = 3 in s
# current = 3, length = 3

# current+1 = 4 in s
# current = 4, length = 4

# current+1 = 5 not in s → stop

# longest = max(1,4) = 4

# Loop 5:
# x = 3
# check x-1 = 2
# 2 in s → skip

# Loop 6:
# x = 2
# check x-1 = 1
# 1 in s → skip

# Final longest = 4
# Output = 4