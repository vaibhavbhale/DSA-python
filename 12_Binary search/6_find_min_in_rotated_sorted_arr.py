from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]


# Example input
nums = [4, 5, 6, 7, 0, 1, 2]

obj = Solution()
print(obj.findMin(nums))

# Dry run:
#
# Initial:
# l = 0, r = 6
#
# Iteration 1:
# mid = (0 + 6) // 2 = 3
# nums[mid] = 7, nums[r] = 2
# 7 > 2
# l = mid + 1 = 4
#
# Iteration 2:
# l = 4, r = 6
# mid = (4 + 6) // 2 = 5
# nums[mid] = 1, nums[r] = 2
# 1 <= 2
# r = mid = 5
#
# Iteration 3:
# l = 4, r = 5
# mid = (4 + 5) // 2 = 4
# nums[mid] = 0, nums[r] = 1
# 0 <= 1
# r = mid = 4
#
# Now:
# l = 4, r = 4
#
# Return nums[4] = 0