def lowerBound(nums, target):
    n = len(nums)
    l = 0
    r = n - 1
    ans = n

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] >= target:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans


def upperBound(nums, target):
    n = len(nums)
    l = 0
    r = n - 1
    ans = n

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] > target:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans


def searchRange(nums, target):
    lb = lowerBound(nums, target)
    ub = upperBound(nums, target)

    if lb == ub:
        return [-1, -1]
    else:
        return [lb, ub - 1]


# Input
nums = [5, 7, 7, 8, 8, 10]
target = 8

# Function call
print(searchRange(nums, target))


# Dry Run:

# nums = [5,7,7,8,8,10]
# target = 8


# -------- Lower Bound --------
# Find first index where nums[i] >= 8

# Initial:
# l = 0, r = 5, ans = 6

# Iteration 1:
# mid = (0+5)//2 = 2
# nums[2] = 7
# 7 >= 8 ? No
# Move right → l = 3

# Iteration 2:
# l = 3, r = 5
# mid = (3+5)//2 = 4
# nums[4] = 8
# 8 >= 8 ? Yes
# ans = 4
# Move left → r = 3

# Iteration 3:
# l = 3, r = 3
# mid = (3+3)//2 = 3
# nums[3] = 8
# 8 >= 8 ? Yes
# ans = 3
# Move left → r = 2

# Stop (l > r)

# lowerBound = 3


# -------- Upper Bound --------
# Find first index where nums[i] > 8

# Initial:
# l = 0, r = 5, ans = 6

# Iteration 1:
# mid = (0+5)//2 = 2
# nums[2] = 7
# 7 > 8 ? No
# Move right → l = 3

# Iteration 2:
# l = 3, r = 5
# mid = (3+5)//2 = 4
# nums[4] = 8
# 8 > 8 ? No
# Move right → l = 5

# Iteration 3:
# l = 5, r = 5
# mid = (5+5)//2 = 5
# nums[5] = 10
# 10 > 8 ? Yes
# ans = 5
# Move left → r = 4

# Stop (l > r)

# upperBound = 5


# -------- Final Result --------
# lb = 3
# ub = 5

# return [lb, ub-1]
# return [3,4]