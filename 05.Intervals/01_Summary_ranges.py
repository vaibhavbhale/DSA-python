from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        result = []   
        
        def create_range(start, end):
            if start != end:
                return "{}->{}".format(nums[start], nums[end])
            else:
                return "{}".format(nums[start])
        
        start = end = 0

        for i in range(1, len(nums)):
            if nums[i] - nums[end] == 1:
                end += 1
            else:
                result.append(create_range(start, end))
                start = end = i

        result.append(create_range(start, end))
        return result
    
print(Solution().summaryRanges([0,1,2,4,5,7]))

            # --------------------------
            # i = 1 → nums[1] = 1
            # Check: 1 - 0 == 1 → Yes (continuous)
            # end = 1
            # --------------------------
            
            # i = 2 → nums[2] = 2
            # Check: 2 - 1 == 1 → Yes (continuous)
            # end = 2
            # --------------------------
            
            # i = 3 → nums[3] = 4
            # Check: 4 - 2 == 1 → No
            # Range ended from index 0 to 2
            # create_range(0,2) → "0->2"
            # result = ["0->2"]
            # start = end = 3
            # --------------------------
            
            # i = 4 → nums[4] = 5
            # Check: 5 - 4 == 1 → Yes
            # end = 4
            # --------------------------
            
            # i = 5 → nums[5] = 7
            # Check: 7 - 5 == 1 → No
            # Range ended from index 3 to 4
            # create_range(3,4) → "4->5"
            # result = ["0->2", "4->5"]
            # start = end = 5
            # --------------------------

           

        # After loop:
        # Last remaining number at index 5
        # create_range(5,5) → "7"
        # result = ["0->2", "4->5", "7"]
