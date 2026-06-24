from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

print(Solution().threeSum(nums = [-1,0,1,2,-1,-4]))



"""i = 0 → nums[i] = -4

left = 1 (-1)
right = 5 (2)

Try combinations:

-4 + (-1) + 2 = -3 ❌ < 0
→ Move left

-4 + (-1) + 2 = -3 ❌
→ Move left

-4 + 0 + 2 = -2 ❌
→ Move left

-4 + 1 + 2 = -1 ❌
→ Move left

No triplet found.

i = 1 → nums[i] = -1

left = 2 (-1)
right = 5 (2)

Check:

-1 + (-1) + 2 = 0 ✅

Add:

[-1, -1, 2]

Move both pointers:

left = 3
right = 4

Now:

-1 + 0 + 1 = 0 

Add:

[-1, 0, 1]

Move pointers:

left = 4
right = 3 → stop

 i = 2 → nums[i] = -1

Duplicate of previous → skip

i = 3 → nums[i] = 0

left = 4 (1)
right = 5 (2)

0 + 1 + 2 = 3 ❌ > 0
→ Move right

Stop loop.
Final Result
[[-1, -1, 2], [-1, 0, 1]]
"""