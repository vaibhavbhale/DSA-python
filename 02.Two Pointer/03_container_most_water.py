from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0                      # left pointer at index 0
        r = len(height) - 1        # right pointer at last index
        maxArea = 0                # store maximum area found


        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))

# -------- Iteration 1 --------
            # l = 0 (height=1)
            # r = 8 (height=7)
            # width = 8 - 0 = 8
            # area = min(1,7) * 8 = 8
            # maxArea = 8
            # move l because 1 < 7

            # -------- Iteration 2 --------
            # l = 1 (height=8)
            # r = 8 (height=7)
            # width = 8 - 1 = 7
            # area = min(8,7) * 7 = 49
            # maxArea = 49
            # move r because 8 > 7

            # -------- Iteration 3 --------
            # l = 1 (8)
            # r = 7 (3)
            # width = 6
            # area = 3 * 6 = 18
            # maxArea still 49
            # move r

            # -------- Iteration 4 --------
            # l = 1 (8)
            # r = 6 (8)
            # width = 5
            # area = 8 * 5 = 40
            # maxArea still 49
            # move r

            # Remaining iterations give smaller area
            # Loop stops when l == r