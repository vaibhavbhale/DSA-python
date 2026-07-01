from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1

        for j in range (1,len(nums)):# Compare cur. ele with unique element
           if nums[j] != nums[i - 1]:# If different, place nums[j] at index i 
               #  0 != 0 
             nums[i]=nums[j]
             i+=1
             
        return i #uniq.ele

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))