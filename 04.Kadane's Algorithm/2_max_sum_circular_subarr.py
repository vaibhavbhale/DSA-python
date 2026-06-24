from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        curr_max = curr_min = 0
        max_sum = nums[0]
        min_sum = nums[0]

        for num in nums:
            total_sum += num

           
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)

        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)
    
print(Solution().maxSubarraySumCircular([1,-2,3,-2]))

            # -------------------------
            # 1st iteration → num = 1
            # -------------------------
            # total_sum = 1
            # curr_max = max(1, 0+1) = 1
            # max_sum = max(1,1) = 1
            # curr_min = min(1, 0+1) = 1
            # min_sum = min(1,1) = 1

            # -------------------------
            # 2nd iteration → num = -2
            # -------------------------
            # total_sum = -1
            # curr_max = max(-2, 1-2) = -1
            # max_sum = max(1,-1) = 1
            # curr_min = min(-2, 1-2) = -2
            # min_sum = min(1,-2) = -2

            # -------------------------
            # 3rd iteration → num = 3
            # -------------------------
            # total_sum = 2
            # curr_max = max(3, -1+3) = 3
            # max_sum = max(1,3) = 3
            # curr_min = min(3, -2+3) = 1
            # min_sum = min(-2,1) = -2

            # -------------------------
            # 4th iteration → num = -2
            # -------------------------
            # total_sum = 0
            # curr_max = max(-2, 3-2) = 1
            # max_sum = max(3,1) = 3
            # curr_min = min(-2, 1-2) = -2
            # min_sum = min(-2,-2) = -2

 # After loop:
        # total_sum = 0
        # max_sum = 3
        # min_sum = -2

        # Since max_sum > 0, we check:
        # total_sum - min_sum = 0 - (-2) = 2

        # Final answer = max(3, 2) = 3