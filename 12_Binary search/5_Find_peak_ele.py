from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            # Left neighbor is greater
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1

            # Right neighbor is greater
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1

            # Peak element found
            else:
                return m


# Input
nums = [1, 2, 3, 1]

obj = Solution()
print(obj.findPeakElement(nums))


# -------------------- Dry Run --------------------
# nums = [1, 2, 3, 1]
#
# Initial:
# l = 0
# r = 3
#
# Iteration 1:
# m = 0 + (3 - 0) // 2
#   = 1
#
# nums[m] = nums[1] = 2
#
# Check 1:
# m > 0 and nums[1] < nums[0]
# 1 > 0 and 2 < 1
# False
#
# Check 2:
# m < 3 and nums[1] < nums[2]
# 1 < 3 and 2 < 3
# True
#
# l = m + 1 = 2
#
# --------------------------------
#
# Iteration 2:
# l = 2
# r = 3
#
# m = 2 + (3 - 2) // 2
#   = 2
#
# nums[m] = nums[2] = 3
#
# Check 1:
# m > 0 and nums[2] < nums[1]
# 2 > 0 and 3 < 2
# False
#
# Check 2:
# m < 3 and nums[2] < nums[3]
# 2 < 3 and 3 < 1
# False
#
# Neither neighbor is greater.
# Therefore, index 2 is a peak.
#
# Return 2
#
# Output: 2