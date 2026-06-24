from typing import List 

class Solution:
    def jump(self, nums: List[int]) -> int:
        n =len(nums)

        if n == 1:
          return 0

        max_jump = 0
        jump = 0
        end = 0
       
        for i in range(0 ,n-1):
            max_jump = max(max_jump , i + nums[i])

            if i == end:
                end = max_jump
                jump +=1     
        
        return jump 
    
print(Solution().jump([2,3,0,1,4]))


            # ----------------------------
            # i = 0
            # max_jump = max(0, 0+2) = 2
            # i == end (0 == 0) → True
            # end = 2
            # jump = 1
            # ----------------------------

            # i = 1
            # max_jump = max(2, 1+3) = 4
            # i == end (1 == 2) → False
            # ----------------------------

            # i = 2
            # max_jump = max(4, 2+0) = 4
            # i == end (2 == 2) → True
            # end = 4
            # jump = 2
            # ----------------------------

            # i = 3
            # max_jump = max(4, 3+1) = 4
            # i == end (3 == 4) → False