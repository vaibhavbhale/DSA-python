from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        h=0

        for i in range(len(citations)):
            if citations[i] >=  i+1:
                h += 1
            else:
                break
        return h

print(Solution().hIndex([3,0,6,1,5]))

  # -------- Iteration 1 --------
            # i = 0
            # citations[0] = 6
            # Check: 6 >= (0+1) → 6 >= 1 → True
            # So h = 1
            
            # -------- Iteration 2 --------
            # i = 1
            # citations[1] = 5
            # Check: 5 >= (1+1) → 5 >= 2 → True
            # So h = 2
            
            # -------- Iteration 3 --------
            # i = 2
            # citations[2] = 3
            # Check: 3 >= (2+1) → 3 >= 3 → True
            # So h = 3
            
            # -------- Iteration 4 --------
            # i = 3
            # citations[3] = 1
            # Check: 1 >= (3+1) → 1 >= 4 → False
            # Loop breaks here
            