from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       ls =[1] * len(nums)
       rs =[1] * len(nums)
       f =[1] * len(nums)

       for i in range(1,len(nums)):
        ls[i] = ls[i-1] * nums[i-1]

       for j in range(len(nums)-2,-1,-1):
        rs[j] = rs[j+1] * nums[j+1]

       for k in range(len(nums)):
         f[k] = ls[k] * rs[k]
    
       return f
   
print(Solution().productExceptSelf([1,2,3,4]))

        # -------- Left Pass --------
        # i = 1
        # ls[1] = ls[0] * nums[0]
        #       = 1 * 1 = 1
        # ls = [1,1,1,1]

        # i = 2
        # ls[2] = ls[1] * nums[1]
        #       = 1 * 2 = 2
        # ls = [1,1,2,1]

        # i = 3
        # ls[3] = ls[2] * nums[2]
        #       = 2 * 3 = 6
        # ls = [1,1,2,6]
        
        
        # -------- Right Pass --------
        # j = 2
        # rs[2] = rs[3] * nums[3]
        #       = 1 * 4 = 4
        # rs = [1,1,4,1]

        # j = 1
        # rs[1] = rs[2] * nums[2]
        #       = 4 * 3 = 12
        # rs = [1,12,4,1]

        # j = 0
        # rs[0] = rs[1] * nums[1]
        #       = 12 * 2 = 24
        # rs = [24,12,4,1]
        
        
        # -------- Final Multiplication --------
        # k = 0 → f[0] = 1 * 24 = 24
        # k = 1 → f[1] = 1 * 12 = 12
        # k = 2 → f[2] = 2 * 4  = 8
        # k = 3 → f[3] = 6 * 1  = 6
        # f = [24,12,8,6]