from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 0:
            return False

        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            else:
                hashmap[target - nums[i]] = i

nums = [2,7,11,15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))

# nums = [2,7,11,15]
# target = 9

# hashmap = {}

# i = 0
# nums[0] = 2
# Check: 2 in hashmap? → No
# Store complement:
# target - 2 = 7
# hashmap = {7: 0}

# i = 1
# nums[1] = 7
# Check: 7 in hashmap? → Yes
# hashmap[7] = 0
# So return [0, 1]

# Loop stops here.

# Final Answer:
# [0, 1]