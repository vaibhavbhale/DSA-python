def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        # Left sorted part
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        # Right sorted part
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1


# Input
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

# Function call
print(search(nums, target))


# Dry Run:

# Initial:
# nums = [4,5,6,7,0,1,2]
# target = 0
# l = 0
# r = 6

# Iteration 1:
# mid = (0+6)//2 = 3
# nums[mid] = 7

# Check:
# 7 == 0 ? No

# Left part [4,5,6,7] is sorted
# nums[l] = 4, nums[mid] = 7

# Check if target lies in left part:
# 4 <= 0 < 7 ? No

# Move right:
# l = mid + 1 = 4


# Iteration 2:
# l = 4
# r = 6
# mid = (4+6)//2 = 5
# nums[mid] = 1

# Check:
# 1 == 0 ? No

# Left part [0,1] is sorted
# nums[l] = 0, nums[mid] = 1

# Check if target lies in left part:
# 0 <= 0 < 1 ? Yes

# Move left:
# r = mid - 1 = 4


# Iteration 3:
# l = 4
# r = 4
# mid = (4+4)//2 = 4
# nums[mid] = 0

# Check:
# 0 == 0 ? Yes

# Return 4