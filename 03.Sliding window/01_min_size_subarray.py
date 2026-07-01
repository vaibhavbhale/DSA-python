from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minimum = float('inf')
        current_sum = 0

        for r in range(len(nums)):
            current_sum += nums[r]

            while current_sum >= target:
                minimum = min(minimum, r - l + 1)
                current_sum -= nums[l]
                l += 1

        return 0 if minimum == float('inf') else minimum


print(Solution().minSubArrayLen(target =7, nums = [2,3,1,2,4,3]))