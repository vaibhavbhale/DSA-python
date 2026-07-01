from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m-1 
        p2 = n-1          
        pos = m+n-1    

        while p2 >= 0:
            n1 = nums1[p1] if p1 >= 0 else float("-inf")
            n2 = nums2[p2]

            if n1 > n2:
                nums1[pos] = n1
                p1 -= 1
            else:
                nums1[pos] = n2
                p2 -= 1

            pos -= 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

Solution().merge(nums1, m, nums2, n)
print(nums1)


'''
 Initial State:
nums1: [1, 2, 3, 0, 0, 0]
nums2: [2, 5, 6]
p1: 2 p2: 2 pos: 5
--------------------------------
Comparing n1: 3 and n2: 6
Placing 6 at position 5
Updated nums1: [1, 2, 3, 0, 0, 6]
p1: 2 p2: 1 pos: 4
--------------------------------
Comparing n1: 3 and n2: 5
Placing 5 at position 4
Updated nums1: [1, 2, 3, 0, 5, 6]
p1: 2 p2: 0 pos: 3
--------------------------------
Comparing n1: 3 and n2: 2
Placing 3 at position 3
Updated nums1: [1, 2, 3, 3, 5, 6]
p1: 1 p2: 0 pos: 2
--------------------------------
Comparing n1: 2 and n2: 2
Placing 2 at position 2
Updated nums1: [1, 2, 2, 3, 5, 6]
p1: 1 p2: -1 pos: 1
--------------------------------
Final nums1: [1, 2, 2, 3, 5, 6]
'''