from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        for i in range(1 , len(nums)):
            curr_sum = max(curr_sum + nums[i],nums[i])
            max_sum = max(curr_sum , max_sum)
       
        return  max_sum 

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

#Step 1: Decide whether to continue previous subarray
# or start a new subarray from current element
            
            # Formula:
            # curr_sum = max(curr_sum + nums[i], nums[i])

            # ---- Dry Run ----
            # i=1 → nums[1]=1
            # curr_sum = max(-2+1, 1) = 1
            # max_sum = max(1, -2) = 1

            # i=2 → nums[2]=-3
            # curr_sum = max(1-3, -3) = -2
            # max_sum = max(-2, 1) = 1

            # i=3 → nums[3]=4
            # curr_sum = max(-2+4, 4) = 4
            # max_sum = max(4, 1) = 4

            # i=4 → nums[4]=-1
            # curr_sum = max(4-1, -1) = 3
            # max_sum = max(3, 4) = 4

            # i=5 → nums[5]=2
            # curr_sum = max(3+2, 2) = 5
            # max_sum = max(5, 4) = 5

            # i=6 → nums[6]=1
            # curr_sum = max(5+1, 1) = 6
            # max_sum = max(6, 5) = 6

            # i=7 → nums[7]=-5
            # curr_sum = max(6-5, -5) = 1
            # max_sum = max(1, 6) = 6

            # i=8 → nums[8]=4
            # curr_sum = max(1+4, 4) = 5
            # max_sum = max(5, 6) = 6
