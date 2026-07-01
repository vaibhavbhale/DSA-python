def containsNearbyDuplicate(nums, k):
    n = len(nums)
    d1 = {}

    for i in range(n):
        if nums[i] in d1:
            ans = abs(d1[nums[i]] - i)
            if ans <= k:
                return True

        d1[nums[i]] = i

    return False

nums = [1, 2, 3, 1]
k = 3

# Function call
print(containsNearbyDuplicate(nums, k))


# Dry Run:

# Initial:
# nums = [1,2,3,1]
# k = 3
# d1 = {}

# Iteration 1:
# i = 0
# nums[0] = 1
# 1 not in d1
# store d1[1] = 0
# d1 = {1:0}

# Iteration 2:
# i = 1
# nums[1] = 2
# 2 not in d1
# store d1[2] = 1
# d1 = {1:0, 2:1}

# Iteration 3:
# i = 2
# nums[2] = 3
# 3 not in d1
# store d1[3] = 2
# d1 = {1:0, 2:1, 3:2}

# Iteration 4:
# i = 3
# nums[3] = 1
# 1 found in d1 at index 0
# ans = abs(0 - 3) = 3

# Check:
# ans <= k
# 3 <= 3 → True

# Return True