from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)      # n = 7
        k = k % n      # k = 3 % 7 = 3
    
        if k != 0:
          nums[0 :] = nums[-k:] + nums[:-k] # nums[-3:] → [5,6,7],nums[:-3] → [1,2,3,4]

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print(nums)

 # nums[-k:]  → nums[-3:] → last 3 elements → [5, 6, 7]
            # nums[:-k]  → nums[:-3] → first 4 elements → [1, 2, 3, 4]
            
            # Combine both:
            # [5, 6, 7] + [1, 2, 3, 4]
            # → [5, 6, 7, 1, 2, 3, 4]