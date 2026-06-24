from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      i=0  # Pointer i tracks the position to place elements not equal to val
      
      for x in nums:
        if x!=val:
          nums[i]=x #store the ele at index i
          i+=1
      return i
  
nums = [3,2,2,3]
val = 3

print(Solution().removeElement(nums,val))