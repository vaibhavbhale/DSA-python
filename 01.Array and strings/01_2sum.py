from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<=0:
         return False
 
        dict={}
        for i in range(len(nums)):#check no.in dict
             if nums[i] in dict:
                return dict[nums[i]]
             else:
                dict[target-nums[i]]=i   # Store the no. to reach target with current index
   
nums = [2,7,11,15]
target = 9 

print(Solution().twoSum(nums, target))

'''
i = 0
nums[i] = 2
Check:
Is 2 in dict?

❌ No (dict is empty)

Execute else:
dict[target - nums[i]] = i
dict[9 - 2] = 0
dict[7] = 0
dict becomes:
{7: 0}

 Iteration 2
i = 1
nums[i] = 7
Check:
Is 7 in dict?

✅ Yes (7 exists in dict)

Execute if:
return dict[7]

dict[7] = 0

So function returns:

0

'''