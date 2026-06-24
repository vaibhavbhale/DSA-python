from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        for i in range(0,len(nums)):
            #---- Iteration 1 ----
            # i = 0
            # max_idx = 0
            # Check: 0 > 0 ? False
            # max_idx = max(0, 0 + 2)
            # max_idx = 2
            
            # ---- Iteration 2 ----
            # i = 1
            # max_idx = 2
            # Check: 1 > 2 ? False
            # max_idx = max(2, 1 + 3)
            # max_idx = 4
            
            # ---- Iteration 3 ----
            # i = 2
            # max_idx = 4
            # Check: 2 > 4 ? False
            # max_idx = max(4, 2 + 1)
            # max_idx = 4
            
            if i > max_idx:
                return False
            max_idx = max(max_idx,i + nums[i])
        return True

nums = [2,3,1,1,4]
print(Solution().canJump(nums))