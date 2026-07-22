from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = len(nums1)
        y = len(nums2)
        
        if x > y:
            return self.findMedianSortedArrays(nums2, nums1)

        low = 0
        high = x

        while low <= high:
            px = (low + high) // 2
            py = (x + y + 1) // 2 - px

            maxLeftX = float("-inf") if px == 0 else nums1[px - 1]
            minRightX = float("inf") if px == x else nums1[px]

            maxLeftY = float("-inf") if py == 0 else nums2[py - 1]
            minRightY = float("inf") if py == y else nums2[py]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                # Total number of elements is even
                if (x + y) % 2 == 0:
                    return (
                        max(maxLeftX, maxLeftY)
                        + min(minRightX, minRightY)
                    ) / 2

                # Total number of elements is odd
                else:
                    return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:
                high = px - 1

            else:
                low = px + 1

nums1 = [1, 3]
nums2 = [2]

obj = Solution()
print("Median =", obj.findMedianSortedArrays(nums1, nums2))


# Dry Run
# Input:
# nums1 = [1, 3]
# nums2 = [2]

# Since len(nums1) > len(nums2),
# function calls:
# findMedianSortedArrays([2], [1, 3])

# nums1 = [2]
# nums2 = [1, 3]

# x = 1
# y = 2

# low = 0
# high = 1

# -------------------- Iteration 1 --------------------

# px = (0 + 1) // 2
# px = 0

# py = (1 + 2 + 1) // 2 - 0
# py = 2

# maxLeftX = -∞
# minRightX = 2

# maxLeftY = nums2[1] = 3
# minRightY = +∞

# Check:
# maxLeftX <= minRightY
# -∞ <= +∞ ✓

# maxLeftY <= minRightX
# 3 <= 2 ✗

# Therefore:
# low = px + 1 = 1

# -------------------- Iteration 2 --------------------

# px = (1 + 1) // 2
# px = 1

# py = (1 + 2 + 1) // 2 - 1
# py = 1

# maxLeftX = nums1[0] = 2
# minRightX = +∞

# maxLeftY = nums2[0] = 1
# minRightY = nums2[1] = 3

# Check:
# 2 <= 3 ✓
# 1 <= +∞ ✓

# Correct partition found.

# Total elements = 3 (odd)

# Median = max(maxLeftX, maxLeftY)
#        = max(2, 1)
#        = 2

# Output: 2