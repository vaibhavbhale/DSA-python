from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))

 # -----------------------------
            # 1st iteration → interval = [1,3]
            # merged is empty → append
            # merged = [[1,3]]
            # -----------------------------
            
            # 2nd iteration → interval = [2,6]
            # Last merged interval = [1,3]
            # Check: 3 < 2 ? → No (overlap exists)
            # Merge:
            # New end = max(3,6) = 6
            # merged = [[1,6]]
            # -----------------------------
            
            # 3rd iteration → interval = [8,10]
            # Last merged interval = [1,6]
            # Check: 6 < 8 ? → Yes (no overlap)
            # Append
            # merged = [[1,6],[8,10]]
            # -----------------------------
            
            # 4th iteration → interval = [15,18]
            # Last merged interval = [8,10]
            # Check: 10 < 15 ? → Yes (no overlap)
            # Append
            # merged = [[1,6],[8,10],[15,18]]
            # -----------------------------
            
            