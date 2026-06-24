def lowerBound(nums, target):
    n = len(nums)
    l = 0
    r = n - 1
    ans = n

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] >= target:
            ans = mid
            r = mid - 1   # move left
        else:
            l = mid + 1   # move right

    return ans


def searchInsert(nums, target):
    return lowerBound(nums, target)


# Input
nums = [1, 3, 5, 6]
target = 5

# Function call
print(searchInsert(nums, target))


# Dry Run:

# Initial:
# nums = [1,3,5,6]
# target = 5
# l = 0
# r = 3
# ans = 4

# Iteration 1:
# mid = (0+3)//2 = 1
# nums[1] = 3

# Check:
# 3 >= 5 ? No

# Move right:
# l = mid + 1 = 2

# Now:
# l = 2, r = 3, ans = 4


# Iteration 2:
# mid = (2+3)//2 = 2
# nums[2] = 5

# Check:
# 5 >= 5 ? Yes

# Update:
# ans = 2
# r = mid - 1 = 1

# Now:
# l = 2, r = 1

# Condition fails (l > r)

# Return ans = 2